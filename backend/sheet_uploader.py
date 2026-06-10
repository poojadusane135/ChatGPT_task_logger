import requests

APPS_SCRIPT_URL = (
    "app_script_url_to_google_sheet_endpoint"
)


def upload_task(task):

    from datetime import date

    today = str(date.today())

    payload = {
        "task": task,
        "start_date": today,
        "end_date": today
    }

    response = requests.post(
        APPS_SCRIPT_URL,
        json=payload,
        timeout=30
    )

    print(
        "SHEET RESPONSE:",
        response.text
    )