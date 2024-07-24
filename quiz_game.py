print ("Bem-vindo ao QUIZ")

jogar = input("Quer jogar meu QUIZ? ")
if jogar.lower() != 'sim':
    quit()
print("Então vamos nessa! ")
total  = 0

pergunta = input("Qual a marca da CPU eu uso? ")
if pergunta.lower() == "asus":
    print("certa! ")
    total +=1
else:
    print("Incorreta!")

pergunta = input("Qual a função da GPU? ")
if pergunta.lower() == "processamento de gráfico":
    print("certa! ")
    total +=1
else:
    print("Incorreta!")

pergunta = input("O que RAM faz? ")
if pergunta.lower() == "processamento de memória":
    print("certa! ")
    total +=1
else:
    print("incorreta!")

pergunta = input("O que psu faz? ")
if pergunta.lower() == "power de suport":
    print("certa! ")
    total +=1
else:
    print("incorreta!")

print(f"Você tem {total} de questões corretas")
print(f"Você tem {(total / 4) * 100} %")