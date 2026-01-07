import sympy as sp

a, b, c, d, e, f, g, h = sp.symbols('a b c d e f g h')
l = sp.Symbol('lambda')

H = sp.Matrix([
    [-l, a, 0, b, 0, c],
    [sp.conjugate(a), -l, d, 0, e, 0],
    [0, sp.conjugate(d), -l, f, 0, g],
    [sp.conjugate(b), 0, sp.conjugate(f), -l, f, 0],
    [0, sp.conjugate(e), 0, sp.conjugate(f), -l, h],
    [sp.conjugate(c), 0, sp.conjugate(g), 0, sp.conjugate(h), -l]
])
A = H.det()

d1 = sp.Symbol('d1', real=True)
d2 = sp.Symbol('d2', real=True)
k = sp.Symbol('k', real=True)


D = A.subs([
    (a, 2 * sp.cos(k*d1)),
    (b, 2 * sp.cos((k/2) * (d1 + 3 * d2))),
    (c, 2 * sp.cos((k / 2) * (3 * d2 - d1))),
    (d, sp.exp(1j * k * d2)),
    (e, sp.exp(-1j * k * d2)),
    (f, sp.exp((1j / 2) * k * (d2 - d1))),
    (g, sp.exp((1j / 2) * k * (d1 + d2))),
    (h, sp.exp((-1j / 2) * k * (d2 + d1)))
])

print(D)
