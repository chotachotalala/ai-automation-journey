from lead_utils import create_lead
import json

with open("lead.json", "r", encoding="utf-8") as file:
    leads = json.load(file)

name = input("Имя: ")
service = input("Услуга: ")
budget = int(input("Бюджет: "))

lead1 = create_lead(name, service, budget)

leads.append(lead1)

print(json.dumps(leads, ensure_ascii=False, indent=4))

with open("lead.json", "w", encoding="utf-8") as file:
    json.dump(leads, file, ensure_ascii=False, indent=4)