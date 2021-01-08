def index(array, n):
    if n >= len(array):
        return -1
    elif n >= 0:
        return array[n]**n
    else:
        return -1
