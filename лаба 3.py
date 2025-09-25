students = {}  # створюємо порожній словник, де будемо зберігати студентів та їх оцінки

while True:  # запускаємо нескінченний цикл для введення даних
    name = input("Введи ім'я студента або 'stop' для виходу: ")
    if name == "stop":  # якщо введено слово 'stop'
        break

    while True:
        grade = int(input("Введи оцінку студента (0-12): "))
        if 0 <= grade <= 12:  # якщо оцінка у допустимому діапазоні
            break
        else:
            print("Оцінка має бути від 0 до 12. Спробуй ще раз.")

    students[name] = grade  # додаємо у словник пару: ім’я, оцінка

print("Оцінки студентів:")
for name in students:  # перебираємо всіх студентів у словнику
    print(name, "-", students[name])

total = sum(students.values())  # рахуємо суму всіх оцінок
average = total / len(students) if students else 0  # обчислюємо середній бал або 0, якщо студентів нема
print("Середній бал:", average)

excellent = 0
good = 0
failing = 0
not_passed = 0
excellent_names = []  # список імен відмінників

for name, grade in students.items():  # перебираємо всіх студентів і їх оцінки
    if 10 <= grade <= 12:  # якщо оцінка від 10 до 12
        excellent += 1  # додаємо до кількості відмінників
        excellent_names.append(name)  # зберігаємо ім’я відмінника
    elif 7 <= grade <= 9:
        good += 1
    elif 4 <= grade <= 6:
        failing += 1
    elif 1 <= grade <= 3:
        not_passed += 1

print("Відмінників:", excellent)
print("Імена відмінників:", ", ".join(excellent_names) if excellent_names else "немає")
print("Хорошистів:", good)
print("Відстаючих:", failing)
print("Не здали:", not_passed)






