# TODO Напишите функцию find_common_participants
def find_common_participants(company_1,company_2, r = ','):
    list_1 = set(company_1.split(r))
    list_2 = set(company_2.split(r))
    same_list = sorted(list(list_1.intersection(list_2)))
    # приводим обе строки к множеству, выбираем общее и сортируем
    return same_list

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
