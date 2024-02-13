

class Matrix:
    """
    The 'Matrix' class represents a matrix of size 4x4.
    """
    def __str__(self):
        """
        Return a string to print of this vector.
        """
        return "\n".join("%10r %10r %10r %10r" % tuple(mi) for mi in self.m)
    
    def __repr__(self):
        """
        Return the representation of this vector.
        """
        return "%s(m0 = %r, m1 = %r, m2 = %r, m3 = %r)" % tuple(
            [self.__class__.__name__] + self.m)
    
    def __init__(self, m0, m1, m2, m3):
        """
        Initialise the matrix with the row vectors 'm0', 'm1', 'm2',
        and 'm3'.
        """
        self.m = [[mij for mij in mi] for mi in [m0, m1, m2, m3]]
    
    def __getitem__(self, k):

        """
        Return the 'ij' component of the matrix.
        """
        i, j = k
        return self.m[i][j]
    
    def __setitem__(self, k, s):
        """
        Set the 'ij' component of the matrix with the scalar 's'.
        """
        i, j = k
        self.m[i][j] = s

    def __pos__(self):
        """
        Return a copy of this matrix with the '+' operator applied to
        each element.
        """
        return self.__class__(
            m0 = self.m[0], m1 = self.m[1], m2 = self.m[2], m3 = self.m[3])

    def __neg__(self):
        """
        Return a copy of this matrix with the '-' operator applied to
        each element.
        """
        m = +self
        for i in range(0, 4):
            for j in range(0, 4): m[i, j] = -m[i, j]
        return m
    
    def __iadd__(self, m):
        """
        Augmented assignment '+=' for adding a matrix 'm' to this matrix.
        """
        for i in range(0, 4):
            for j in range(0, 4): self[i, j] += m[i, j]
        return self
    
    def __isub__(self, m):
        """
        Augmented assignment '-=' for subtracting a matrix 'm' from
        this matrix.
        """
        for i in range(0, 4):
            for j in range(0, 4): self[i, j] -= m[i, j]
        return self
    
    def __add__(self, m):
        """
        Return the addition of this matrix with the matrix 'm'.
        """
        l = +self
        l += m
        return l
    
    def __sub__(self, m):
        """
        Return the subtraction of this matrix with the matrix 'm'.
        """
        l = +self
        l -= m
        return l
    
    def __invert__(self):
        """
        Return the complex transpose of this matrix.
        """
        m = +self
        for i in range(0, 4):
            for j in range(0, 4):
                try: m[j, i] = self[i, j].conjugate()
                except: m[j, i] = self[i, j]
        return m
    
    def __imul__(self, x):
        """
        Augmented assignment '*=' for multiplying this matrix with a
        vector, matrix, or scalar 'x'.
        """
        # The vector case.
        try:
            x[0]
            v = +x
            for i in range(0, 4):
                v[i] = sum([self[i, j]*x[j] for j in range(0, 4)])
            self = v
        except:
            # The matrix case.
            try:
                x[0, 0]
                m = +self
                for i in range(0, 4):
                    for j in range(0, 4):
                        self[i, j] = sum(
                            [m[i, k]*x[k, j] for k in range(0, 4)])
            # The scalar case.
            except:
                for i in range(0, 4):
                    for j in range(0, 4): self[i, j] *= x
        return self
    
    def __mul__(self, x):
        """
        Return the multiplication of this matrix with either a
        matrix or a scalar.
        """
        l = +self
        l *= x
        return l
    
    def __rmul__(self, x):
        """
        Return the multiplication of a vector, matrix, or scalar 'x'
        with this matrix. The operation x*m where x is a vector or
        matrix is not used.
        """
        return self*x
    
    def __itruediv__(self, s):
        """
        Augmented assignment '/=' for dividing this matrix with a
        scalar 's'.
        """
        for i in range(0, 4):
            for j in range(0, 4): self[i, j] /= s
        return self
    
    def __truediv__(self, s):
        """
        Return the division of this matrix by a scalar 's'. The reflected
        operator, 's/m', requires the inverse of the matrix and is not
        implemented.
        """
        l = +self
        l /= s
        return l
    
    def __abs__(self):
        """
        Return the norm of the matrix.
        """
        from math import sqrt
        n = 0
        for i in range(0, 4):
            for j in range(0, 4):
                try: n += self[i, j].conjugate()*self[i, j]
                except: n += self[i, j]*self[i, j]
        try: return sqrt(n.real)
        except: return sqrt(n)
    
    def __ipow__(self, i):
        """
        Augmented assignment '**=' for raising this matrix to the
        integer power 'i'.
        """
        if i < 0: raise ValueError('power must be positive')
        # Special case for 0.
        if i == 0:
            for j in range(0, 4):
                for k in range(0, 4):
                    self[j, k] = float(j == k)
        # When i > 1.
        else:
            u = +self
            for j in range(1, i): self *= u
        return self
    
    def __pow__(self, i):
        """
        Return this vector raised to the integer power 'i'. For even
        'i' this is a scalar and odd 'i' a vector.
        """
        u = +self
        u **= i
        return u











