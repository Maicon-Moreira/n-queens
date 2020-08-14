from numba import jit
from tqdm import tqdm


@jit()
def isPrime(num):
    for divisor in range(2, int(num/2)):
        if num % divisor == 0:
            return False

    return True


def calculate():
    for num in tqdm(range(100000)):
        if isPrime(num):
            # print(num)
            pass


calculate()
