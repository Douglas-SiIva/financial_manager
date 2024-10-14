import pandas as pd
from datetime import datetime
import os

# Define o caminho do arquivo CSV para armazenar as transações
TRANSACTION_FILE = 'data/transactions.csv'

def add_transaction(type, amount, category, description=''):
    """
    Adiciona uma transação ao arquivo CSV.
    :param type: 'receita' ou 'despesa'
    :param amount: valor da transação (positivo para receita negativo para despesa)
    :param category: categoria da transação (ex: 'salário', 'aluguel', 'alimentação')
    :param description: descrição opiconal
    """
    
    # Lê as transações existentes
    df = load_transactions()

    # Cria a nova transação
    new_transaction = {
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'type': type,
        'amount': amount if type == 'receita' else -abs(amount),
        'category': category,
        'description': description
    }
    
    # Adiciona ao dataframe usando pd.concat
    df = pd.concat([df, pd.DataFrame([new_transaction])], ignore_index=True)

    
    # Salva de volta no CSV
    df.to_csv(TRANSACTION_FILE, index=False)
    print('Transação adicionada com sucesso!')

def load_transactions():
    """
    Carrega as transações do arquivo CSV.
    :return: dataframe com as transações
    """
    if not os.path.exists(TRANSACTION_FILE) or os.stat(TRANSACTION_FILE).st_size == 0:
        # Cria um dataframe vazio com as colinas e salva no arquivo csv
        df = pd.DataFrame(columns=['date', 'type', 'amount', 'category', 'description'])
        df.to_csv(TRANSACTION_FILE, index=False)
        return df
    return pd.read_csv(TRANSACTION_FILE) # Retorna o dataframe carregado

def list_transactions():
    """
    Lista todas as transações.
    """

    df = load_transactions()
    
    print("\n========================================")
    print("               Transações              ")
    print("========================================")
    
    if df.empty:
        print("Nenhuma transação registrada.")
    else:
        # Formatar e imprimir as transações
        for index, row in df.iterrows():
            date = row['date']
            transaction_type = row['type'].capitalize()
            amount = f"R${row['amount']:.2f}"
            category = row['category']
            description = row['description'] if pd.notnull(row['description']) else 'N/A'
            
            print(f"{date} | {transaction_type} | {amount} | {category} | {description}")

    print("========================================\n")
