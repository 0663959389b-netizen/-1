import requests
import numpy as np
import pandas as pd
from faker import Faker
from tqdm import tqdm

# 1) requests — пробуємо отримати сторінку
try:
    print("\n[1] Використання requests:")
    response = requests.get("https://example.com", timeout=5)
    print("Статус відповіді:", response.status_code)
except Exception as e:
    print("Помилка в requests:", e)

# 2) numpy — створюємо масив і рахуємо середнє
try:
    print("\n[2] Використання numpy:")
    arr = np.array([1, 2, 3, 4, 5])
    print("Масив:", arr)
    print("Середнє значення:", np.mean(arr))
except Exception as e:
    print("Помилка в numpy:", e)

# 3) pandas — створюємо просту таблицю
try:
    print("\n[3] Використання pandas:")
    data = {"Ім'я": ["Анна", "Олег", "Марія"], "Вік": [20, 22, 19]}
    df = pd.DataFrame(data)
    print(df)
except Exception as e:
    print("Помилка в pandas:", e)

# 4) Faker — генеруємо випадкові імена
try:
    print("\n[4] Використання Faker:")
    fake = Faker("uk_UA")
    for _ in range(3):
        print("Випадкове ім’я:", fake.name())
except Exception as e:
    print("Помилка у Faker:", e)

# 5) tqdm — показуємо індикатор прогресу
try:
    print("\n[5] Використання tqdm:")
    for i in tqdm(range(5)):
        pass  # просто показуємо хід циклу
except Exception as e:
    print("Помилка в tqdm:", e)

print("\n=== Кінець виконання програми ===")
