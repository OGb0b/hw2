import pytest
from src.main import binary_search

@pytest.mark.parametrize(
    'arr, target',
    [
        ([1, 2, None, 3, None, 4], 5),
        ([1, 2, None, None, 5, 6, 7, None, 10, 11], 7),
        ([1, 2, None, None, 5, 6, 7, None, 10, 11], 3),
        ([1, 2, None, None, 5, 6, 7, None, 10, 11], 10)

    ]
)
def binary_search(arr, target):
    assert binary_search(arr, target)