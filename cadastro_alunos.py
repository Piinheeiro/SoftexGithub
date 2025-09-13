alunos = []

while True:
    print("1 - Cadastrar Novo Aluno")
    print("2 - Listar Alunos Cadastrados")
    print("3 - Buscar Aluno por Matrícula")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            nome = input("Nome do aluno: ")
            matricula = input("Matrícula: ")
            curso = input("Curso: ")
            aluno = {"nome": nome, "matricula": matricula, "curso": curso}
            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar aluno: {e}")

    elif opcao == "2":
        if alunos:
            print("\nAlunos cadastrados:")
            for aluno in alunos:
                print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}, Curso: {aluno['curso']}")
        else:
            print("Nenhum aluno cadastrado.")

    elif opcao == "3":
        busca = input("Digite a matrícula do aluno: ")
        encontrado = False
        for aluno in alunos:
            if aluno["matricula"] == busca:
                print(f"Aluno encontrado: Nome: {aluno['nome']}, Curso: {aluno['curso']}")
                encontrado = True
                break
        if not encontrado:
            print("Aluno não encontrado.")

    elif opcao == "4":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")