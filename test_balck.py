my_list = [7, 5, 8, 2, 11, 1, 14]

# # Sorted
# my_list.sort(key=lambda x: x%2)
# print(my_list)
#
# # reverse
# my_list.reverse()
# print(my_list)

# result_list = [2, 'text', 456, 45.3, None]
#
# # copy
# copy_list = result_list.copy()
# print(copy_list)

# result_list = [2, 'text', 456, 45.3, None]
#
# # clear
# result_list.clear()
# print(result_list)

# my_set = {400, None, "text", True}
# print(my_set)

#list_01 = [4, 'strech', 81, 'a', 2]
#for i in range(0, list_01):
 #   type(list_01(i))

# print(type([4, 'strech', 81, 'a', 2]))


def copy_file(file_name, file_name_new):
    with open(file_name, 'r', encoding="utf-8", newline='') as file:
        # reader = DictReader(file)
        list_1 = read_file(file_name)

        y = int(input(f"Выберите номер строки от 1 до {len(list_1)}: "))
        obj = list_1[y - 1]
        res = []
        res.append(obj)

        with open(file_name_new, 'w', encoding="utf-8", newline='') as data:
            fieldnames = ['Имя', 'Фамилия', 'Телефон']  # Replace with appropriate header names
            f_writer = DictWriter(data, fieldnames=fieldnames)
            f_writer.writeheader()
            f_writer.writerows(res)
