# Problema de Introduccion a Sets de HackerRank

# Funcion para calcular el average dado por la formula del problema

def average(array):
    unique_arr = set(array)
    for i in range(len(unique_arr)):
        sum = sum + unique_arr[i]
    
    average = sum / len(unique_arr)
    return average


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)