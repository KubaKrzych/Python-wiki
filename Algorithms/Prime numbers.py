from math import sqrt


class Primes:
    def __init__(self, n_numbers):
        self.n = n_numbers

    def n_primes(self):
        result = [True for i in range(self.n)]
        result[0], result[1] = False, False
        for i in range(2, int(sqrt(self.n)) + 1):    # Check, whether it's safe to remove that -1
            if result[i]:
                j = i*2
                while j < self.n:
                    result[j] = False
                    j += i
        return result

    @staticmethod
    def gcd(a: int, b: int):
        if b > a:
            a, b = b, a
        if b:
            return Primes.gcd(b, a%b)
        return a


if __name__ == "__main__":
    primes = Primes(100)
    print(primes.n_primes())