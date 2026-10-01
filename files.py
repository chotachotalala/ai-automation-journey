with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Иван\n")
    file.write("Telegram-бот\n")

with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)