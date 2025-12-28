from collections import Counter
from typing import List


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return sorted(x) == sorted(y)


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    max_prod = -1
    for i in range(len(x) - 1):
        a, b = x[i], x[i+1]
        if a % 3 == 0 or b % 3 == 0:
            prod = a * b
            if prod > max_prod:
                max_prod = prod
    return max_prod


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    h, w, c = len(image), len(image[0]), len(image[0][0])
    result = [[0.0 for _ in range(w)] for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            s = 0.0
            for k in range(c):
                s += image[i][j][k] * weights[k]
            result[i][j] = s
    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    i, j = 0, 0
    res = 0
    len_x = sum(c for _, c in x)
    len_y = sum(c for _, c in y)

    if len_x != len_y:
        return -1

    cx, cy = x[0][1], y[0][1]   # оставшиеся повторы
    vx, vy = x[0][0], y[0][0]   # текущие значения

    while i < len(x) and j < len(y):
        k = min(cx, cy)         # сколько элементов совпадает по длине
        res += vx * vy * k

        cx -= k
        cy -= k

        if cx == 0:
            i += 1
            if i < len(x):
                vx, cx = x[i]
        if cy == 0:
            j += 1
            if j < len(y):
                vy, cy = y[j]

    return res

def scal_prod(x,y):
    s=0
    for i in range(len(x)):
        s+=x[i]*y[i]
    return s
    
def cosinus(x, y):
    num = scal_prod(x, y)
    den = 0
    for elem in x:
        den += elem*elem
    temp = 0
    for elem in y:
        temp += elem*elem
    denominator = (temp ** (1/2)) * (den ** (1/2))
    return num/denominator

def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    mas = [0] * len(X) 
    for i in range(len(X)): 
        mas[i] = [0] * len(Y)
    for index in range(len(X)):
        zero = [0]*len(X[i])
        for j in range(len(Y)):
            mas[index][j] = cosinus(X[index], Y[j]) if (X[index] != zero and Y[j] != zero) else 1
    return mas