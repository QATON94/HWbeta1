import os
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize("arg_1, arg_2, expected_mess", [(1, 2, " foo ok"),
                                                         (1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                         (1, '0', " foo error: TypeError. Inputs: (1, '0'), {}")])
def test_log(arg_1: Any, arg_2: Any, expected_mess: str) -> None:
    """Тесты декоратора на получение данных в файл"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    @log(filename="test_log.txt")
    def foo(x, y):
        return x / y

    foo(arg_1, arg_2)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("test_log.txt", "r") as file:
        log_mess = file.read().strip()
    expected_log = now + expected_mess
    assert log_mess == expected_log


@pytest.mark.parametrize("arg_1, arg_2, expected_mess", [(1, 2, " foo ok"),
                                                         (1, 0, " foo error: ZeroDivisionError. Inputs: (1, 0), {}"),
                                                         (1, '0', " foo error: TypeError. Inputs: (1, '0'), {}")])
def test_console_log(capsys: Any, arg_1: Any, arg_2: Any, expected_mess: str) -> None:
    """Тесты декоратора на правильный вывод данных в консоль"""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    @log()
    def foo(x, y):
        return x / y

    foo(arg_1, arg_2)

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_mess = capsys.readouterr()
    expected_log = now + expected_mess
    assert log_mess.out.strip() == expected_log
