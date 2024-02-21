from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class XMLDataReader(DataReader):
    """Чтение данных из xml файла"""
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)   # Создание дерева элементов
        root = tree.getroot()   # Получение корня дерева

        # Обход всех студентов, описанных в файле
        for student in root:
            self.students[student.attrib["name"]] = \
                [(subject.attrib["name"], int(subject.text))
                 for subject in student]

        return self.students
