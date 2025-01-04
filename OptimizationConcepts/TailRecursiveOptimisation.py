class TailRecursiveOptimisation:

    def factorial(self, n):
        if n <= 1 :
            return 1
        else :
            return n * self.factorial(n-1)


    def factorialWithTRO(self, n):
        fact = 1
        for i in range(2, n+1) :
            fact *= i
        return fact


if __name__ == "__main__" :
    number = 7
    t = TailRecursiveOptimisation()
    fact = t.factorial(number)
    factWithTro = t.factorialWithTRO(number)
    print("Factorial(without TRO) of: "+ str(number) + " is " + str(fact))
    print("Factorial(with TRO) of: " + str(number) + " is " + str(factWithTro))
