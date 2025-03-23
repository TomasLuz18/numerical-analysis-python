from cmath import exp

def f(x):
    return x**3 -10000

def df(x):
    return 3*x**2

x0 = 50
tol = 10**-9
max_iter = 10

def newton(x0, tol, max_iter):
    iter_count = 0
    erro = 1
    while abs(erro) >= tol and iter_count < max_iter:
        x_anterior = x0
        x0 = x0 - f(x0) / df(x0)
        erro = abs((x0 - x_anterior) / x0)
        iter_count += 1
    return (x0, erro, iter_count)


res = newton(x0, tol, max_iter)

print('O valor da raiz e: ', res[0])
print('O numero de iteracoes foi: ', res[1])
