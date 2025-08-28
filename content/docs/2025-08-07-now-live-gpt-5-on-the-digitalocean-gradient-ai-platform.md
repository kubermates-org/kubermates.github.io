---
title: 'Now Live: GPT-5 on the DigitalOcean Gradient™ AI Platform'
date: '2025-08-07T23:00:48.136000+00:00'
tags:
- kubernetes
source: Digital Ocean
external_url: https://www.digitalocean.com/blog/gpt-5-now-on-digitalocean-gradient-ai-platform
post_kind: link
draft: false
tldr: "Now Live: GPT-5 on the DigitalOcean Gradientâ\x84¢ AI Platform Get started\
  \ now Why GPT-5? Whatâ\x80\x99s New Deploy today About the author(s) Try DigitalOcean\
  \ for free Related Articles Announcing OpenAI gpt-oss Models on the DigitalOcean\
  \ Gradientâ\x84¢ AI Platform Build smarter AI agents: new tools now available for\
  \ the DigitalOcean Gradientâ\x84¢ AI Platform Introducing GPU Droplets accelerated\
  \ by NVIDIA HGX H200 By Grace Morgan , Yogesh Sharma , and Amit Jotwani Updated:\
  \ August 11, 2025 2 min read Weâ\x80\x99re excited to announce that GPT-5 is now\
  \ available on the DigitalOcean Gradientâ\x84¢ AI Platform. With this update, developers\
  \ can start using GPT-5 immediately via serverless inference APIs or the Gradient\
  \ AI Platform SDK."
summary: "Now Live: GPT-5 on the DigitalOcean Gradientâ\x84¢ AI Platform Get started\
  \ now Why GPT-5? Whatâ\x80\x99s New Deploy today About the author(s) Try DigitalOcean\
  \ for free Related Articles Announcing OpenAI gpt-oss Models on the DigitalOcean\
  \ Gradientâ\x84¢ AI Platform Build smarter AI agents: new tools now available for\
  \ the DigitalOcean Gradientâ\x84¢ AI Platform Introducing GPU Droplets accelerated\
  \ by NVIDIA HGX H200 By Grace Morgan , Yogesh Sharma , and Amit Jotwani Updated:\
  \ August 11, 2025 2 min read Weâ\x80\x99re excited to announce that GPT-5 is now\
  \ available on the DigitalOcean Gradientâ\x84¢ AI Platform. With this update, developers\
  \ can start using GPT-5 immediately via serverless inference APIs or the Gradient\
  \ AI Platform SDK. Alternatively, you can bring your own OpenAI API key to integrate\
  \ the new model into your Gradient AI Platform agent workflow. Curl command curl\
  \ https://inference. do-ai. run/v1/chat/completions \\ -H \"Authorization: Bearer\
  \ YOUR_API_KEY\" \\ -H \"Content-Type: application/json\" \\ -d ' { \"model\": \"\
  openai-gpt-5\", \"messages\": [ { \"role\": \"user\", \"content\": \"Explain quantum\
  \ computing in simple terms\" } ], \"temperature\": 0. 7, \"max_tokens\": 1000 }\
  \ ' curl https://inference. do-ai. run/v1/chat/completions \\ -H \"Authorization:\
  \ Bearer YOUR_API_KEY\" \\ -H \"Content-Type: application/json\" \\ -d ' { \"model\"\
  : \"openai-gpt-5\", \"messages\": [ { \"role\": \"user\", \"content\": \"Explain\
  \ quantum computing in simple terms\" } ], \"temperature\": 0. 7, \"max_tokens\"\
  : 1000 } ' Gradient AI Platform SDK from gradient import Gradient inference_key\
  \ = \"YOUR_GRADIENT_INFERENCE_KEY\" inference_client = Gradient( inference_key=inference_key,\
  \ ) inference_response = inference_client. chat. completions."
---
Open the original post ↗ https://www.digitalocean.com/blog/gpt-5-now-on-digitalocean-gradient-ai-platform
