from fn import Stream
from fn.iters import filter, take


def odd():
    i = 3
    while True:
        yield i
        i += 2


def isPrime(x):
    for i in prime:
        if i * i > x:
            return True
        elif x % i == 0:
            return False


prime = Stream() << [2] << filter(isPrime, odd())


if __name__ == '__main__':
    print list(take(10, prime))
