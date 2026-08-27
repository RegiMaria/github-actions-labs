"""Script de exemplo para o Lab 11 - tem um problema de lint de propósito."""
import os   # <- import não usado, o Ruff vai reclamar disso (regra F401)


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


if __name__ == "__main__":
    print(somar(2, 3))