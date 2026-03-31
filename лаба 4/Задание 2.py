# TODO импортировать необходимые молули
import  json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as file:
        # открываем для чтения исходный файл
        data = [i for i in csv.DictReader(file, delimiter=',', quotechar="\n")]
    #     создаем список, в котором рассматриваем каждую строку как словарь, с разденителем значений
    #     по запятой и переносом, как символом следующей строки
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as file:
        # отурываем файл для записи
        json.dump(data, file, ensure_ascii=False, indent=4 )
    #     Методом dump сериализуем данные и записываем их в файловый объект с отступами в 4

    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()
    with open(OUTPUT_FILENAME) as output_f:
        # считываем файл
        for line in output_f:
            # проходимся по каждой строке
            print(line, end="")