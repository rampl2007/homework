# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

import random
a, b, c = random.randint(0,2), random.randint(3,5), random.randint(6,8)
print(f"Три песни {my_favorite_songs[a][0]}, {my_favorite_songs[b][0]}, {my_favorite_songs[c][0]}", end="") 
print(f' звучат {round(my_favorite_songs[a][1] + my_favorite_songs[b][1] + my_favorite_songs[c][1])} минут')

# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# сделал из словаря список списков
my_favorite_songs_2 = []
for song in my_favorite_songs_dict:
    my_favorite_songs_2.extend([[song, my_favorite_songs_dict[song]]])

# print(my_favorite_songs_2)

# список из трех рандомных песен
import random

random_songs = []
count = 0

while count < 3:
    random_songs.append(my_favorite_songs_2[random.randint(0, len(my_favorite_songs_2) - 1)])
    count += 1

# print(random_songs)

# вывод
print(f"Три песни {random_songs[0][0]}, {random_songs[1][0]}, {random_songs[2][0]}", end="") 
print(f' звучат {sum([i[1] for i in random_songs])} минут')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 

