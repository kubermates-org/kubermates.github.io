---
title: Tool descriptions are eating up all your AI tokens (but they don’t have to)
date: '2025-10-31T14:00:00+00:00'
tags:
- cncf
source: CNCF
external_url: https://www.cncf.io/blog/2025/10/31/tool-descriptions-are-eating-up-all-your-ai-tokens-but-they-dont-have-to/
post_kind: link
draft: false
tldr: Where the waste comes from Reducing token waste with smarter tool selection
  Community-driven innovation Looking ahead Posted on October 31, 2025 by Craig McLuckie,
  Stacklok The vast majority of developers now use AI coding assistants daily. As
  these tools become more advanced and widely adopted, usage quotas and rate limits
  have also become a familiar frustration.
summary: 'Where the waste comes from Reducing token waste with smarter tool selection
  Community-driven innovation Looking ahead Posted on October 31, 2025 by Craig McLuckie,
  Stacklok The vast majority of developers now use AI coding assistants daily. As
  these tools become more advanced and widely adopted, usage quotas and rate limits
  have also become a familiar frustration. Many providers enforce weekly or monthly
  usage caps to manage compute costs. Once you hit a limit, you might be blocked,
  throttled, or shifted to slower processing queues — halting productivity and disrupting
  your workflow. But there’s a surprising reason behind much of this token consumption:
  wasted tool metadata. As contributors exploring the Model Context Protocol (MCP)
  have found, the vast majority of tokens consumed by AI coding assistants come not
  from your prompts or code, but from unnecessary tool descriptions that get bundled
  into each request. Let’s say you’ve installed MCP servers for GitHub, Grafana, and
  Notion. You ask your AI coding assistant to: “List the 10 most recent issues from
  my GitHub repo. ” That simple prompt uses 102,000 tokens, not because the task is
  complex, but because the model receives metadata for 114 tools, most of which have
  nothing to do with the request. Other common prompts create similar waste: “Summarize
  my meeting notes from October 19, 2025” uses 240,600 tokens, again with 114 tools
  injected, even though only the Notion server is relevant “Search dashboards related
  to RDS” consumes 93,600 tokens In each case, only a small fraction of those tokens
  are relevant to the task. Even saying “hello” burns more than 46,000 tokens. Multiply
  that across even a few dozen prompts per day, and you’re burning millions of tokens
  on context the model doesn’t need.'
---
Open the original post ↗ https://www.cncf.io/blog/2025/10/31/tool-descriptions-are-eating-up-all-your-ai-tokens-but-they-dont-have-to/
