# Задача 1.1.

# Есть строка с перечислением песен

# во второй песне похоже опечатка (Staying\' Alive), вывел как есть :)

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

print(my_favorite_songs[0:13])
print(my_favorite_songs[64:])
print(my_favorite_songs[16:30])
print(my_favorite_songs[-61:-47])

# Да, но можно решить задачку, используя встроенные методы строк
# Например
# Решение с помощью индексации строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
