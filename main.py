import pytest

# Функция для проверки четности числа
def is_even(number):
    return number % 2 == 0

# Функция для проверки четности чисел в списке
def all_even(numbers):
    return all(is_even(number) for number in numbers)

# Тесты для float
def test_float_valid_even():
    assert is_even(2.0) == True

def test_float_valid_odd():
    assert is_even(1.5) == False

# Тесты для list
def test_list_valid_even():
    assert all_even([2, 4, 6]) == True

def test_list_valid_odd():
    assert all_even([1, 3, 5]) == False

# Тесты для tuple
def test_tuple_valid_even():
    assert all_even((2, 4, 6)) == True

def test_tuple_valid_odd():
    assert all_even((1, 3, 5)) == False

# Параметризованный тест для проверки четности
@pytest.mark.parametrize("number", [-100, -1, 0, 1, 100])
def test_is_even_valid(number):
    assert is_even(number) == (number % 2 == 0)

# Параметризованный тест для проверки нечетности
@pytest.mark.parametrize("number", [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_is_even_invalid(number):
    assert is_even(number) == (number % 2 == 0)

# Негативный тест на деление на ноль
def test_division_by_zero():
    try:
        assert 1 / 0
    except ZeroDivisionError:
        pass