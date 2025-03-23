import numpy as np
from sympy import symbols, Eq, lambdify, sympify, diff

def pedir_equacoes():
    while True:
        try:
            num_eqs = int(input("Digite o número de equações no sistema: "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    eqs = []
    x, y = symbols('x y')

    for i in range(num_eqs):
        while True:
            try:
                eq_str = input(f"Digite a {i + 1}ª equação em termos de x e y, usando 'x' e 'y': ")
                eq = Eq(sympify(eq_str), 0)
                eqs.append(eq)
                break
            except Exception:
                print("Por favor, insira uma expressão válida.")

    return eqs

def pedir_pontos_iniciais():
    x0 = float(input('Digite o valor inicial para x: '))
    y0 = float(input('Digite o valor inicial para y: '))
    return np.array([x0, y0])

def newton_method(F, J, x0, k, max_iter, tol):
    x = x0
    iteracoes = []

    for _ in range(k):
        F_val = F(*x)
        J_val = J(*x)

        try:
            x_new = x - np.linalg.solve(J_val, F_val)
        except np.linalg.LinAlgError:
            print("Não foi possível calcular a solução. A matriz Jacobiana é singular.")
            return None

        x = x_new

    for i in range(max_iter):
        F_val = F(*x)
        J_val = J(*x)

        try:
            x_new = x - np.linalg.solve(J_val, F_val)
        except np.linalg.LinAlgError:
            print("Não foi possível calcular a solução. A matriz Jacobiana é singular.")
            return None

        iteracoes.append(x_new)
        x = x_new

        if np.linalg.norm(F_val) < tol:
            print(f'Solução encontrada: {x} após {i + k + 1} iterações.')
            return x, iteracoes

    print(f'O método de Newton não convergiu após {max_iter} iterações.')
    return None

def main():
    eqs = pedir_equacoes()
    x, y = symbols('x y')

    F = lambdify((x, y), [eq.lhs for eq in eqs])
    J = lambdify((x, y), [[diff(eq.lhs, var) for var in (x, y)] for eq in eqs])

    x0 = pedir_pontos_iniciais()
    k = int(input('Digite a ordem da iteração (k=0): '))
    max_iter = int(input('Digite o número máximo de iterações: '))
    tol = float(input('Digite a tolerância absoluta (norma infinito): '))

    resultado = newton_method(F, J, x0, k, max_iter, tol)

    if resultado is not None:
        x_final, iteracoes = resultado
        print("Resultado final:", x_final)
        print("Número de iterações:", len(iteracoes))

if __name__ == "__main__":
    main()
