import json

lead = {
    "name": "Иван",
    "service": "Telegram-бот",
    "budget": 50000
}

with open("lead.json", "w", encoding="utf-8") as file:
    json.dump(lead, file, ensure_ascii=False, indent=4) 