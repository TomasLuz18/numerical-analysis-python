def convert_to_base(n, base):
    if base < 2 or base > 62:
        return "Base fora do intervalo (2-62)"

    if n < 0:
        sign = "-"
        n = abs(n)
    else:
        sign = ""

    int_part = int(n)
    decimal_part = n - int_part

    int_part_str = ""
    decimal_part_str = ""

    # Parte inteira
    while int_part > 0:
        remainder = int_part % base
        if remainder < 10:
            int_part_str = str(remainder) + int_part_str
        else:
            int_part_str = chr(55 + remainder) + int_part_str
        int_part //= base

    if int_part_str == "":
        int_part_str = "0"

    # Parte decimal
    precision = 8
    while decimal_part > 0 and precision > 0:
        decimal_part *= base
        digit = int(decimal_part)
        if digit < 10:
            decimal_part_str += str(digit)
        else:
            decimal_part_str += chr(87 + digit)
        decimal_part -= digit
        precision -= 1

    if decimal_part_str:
        result = sign + int_part_str + "." + decimal_part_str
    else:
        result = sign + int_part_str

    return result

def main():
    try:
        number = float(input("Digite o número a ser convertido: "))
        base_from = int(input("Digite a base atual (2-62): "))
        base_to = int(input("Digite a nova base (2-62): "))

        if not (2 <= base_from <= 62) or not (2 <= base_to <= 62):
            print("As bases devem estar no intervalo de 2 a 62.")
        else:
            result = convert_to_base(number, base_to)
            print(f"Resultado: {result} (base {base_to})")

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número real válido e bases numéricas válidas.")

if __name__ == "__main__":
    main()
