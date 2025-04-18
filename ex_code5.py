import random

def stage_1():
    try:
        # Гравець вводить кількість деревини для побудови плоту
        wood = int(input("Введіть кількість деревини для побудови плоту (від 1 до 10): "))
        
        # Перевірка, чи кількість деревини достатня
        if wood < 3:
            print("Деревини замало, пліт затонув!")
            return False  # Гра завершена
    except ValueError:
        # Якщо введено нечислове значення
        print("Це не число!")
        return False  # Гра завершена
    
    return True  # Перехід до наступного етапу

def stage_2():
    try:
        # Гравець обирає спосіб втечі
        escape_choice = input("Обирайте спосіб втечі: 'бігти', 'сховатися', 'битися': ").lower()

        # Перевірка введеного варіанту
        if escape_choice not in ['бігти', 'сховатися', 'битися']:
            raise ValueError("Такого варіанту немає")
    except ValueError:
        # Обробка помилки, якщо вибір неправильний
        print("Такого варіанту немає, пірати вас спіймали!")
        return False  # Гра завершена
    
    return True  # Перехід до наступного етапу

def stage_3():
    # Генеруємо секретний код (двозначне число)
    secret_code = random.randint(10, 99)
    
    try:
        # Гравець вводить секретний код
        player_code = int(input("Введіть секретний код для відкриття скрині (двозначне число): "))
        
        # Перевірка правильності коду
        if player_code != secret_code:
            print("Неправильний код, скриня вибухнула! Гру завершено.")
            return False  # Гра завершена
        else:
            print("Скарб ваш, ви врятовані!")
    except ValueError:
        # Обробка помилки, якщо введено нечислове значення
        print("Це не число!")
        return False  # Гра завершена

    return True  # Гра завершена успішно

def main():
    print("Ви опинилися на острові піратів і повинні втекти!")
    
    # Етап 1: Перетин річки
    if not stage_1():
        print("Гра завершена.")
        return
    
    # Етап 2: Втеча від піратів
    if not stage_2():
        print("Гра завершена.")
        return
    
    # Етап 3: Відкриття скрині зі скарбами
    if not stage_3():
        print("Гра завершена.")
        return
    
    print("Вітаємо, ви успішно втекли з острова піратів!")

# Завжди виводимо повідомлення в кінці гри
try:
    main()
finally:
    print("Гра завершена. Дякуємо за участь у пригоді!")
