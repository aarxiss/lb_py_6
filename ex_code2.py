import random
import time

def game():
    # Генерація випадкового тризначного коду
    code = random.randint(100, 999)
    attempts_left = 5

    print("Ваша задача — зламати код сейфу за 5 спроб!")
    
    while attempts_left > 0:
        try:
            # Введення числа гравцем
            guess = int(input(f"Введіть тризначний код (залишилось {attempts_left} спроб): "))
            
            # Перевірка чи введено правильний код
            if guess == code:
                print("Вітаємо! Ви вгадали код сейфу!")
                break
            elif guess < code:
                print("Код більший!")
            else:
                print("Код менший!")
        
        except ValueError:
            print("Помилка: введено нечислове значення! Спробуйте ще раз.")
        
        finally:
            attempts_left -= 1  # Зменшення кількості спроб
            if attempts_left == 0:
                print(f"Ви вичерпали всі спроби. Код сейфу був: {code}")
            else:
                print(f"Залишилось {attempts_left} спроб.")
                
            time.sleep(1)  # Додаємо паузу між спробами

# Запуск гри
game()
