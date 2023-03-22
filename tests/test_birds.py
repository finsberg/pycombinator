import pytest

from pycombinator import birds


@pytest.mark.parametrize(
    "input, expected_output",
    [
        ("tweet", "tweet"),
        ("chirp", "chirp"),
        (birds.Idiot, birds.Idiot),
    ],
)
def test_Idiot(input, expected_output) -> None:
    output = birds.Idiot(input)
    assert output == expected_output


def test_MockingBird_with_Idiot() -> None:
    output = birds.MockingBird(birds.Idiot)
    assert output == birds.Idiot


def test_MockingBird_with_MockingBird_raises_RecursionError() -> None:
    with pytest.raises(RecursionError):
        birds.MockingBird(birds.MockingBird)
