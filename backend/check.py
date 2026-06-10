from database import get_today_chats

rows = get_today_chats()

for row in rows:

    print("========== CHAT ==========")
    print(row)

