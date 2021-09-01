import pytest

from lesson1.taskA import condition
from tests.imports import set_keyboard_input


@pytest.mark.parametrize(
    ["troom_tcond", "mode", "result"],
    [("10 20", "heat", 20), ("10 20", "freeze", 10)],
)
def test_condition_exampletests(capfd, troom_tcond, mode, result):
    set_keyboard_input([troom_tcond, mode])
    condition()
    output, stderr = capfd.readouterr()
    assert int(output) == result
