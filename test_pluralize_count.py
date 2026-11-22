import pytest

import inflection


@pytest.mark.parametrize('count, word, expected', [
    (0, 'cat', '0 cats'), (1, 'cat', '1 cat'), (2, 'cat', '2 cats'),
    (2, 'person', '2 people'), (1, 'sheep', '1 sheep'),
    (3, 'sheep', '3 sheep'), (2, 'Person', '2 People'),
])
def test_pluralize_count(count: int, word: str, expected: str) -> None:
    assert inflection.pluralize_count(count, word) == expected


def test_pluralize_still_returns_only_the_word() -> None:
    assert inflection.pluralize('cat') == 'cats'
