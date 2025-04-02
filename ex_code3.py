import random

# Функція для визначення переможця
def determine_winner(player_choice, computer_choice):
    # Правила гри
    rules = {
        "камінь": ["ножиці", "ящірка"],
        "ножиці": ["папір", "ящірка"],
        "папір": ["камінь", "Спок"],
        "ящірка": ["папір", "Спок"],
        "Спок": ["ножиці", "камінь"]
    }
    
    if player_choice == computer_choice:
        return "Нічия!"
    elif computer_choice in rules[player_choice]:
        return "Ви виграли!"
    else:
        return "Ви програли!"

# Список варіантів для вибору
choices = ["камінь", "ножиці", "папір", "ящірка", "Спок"]

# Головна функція гри
def play_game():
    print("Вітаємо в грі Камінь-Ножиці-Папір-Ящірка-Спок!")
    print("Доступні варіанти: камінь, ножиці, папір, ящірка, Спок.")
    
    # Запитуємо вибір користувача
    player_choice = input("Ваш вибір: ").lower()
    
    if player_choice not in choices:
        print("Невірний вибір! Спробуйте знову.")
        return
    
    # Комп'ютер вибирає випадковий варіант
    computer_choice = random.choice(choices)
    
    print(f"Комп'ютер вибрав: {computer_choice}")
    
    # Визначаємо переможця
    result = determine_winner(player_choice, computer_choice)
    
    print(result)

# Викликаємо функцію для запуск
