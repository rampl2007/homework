# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


# функция сортировки методом вставки
def insertion(data):
  n = len(data)
  for i in range(n):
    j = i -1
    val = data[i]
    while data[j] > val and j >= 0:
      data[j +1] = data[j]
      j -= 1
    data[j +1] = val
  return(data)

def minimum(arr):
    for data in arr:
       return insertion(arr)[0]

def maximum(arr):
    for data in arr:
       return insertion(arr)[len(arr) - 1]
    
# функция вывода     
def print_array(arr):
   for i in range(len(arr)):
    print(f"{arr[i]}       -> max = {maximum(arr[i])}, min = {minimum(arr[i])}")
   
    
array = [[4,6,2,1,9,63,-134,566],
         [-52, 56, 30, 29, -54, 0, -110],
         [42, 54, 65, 87, 0],
         [5]
        ]
    
print_array(array)


