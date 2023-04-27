# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

my_list = [1,2,2,3,4,4,5,5,5,6,7,88]
new_list = []
for i in range(len(my_list)):
    if my_list.count(my_list[i])>1:
        new_list.append(my_list[i])

print(list(set(new_list)))



