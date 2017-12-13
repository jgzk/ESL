class Zespolona:

def init(self, rzeczywista, urojona):
self.r = rzeczywista
self.i = urojona

def add(self, other):
r_wy = self.r + other.r
i_wy = self.i + other.i
return Complex(r_wy, i_wy)

def sub(self, other):
r_wy = self.r - other.r
i_wy = self.i - other.i
return Complex(r_wy, i_wy)


def multi(self, r2, i2):
return (self.r*other.r - self.i*other.i, self.r*other.i+ self.1*other.r)


def module(self):
mod = sqrt(self.r* self.r + self.i* self.i)
return mod