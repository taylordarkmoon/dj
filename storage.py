import json
import os
from typing import Any

DATA_DIR = "data"


def load_data(filename: str) -> list[dict[str, Any]]:
    """Загружает данные из JSON-файла."""
    filepath = os.path.join(DATA_DIR, filename)
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Ошибка чтения {filename}. Файл поврежден.")
        return []


def save_data(filename: str, data: list[dict[str, Any]]) -> None:
    """Сохраняет данные в JSON-файл."""
    os.makedirs(DATA_DIR, exist_ok=True)
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)