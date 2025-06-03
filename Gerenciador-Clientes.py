import csv
import os 

NOME_ARQUIVO = 'clientes_salao.csv'
CAMPOS = ['Nome', 'MesNascimento', 'Contato', 'UltimoServico']

def inicializar_arquivo():
    """Cria o arquivo CSV com o cabeçalho se ele não existir."""
    try:
        with open(NOME_ARQUIVO, 'x', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(CAMPOS)
        print(f"Arquivo '{NOME_ARQUIVO}' criado com sucesso.")
    except FileExistsError:
        pass 
    except Exception as e:
        print(f"Erro ao inicializar o arquivo: {e}")

def adicionar_cliente():
    """Coleta os dados do cliente e os salva no arquivo CSV."""
    print("\n--- Adicionar Novo Cliente ---")
    nome = input("Nome do Cliente: ").strip()
    mes_nascimento = input("Mês de Nascimento (ex: Janeiro): ").strip()
    contato = input("Contato (telefone ou WhatsApp): ").strip()
    ultimo_servico = input("Último Serviço Realizado (ex: Coloração, Corte, Tratamento): ").strip()

    cliente = {
        'Nome': nome,
        'MesNascimento': mes_nascimento,
        'Contato': contato,
        'UltimoServico': ultimo_servico
    }

    try:
        with open(NOME_ARQUIVO, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=CAMPOS)
            writer.writerow(cliente)
        print(f"Cliente '{nome}' adicionado com sucesso!")
    except Exception as e:
        print(f"Erro ao adicionar cliente: {e}")

def consultar_clientes():
    """Permite consultar clientes pelo nome ou mês de nascimento."""
    print("\n--- Consultar Clientes ---")
    termo_busca = input("Digite o nome ou mês de nascimento para buscar: ").strip().lower()
    encontrados = []

    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if termo_busca in row['Nome'].lower() or termo_busca in row['MesNascimento'].lower():
                    encontrados.append(row)
        
        if encontrados:
            print("\nClientes encontrados:")
            for cliente in encontrados:
                print(f"Nome: {cliente['Nome']}, Mês Nasc.: {cliente['MesNascimento']}, Contato: {cliente['Contato']}, Último Serviço: {cliente['UltimoServico']}")
        else:
            print("Nenhum cliente encontrado com o termo informado.")
    except FileNotFoundError:
        print(f"O arquivo '{NOME_ARQUIVO}' não foi encontrado. Adicione clientes primeiro.")
    except Exception as e:
        print(f"Erro ao consultar clientes: {e}")

def excluir_cliente():
    """Exclui um cliente pelo nome."""
    print("\n--- Excluir Cliente ---")
    nome_para_excluir = input("Digite o NOME COMPLETO do cliente para excluir: ").strip()
    
    clientes_restantes = []
    cliente_encontrado = False

    try:
        
        if not os.path.exists(NOME_ARQUIVO) or os.stat(NOME_ARQUIVO).st_size == 0:
            print(f"O arquivo '{NOME_ARQUIVO}' está vazio ou não existe. Não há clientes para excluir.")
            return

        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                if row['Nome'].strip().lower() != nome_para_excluir.lower():
                    clientes_restantes.append(row)
                else:
                    cliente_encontrado = True
        
        if cliente_encontrado:
            
            with open(NOME_ARQUIVO, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=CAMPOS)
                writer.writeheader() 
                writer.writerows(clientes_restantes) 
            print(f"Cliente '{nome_para_excluir}' excluído com sucesso!")
        else:
            print(f"Cliente '{nome_para_excluir}' não encontrado.")
    except FileNotFoundError:
        print(f"O arquivo '{NOME_ARQUIVO}' não foi encontrado.")
    except Exception as e:
        print(f"Erro ao excluir cliente: {e}")

def menu():
    """Exibe o menu principal do programa."""
    inicializar_arquivo() 

    while True:
        print("\n--- Gerenciador de Clientes do Salão ---")
        print("1. Adicionar Novo Cliente")
        print("2. Consultar Clientes")
        print("3. Excluir Cliente") 
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            consultar_clientes()
        elif opcao == '3': 
            excluir_cliente()
        elif opcao == '4':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")


if __name__ == "__main__":
    menu()
