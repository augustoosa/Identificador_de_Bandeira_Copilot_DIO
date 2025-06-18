def identificar_bandeira(numero):
    numero = numero.replace(' ', '').replace('-', '')
    if not numero.isdigit():
        return "Número inválido"

    comprimento = len(numero)
    prefixo2 = int(numero[:2]) if len(numero) >= 2 else 0
    prefixo3 = int(numero[:3]) if len(numero) >= 3 else 0
    prefixo4 = int(numero[:4]) if len(numero) >= 4 else 0
    prefixo6 = int(numero[:6]) if len(numero) >= 6 else 0
    prefixo1 = int(numero[0]) if len(numero) >= 1 else 0

    # MasterCard
    if (51 <= prefixo2 <= 55 or 2221 <= prefixo4 <= 2720) and comprimento == 16:
        return "MasterCard"
    # Visa
    if prefixo1 == 4 and comprimento == 16:
        return "Visa"
    # American Express
    if (prefixo2 == 34 or prefixo2 == 37) and comprimento == 15:
        return "American Express"
    # Diners Club (Internacional)
    if (prefixo2 in [30, 36, 38, 39]) and 14 <= comprimento <= 19:
        return "Diners Club (Internacional)"
    # Diners Club (EUA & Canadá)
    if (prefixo2 == 54 or prefixo2 == 55) and comprimento == 16:
        return "Diners Club (EUA & Canadá)"
    # Discover
    if ((prefixo4 == 6011 or 644 <= prefixo3 <= 649 or prefixo2 == 65) and 16 <= comprimento <= 19):
        return "Discover"
    # enRoute
    if (prefixo4 == 2014 or prefixo4 == 2149) and comprimento == 15:
        return "enRoute"
    # JCB
    if (3528 <= prefixo4 <= 3589) and 16 <= comprimento <= 19:
        return "JCB"
    # Voyager
    if prefixo4 == 8699 and comprimento == 16:
        return "Voyager"
    # Hipercard
    if ((384100 <= prefixo6 <= 384120 or prefixo6 == 606282) and comprimento == 16):
        return "Hipercard"
    # Aura
    if prefixo6 == 507860 and comprimento == 16:
        return "Aura"
    return "Bandeira não identificada"

if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    print("Bandeira:", identificar_bandeira(numero))
