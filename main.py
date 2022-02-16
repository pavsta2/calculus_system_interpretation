from abc import ABC, abstractmethod
from typing import Union


class NumberInterpretFactoryMethod(ABC):
    """
    Абстракиный метод инициализации интерпретаторов чисел
    """

    @abstractmethod
    def get_number_interpret(self):
        pass


class From2To10CalcSysNumberInterpretFactoryMethod(NumberInterpretFactoryMethod):
    """
    Инициализация интерпретатора чисел между системами от двоичной до десятичной.
    """

    def get_number_interpret(self):
        value = int(input("Введите Ваше число"))
        sys = int(input("В какой системе исисления оно выражено?"))
        new_sys = int(input("В какую систему исчисления Вы хотите перевести число?"))
        return NumberInterpretIn2Till10CalcSys(value, sys, new_sys)


class From2To16CalcSysNumberInterpretFactoryMethod(NumberInterpretFactoryMethod):
    """
    Инициализация интерпретатора чисел между системами от 2 до 16ричной.
    """

    def get_number_interpret(self):
        value = input("Введите Ваше число")
        sys = int(input("В какой системе исисления оно выражено?"))
        new_sys = int(input("В какую систему исчисления Вы хотите перевести число?"))
        return NumberInterpretIn11Till16CalcSys(value, sys, new_sys)


class NumberInterpret(ABC):
    """Абстрактный класс - интерфейс конечного интерпретатора, где д.б.
    два метода: сначала перевод в десятичную систему и потом в любую другую"""
    @abstractmethod
    def value_in_10_calc_sys(self) -> int:
        pass

    @abstractmethod
    def change_calc_sys(self, *args, **kwargs) -> int:
        pass


class NumberInterpretIn2Till10CalcSys(NumberInterpret):
    """
    Перевод числа в системы исчисления от двоичной до десятичной
    """

    def __init__(self, value: int, sys: int, new_sys: int):
        self.value = value
        self.sys = sys
        self.new_sys = new_sys

    def value_in_10_calc_sys(self) -> int:
        if self.sys == 10:
            value_in_10 = self.value
            return value_in_10
        list_ = list(str(self.value))
        list_d = [int(d) for d in list_]
        value_in_10 = 0
        dig = len(list_d) - 1
        for i in list_d:
            value_in_10 += i * (self.sys ** dig)
            dig -= 1
        return value_in_10

    def change_calc_sys(self) -> int:
        operation_div = self.value_in_10_calc_sys()
        operation_ost = self.value_in_10_calc_sys() % self.new_sys
        result = []
        while operation_div >= self.new_sys:
            result.append(operation_ost)
            operation_div = operation_div // self.new_sys
            operation_ost = operation_div % self.new_sys
        result.append(operation_div)
        result.reverse()
        result = int("".join([str(d) for d in result]))
        return result


class NumberInterpretIn11Till16CalcSys(NumberInterpret):
    """
    Перевод числа в системы исчисления с 11 по 16-ую
    """
    symbol_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    def __init__(self, value: Union[int, str], sys: int, new_sys: int):
        self.value = value
        self.sys = sys
        self.new_sys = new_sys

    def value_in_10_calc_sys(self) -> int:
        d = self.symbol_dict
        if self.sys == 10:
            value_in_10 = self.value
            return value_in_10
        elif self.sys < 10:
            list_ = list(str(self.value))
            list_d = [int(d) for d in list_]
            value_in_10 = 0
            dig = len(list_d) - 1
            for i in list_d:
                value_in_10 += i * (self.sys ** dig)
                dig -= 1
            return value_in_10
        else:
            list_ = list(str(self.value))
            for key in d.keys():
                if key in list_:
                    list_[list_.index(key)] = d[key]
            list_d = [int(d) for d in list_]
            value_in_10 = 0
            dig = len(list_d) - 1
            for i in list_d:
                value_in_10 += i * (self.sys ** dig)
                dig -= 1
            return value_in_10

    def change_calc_sys(self) -> Union[int, str]:
        d = self.symbol_dict
        operation_div = self.value_in_10_calc_sys()
        operation_ost = self.value_in_10_calc_sys() % self.new_sys
        result = []
        while operation_div >= self.new_sys:
            if operation_ost > 9:
                operation_ost = d[operation_ost]
            result.append(operation_ost)
            operation_div = operation_div // self.new_sys
            operation_ost = operation_div % self.new_sys
        if operation_div > 9:
            operation_div = d[operation_div]
        result.append(operation_div)
        result.reverse()
        result = ("".join([str(d) for d in result]))
        return result


if __name__ == "__main__":
    a = NumberInterpretIn11Till16CalcSys(50, 11, 10)

    print(a.change_calc_sys())
    # symbol_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    # for key, value in enumerate(symbol_dict):
    #     print(key, value)
