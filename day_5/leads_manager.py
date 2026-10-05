import json

with open("lead.json", "r", encoding="utf-8") as file:
    leads = json.load(file)


# 1. Вывести все заявки
print("Все заявки:\n")

for lead in leads:
    print("Имя:", lead["name"])
    print("Услуга:", lead["service"])
    print("Бюджет:", lead["budget"], "₽")
    print("--------------------")


# 2. Посчитать, сколько всего заявок
print("\nВсего заявок:", len(leads))


# 3. Заявки с бюджетом от 30 000 ₽
print("\nЗаявки с бюджетом от 30 000 ₽:\n")

for lead in leads:
    if lead["budget"] >= 30000:
        print(
            "Имя:", lead["name"],
            "| Услуга:", lead["service"],
            "| Бюджет:", lead["budget"], "₽"
        )


# 4. Средний бюджет
total_budget = 0

for lead in leads:
    total_budget += lead["budget"]

average_budget = total_budget / len(leads)

print(f"\nСредний бюджет: {average_budget:.2f} ₽")