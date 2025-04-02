def calculate_bonus_score(score):
    # Визначаємо рейтинг і множник на основі кількості очок
    if 0 <= score <= 49:
        rating = "Початківець"
        multiplier = 1
    elif 50 <= score <= 69:
        rating = "Срібний гравець"
        multiplier = 1.5
    elif 70 <= score <= 89:
        rating = "Золотий гравець"
        multiplier = 2
    elif 90 <= score <= 100:
        rating = "Платиновий гравець"
        multiplier = 3
    else:
        rating = None
        multiplier = None
    
    if rating:
        final_score = score * multiplier
        return rating, final_score, multiplier
    else:
        return None, None, None

def main():
    try:
        # Користувач вводить кількість набраних очок
        score = int(input("Введіть кількість набраних очок (від 0 до 100): "))
        
        # Перевіряємо на коректність введення
        if score < 0 or score > 100:
            raise ValueError
        
        # Отримуємо рейтинг, фінальну кількість балів та множник
        rating, final_score, multiplier = calculate_bonus_score(score)
        
        # Виводимо результат
        if rating:
            print(f"Ваш рейтинг: {rating}! Ви отримали {final_score:.2f} балів (множник ×{multiplier})!")
        else:
            print("Некоректне введення! Кількість очок повинна бути в межах від 0 до 100.")
    
    except ValueError:
        print("Некоректне введення! Кількість очок повинна бути в межах від 0 до 100.")

# Викликаємо основну функцію для запуску програми
if __name__ == "__main__":
    main()
