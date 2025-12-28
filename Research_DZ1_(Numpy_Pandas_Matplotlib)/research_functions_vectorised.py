import numpy as np


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    x_arr, y_arr = np.array(x), np.array(y)
    return np.array_equal(np.sort(x_arr), np.sort(y_arr))


def max_prod_mod_3(x: np.ndarray) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    arr = np.array(x)
    prod = arr[:-1] * arr[1:]
    mask = (arr[:-1] % 3 == 0) | (arr[1:] % 3 == 0)
    
    if not np.any(mask):
        return -1
    
    return prod[mask].max()


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    return np.dot(image, weights)


def myfunc(a):
    return np.array([a[0]]*a[1])


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    newx = np.repeat(x[..., 0], x[..., 1])
    newy = np.repeat(y[..., 0], y[..., 1])
    return int(np.dot(newy, newx)) if newx.shape[0] == newy.shape[0] else -1


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    norm1 = np.linalg.norm(X, axis=1)
    norm2 = np.linalg.norm(Y, axis=1)
    norm = np.outer(norm1, norm2)
    matrix = X.dot(Y.T) 
    return np.where(norm == 0, 1, matrix/norm)