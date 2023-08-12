from typing import Union


class Calculator:
    def divide(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        # если принимаются не числа, то выдаём ошибку типа
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        # ошибка деления на 0
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y

    def add(self, x: Union[int, float], y: Union[int, float]) -> int | float:
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Both arguments should be numeric")
        return x + y


if __name__ == "__main__":
    calculator = Calculator()
