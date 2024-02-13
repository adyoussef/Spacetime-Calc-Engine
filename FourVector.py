from VectorClass import Vector


class FourVector(Vector):
    """
    The 'FourVector' class represents a physics four-vector.
    """
    
    def __init__(self, *args):
        """
        Constructs the four-vector from its base Vector class.
        """
        Vector.__init__(self, *args)
    
    def __invert__(self):
        """
        Return the lowered index of this vector, e.g. p_mu.
        """
        v = +self
        for i in range(1, 4): v[i] = -v[i]
        return v

