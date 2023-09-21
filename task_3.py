import random

my_dict = {"фонарик": 5, "спальник": 10,
           "аптечка": 7, "тушенка": 25,
           "вода": 15, "хлеб": 10,
           "одежда": 25, "компас": 5}

max_load = 50
count = 0
my_list_things = []
while count < max_load:
    key, value = random.choice(list(my_dict.items()))
    if key in my_list_things:
        continue
    if count + value > max_load:
        break
    count += value
    my_list_things += (str(key), str(value))
print(my_list_things, "=", count)