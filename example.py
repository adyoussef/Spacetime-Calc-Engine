from VectorClass import Vector
from MatrixClass import Matrix
from FourVector import FourVector
from Boost import BoostMatrix



def show(expr):
    """
    Print and evaluate an expression.
    """
    print("%s\n%10s:\n%s\n%s\n" % ("-"*20, expr, "-"*20, eval(expr)))

def vector(p, idx):
    """
    Return a vector, given the mass and momentum, 'idx' specifies
    energy index.
    """
    from math import sqrt
    e = sqrt(sum([pi**2 for pi in p[0:3]]) + p[3]**2)
    if idx == 0: return (e, p[0], p[1], p[2])
    else: return (p[0], p[1], p[2], e)



if __name__== "__main__":
    # Vector class.
    v0 = Vector(1, 2, 3, 4)
    v1 = Vector(1.0, 2j, 3, 0)
    s0 = 4.0
    show("v0")
    show("v1")
    show("s0")
    show("v0 + v1")
    show("v0 - v1")
    show("~v1")
    show("v0 * v0")
    show("v0**2")
    show("v0**3")
    show("v0/s0")

    # Matrix class.
    v2 = [0.5, 6.0, 7.0, 8.0]
    v3 = [1.0, -5.3, 6.0, 0.0]
    m0 = Matrix(v0, v1, v2, v3)
    m1 = Matrix(v2, v2, v1, v1)
    show("m0")
    show("m1")
    show("m0 + m1")
    show("m0 - m1")
    show("~m1")
    show("s0*m0")
    show("m0*v0")
    show("v0*m0")
    show("m0*m0")
    show("m0/s0")
    show("abs(m0)")
    show("m0**0")
    show("m0**2")

    # FourVector class.
    p0 = [1e3, 4e2, 6.8e9, 5.0]
    p1 = [0.3, 1.2, 1, 5.0]
    fv0 = FourVector(*vector(p0, 0))
    fv1 = FourVector(*vector(p1, 0))
    show("fv0")
    show("fv1")
    show("fv0*fv0")
    show("~fv0*fv0")
    show("abs(fv0)")

    # BoostMatrix class.
    bm0 = BoostMatrix(fv0)
    bm1 = BoostMatrix(fv0, p0[3])
    show("bm0")
    show("bm0*fv1")
    show("bm1*fv1")

    # Check against Pythia 8.
    try:
        from math import sqrt
        import pythia8
        v0 = pythia8.Vec4(*vector(p0, 3))
        v1 = pythia8.Vec4(*vector(p1, 3))
        v1.bstback(v0)
        v1 = pythia8.Vec4(*vector(p1, 3))
        v1.bstback(v0, p0[3])
        show(v1)
    except: pass

    # Example boost for the LHC.
    mp = 0.93827
    pp = 7000.0
    ep = (mp**2 + pp**2)**0.5
    fv0 = FourVector(ep, 0.0, 0.0, pp)
    fv1 = FourVector(ep, 0.0, 0.0, -pp)
    bm0 = BoostMatrix(fv0)
    show("abs(fv0 + fv1)")
    show("bm0*fv0")
    show("(bm0*fv1)")
    fv0p = bm0*fv0
    fv1p = bm0*fv1
    show("abs(fv0p + fv1p)")





