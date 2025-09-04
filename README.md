# marks-movie-graph
Explore Mark's Movie Collection with Neo4j, FastAPI, and React

```bash
litellm --model ollama/qwen2.5-coder:14b --host 127.0.0.1 --port 4000
set OPENAI_API_KEY="sk-local-anything"
set OPENAI_API_BASE="http://127.0.0.1:4000/v1"
```


```bash
docker run --rm -it \
  -v $PWD:/workspace \
  -w /workspace \
  -p 5173:5173 -p 8000:8000 \
  python:3.11-slim bash
  ```