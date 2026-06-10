# summarizer.py

import ollama


def generate_summary(chat_text):

    prompt = f"""
You are a Technical Project Manager.

Below are ChatGPT conversations from today's work.

Generate a professional task report.

Rules:
- Include only work actually performed today.
- Ignore questions asking for definitions.
- Ignore casual conversations.
- Ignore general learning discussions unless implementation or evaluation work was performed.
- Use action verbs such as:
  Researched, Implemented, Built, Evaluated, Tested, Designed, Integrated, Debugged.
- Maximum 10 points.
- Output only numbered points.
- No explanations.
- No markdown.
- No headings.

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