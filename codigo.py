import pandas as pd
import os  

# Configura o pandas para mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Função para buscar um atleta pelo nome
def buscar_atleta_por_nome(nome_atleta, dados):
    # Use str.contains para encontrar todas as correspondências no nome do atleta
    atletas_encontrados = dados[dados['Atletas'].str.contains(nome_atleta, case=False, na=False)]
    return atletas_encontrados[['Atletas', 'Mês de entrada', 'Time', 'Posição', 'Idade', 'Ano de Nascimento', 'Vídeo (link ou min)', 'VIDEO', 'EUA (HS/college) ou Europa']]

# Função para adicionar um novo atleta à planilha
def adicionar_atleta(novo_atleta, dados):
    # Verifica se o arquivo Excel já existe
    if os.path.exists(planilha_excel):
        # Abre a planilha em modo de escrita
        with pd.ExcelWriter(planilha_excel, mode='a', engine='openpyxl') as writer:
            # Carrega os dados existentes
            dados_existentes = pd.read_excel(writer, header=0)
            
            # Cria um DataFrame com os dados do novo atleta
            novo_atleta_df = pd.DataFrame([novo_atleta], columns=dados_existentes.columns)
            
            # Concatena o DataFrame do novo atleta com os dados existentes
            dados_atualizados = pd.concat([dados_existentes, novo_atleta_df], ignore_index=True)
            
            # Salva os dados atualizados de volta na planilha
            dados_atualizados.to_excel(writer, index=False, header=True)
    else:
        # Se o arquivo Excel não existe, crie-o e adicione os dados do novo atleta
        novo_atleta_df = pd.DataFrame([novo_atleta], columns=dados.columns)
        novo_atleta_df.to_excel(planilha_excel, index=False)

# Carrega a planilha
planilha_excel = './planilha/Next SP.xlsx'
dados = pd.read_excel(planilha_excel, header=0)  # Use header=0 para usar a primeira linha como cabeçalho

while True:
    print("\nOpções:")
    print("1. Buscar atleta")
    print("2. Adicionar novo atleta")
    print("3. Sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == '1':
        nome_atleta = input("Digite o nome do atleta que deseja buscar: ")
        resultado = buscar_atleta_por_nome(nome_atleta, dados)
        
        if not resultado.empty:
            print("\nInformações do(s) atleta(s) encontrado(s):")
            for index, row in resultado.iterrows():
                print("-" * 30)
                print("Nome do Atleta:", row['Atletas'])
                print("Mês de Entrada:", row['Mês de entrada'])
                print("Time:", row['Time'])
                print("Posição:", row['Posição'])
                print("Idade:", row['Idade'])
                print("Ano de Nascimento:", row['Ano de Nascimento'])
                print("Vídeo (link ou min):", row['Vídeo (link ou min)'])
                print("VIDEO:", row['VIDEO'])
                print("EUA (HS/college) ou Europa:", row['EUA (HS/college) ou Europa'])
        else:
            print("\nNenhum atleta encontrado com esse nome.")
    elif escolha == '2':
        novo_atleta = {
            'Atletas': input("Nome do novo atleta: "),
            'Mês de entrada': input("Mês de entrada: "),
            'Time': input("Time: "),
            'Posição': input("Posição: "),
            'Idade': int(input("Idade: ")),
            'Ano de Nascimento': int(input("Ano de Nascimento: ")),
            'Vídeo (link ou min)': input("Link do vídeo: "),
            'VIDEO': input("Vídeo disponível (SIM ou NÃO): "),
            'EUA (HS/college) ou Europa': input("Destino (EUA ou Europa): ")
        }
        adicionar_atleta(novo_atleta, dados)
        print("\nNovo atleta adicionado à planilha.")
    elif escolha == '3':
        break
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.")
