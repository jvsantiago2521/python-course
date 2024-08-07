#Gera numeros aleatorios seguros (DIFERENTE DO RANDOM)
import secrets
import string as s
from secrets import SystemRandom as Sr

#Tudo que temos no random, vamos ter aqui, porem com segurança
random = secrets.SystemRandom()

#Gera numero aleatorio abaixo de 100
print(secrets.randbelow(100))

#print em todas as letras minusculas e maiusculas, numeros e pontuacoes/simbolos
print(s.ascii_letters, s.digits, s.punctuation)

#Gera uma senha aleatoria unindo todos os valores do resultado de choices de todas as letras minusculas e maiusculas, numeros e pontuacoes/simbolos
senha_aleatoria = "".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=10))
print(f"Sua senha é: {senha_aleatoria}")