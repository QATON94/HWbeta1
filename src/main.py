from src.processing import choice_state, sort_date
from src.widget import get_data


def main() -> None:
    list_data = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, ]

    print(choice_state(list_data))
    print(sort_date(list_data))
    print(get_data("2018-07-11T02:26:18.671407"))


if __name__ == "__main__":
    main()
