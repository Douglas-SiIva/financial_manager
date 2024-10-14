from transactions import add_transaction, list_transactions
from report import generate_summary, category_report

def display_menu():
    print("\n" + "=" * 40)
    print("Sistema de Controle Financeiro".center(40))
    print("=" * 40)
    print("Escolha uma opção:")
    print("1. Adicionar Receita")
    print("2. Adicionar Despesa")
    print("3. Listar Transações")
    print("4. Gerar Resumo")
    print("5. Relatório de Despesas por Categoria")
    print("6. Sair")
    print("=" * 40)


def main():
    while True:
        display_menu()  # Exibe o menu formatado

        choice = input('Digite sua opção: ')

        if choice == '1':
            amount = float(input('Digite o valor da receita: '))
            category = input('Digite a categoria: ')
            description = input('Descrição (opcional): ')
            add_transaction('receita', amount, category, description)

        elif choice == '2':
            amount = float(input('Digite o valor da despesa: '))
            category = input('Digite a categoria: ')
            description = input('Descrição (opcional): ')
            add_transaction('despesa', amount, category, description)

        elif choice == '3':
            list_transactions()

        elif choice == '4':
            generate_summary()

        elif choice == '5':
            category_report()

        elif choice == '6':
            print('Saindo...')
            break
        
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
