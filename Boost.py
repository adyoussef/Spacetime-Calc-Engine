from MatrixClass import Matrix

class BoostMatrix(Matrix):
    """
    The 'BoostMatrix' class represents a Lorentz boost matrix.
    """
    def __init__(self, p = None, mass = None,
                 m0 = None, m1 = None, m2 = None, m3 = None):
        """
        Initialise the boost matrix given a momentum four-vector, 'p'. An
        additional 'mass' can be passed which can be used to stabilise
        large boosts. Finally, the 'mi' vectors can be passed so this
        can be constructed using the same initialisation as the
        'Matrix' class.
        """
        from math import sqrt
        if m0 and m1 and m2 and m3: Matrix.__init__(self, m0, m1, m2, m3)
        else:
            betas = [float(p[i])/p[0] for i in range(1, 4)]
            if mass: gamma = p[0]/mass
            else: gamma = 1/sqrt(1 - sum([b**2 for b in betas]))
            alpha = gamma**2/(1 + gamma)
            m0 = [gamma, -gamma*betas[0], -gamma*betas[1], -gamma*betas[2]]
            m1 = [m0[1], 1 + alpha*betas[0]**2, alpha*betas[0]*betas[1],
                  alpha*betas[0]*betas[2]]
            m2 = [m0[2], m1[2], 1 + alpha*betas[1]**2, alpha*betas[1]*betas[2]]
            m3 = [m0[3], m1[3], m2[3], 1 + alpha*betas[2]**2]
            self.m = [m0, m1, m2, m3]


