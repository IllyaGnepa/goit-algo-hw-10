import pulp

# Створюємо модель
model = pulp.LpProblem("Maximize_drink_production", pulp.LpMaximize)

# Змінні рішень
x_lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
x_fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Обмеження ресурсів
water_limit = 100
sugar_limit = 50
lemon_juice_limit = 30
fruit_puree_limit = 40

# Обмеження на інгредієнти для кожного продукту
model += (2 * x_lemonade + 1 * x_fruit_juice <= water_limit), "Water constraint"
model += (1 * x_lemonade <= sugar_limit), "Sugar constraint"
model += (1 * x_lemonade <= lemon_juice_limit), "Lemon juice constraint"
model += (2 * x_fruit_juice <= fruit_puree_limit), "Fruit puree constraint"

# Цільова функція: максимізувати кількість напоїв
model += x_lemonade + x_fruit_juice, "Objective"

# Розв'язуємо модель
model.solve()

# Виводимо результати
print(f"Максимальна кількість Лимонаду: {x_lemonade.value()} одиниць")
print(f"Максимальна кількість Фруктового соку: {x_fruit_juice.value()} одиниць")
print(f"Загальна кількість продуктів: {x_lemonade.value() + x_fruit_juice.value()} одиниць")