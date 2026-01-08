def soma(a: float, b: float) -> float:
    return a + b


def subtracao(a: float, b: float) -> float:
    return a - b


def multiplicacao(a: float, b: float) -> float:
    return a * b


def divisao(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


def aumento_percentual(salario: float, percentual: float) -> float:
    return salario * (1 + percentual / 100)


def litros_tinta(largura: float, altura: float, rendimento_m2_por_litro: float = 2.0) -> float:
    if rendimento_m2_por_litro <= 0:
        raise ValueError("O rendimento deve ser maior que zero.")
    area = largura * altura
    litros = area / rendimento_m2_por_litro
    return round(litros, 2)
