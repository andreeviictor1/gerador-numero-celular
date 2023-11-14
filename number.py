import random

def gerar_numero_celular():
    # Gerar um DDD aleatório entre 11 e 99
    ddd = random.randint(11, 99)

    # Gerar os 4 primeiros dígitos do número do celular
    prefixo = random.randint(1000, 9999)

    # Gerar os 4 últimos dígitos do número do celular
    sufixo = random.randint(1000, 9999)

    # Formatar o número de telefone
    numero_celular = f"({ddd}) {prefixo}-{sufixo}"

    return numero_celular

# Gerar um número de celular aleatório
numero_aleatorio = gerar_numero_celular()
print("Número de celular gerado:", numero_aleatorio)
