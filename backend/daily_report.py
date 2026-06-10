from database import get_today_chats
from summarizer import generate_summary
from sheet_uploader import upload_task


PROJECT_KEYWORDS = [
"chat keywords to logged in the database"
]


def build_daily_report():

    rows = get_today_chats()

    filtered = []

    for row in rows:

        content = row[3]

        content_lower = content.lower()

        if any(
            keyword in content_lower
            for keyword in PROJECT_KEYWORDS
        ):
            filtered.append(content)

    # remove duplicates
    unique = []

    seen = set()

    for item in filtered:

        if item not in seen:

            seen.add(item)

            unique.append(item)

    chat_text = "\n\n".join(unique)

    chat_text = chat_text[:12000]

    summary = generate_summary(chat_text)

    print("\n")
    print("=" * 80)
    print("DAILY REPORT")
    print("=" * 80)
    print(summary)
    print("=" * 80)

    print("\nUPLOADING TO SHEET...\n")

    for line in summary.split("\n"):

        line = line.strip()

        if not line:
            continue

        upload_task(line)

    print("\nDONE")


if __name__ == "__main__":

    build_daily_report()