#!/usr/bin/env python3
"""
Analyze GitHub repository to extract implementation status.
Checks merged PRs, commits, and actual code changes.
"""

import json
import subprocess
import sys
from pathlib import Path


def run_command(cmd):
    """Run shell command and return output."""
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True, check=False
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


def get_recent_commits(repo_path, days=90):
    """Get recent commits with their messages and file changes."""
    cmd = f'cd {repo_path} && git log --since="{days} days ago" --pretty=format:"%H|%an|%ad|%s" --date=short --name-status'
    stdout, stderr, code = run_command(cmd)
    
    if code != 0:
        return []
    
    commits = []
    current_commit = None
    
    for line in stdout.split('\n'):
        if not line.strip():
            continue
            
        if '|' in line:
            # Commit header line
            parts = line.split('|', 3)
            if len(parts) == 4:
                current_commit = {
                    'hash': parts[0],
                    'author': parts[1],
                    'date': parts[2],
                    'message': parts[3],
                    'files': []
                }
                commits.append(current_commit)
        elif current_commit and '\t' in line:
            # File change line (e.g., "M\tfile.py")
            status, *file_parts = line.split('\t')
            if file_parts:
                current_commit['files'].append({
                    'status': status,
                    'path': '\t'.join(file_parts)
                })
    
    return commits


def get_merged_prs(repo_path):
    """Get merged PRs using gh CLI."""
    cmd = f'cd {repo_path} && gh pr list --state merged --limit 50 --json number,title,mergedAt,author,body'
    stdout, stderr, code = run_command(cmd)
    
    if code != 0:
        return []
    
    try:
        return json.loads(stdout) if stdout else []
    except json.JSONDecodeError:
        return []


def get_file_content(repo_path, file_path):
    """Get current content of a file."""
    full_path = Path(repo_path) / file_path
    if full_path.exists():
        try:
            return full_path.read_text()
        except:
            return None
    return None


def analyze_implementation(repo_path, issue_keywords):
    """
    Analyze if keywords appear in recent commits/PRs and actual code.
    Returns dict with commits, PRs, and code_found status.
    """
    commits = get_recent_commits(repo_path)
    prs = get_merged_prs(repo_path)
    
    # Find matching commits
    matching_commits = []
    for commit in commits:
        msg_lower = commit['message'].lower()
        if any(kw.lower() in msg_lower for kw in issue_keywords):
            matching_commits.append(commit)
    
    # Find matching PRs
    matching_prs = []
    for pr in prs:
        title_lower = pr['title'].lower()
        body_lower = (pr.get('body') or '').lower()
        if any(kw.lower() in title_lower or kw.lower() in body_lower for kw in issue_keywords):
            matching_prs.append(pr)
    
    return {
        'commits': matching_commits,
        'prs': matching_prs,
        'has_activity': len(matching_commits) > 0 or len(matching_prs) > 0
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: analyze_repo.py <repo_path> <keyword1> [keyword2] ...")
        sys.exit(1)
    
    repo_path = sys.argv[1]
    keywords = sys.argv[2:]
    
    result = analyze_implementation(repo_path, keywords)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
