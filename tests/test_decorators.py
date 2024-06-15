import os.path

import pytest

from src.decorators import log


def test_log_stdout(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест функции log, вывода в консоль"""

    @log()
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == f"{my_function.__name__} ok. Result: {result}\n"


def test_log_stdout_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест функции log, вывода в консоль и ошибки ValueError"""

    @log()
    def my_function(x: int, y: int) -> int:
        raise ValueError
        x + y

    with pytest.raises(ValueError):
        my_function(1.1, 5.1)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ValueError. Inputs: (1.1, 5.1), {}\n"


def test_log_file() -> None:
    """Тест функции log, вывода в файл"""

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        return x + y

    result = my_function(1, 2)

    with open(os.path.join(r"log", "mylog.txt"), "rt") as file:
        for line in file:
            msg = line
    assert msg == f"{my_function.__name__} ok. Result: {result}\n"


def test_log_file_error() -> None:
    """Тест функции log, вывода в файл и ошибки ValueError"""

    @log(filename="mylog.txt")
    def my_function(x: int, y: int) -> int:
        raise ValueError
        x + y

    with pytest.raises(ValueError):
        my_function(1.1, 0.1)
    with open(os.path.join(r"log", "mylog.txt"), "rt") as file:
        for line in file:
            msg = line
    assert msg == "my_function error: ValueError. Inputs: (1.1, 0.1), {}\n"
