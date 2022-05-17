import numpy as np

# Метод минимальной невязки
e = 1.0E-2  # погрешность решения


def min_discrepancies(A, b, x):
    r = A * x - b  # высчитываем направление невязки (вектор)
    # высчитываем коэф. поправки вектора невязки
    t = np.dot((A * r).transpose(), r) / (np.linalg.norm(A * r) ** 2)
    x = x - float(t) * r  # новое решение СЛАУ
    return A, b, x


def file_input():
    with open('data.txt', 'r') as file:
        matrix_height = int(file.readline())
        A = np.matrix([list(map(float, file.readline().split()))
                       for i in range(matrix_height)])
        b = np.matrix(list(map(float, file.readline().split()))).transpose()
        x = np.matrix(list(map(float, file.readline().split()))).transpose()
        return A, b, x


A, b, x = file_input()
file = open('out_data.txt', 'w', encoding='utf-8')
while np.linalg.norm(A * x - b) > e:
    # print(x.transpose())
    A, b, x = min_discrepancies(A, b, x)

file.write(f'Вектор решения с точностью {e} : {x.transpose()}')
