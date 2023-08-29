from simple_calculator.main import SimpleCalculator



def test_add_two_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(4,5)

    assert result == 9


def test_add_three_numbers():
    calculator = SimpleCalculator()

    result = calculator.add(5,5,5)

    assert result == 15


def test_add_fifteen_numbers():
    numbers = range(15)
    calculator = SimpleCalculator()

    result = calculator.add(*numbers)

    assert result == 105