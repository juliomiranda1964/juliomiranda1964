"""Programinha para verificar a maioridade"""


def verificar_maioridade():
    """Esta função serve para verificar a maioridade."""

    idade = int(input("Digite a sua idade: "))  # Recebe a idade

    if idade >= 18:  # Se a idade for maior ou igual a 18
        print("Maior de idade.")
    else:
        print("Menor de idade")


verificar_maioridade()  # Chama a função
