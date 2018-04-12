#  A simple class for performing basic operations on integers
class Modulo:

    # Classical iterative Euclidean gcd(a, b) algorithm
    @staticmethod
    def euclid_iterative_gcd(a, b):
        # make sure a = max(a, b)
        if b > a:
            a = a ^ b
            b = a ^ b
            a = a ^ b
        return Modulo._e_i_gcd(a, b)

    # Classical recursive Euclidean gcd(a, b) algorithm
    @staticmethod
    def euclid_recursive_gcd(a, b):
        # make sure a = max(a, b)
        if b > a:
            a = a ^ b
            b = a ^ b
            a = a ^ b
        return Modulo._e_r_gcd(a, b)

    # Generalized Euclidean algorithm
    @staticmethod
    def extended_euclid(b, a):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while a != 0:
            q, b, a = b // a, a, b % a
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return b, x0, y0

    # Determine the multiplicative inverse of x in mod n -> x ^ (-1) mod n <-> x * (x ^ (-1)) = 1 mod n
    @staticmethod
    def multiplicative_inverse(x, n):
        g, b, _ = Modulo.extended_euclid(x, n)
        if g == 1:
            return b % n

    # Prime factors decomposition
    @staticmethod
    def prime_factors(a):
        factors = []
        limit = int(a / 2)
        for j in range(2, limit):
            while a % j == 0:
                factors.append(j)
                a = a / j
        # Prime numbers by convention are divisible by 1 and the actual number
        if len(factors) == 0:
            factors.append(1)
            factors.append(a)
        return factors

    # Check if the given number is prime
    @staticmethod
    def check_prime(a):
        limit = a / 2
        for j in range(2, limit):
            if a % j == 0:
                return 1
        return 0

    # Check if the given numbers are coprime <-> gcd(a, b) = 1
    @staticmethod
    def check_coprimes(a, b):
        if Modulo.euclid_iterative_gcd(a, b) == 1:
            return 1
        return 0

    # Iterative Euclidean gcd(a, b) algorithm with a > b
    @staticmethod
    def _e_i_gcd(a, b):
        # start dividing
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    # Recursive Euclidean gcd(a, b) algorithm with a > b
    @staticmethod
    def _e_r_gcd(a, b):
        # fundamental case
        if b == 0:
            return a
        # recursion
        return Modulo._e_r_gcd(b, a % b)
