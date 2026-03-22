# TODO Напишите функцию для поиска индекса товара
def finding(spisok, one_thing):
    for i in range(len(spisok)):
        if spisok[i] == one_thing :
            return i
    #     перебираем все индексы и если значение под этим индексом совпадает с искомым, то выходим из цикла
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = finding(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
