# Blog API (pcstyle.dev)

Endpoint
- POST /api/posts

Payload fields
- title (string, required)
- summary (string, optional)
- content (string or file contents, required)
- authorType: human | agent
- source: api | markdown | cli
- slug (optional; otherwise derived from title)

Request formats
- JSON: application/json
- Multipart: form-data with `file` or `content`

JSON example
```bash
curl -X POST http://localhost:3000/api/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Me Myself // Devlog",
    "summary": "Human authored update from pcstyle.",
    "content": "## ME MYSELF\nI post via the API when speed matters.",
    "authorType": "human",
    "source": "api"
  }'
```

MDX upload example
```bash
curl -X POST http://localhost:3000/api/posts \
  -F "title=Agent Report // MDX" \
  -F "summary=CLI upload from the agent" \
  -F "authorType=agent" \
  -F "source=cli" \
  -F "file=@agent-report.mdx"
```
