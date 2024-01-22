
def adicionarContato(pAgendaContatos, nome, telefone, email): 
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    pAgendaContatos.append(contato)
    print(f"Contato {nome} foi adicionado com sucesso!")
    return True

def listarContatos(pAgendaContatos):
    print("\nLista de Contatos...")
    for indice,contato in enumerate(pAgendaContatos, start=1):
        status = "✓" if contato["favorito"]==True else " "
        print(f"{indice}. [{status}] {contato['nome']}, {contato['telefone']}, {contato['email']}")
    return True

def atualizarContato(pAgendaContatos, indiceContato, novoNome, novoTelefone, novoEmail):  
    indiceAjustado = int(indiceContato) - 1
    if indiceAjustado >= 0 and indiceAjustado < len(pAgendaContatos):
        pAgendaContatos[indiceAjustado]['nome'] = novoNome
        pAgendaContatos[indiceAjustado]['telefone'] = novoTelefone
        pAgendaContatos[indiceAjustado]['email'] = novoEmail
        print(f"Contato {indiceContato} atualizado")
    else:
        print("Indice inválido !")
    return True

def definirStatusFavorito(pAgendaContatos, indiceContato): 
    indiceAjustado = int(indiceContato) - 1
    if indiceAjustado >= 0 and indiceAjustado < len(pAgendaContatos):
        pAgendaContatos[indiceAjustado]['favorito'] = not (pAgendaContatos[indiceAjustado]['favorito'])
        print(f"Status de favorito do Contato {indiceContato} atualizado")
    else:
        print("Indice inválido !")
    return True

def listarContatosFavoritos(pAgendaContatos):
    print("\nLista de Contatos FAVORITOS...")
    for indice,contato in enumerate(pAgendaContatos, start=1):
        if contato["favorito"]==True:
            status = "✓"
            print(f"{indice}. [{status}] {contato['nome']}, {contato['telefone']}, {contato['email']}")
    return True

def deletarContato(pAgendaContatos, indiceContato): 
    indiceAjustado = int(indiceContato) - 1
    for indice,contato in enumerate(pAgendaContatos):
        if indice == indiceAjustado:
             pAgendaContatos.remove(contato)
    print("Contato excluido com sucesso...")         
    return True


agendaContatos = []

while True:
    print("\nMenu da Agenda de Contatos:")
    print("1. Adicionar Contato")
    print("2. Ver Lista de Contatos")
    print("3. Atualizar Contato")
    print("4. Marcar/Desmarcar Contato Favorito")
    print("5. Listar Contatos Favoritos")
    print("6. Deletar Contato")
    print("7. Sair")
    
    escolha = input("Digite a sua escolha: ")
    
    if escolha == "1":
        nome = input("Digite o NOME do contato que deseja adicionar:")
        fone = input("Digite o TELEFONE do contato que deseja adicionar:")
        email = input("Digite o EMAIL do contato que deseja adicionar:")
        adicionarContato(agendaContatos, nome, fone, email)
    elif escolha == "2":
        listarContatos(agendaContatos)
    elif escolha == "3":
        listarContatos(agendaContatos)
        indice_contato = input("Digite o indice do contato para atualizar:")
        nome = input("Digite o NOME do contato que deseja adicionar:")
        fone = input("Digite o TELEFONE do contato que deseja adicionar:")
        email = input("Digite o EMAIL do contato que deseja adicionar:")
        atualizarContato(agendaContatos, indice_contato,nome,fone,email)  
    elif escolha == "4":
        listarContatos(agendaContatos)
        indice_contato = input("Digite o indice do contato para alterar status de favorito:")
        definirStatusFavorito(agendaContatos, indice_contato)
    elif escolha == "5":
        listarContatosFavoritos(agendaContatos)               
    elif escolha == "6":
        listarContatos(agendaContatos)
        indice_contato = input("Digite o indice do contato a ser excluído:")
        confirma = input("Confirma a exclusão do contato selecionado (S/N) ?")
        if confirma.upper() == "S":
            deletarContato(agendaContatos, indice_contato)
        listarContatos(agendaContatos)    
    elif escolha=="7":
        break
    
print("Programa finalizado!")