# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.XMLDataReader import XMLDataReader


class TestXMLDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '''<root>
                    <student name="Иванов Иван Иванович">
                        <subject name="математика">100</subject>
                        <subject name="литература">100</subject>
                        <subject name="программирование">100</subject>
                    </student>
                    <student name="Петров Петр Петрович">
                        <subject name="математика">78</subject>
                        <subject name="химия">87</subject>
                        <subject name="социология">61</subject>
                    </student>
                  </root>'''
        data = {
            "Иванов Иван Иванович": [
                ("математика", 100),
                ("литература", 100),
                ("программирование", 100)
            ],
            "Петров Петр Петрович": [
                ("математика", 78),
                ("химия", 87),
                ("социология", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = XMLDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
