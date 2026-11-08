from typing import Any
import storage
import events
import venues
import registrations
import utils


def show_events(events_list: list[dict[str, Any]]) -> None:
    """Выводит список всех мероприятий."""
    if not events_list:
        print("Мероприятий пока нет.")
        return
    for event in events_list:
        print(
            f"ID: {event['id']} | {event['name']} | "
            f"Дата: {event['date']} | Цена: {event['price']} руб."
        )


def main() -> None:
    """Точка запуска приложения и главное меню."""
    venues_list = storage.load_data("venues.json")
    events_list = storage.load_data("events.json")
    regs_list = storage.load_data("registrations.json")

    # Начальные данные, если база пуста
    if not venues_list:
        venues.add_venue(venues_list, "Лофт 'Код'", 50)
        storage.save_data("venues.json", venues_list)
    if not events_list:
        events.add_event(events_list, "Python-митап", 1, "2026-12-10", 1500.0)
        storage.save_data("events.json", events_list)

    while True:
        print("\n=== СЕРВИС МЕРОПРИЯТИЙ ===")
        print("1. Показать все мероприятия")
        print("2. Зарегистрироваться на мероприятие")
        print("3. Проверить статус мест")
        print("0. Выход")
        
        choice = input("Выберите действие: ")

        if choice == "1":
            show_events(events_list)
        elif choice == "2":
            event_id = utils.input_int("Введите ID мероприятия: ")
            user_name = input("Введите ваше имя: ")
            success = registrations.create_registration(
                events_list, venues_list, regs_list, event_id, user_name
            )
            if success:
                storage.save_data("registrations.json", regs_list)
        elif choice == "3":
            event_id = utils.input_int("Введите ID мероприятия: ")
            is_avail = registrations.is_spot_available(
                events_list, venues_list, regs_list, event_id
            )
            print(events.get_event_status(is_avail))
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()