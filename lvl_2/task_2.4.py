# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):

    s1 = ""
    s1 = s.replace("!", "")
    return s1


foo, foo1, foo2 = ("Hi! Hello!"), (""), ("Oh, no!!!")

print("Результат выполнения функции 1 : ", remove_exclamation_marks(foo))
print("Результат выполнения функции 1 : ", remove_exclamation_marks(foo1))
print("Результат выполнения функции 1 : ", remove_exclamation_marks(foo2))

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):

    s1 = ""
    if s[-1] == "!":
        s1 = s[0:-1]
        return s1
    else:
        return s


remove, remove1, remove2 = "Hi!", "Hi!!!", "!Hi"

print("Результат выполнения функции 2: ", remove_last_em(remove))
print("Результат выполнения функции 2: ", remove_last_em(remove1))
print("Результат выполнения функции 2: ", remove_last_em(remove2))

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):

    s1 = s.split()
    s2 = ""

    for i in range(len(s1)):    # проход по элементам списка
        
        count = 0
        for el in s1[i]:        # проход по символам элемента
            
            if el == "!":       # подсчет количества искомых символов
                count += 1
                
        if count != 1:          # если количество не равно 1 добавляем значение элемента списка в новую строку
            s2 = s2 + "".join(s1[i]) + " "
            
    return s2


rem1, rem2, rem3, rem4, rem5, rem6, rem7 = "Hi!", "Hi! Hi!", "Hi! Hi! Hi!", "Hi Hi! Hi!", "Hi! !Hi Hi!", "Hi! Hi!! Hi!", "Hi! !Hi! Hi!"
rem8 = "Hi! Hi! Hi! Hi! Q!!!!! Hi! Hi! Hi Hi! Hi! !R!!! Hi! !Hi Hi! Hi! Hi!! P! Hi! Hi! !Hi! Hi!"

print("Результат выполнения функции 3: ", remove_word_with_one_em(rem1))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem2))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem3))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem4))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem5))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem6))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem7))
print("Результат выполнения функции 3: ", remove_word_with_one_em(rem8))