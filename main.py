# Импорт модуля для работы с датами (требование ПР1)
from datetime import date

# --- Исходные данные (простые типы) ---
event_name = "Python-митап"
venue_name = "Лофт 'Код'"
venue_capacity = 50       # Вместимость площадки (int)
registered_count = 45     # Уже зарегистрировано (int)
base_price = 1500.0       # Базовая цена (float)
is_early_bird = True      # Ранняя регистрация (bool)
event_date = date(2026, 12, 10)
user_name = "Иван"
user_role = "participant" # Роль пользователя (str)


# --- Функция 1: Проверка доступности мест ---
def check_availability(capacity, registered):
    """Проверяет, остались ли свободные места."""
    if registered < capacity:
        free_seats = capacity - registered
        # Преобразование типов при выводе
        return "Есть места! Свободно: " + str(free_seats)
    else:
        return "Мест нет. Регистрация закрыта."


# --- Функция 2: Расчет стоимости билета ---
def calculate_price(price, early_bird):
    """Считает цену с учетом скидки 20% за раннюю регистрацию."""
    if early_bird == True:
        discount = price * 0.20
        final_price = price - discount
        return final_price
    else:
        return price


# --- Функция 3: Приветствие по роли ---
def get_greeting(name, role):
    """Возвращает приветствие в зависимости от роли."""
    if role == "organizer":
        return f"Здравствуйте, {name}! Вы вошли как организатор."
    elif role == "participant":
        return f"Привет, {name}! Рады видеть вас как участника."
    else:
        return f"Привет, {name}! Ваша роль пока не определена."


# --- Основной сценарий программы ---
print("=== СЕРВИС МЕРОПРИЯТИЙ ===")
print(get_greeting(user_name, user_role))
print("Мероприятие:", event_name)
print("Площадка:", venue_name)
print("Дата проведения:", event_date)
print("-----------------------------")

# Вызов функций и вывод результатов
status = check_availability(venue_capacity, registered_count)
print("Статус мест:", status)

ticket_price = calculate_price(base_price, is_early_bird)
print("Стоимость билета:", ticket_price, "руб.")