# TODO решите задачу
import  json
# импортируем библиотеку. чтобы использовать функции из нее

json_file = "input.json"
# передаем файл в переменную
def task() -> float:
    with open(json_file, 'r', encoding='utf-8') as file:
        out_file = json.load(file)
        # открываем файл для чтения с сохранением русских букв и десериализировали
        # его содержимое в объект Python.
        return round(sum([i["score"] * i["weight"] for i in out_file]), 3)

#   проходимся по каждому словарю и умножаем значения по ключам

print(task())
