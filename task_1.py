list_element = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8]
count = 0
set_list_element = []
for i in list_element:
    for j in list_element:
        if i == j:
            count += 1
            if j not in set_list_element and count > 1:
                set_list_element.append(j)
    count = 0
print(set_list_element)