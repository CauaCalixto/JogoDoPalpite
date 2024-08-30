import random
from time import sleep

# Função para exibir a mensagem de boas-vindas
def exibir_boas_vindas():
    print('-=' * 30)
    print('\t\t🎮 Jogo de Adivinhação 🎮')
    print('-=' * 30)
    print("Bem-vindo(a)! Tente adivinhar o número que a IA gerou entre 1 e 50.")
    print('-=' * 30)
    print()

# Função principal do jogo
def jogar():
    IA_geradora = random.randint(1, 50)
    tentativas = 0

    while tentativas < 3:
        try:
            entrada = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        print(f"Analisando se o número {entrada} foi o valor que a IA gerou...")
        sleep(1)  # Pausa para criar suspense

        if entrada == IA_geradora:
            print("\n✅ Parabéns! Você acertou o número!\n")
            break
        else:
            tentativas += 1
            print(f"\n❌ Não foi dessa vez. Tentativa número: {tentativas}.\n")
    else:
        print("\nVocê atingiu o número máximo de tentativas.")
        print(f"O número gerado pela IA era: {IA_geradora}\n")

    jogar_novamente = input("Deseja jogar novamente? (S/N): ").strip().lower()
    if jogar_novamente == 's':
        print()
        jogar()
    else:
        print("\nObrigado por jogar! Volte sempre!\n")

# Executa o jogo
exibir_boas_vindas()
jogar()
