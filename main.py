import sqlite3

# Підключення до бази даних
connection = sqlite3.connect(r'c:\Users\PC\Desktop\10.05\data.db')
cursor = connection.cursor()

# Виконання запиту
query = "SELECT AVG(price) AS average_price FROM products;"
cursor.execute(query)

# Отримання результату
result = cursor.fetchone()
average_price = result[0]

# Виведення результату
print(f"Середня ціна товарів: {average_price:.2f}")

# Закриття з'єднання
cursor.close()
connection.close()