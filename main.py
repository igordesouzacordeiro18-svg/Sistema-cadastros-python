cadastros= []

while True:
    print('1- Fazer cadastros.')
    print('2- Ver cadastros.')
    print('3- Excluir cadastro.')
    print('4- Sair.')
    
    opcao= input('\nEscolha uma opção(1,2,3 ou 4):\n ').strip()
    
    if opcao == '1':
        cpf_existe=False
        email_existe=False
        
        nome=input('Digite seu  nome:')
        email=input('Digite seu E-mail: ').strip().lower()
        cpf=input('Digite seu CPF: ').strip()
        
        for pessoa in cadastros:
            if pessoa['email']== email:
                email_existe=True
            if pessoa['cpf']==cpf:
                cpf_existe=True
            
            
        if email_existe:
            print('\nErro.Esse E-mail já existe,tente novamente\n')
            
        elif cpf_existe:
            print('\nErro.Esse CPF já existe,tente novamente\n')
                
        else:
        
            pessoa={'nome': nome,'email': email,'cpf': cpf}
            cadastros.append(pessoa)
            print('\nCadastro concluído!\n')
        
    elif opcao =='2':
        
        if not cadastros:
            print('\nNenhum usuário foi cadastrado.\n')
            
        else:
            for i,pessoa in enumerate(cadastros, 1):
                print(f'\nPessoa {i}')
                print(f'Nome: {pessoa["nome"]}')
                print(f'E-mail: {pessoa["email"]}')
                print(f'CPF: {pessoa["cpf"]}')
                
            continuar= input('\nDeseja continuar os cadastros(s/n): \n').strip().lower()
            
            if continuar == 'n':
                print('\nSaindo do programa.')
                break
    
    elif opcao == '3':
        if not cadastros:
            print('\nNão há cadastros para excluir.\n')
        
        else:
            cpf_excluir =input('\nDigite o CPF do cadastro que deseja excluir: ').strip()
            encontrado = False
            
            for pessoa in cadastros:
                if pessoa['cpf']== cpf_excluir:
                    encontrado = True
                    cadastros.remove(pessoa)
                    print('\nCadastro removido com sucesso.\n')
                    break
                
            if not encontrado:
                print('\nEsse CPF não está cadastrado,tente novamente\n')
            
            
    elif opcao == '4':
        print('\nSaindo do programa.')
        break
    
    else:
        print('\nOpção inválida. Tente novamente\n')
