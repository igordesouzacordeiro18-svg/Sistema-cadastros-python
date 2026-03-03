def menu():
    
    print('\n===MENU===\n')
    print('1- Fazer cadastros.')
    print('2- Listar cadastros.')
    print('3- Excluir cadastro.')
    print('4- Sair')

def cadastrar(cadastros):
    print('\n===NOVO CADASTRO===\n')

    nome =input('Digite seu nome: ').strip()
    email =input('Digite seu e-mail: ').strip().lower()
    cpf =input('Digite seu CPF: ').strip()

    #verificar se existe e-mail ou cpf repetido

    email_existe = any(pessoa['email']== email for pessoa in cadastros)
    cpf_existe = any(pessoa['cpf']== cpf for pessoa in cadastros)

    if email_existe:
        print('\nErro. Esse e-mail já existe,tente novamente.\n')

    elif cpf_existe:
        print('\nErro.Esse CPF já existe,tente novamente.\n')
    else:
        nova_pessoa={
            'nome': nome,
            'email': email,
            'cpf': cpf
        }

        cadastros.append(nova_pessoa)
        print('\nCadastro concluído.\n')

def listar(cadastros):
    if not cadastros:
        print('\nNenhum usuário foi cadastrado.\n')
        
    else:
        print('\n===LISTA DE CADASTROS===\n')
        for i,pessoa in enumerate(cadastros,1):
            print(f'Pessoa{i}')
            print(f'Nome: {pessoa["nome"]}')
            print(f'E-mail: {pessoa["email"]}')
            print(f'CPF: {pessoa["cpf"]}\n')


def excluir(cadastros):
    if not cadastros:
        print('\nNão há cadastros para excluir.\n')
        return
    
    cpf_excluir=input('\nDigite o CPF do cadastro que deseja excluir: ')

    for pessoa in cadastros:
        if pessoa['cpf']==cpf_excluir:
            cadastros.remove(pessoa)
            print('\nCadastro removido com sucesso.\n')
            return
            
    
    print('\nEsse CPF não está cadastrado.\n')

def main():
    cadastros=[]
    while True:
        menu()
        opcao= input('\nEscolha uma opção(1,2,3 ou 4):\n ').strip()

        if opcao == '1':
            cadastrar(cadastros)
        elif opcao=='2':
            listar(cadastros)
        elif opcao == '3':
            excluir(cadastros)
        elif opcao == '4':
            print('\nSaindo do programa...\n')
            break
        else:
            print('\nOpção inválida,tente novamente\n')
if __name__ == "__main__":
    main()

