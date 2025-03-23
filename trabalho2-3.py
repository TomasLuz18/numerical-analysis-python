def f(x):
    return x**3 - 6*x**2 + 11*x - 6

tol = 1e-9
max_iter = 10
x0 = 0
x1 = 2

def secante(x0, x1, tol, max_iter):
    iter_count = 0
    erro = 1
    xa1 = x0
    x = x1
    while abs(erro) > tol and iter_count < max_iter:
        xa2 = xa1
        xa1 = x
        
        x = xa1 - f(xa1) * (xa2 - xa1) / (f(xa2) - f(xa1))
        erro = abs((x - xa1)/ x)
        iter_count += 1
    return (x, iter_count)

res = secante(x0, x1, tol, max_iter)

print('O valor da raiz é:', res[0])
print('O número de iterações foi:', res[1])
