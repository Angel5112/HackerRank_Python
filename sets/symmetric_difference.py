# Programa para resolver el desafio de Symmetric Difference de Hackerrank

# Funcion para hallar la diferencia simetrica y ordenar sus elementos

def symmetric_difference(set_a, set_b):
    aux_set_a = set_a.difference(set_b)
    aux_set_b = set_b.difference(set_a)
    symmetric_diff = list(aux_set_a.union(aux_set_b))
    symmetric_diff.sort()
    return symmetric_diff


# Funcion para imprimir de uno a uno los elementos de la diferencia simetrica

def print_symmetric_difference(s_diff):
    for i in range(len(s_diff)):
        print(s_diff[i])    


if __name__ == '__main__':
    M = int(input())
    set_M = set(list(map(int, input().split())))
    N = int(input())
    set_N = set(list(map(int, input().split())))
    s_difference = symmetric_difference(set_M, set_N)
    print_symmetric_difference(s_difference)
    