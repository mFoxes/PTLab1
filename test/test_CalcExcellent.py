from src.Types import DataType
from src.CalcExcellent import CalcExcellent
import pytest


class TestCalcExcellent:

    @pytest.fixture()
    def input_data_success(self) -> tuple[DataType, str]:
        data = {
            'Иванов Иван Иванович':
                [
                    ('математика', 100),
                    ('литература', 100),
                    ('программирование', 100)
                ],
            'Петров Петр Петрович':
                [
                    ('математика', 78),
                    ('химия', 87),
                    ('социология', 61)
                ]
        }

        result = 'Иванов Иван Иванович'

        return data, result

    @pytest.fixture()
    def input_data_fail(self) -> DataType:
        data = {
            'Иванов Иван Иванович':
                [
                    ('математика', 100),
                    ('литература', 100),
                    ('программирование', 99)
                ],
            'Петров Петр Петрович':
                [
                    ('математика', 78),
                    ('химия', 87),
                    ('социология', 61)
                ]
        }

        return data

    def test_init_calc_excellent(self, input_data_success) -> None:
        calc_rating = CalcExcellent(input_data_success[0])
        assert input_data_success[0] == calc_rating.data

    def test_success(self, input_data_success: tuple[DataType, str]):
        e = CalcExcellent(input_data_success[0])
        result = e.calc()
        assert result == input_data_success[1]

    def test_fail(self, input_data_fail: DataType):
        e = CalcExcellent(input_data_fail)
        result = e.calc()
        assert result is None
