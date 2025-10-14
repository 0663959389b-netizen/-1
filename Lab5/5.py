import requests        
import numpy as np      
import pandas as pd     
from faker import Faker 
from tqdm import tqdm   
from PIL import Image   
import matplotlib.pyplot as plt  
from dotenv import load_dotenv   
import yaml              
from bs4 import BeautifulSoup   

# 1. requests — отримуємо сторінку
try:
    print("Використання requests:")   # повідомляємо про початок роботи з requests
    response = requests.get("https://httpbin.org/get", timeout=5)  # надсилаємо GET-запит на адресу з таймаутом 5 сек
    print("Статус відповіді:", response.status_code)  # друкуємо HTTP статус-код відповіді
except Exception as e:
    print("Requests error:", e)  # у разі помилки виводимо повідомлення з описом

# 2. numpy — обчислення середнього значення масиву
try:
    print("Використання numpy:")   # повідомляємо про початок роботи з numpy
    arr = np.array([10, 20, 30, 40, 50])   # створюємо масив numpy з п'яти чисел
    print("Середнє значення:", np.mean(arr))    # виводимо середнє арифметичне значення масиву
except Exception as e:
    print("Numpy error:", e)   # у разі помилки виводимо повідомлення з описом

# 3. pandas — створюємо DataFrame
try:
    print(" Використання pandas:")   # повідомляємо про початок роботи з pandas
    df = pd.DataFrame({               # створюємо об'єкт DataFrame з двома колонками: "Назва" і "Ціна"
        "Назва": ["Товар A", "Товар B", "Товар C"],
        "Ціна": [120, 150, 90]
    })
    print(df)    # виводимо таблицю на екран
except Exception as e:
    print("Pandas error:", e)   # у разі помилки виводимо повідомлення з описом

# 4. Faker — генерація випадкових імен
try:
    print("Використання Faker:")   # повідомляємо про початок роботи з Faker
    fake = Faker("uk_UA")           # створюємо об'єкт Faker для генерації українських даних
    for _ in range(3):              # генеруємо та друкуємо три випадкових імені
        print("Ім'я:", fake.name())
except Exception as e:
    print("Faker error:", e)   # у разі помилки виводимо повідомлення з описом

# 5. tqdm — індикатор прогресу
try:
    print("Використання tqdm:")   # повідомляємо про початок роботи з tqdm
    for i in tqdm(range(5), desc="Обробка елементів"):   # проходимо цикл з 5 ітерацій з індикатором прогресу
        pass  # тут можна вставляти операції, поки просто пропускаємо
except Exception as e:
    print("TQDM error:", e)   # у разі помилки виводимо повідомлення з описом

print("Кінець виконання програми")   # виводимо повідомлення про закінчення роботи програми
