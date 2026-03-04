def menu():
    print('\n=== MENU ===')
    print('1 - Fazer cadastros.')
    print('2 - Ver cadastros.')
    print('3 - Excluir cadastros.')
    print('4- Editar cadastros.')
    print('5 - Sair.')
    


def cadastrar(cadastros):
    nome = input('\nDigite seu nome: ').strip()
    email = input('Digite seu E-mail: ').strip().lower()
    cpf = input('Digite seu CPF: ').strip()

    # Verifica se já existe email ou CPF
    email_existe = any(pessoa['email'] == email for pessoa in cadastros)
    cpf_existe = any(pessoa['cpf'] == cpf for pessoa in cadastros)

    if email_existe:
        print('\nErro: Esse e-mail já existe. Tente novamente.\n')
    elif cpf_existe:
        print('\nErro: Esse CPF já existe. Tente novamente.\n')
    else:
        nova_pessoa = {
            'nome': nome,
            'email': email,
            'cpf': cpf
        }
        cadastros.append(nova_pessoa)
        print('\nCadastro concluído!\n')


def listar(cadastros):
    if not cadastros:
        print('\nNenhum usuário cadastrado.\n')
        return

    print('\n=== LISTA DE CADASTROS ===')
    for i, pessoa in enumerate(cadastros, 1):
        print(f'\nPessoa {i}')
        print(f'Nome: {pessoa["nome"]}')
        print(f'E-mail: {pessoa["email"]}')
        print(f'CPF: {pessoa["cpf"]}')


def excluir(cadastros):
    if not cadastros:
        print('\nNão há cadastros para excluir.\n')
        return

    cpf_excluir = input('Digite o CPF do cadastro que deseja excluir: ').strip()

    for pessoa in cadastros:
        if pessoa['cpf'] == cpf_excluir:
            cadastros.remove(pessoa)
            print('\nCadastro removido com sucesso!\n')
            return

    print('\nEsse CPF não está cadastrado.\n')
    
def editar(cadastros):
    if not cadastros:
        print('\nNão há cadastros para editar.\n')
        return
    cpf_encontrar= input('Digite o CPF que deseja encontrar:')
    for pessoa in cadastros:
        if pessoa ['cpf']== cpf_encontrar:
            print('\nDigite o que voce deseja editar?\n')
            opcao_editar= input('1-Nome | 2-E-mail | 3-Ambos: ').strip()
            
            if opcao_editar =='1':
                novo_nome=input('Digite um novo nome: ')
                pessoa['nome'] = novo_nome
                print('\nCadastro atualizado com sucesso.')
                return
                
            elif opcao_editar == '2':
                novo_email=input('Digite um novo e-mail: ')
                pessoa['email'] = novo_email
                print('\nCadastro atualizado com sucesso.')
                return
                
            elif opcao_editar=='3':
                novo_nome=input('Digite um novo nome: ')
                novo_email=input('Digite um novo e-mail: ')
                pessoa['nome'] = novo_nome
                pessoa['email'] = novo_email
                print('\nCadastro atualizado com sucesso.')
                return
    
    print('\nEsse CPF não está cadastrado\n')
                

def main():
    cadastros = []

    while True:
        menu()
        opcao = input('\nEscolha uma opção (1-5): ').strip()

        if opcao == '1':
            cadastrar(cadastros)
        elif opcao == '2':
            listar(cadastros)
        elif opcao == '3':
            excluir(cadastros)
        elif opcao== '4':
            editar(cadastros)
        elif opcao == '5':
            print('\nSaindo do programa...')
            break
        else:
            print('\nOpção inválida. Tente novamente.\n')


# Inicia o programa
main()

