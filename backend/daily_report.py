from database import get_today_chats
from summarizer import generate_summary
from sheet_uploader import upload_task


def build_daily_report():

    rows = get_today_chats()

    print(f"\nTOTAL CHATS FOUND: {len(rows)}\n")

    filtered = []

    # Take all chats
    for row in rows:

        content = row[3]

        if not content:
            continue

        filtered.append(content)

    print(f"TOTAL NON-EMPTY CHATS: {len(filtered)}")

    # Remove duplicates
    unique = []

    seen = set()

    for item in filtered:

        if item not in seen:

            seen.add(item)

            unique.append(item)

    print(f"UNIQUE CHATS FOUND: {len(unique)}")

    # Newest chats first
    unique = unique[::-1]

    # Take latest chats
    latest_chats = unique[:10]

    chat_text = "\n\n".join(latest_chats)

    print("\n")
    print("=" * 80)
    print("TEXT SENT TO QWEN")
    print("=" * 80)
    print(chat_text[:5000])
    print("=" * 80)

    summary = generate_summary(chat_text)

    print("\n")
    print("=" * 80)
    print("DAILY REPORT")
    print("=" * 80)
    print(summary)
    print("=" * 80)

    print("\nUPLOADING TO SHEET...\n")

    uploaded_count = 0

    for line in summary.split("\n"):

        line = line.strip()

        if not line:
            continue

        # Upload only numbered points
        if not line[0].isdigit():
            continue

        upload_task(line)

        uploaded_count += 1

    print(f"\nUPLOADED {uploaded_count} TASKS")
    print("DONE")


if __name__ == "__main__":

    build_daily_report()
