def descending_order(num):
    # Bust a move right here
    num = str(num)
    noL = []
    for n in num:
        noL.append(n)
    noL.sort(reverse=True)
    largestNum = int("".join(noL))
    return largestNum
