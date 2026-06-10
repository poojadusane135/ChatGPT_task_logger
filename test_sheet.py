import requests

url = "app_script_url_to_google_sheet_endpoint"

payload = {
    "task": "Testing Sheet Integration",
    "start_date": "2026-06-10",
    "end_date": "2026-06-10"
}

r = requests.post(url, json=payload)

print(r.status_code)
print(r.text)