import csv

def ler_clientes(arquivo):
    clientes = []
    with open(arquivo, mode='r', encoding='utf-8') as file:
        leitor = csv.reader(file, delimiter=';')
        for linha in leitor:
            nome, cidade, idade, renda = linha
            clientes.append((nome, cidade, int(idade), float(renda)))
    return clientes    