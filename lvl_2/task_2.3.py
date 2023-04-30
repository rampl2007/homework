# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


def switch_it_up(number):
    lst = ['ноль','один','два','три','четыре','пять','шесть','семь','восемь','девять']
    try:
        return lst[number]
    except:
        return "Введённая цифра не попадает в диапазон от 0 до 9."
    

number = int(input("Введите цифру от 0 до 9: "))

if number >= 0 and number < 10:
    print(switch_it_up(number))
else:
    print("Введённый символ не попадает в диапазон от 0 до 9.")   