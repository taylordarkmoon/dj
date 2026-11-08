from typing import Any


def is_spot_available(
    events: list[dict[str, Any]],
    venues: list[dict[str, Any]],
    registrations: list[dict[str, Any]],
    event_id: int,
) -> bool:
    """Проверяет, есть ли свободные места на мероприятии."""
    event = next((e for e in events if e["id"] == event_id), None)
    if not event:
        return False

    venue = next((v for v in venues if v["id"] == event["venue_id"]), None)
    if not venue:
        return False

    # Считаем количество регистраций на это мероприятие
    registered_count = sum(
        1 for r in registrations if r["event_id"] == event_id
    )
    return registered_count < venue["capacity"]


def create_registration(
    events: list[dict[str, Any]],
    venues: list[dict[str, Any]],
    registrations: list[dict[str, Any]],
    event_id: int,
    user_name: str,
) -> bool:
    """Регистрирует участника, если есть места."""
    if not is_spot_available(events, venues, registrations, event_id):
        print("Ошибка: свободных мест нет.")
        return False

    reg_id = len(registrations) + 1
    registration = {
        "id": reg_id,
        "event_id": event_id,
        "user_name": user_name,
    }
    registrations.append(registration)
    print(f"Участник {user_name} успешно зарегистрирован!")
    return True