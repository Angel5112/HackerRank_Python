# Programa para el Challenge de No Idea! de HackerRank

# Funcion para calcular la felicidad dependiendo de los elementos del array

def happiness(arr, set_a, set_b):
    happiness_level = 0
    for i in range(len(arr)):
        if arr[i] in set_a:
            happiness_level += 1
        elif arr[i] in set_b:
            happiness_level -= 1

    return happiness_level


if __name__ == '__main__':
    n, m = int(input().split())
    arr = list(map(int, input().split()))
    set_a = set(list(map(int, input().split())))
    set_b = set(list(map(int, input().split())))
    happiness_level = happiness(arr, set_a, set_b)
    print(happiness_level)