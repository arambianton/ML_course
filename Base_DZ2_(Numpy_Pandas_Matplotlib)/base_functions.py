from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n 
    и c 120 по 500 c шагом 5 по оси размерности m
    """
    result = []
    for i in range(0, len(X), 4):
        row = []
        for j in range(120, 500, 5):
            row.append(X[i][j])
        result.append(row)
    return result


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    n = len(X)
    m = len(X[0]) if n > 0 else 0
    diag_len = min(n, m)

    s = 0
    count = 0
    for i in range(diag_len):
        if X[i][i] >= 0:
            s += X[i][i]
            count += 1

    return s if count > 0 else -1


def replace_values(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    n = len(X)
    m = len(X[0]) if n > 0 else 0
    result = deepcopy(X)

    for j in range(m):
        col = [X[i][j] for i in range(n)]
        M = sum(col) / n
        for i in range(n):
            if result[i][j] < 0.25 * M or result[i][j] > 1.5 * M:
                result[i][j] = -1
    return result
