import requests

payload = {
    "timestamp": "2026-06-05",
    "title": "Test Chat",
    "content": "Testing SQLite insert"
}

r = requests.post(
    "http://localhost:5000/save_chat",
    json=payload,
    timeout=10
)

print("STATUS:", r.status_code)
print("TEXT:", r.text)
