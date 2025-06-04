import sqlite3

c = sqlite3.connect("bank.db")
cursor = c.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    balance REAL
)
""")
c.commit()

def register_client(name, phone):
    cursor.execute("INSERT INTO clients (name, phone, balance) VALUES (?, ?, ?)", (name, phone, 0.0))
    c.commit()
    print(f"клиент {name} зарегистрирован")

def find_client(name, phone):
    cursor.execute("SELECT * FROM clients WHERE name = ? AND phone = ?", (name, phone))
    client = cursor.fetchone()
    if client:
        print(f"найден клиент: ID = {client[0]}, имя = {client[1]}, телефон = {client[2]}, баланс = {client[3]: }")
        return client
    else:
        print("клиент не найден")
        return None

def deposit(client_id, amount):
    cursor.execute("UPDATE clients SET balance = balance + ? WHERE id = ?", (amount, client_id))
    c.commit()
    print(f"баланс пополнен на {amount: }")

def withdraw(client_id, amount):
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    current_balance = cursor.fetchone()[0]
    if current_balance >= amount:
        cursor.execute("UPDATE clients SET balance = balance - ? WHERE id = ?", (amount, client_id))
        c.commit()
        print(f"снято {amount: }")
    else:
        print("недостаточно средств.")

def view_balance(client_id):
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    balance = cursor.fetchone()[0]
    print(f"текущий баланс: {balance: }")

def calculate_deposit(client_id, months):
    if months not in [12, 24, 36]:
        print("можно выбрать только 12, 24 или 36 месяцев")
        return
    cursor.execute("SELECT balance FROM clients WHERE id = ?", (client_id,))
    balance = cursor.fetchone()[0]
    rate = 0.24
    years = months / 12
    final_amount = balance * ((1 + rate) ** years)
    print(f"через {months} месяцев на счету будет {final_amount: }")


while True:
    print("\nменю:")
    print("1. регистрация клиента")
    print("2. поиск клиента")
    print("3. пополнение баланса")
    print("4. снятие денег")
    print("5. просмотр баланса")
    print("6. подсчет вклада")
    print("7. выход")
    choice = input("выберите пункт: ")

    if choice == "1":
        name = input("введите имя: ")
        phone = input("введите телефон: ")
        register_client(name, phone)
    elif choice == "2":
        name = input("введите имя: ")
        phone = input("введите телефон: ")
        find_client(name, phone)
    elif choice == "3":
        client_id = int(input("введите ID клиента: "))
        amount = float(input("введите сумму пополнения: "))
        deposit(client_id, amount)
    elif choice == "4":
        client_id = int(input("введите ID клиента: "))
        amount = float(input("введите сумму снятия: "))
        withdraw(client_id, amount)
    elif choice == "5":
        client_id = int(input("введите ID клиента: "))
        view_balance(client_id)
    elif choice == "6":
        client_id = int(input("введите ID клиента: "))
        months = int(input("введите срок вклада (12, 24, 36): "))
        calculate_deposit(client_id, months)
    elif choice == "7":
        print("выход из программы")
        break
    else:
        print("попробуйте снова")