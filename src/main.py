# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XMLDataReader import XMLDataReader
from CalcExcellent import CalcExcellent


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])    # 'data//data.xml'

    # Выбор класса для чтения файла по его расширению
    *name, ext = path.split(".")
    if ext == "txt":
        reader = TextDataReader()
    elif ext == "xml":
        reader = XMLDataReader()
    else:
        print("Неподдерживаемый формат файла")
        return

    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    # Выбор студента с оценками 100 по всем предметам
    excellent = CalcExcellent(students).calc()
    if excellent is None:
        print("Excellent student not found")
    else:
        print("Excellent student:", excellent)


if __name__ == "__main__":
    main()
