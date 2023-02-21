# Programa para el challenge de set.add()

# Funcion para agregar el nombre de un pais al set

def add_country(n):
    country_set = set([input() for i in range(1, n + 1)])
    return len(country_set)


if __name__ == '__main__':
    N = int(input())
    country_stamp_counter = add_country(N)
    print(country_stamp_counter)
