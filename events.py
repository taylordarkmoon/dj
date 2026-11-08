from typing import Any


def get_event_status(is_available: bool) -> str:
    """Возвращает текстовый статус (перенесено из ПР1)."""
    if is_available:
        return "Мероприятие доступно для регистрации"
    return "Мест нет или регистрация закрыта"


def add_event(
    events: list[dict[str, Any]],
    name: str,
    venue_id: int,
    date: str,
    price: float,
) -> None:
    """Добавляет новое мероприятие."""
    event_id = len(events) + 1
    event = {
        "id": event_id,
        "name": name,
        "venue_id": venue_id,
        "date": date,
        "price": price,
    }
    events.append(event)


def find_event(
    events: list[dict[str, Any]], query: str
) -> list[dict[str, Any]]:
    """Ищет мероприятия по названию."""
    return [e for e in events if query.lower() in e["name"].lower()]