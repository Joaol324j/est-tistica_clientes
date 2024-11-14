from until import ler_clientes

def calc_media_idade(clientes):
    total_idade = sum(cliente[2] for cliente in clientes)
    return total_idade / len(clientes) if clientes else 0

def calc_media_renda(clientes):
    total_renda = sum(cliente[3] for cliente in clientes)
    return total_renda / len(clientes) if clientes else 0

def exibir_estatisticas(clientes):
    media_idade = calc_media_idade(clientes)
    media_renda = calc_media_renda(clientes)
    print(f'Média de idade: {media_idade:.2f}')
    print(f'Média de renda mensal: {media_renda:.2f}')

def main():
    clientes = ler_clientes('clientes.txt')
    exibir_estatisticas(clientes)

if __name__ == "__main__":
    main()