
def gcf(a, b):
    if b == 0:
        return a
    return gcf(b, a%b)

class Fraction:
    def _reduce(self):
        factor = gcf(self.numerator, self.denominator)
        self.numerator /= factor
        self.denominator /= factor
        if self.denominator<0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __div__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __lt__(self, other):
        if (float(self.numerator)/self.denominator < \
            float(other.numerator)/other.denominator):
            return True
        else:
            return False

    def __gt__(self, other):
        if (float(self.numerator)/self.denominator > \
            float(other.numerator)/other.denominator):
            return True
        else:
            return False

    def __add__(self, other):
        numerator = self.numerator*other.denominator + \
                    self.denominator*other.numerator
        denominator = self.denominator*other.denominator
        return Fraction(numerator, denominator)
        
    def __sub__(self, other):
        negOther = Fraction(-other.numerator, other.denominator)
        return self + negOther # + == __add__()

    

    
        
