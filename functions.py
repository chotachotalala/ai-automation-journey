def greet(name):
    print("Привет,", name)


greet("Иван")
greet("Алексей")

def add(a, b):
    return a + b


result = add(10, 20)

print(result)

def calculate_discount(price, discount):
    newPrice = price - price*discount/100
    print("Вот цена с учетом скидки",newPrice)
    
