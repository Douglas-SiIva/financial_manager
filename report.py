import pandas as pd
from transactions import load_transactions

def generate_summary():
    """
    Gera um resumo das receitas, despesas e saldo total.
    """
    df = load_transactions()
    total_income = df[df['type'] == 'receita']['amount'].sum()
    total_expense = df[df['type'] == 'despesa']['amount'].sum()
    balance = total_income + total_expense

    print("\n" + "=" * 40)
    print("       Resumo Financeiro".center(40))
    print("=" * 40)
    print(f'Receitas Totais: R${total_income:.2f}')
    print(f'Despesas Totais: R${abs(total_expense):.2f}')
    print(f'Saldo: R${balance:.2f}')
    print("=" * 40)


def category_report():
    """
    Exibe um relatório de despesas agrupadas por categoria
    """

    df = load_transactions()
    expense_report = df[df['type'] == 'despesa'].groupby('category')['amount'].sum()
    
    print('\n' + '=' * 40)
    print('    Relatório de Despesas por Categoria')
    print('=' * 40)

    if expense_report.empty:
        print('Nenhuma despesa registrada.')
    else:
        for category, amount in expense_report.items():
            print(f'{category:<20} - R${amount:.2f}')

    print('=' * 40)
