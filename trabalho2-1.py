def bisection(f, a, b, tol=1e-5, max_iter=20):
    if f(a) * f(b) >= 0:
        raise ValueError("A função não muda de sinal em [a, b]")
    
    iter_count = 0
    while (b - a) > tol and iter_count < max_iter:
        x = (a + b) / 2
        if f(x) == 0:
            return x
        elif f(x) * f(a) < 0:
            b = x
        else:
            a = x
        iter_count += 1
    
    return (a + b) / 2

def main():
    expression = input("Insira a função f(x): ")
    a = float(input("Insira o limite 'a': "))
    b = float(input("Insira o limite 'b': "))
    try:
        f = lambda x: eval(expression)
        root = bisection(f, a, b)
        print("Raiz aproximada:", root)
    except (ValueError, SyntaxError):
        print("Erro: Certifique-se de que a função foi inserida corretamente.")
    except Exception as e:
        print("Erro:", str(e))
    
if __name__ == "__main__":
    main()