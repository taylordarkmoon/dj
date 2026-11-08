from events import add_event, get_event_status


def test_add_event():
    events = []
    add_event(events, "Митап", 1, "2026-12-10", 1000.0)
    assert len(events) == 1


def test_get_event_status():
    assert get_event_status(True) == "Мероприятие доступно для регистрации"
    assert get_event_status(False) == "Мест нет или регистрация закрыта"