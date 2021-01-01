def array_diff(a, b):
    #your code here
    if len(b) == 0 or len(a) == 0:
        return a
    else:
        for e in b:
            while e in a:
                a.remove(e)
        return a
