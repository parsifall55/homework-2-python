import numpy as np

# 1. Створення одновимірного масиву з 200 випадкових чисел від -100 до 100
arr = np.random.randint(-100, 101, 200)

print("Початковий масив:")
print(arr)

# 2. Використовуючи маску, відфільтровуємо всі додатні числа
positive_mask = arr > 0
positive_numbers = arr[positive_mask]

print("\nДодатні числа масиву:")
print(positive_numbers)

# 3. Замінюємо всі від’ємні значення на нулі
modified_arr = arr.copy()
modified_arr[modified_arr < 0] = 0

print("\nМасив після заміни від’ємних значень на нулі:")
print(modified_arr)

# 4. Обчислюємо середнє значення отриманого масиву
average_value = np.mean(modified_arr)

print("\nСереднє значення отриманого масиву:")
print(average_value)