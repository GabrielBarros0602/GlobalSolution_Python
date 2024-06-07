def list_options(option, lista):
    if option in range(1, len(lista) + 1):
        print(lista[option - 1])
    else:
        print("Opção inválida! Tente novamente com as opções apresentadas.")

def in_lista(lista, option):
    for i in range(len(lista)):
        elem = lista[i]
        if elem == option:
            return True
    return False

def force_option(message, lista_options, error_message):
    option = input(message)
    while not in_lista(lista_options, option):
        print(error_message)
        option = input(message)
    return option

def print_lista(lista):
    for i in range(len(lista)):
        print(lista[i])

def add_adm_lista(lista_add, lista_name):
    adm_choice = force_option(f"\nDeseja adicionar uma informação a {lista_name} (S - Sim / N - Não) ?\n->", ["S", "N"], "Opção inválida, tente novamente com as opções apresentadas.")

    if adm_choice == "S":
        add_adm_info = input("Adicione a informação no seguinte estilo (Ano - Média informação. Breve explicação.)\n(Digite 'sair' para cancelar a operação)\n-> ")
        if add_adm_info == 'sair':
                print('Cancelando operação...')
        else:
                lista_add.append("\n" + add_adm_info)
                print(f"'{add_adm_info}'\nfoi adicionada à lista com sucesso.")
    else:
        print('Cancelando operação...')

message_options = [
    "Qual dado deseja detalhar:\n1. Nível do mar\n2. Umidade na costa\n3. Temperatura média\n4. Presença de Gáses nocivos\n->",
    "Detalhes do sistema: Banco de Dados público AquaInsight v1.0",
    "Saindo do sistema. Até mais! -- AquaInsight"
]

lista_nivelmar = [
    "\n2019 - Taxa média de aumento: 3.3 mm por ano. Influências como El Niño contribuíram para flutuações temporárias.",
    "\n2020 - Taxa média de aumento: 3.6 mm por ano. Observações de satélite e modelos climáticos indicaram que o aumento continuou em ritmo acelerado, possivelmente devido à combinação de expansão térmica e derretimento de gelo polar.",
    "\n2021 - Taxa média de aumento: 3.7 mm por ano. A continuidade do aquecimento global e eventos climáticos como La Niña afetaram o ritmo de aumento do nível do mar.",
    "\n2022 - Taxa média de aumento: 3.4 mm por ano. A taxa mostrou uma ligeira desaceleração em comparação com os anos anteriores, mas ainda refletia uma tendência de aumento contínuo.",
    "\n2023 - Taxa média de aumento: 3.5 mm por ano. Projeções e dados preliminares indicaram que a tendência de elevação do nível do mar se manteve, seguindo as mudanças climáticas e padrões de derretimento de gelo."
]

lista_umidade = [
    "\n2019 - Umidade relativa média: Cerca de 75%. Variações sazonais e regionais influenciaram a umidade, com picos durante as estações mais quentes e úmidas.",
    "\n2020 - Umidade relativa média: Aproximadamente 76%. Fenômenos climáticos como La Niña contribuíram para um aumento na umidade em algumas regiões costeiras.",
    "\n2021 - Umidade relativa média: Cerca de 74%. O clima global mais quente influenciou a umidade costeira, com algumas regiões experimentando um leve declínio.",
    "\n2022 - Umidade relativa média: Aproximadamente 75%. Flutuações devido a padrões climáticos sazonais e eventos climáticos como El Niño e La Niña.",
    "\n2023 - Umidade relativa média: Cerca de 75%. Dados preliminares indicam que a umidade costeira manteve-se estável, com variações sazonais típicas e influências regionais."
]

lista_temperatura = [
    "\n2019 - Temperatura média: Cerca de 16°C a 18°C. As temperaturas foram influenciadas por um período relativamente estável, com variações sazonais normais.",
    "\n2020 - Temperatura média: Aproximadamente 17°C a 19°C. O ano foi marcado por eventos como La Niña, que impactaram as temperaturas em várias regiões costeiras.",
    "\n2021 - Temperatura média: Cerca de 18°C a 20°C. O aquecimento contínuo contribuiu para um leve aumento nas temperaturas costeiras em comparação com os anos anteriores.",
    "\n2022 - Temperatura média: Aproximadamente 18°C a 20°C. Flutuações devido a padrões climáticos sazonais e eventos como El Niño influenciaram as temperaturas.",
    "\n2023 - Temperatura média: Cerca de 19°C a 21°C. Dados preliminares indicam uma tendência de aquecimento contínuo, com variações regionais e sazonais típicas."
]   

lista_gases = [
    "\n2019 - SO₂: Níveis médios em áreas industriais e portuárias, com picos em regiões com intensa atividade marítima. NOx: Concentrações elevadas em áreas urbanas e portuárias devido ao tráfego de veículos e navios. CO: Concentrações moderadas a elevadas nas áreas urbanas costeiras. O₃: Níveis elevados em áreas urbanas durante os meses de verão. PM10 e PM2.5: Concentrações variáveis, com picos em áreas urbanas e industriais.",
    "\n2020 - SO₂: Leve redução devido à diminuição das atividades industriais e marítimas durante a pandemia. NOx: Redução significativa em áreas urbanas devido à menor circulação de veículos. CO: Redução em áreas urbanas pela diminuição do tráfego. O₃: Concentrações variáveis, influenciadas por mudanças na emissão de precursores. PM10 e PM2.5: Redução em várias áreas devido à menor atividade econômica.",
    "\n2021 - SO₂: Níveis retornando aos valores pré-pandemia, especialmente em áreas industriais. NOx: Aumento nas áreas urbanas com a retomada das atividades. CO: Retorno aos níveis pré-pandemia em áreas urbanas. O₃: Concentrações elevadas em meses de verão, influenciadas pelo aumento das atividades. PM10 e PM2.5: Retorno gradual aos níveis anteriores, com variações regionais.",
    "\n2022 - SO₂: Níveis estabilizados em áreas com controle de emissões. NOx: Concentrações estáveis em áreas urbanas e portuárias. CO: Níveis moderados em áreas urbanas. O₃: Picos durante os meses de verão em áreas urbanas. PM10 e PM2.5: Concentrações variáveis, com influência de eventos como incêndios florestais.",
    "\n2023 - SO₂: Monitoramento contínuo, com níveis controlados em muitas áreas devido a regulamentações. NOx: Concentrações monitoradas com tendências estáveis em áreas urbanas. CO: Monitoramento contínuo com níveis estáveis em áreas urbanas. O₃: Concentrações elevadas durante os meses de verão, com variações regionais. PM10 e PM2.5: Níveis variáveis com influências sazonais e regionais."
]

admin_password = "souadministrador"

print("\nBem-vindo ao banco de dados da AquaInsight!")
access_level = force_option("Deseja acessar como Usuário ou Administrador? (U/A):\n->", ["U", "A"], "Opção inválida, tente novamente com as opções apresentadas.")

if access_level == 'A':
    for i in range(3):
        password = input("Digite a senha do Administrador: ")
        if password == admin_password:
            print("Acesso como Administrador concedido.")
            break
        else:
            print(f"Senha incorreta. Tentativas restantes: {2 - i}")
    else:
        print("Por motivos de segurança, seu acesso como Administrador foi negado.")
        access_level = 'U'
        print("Acesso como Usuário concedido.")
else:
    print("Acesso como Usuário concedido.")

while True:
    if access_level == 'U':

        option = force_option("\nEscolha uma das opções abaixo:\n1. Listar informações presentes no banco\n2. Ver detalhes do sistema\n3. Sair\n->", ["1", "2", "3"], "Opção inválida, tente novamente com as opções apresentadas.")
        
        if option == "1":
            option_1 = force_option(message_options[0], ["1", "2", "3", "4"], "Opção inválida, tente novamente com as opções apresentadas.")

            if option_1 == "1":
                print_lista(lista_nivelmar)
            elif option_1 == "2":
                print_lista(lista_umidade)
            elif option_1 == "3":
                print_lista(lista_temperatura)
            else:
                print_lista(lista_gases)

        elif option == "2":
            print(message_options[1])

        else:
            print(message_options[2])
            break

    else:

        option = force_option("\nEscolha uma das opções abaixo:\n1. Listar informações presentes no banco\n2. Ver detalhes do sistema\n3. Sair\n->", ["1", "2", "3"], "Opção inválida, tente novamente com as opções apresentadas.")
       
        if option == "1":
            option_1 = force_option(message_options[0], ["1", "2", "3", "4"], "Opção inválida, tente novamente com as opções apresentadas.")
            
            if option_1 == "1":
                print_lista(lista_nivelmar)
                add_adm_lista(lista_nivelmar, 'lista nível do mar')
                
            elif option_1 == "2":
                print_lista(lista_umidade)
                add_adm_lista(lista_umidade, 'lista umidade')

            elif option_1 == "3":
                print_lista(lista_temperatura)
                add_adm_lista(lista_temperatura, 'lista temperatura')

            else:
                print_lista(lista_gases)
                add_adm_lista(lista_gases, 'lista gases nocivos')

        elif option == "2":
            print(message_options[1])

        else:
            print(message_options[2])
            break