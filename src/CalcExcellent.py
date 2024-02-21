from Types import DataType


class CalcExcellent:
    """Поиск студента с идеальными баллами"""
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def calc(self) -> str or None:
        for name, scores in self.data.items():
            for subject, score in scores:
                if score != 100:
                    return None
            else:
                return name
