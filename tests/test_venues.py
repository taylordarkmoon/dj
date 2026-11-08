from venues import add_venue, find_venue


def test_add_venue():
    venues = []
    add_venue(venues, "Тестовая площадка", 100)
    assert len(venues) == 1
    assert venues[0]["capacity"] == 100


def test_find_venue():
    venues = [{"id": 1, "name": "Лофт", "capacity": 50}]
    result = find_venue(venues, "лофт")
    assert len(result) == 1