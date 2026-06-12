# summarizer.py

import ollama


def generate_summary(chat_text):

    prompt = f"""
You are a Senior Engineering Manager.

Your job is to generate a DAILY WORK REPORT.

IMPORTANT:

The conversations below contain:
- Questions
- Answers
- Architecture discussions
- Technical explanations
- Research discussions
- Debugging sessions

You must identify ONLY the work actually performed by the user.

DO NOT:
- Explain concepts.
- Explain architectures.
- Explain RAG.
- Explain AI models.
- Copy section headings.
- Copy workflow steps.
- Copy architecture blocks.
- Copy chapter titles.
- Copy lists from assistant responses.

ONLY report actions performed by the user.

Examples:

BAD:
1. PDF Input
2. Knowledge Layer
3. Validation Layer

BAD:
1. RAG Architecture
2. OCR Pipeline

GOOD:
1. Designed a span-centric architecture for question generation.
2. Evaluated hybrid retrieval using vector search, BM25, and knowledge graphs.
3. Implemented Google Sheets integration for daily reporting.
4. Debugged Chrome extension communication issues.
5. Tested SQLite-based chat logging workflows.
6. Researched image description generation approaches.

Rules:

- Output only numbered points.
- Maximum 10 points.
- One sentence per point.
- Use action verbs:
  Researched
  Designed
  Implemented
  Built
  Tested
  Integrated
  Debugged
  Evaluated
  Improved
  Created

- Ignore assistant explanations.
- Focus on user activities.
- No markdown.
- No headings.
- No explanations.

Conversations:

{chat_text}
"""

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
