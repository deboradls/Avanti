def menu():
    print("\n🌿✨ === Programa Estilo de Vida Saudável === ✨🌿")
    print("💪 1. Cadastrar Usuário")
    print("🥗 2. Ver Sugestão de Plano Alimentar")
    print("🏃 3. Ver Dicas de Exercícios")
    print("📊 4. Calcular IMC")
    print("🎯 5. Definir Meta de Saúde")
    print("🏋️ 6. Plano de Exercícios Personalizado")
    print("🚪 7. Sair")
    return input("🎯 Escolha uma opção: ")

usuarios = {}

def cadastrar_usuario():
    nome = input("📝 Digite seu nome: ")
    idade = input("🎂 Digite sua idade: ")
    peso = float(input("⚖️ Digite seu peso (kg): "))
    altura = float(input("📏 Digite sua altura (m): "))
    nivel_atividade = input("🔥 Nível de atividade (Baixo, Médio, Alto): ")
    usuarios[nome] = {"idade": idade, "peso": peso, "altura": altura, "atividade": nivel_atividade, "meta": "", "exercicio": ""}
    print(f"🎉 Usuário {nome} cadastrado com sucesso! Bem-vindo(a) ao Programa Estilo de Vida Saudável! 🍏")

def definir_meta(nome):
    if nome in usuarios:
        meta = input("🎯 Qual sua meta de saúde? (Ex: Perder peso, Ganhar massa, Melhorar resistência): ")
        usuarios[nome]["meta"] = meta
        print(f"🎯 Meta de {nome} definida como: {meta}")
    else:
        print("❌ Usuário não encontrado. Cadastre-se primeiro! 📝")

def plano_exercicios(nome):
    if nome in usuarios:
        nivel = usuarios[nome]['atividade']
        print(f"\n🏋️ Plano de exercícios para {nome}: \n")
        if nivel.lower() == "baixo":
            print("🚶 Caminhada leve por 30 min 5x por semana")
            print("🧘 Yoga ou alongamento 2x por semana")
        elif nivel.lower() == "médio":
            print("🏃 Corrida ou ciclismo 3x por semana")
            print("🏋️ Musculação moderada 2x por semana")
        else:
            print("🔥 Treino HIIT 4x por semana")
            print("💪 Musculação intensa 3x por semana")
    else:
        print("❌ Usuário não encontrado. Cadastre-se primeiro! 📝")

def sugestao_plano(nome):
    if nome in usuarios:
        print(f"\n🥑 Sugestão de plano alimentar para {nome}: 🥗")
        print("🍓 Café da manhã: Frutas, ovos e aveia")
        print("🥩 Almoço: Arroz integral, feijão, frango grelhado e salada")
        print("🍲 Jantar: Sopa de legumes ou omelete com salada")
    else:
        print("❌ Usuário não encontrado. Cadastre-se primeiro! 📝")

def dicas_exercicios():
    print("\n🏋️‍♂️ Dicas de exercícios:")
    print("🚶 Caminhada ou corrida leve por 30 minutos")
    print("💪 Treino funcional 3x por semana")
    print("🧘‍♂️ Alongamento diário para melhorar a postura")

def calcular_imc(nome):
    if nome in usuarios:
        peso = usuarios[nome]['peso']
        altura = usuarios[nome]['altura']
        imc = peso / (altura ** 2)
        print(f"\n📊 O IMC de {nome} é {imc:.2f} 📏")
        if imc < 18.5:
            print("⚠️ Você está abaixo do peso. Consuma mais proteínas, carboidratos saudáveis e gorduras boas. 🥑")
        elif 18.5 <= imc < 24.9:
            print("✅ Seu peso está normal. Mantenha uma alimentação equilibrada e pratique exercícios regularmente. 🥗")
        elif 25 <= imc < 29.9:
            print("⚠️ Você está com sobrepeso. Reduza o consumo de açúcares e aumente a ingestão de vegetais e proteínas. 🍆")
        else:
            print("🚨 Você está com obesidade. Consulte um profissional para uma dieta personalizada e pratique exercícios moderados. 🏃")
    else:
        print("❌ Usuário não encontrado. Cadastre-se primeiro! 📝")

while True:
    opcao = menu()
    if opcao == "1":
        cadastrar_usuario()
    elif opcao == "2":
        nome = input("📝 Digite seu nome: ")
        sugestao_plano(nome)
    elif opcao == "3":
        dicas_exercicios()
    elif opcao == "4":
        nome = input("📝 Digite seu nome: ")
        calcular_imc(nome)
    elif opcao == "5":
        nome = input("📝 Digite seu nome: ")
        definir_meta(nome)
    elif opcao == "6":
        nome = input("📝 Digite seu nome: ")
        plano_exercicios(nome)
    elif opcao == "7":
        print("🚪 Cuide bem da sua saúde! Tchau! 🌿💚")
        break
    else:
        print("❌ Opção inválida! Tente novamente. 🎯")