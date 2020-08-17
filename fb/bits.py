def nextClosest(n):
    # number of 1s to the right of p
    c1 = 1
    # number of 0s to the right of p
    c0 = 0

    p = c1 + c0
    # all 0 except for a 1 at position p
    a = 1 << p
    # all 0 followed by p ones
    b = a - 1
    # all 1s followed by p zeroes
    mask = ~b
    # clear right most p bits
    n = n & mask

    # Add c1 - 1 ones
    # 0s with a 1 at position c1 - 1
    a = 1 << (c1 - 1)
    # 0s with 1s at position 0 through c1 - 1
    b = a - 1
    # inserts 1s at position 0 throuhg c1 - 1
    n = n | b


def getNext(n):
    # Compute c0 and c1
    c = n
    c0 = 0
    c1 = 0

    while c & 1 == 0 and c != 0:
        print(bin(c))
        print(bin(c0))
        c0 += 1
        c >>= 1

    print()
    print('---')
    print()

    while c & 1 == 1:
        print(bin(c))
        print(bin(c1))
        c1 += 1
        c >>= 1





if __name__ == "__main__":
    print('Let\'s play with bits')

    getNext(13984)
