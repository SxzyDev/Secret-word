import os

Palavra_chave = "corda"
letras_acertadas = ["*"] * len(Palavra_chave)
tentativas = 0
max_tentativas = 6

while True:
    letra_digitada = input("Digite uma palavra de 5 letras: ").lower()
    tentativas += 1 

    if len(letra_digitada) > 5:
        print("Digite exatamente cinco letras.")
    else:
        for i in range(5):
            if letra_digitada[i] == Palavra_chave[i]:
                letras_acertadas[i] = letra_digitada[i]

        palavra_formada = "".join(letras_acertadas)
        print("Palavra formada:", palavra_formada)

        if palavra_formada == Palavra_chave:
            os.system("cls")  # No Windows, para limpar a tela; no Linux/Mac use 'clear'
            print("Você achou a Palavra Chave, Parabéns!") 
            print("A palavra era", Palavra_chave)
            print("Tentativas:", tentativas) 
            break

    if tentativas >= max_tentativas:
        print(f"Suas tentativas acabaram. A palavra correta era '{Palavra_chave}'.")
        break
