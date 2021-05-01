def xorAndSum(a, b):
    a , b = int(a, 2), int(b, 2)
    total = a ^ b
    for _ in range(1,314160):
        b *= 2
        total += (a ^ b)
    return total % 1000000007

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    result = xorAndSum(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
