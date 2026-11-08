from typing import Any


def add_venue(
    venues: list[dict[str, Any]], name: str, capacity: int
) -> None:
    """Добавляет новую площадку."""
    venue_id = len(venues) + 1
    venue = {"id": venue_id, "name": name, "capacity": capacity}
    venues.append(venue)


def find_venue(
    venues: list[dict[str, Any]], query: str
) -> list[dict[str, Any]]:
    """Ищет площадку по названию."""
    return [v for v in venues if query.lower() in v["name"].lower()]


def get_venue_by_id(
    venues: list[dict[str, Any]], venue_id: int
) -> dict[str, Any] | None:
    """Возвращает площадку по ID."""
    for venue in venues:
        if venue["id"] == venue_id:
            return venue
    return None