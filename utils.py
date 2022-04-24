import json

import requests

from AAAAAAAAAAAA import list_elements
from config import keys


class CalculationException(Exception):
    pass


class MassCalculation:
    @staticmethod
    def result(vvod: str):
        try:
            for i in list_elements:
                elements_ticker = keys[list_elements[i]]
        except KeyError:
            raise CalculationException(f'Некорректный ввод вещества')