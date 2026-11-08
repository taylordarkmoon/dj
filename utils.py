from datetime import datetime


def input_int(prompt: str) -> int:
    """Запрашивает целое число с обработкой ошибок."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")


def input_date(prompt: str) -> str:
    """Запрашивает дату в формате ГГГГ-ММ-ДД."""
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Ошибка: неверный формат даты. Используйте ГГГГ-ММ-ДД.")


def input_float(prompt: str) -> float:
    """Запрашивает число с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число (например, 1500.50).")