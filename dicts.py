lead = {
    "name": "Иван",
    "phone": "+79990000000",
    "service": "Telegram-бот",
    "budget": 50000
}
print(lead["name"])
print(lead["service"])
print(lead["budget"])


leads = [
    {
        "name": "Иван",
        "service": "Telegram-бот",
        "budget": 50000
    },
    {
        "name": "Мария",
        "service": "AI-ассистент",
        "budget": 80000
    },
    {
        "name": "Алексей",
        "service": "Автоматизация",
        "budget": 20000
    }
]
for lead in leads:
    print(lead["name"])
for lead in leads:
    print(lead["name"],"-",lead["service"],"-",lead["budget"])