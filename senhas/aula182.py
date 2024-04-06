# secrets gera números aleatórios seguros.
import secrets
import string

# numeros_aleatorios = secrets.randbelow(10)
# print(numeros_aleatorios)

caracteres_validos = string.ascii_letters + string.digits

tamanho_senha = 12

senha = ''.join(secrets.choice(caracteres_validos) for i in range(tamanho_senha))

print(f'Senha segura: {senha}')