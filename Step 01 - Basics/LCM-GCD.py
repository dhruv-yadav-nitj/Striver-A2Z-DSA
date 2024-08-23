class Solution:
    def lcmAndGcd(self, A, B):
        # Using Euclidean Maths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        gcd = gcd(A, B)
        lcm = (A * B) // gcd
        return [lcm, gcd]
