import pytest


# Тесты для float
# Проверка умножения на ноль.
def test_float_multiplication_by_zero():
    assert 3.14 * 0 == 0


# Проверка на сравнение двух чисел
def test_float_comparison():
    assert abs(3.14 - 3.14159265359) > 0.0001


# Тесты для list
# Проверка обращения к элементу списка, который находится за его пределами.
def test_list_index():
    my_list = [1, 2, 3]

    try:
        my_list[10]
    except IndexError:
        pass

    assert len(my_list) == 3


# Проверка увеличения длины списка после добавления элемента.
def test_list_append_increases_length():
    lst = []
    lst.append(1)
    assert len(lst) == 1


# Тесты для tuple
@pytest.mark.parametrize("test_input, expected", [
    ((1, 2, 3), 6),   # Сумма элементов кортежа
    ((-1, -2, -3), -6),  # Сумма отрицательных элементов кортежа
    ((0, 0, 0), 0),   # Сумма нулевых элементов кортежа
])
# Параметризованный тест для проверки суммы элементов кортежа для разных входных данных.
def test_tuple_sum(test_input, expected):
    assert sum(test_input) == expected


# Проверка доступа ко второму элементу кортежа.
def test_tuple_second_element():
    assert (1, 2, 3)[1] == 2
