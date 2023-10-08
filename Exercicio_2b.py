# EXERCICIO B => fazer jogo da forca com função
import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento", "for_code"]
    return random.choice(palavras)

def forca():
    palavra = escolher_palavra()
    palavra_secreta = "_" * len(palavra)
    tentativas = 6
    letras_erradas = []

    
    while True:
        letra = input(f"\nPalavra secreta: {palavra_secreta}\nLetras erradas: {', '.join(letras_erradas)}\nTentativas restantes: {tentativas}\nDigite uma letra: ").lower()

        if letra.isalpha() and len(letra) == 1:
            if letra in palavra:
                for i in range(len(palavra)):
                    if palavra[i] == letra:
                        palavra_secreta = palavra_secreta[:i] + letra + palavra_secreta[i + 1:]
                if palavra_secreta == palavra:
                    print(f"\nPalavra secreta: {palavra}\nParabéns! Você venceu!")
                    break
            else:
                if letra not in letras_erradas:
                    letras_erradas.append(letra)
                    tentativas -= 1
                    if tentativas == 0:
                        print(f"\nVocê perdeu! A palavra secreta era '{palavra}'.")
                        break
        else:
            print("Por favor, digite uma única letra válida.")

if __name__ == "__main__":
    forca()
