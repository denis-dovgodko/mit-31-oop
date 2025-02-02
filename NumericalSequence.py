import sympy as sp
class NumericalSequence:
    __equation = "a**(n+1)*(a/(b*n-a))" 

    def __init__(self, a, b, max_numbers):
        self.__a = a
        self.__b = b
        self.__max_number = max_numbers
        self.__refreshSequence()

    @property
    def a(self):
        return self.__a
    @property
    def b(self):
        return self.__b
    @property
    def max_number(self):
        return self.__max_number
    @property
    def sequence(self):
        return self.__sequence
    
    @a.setter
    def a(self, value):
        self.__a = value
        self.__refreshSequence() 

    @b.setter
    def b(self, value):
        self.__b = value
        self.__refreshSequence() 
    
    @max_number.setter
    def max_number(self, value):
        self.__max_number = value
        self.__refreshSequence() 
    
    def calculateSumm(self, n, start=1):
        if n > self.__max_number:
           raise ValueError
        summ = 0
        for i in range(start, n+1):
            summ += self.calculateElement(i)
        return summ

    def calculateElement(self, n):
        expression = sp.sympify(NumericalSequence.__equation)
        element = expression.subs({'n': n, 'a': self.__a, 'b': self.__b})
        return element
    
    def calculateSequence(self, k, m):
        if m > self.__max_number:
            raise ValueError
        sequence = []
        for i in range (k, m+1):
            sequence.append(self.calculateElement(i))
        return sequence
    
    @staticmethod
    def __printSequence(seq):
        print(f'a={seq.a}, b={seq.b}:', *seq.sequence)

    @staticmethod
    def compareSequence(sequence1, sequence2):
        if sequence1.__sequence == sequence2.__sequence:
            return print("True. Seqences are equal")
        print("False. Seqences are not equal")

    def __refreshSequence(self):
        last_element = 7
        if self.__max_number < 7:
            last_element = self.__max_number
        self.__sequence = self.calculateSequence(1, last_element)
        NumericalSequence.__printSequence(self)

sequence1 = NumericalSequence(1, 2, 20)

print(sequence1.calculateElement(1))
print(sequence1.calculateElement(2))

print(sequence1.calculateSumm(2))
print(sequence1.calculateSumm(3, 2))

print(sequence1.calculateSequence(2, 4))

sequence2 = NumericalSequence(3, 4, 8)

NumericalSequence.compareSequence(sequence1, sequence2)

sequence2.a = 1
sequence2.b = 2

NumericalSequence.compareSequence(sequence1, sequence2)

sequence2.max_number = 6

NumericalSequence.compareSequence(sequence1, sequence2)