import numpy as np
'----------------------------------------------------------------------------------------------------------------------'
'### Simulação do Operador Lógico AND ###'

'@Author: Antônio Flávio'
'@Date 27/02/2019 - 16:21'
'@Prof: Márcio Piva'
'----------------------------------------------------------------------------------------------------------------------'

# 1º Criando a matrix com dados de entrada X

# Entradas - Matrix 4 X 4 - Seguindo o PDF do professor
X = np.array([
             [1, 0, 0, 0],
             [1, 0, 1, 0],
             [1, 1, 0, 0],
             [1, 1, 1, 1]])

# 2º Criando o vetor com a saída esperada

# Saída esperada - Vetor
T = np.array(
              [0, 0, 0, 1]
            )
# 3º Criando um vetor com os pesos - iniciando todos com 0 - Seguindo o PDF do professor

# OBS: Pq array com 4 posições ? pq para multiplicar uma matrix, eu preciso que o numero de linha seja igual a numero de colunas.
# Pesos - vetor com o pesos
pesos = np.array(
                  [0.0, 0.0, 0.0, 0.0]
                )
# 4º Taxa de Aprendizado - Seguindo o PDF do professor

# Taxa de Aprendizado
taxaAprendizado = 0.5

# 5º Função degrau - Explicado na aula pelo professor

# Resumindo: Se o valor > 0 ele irá retorna 1, caso contrário 0
def degrau(s):
    return 1 if s > 0 else 0

# 6º Função que recebe as entradas - multiplica as entradas pelos pesos

# Resumindo: Entra um vetor[x] e essa função faz o somatorio do produto
def calculaSaida(e):
    s = e.dot(pesos)
    return degrau(s)

# 7º Função de treinamento


def treinar():

    error = 1
    ciclo = 0

    while(error != 0): #Loop só para quando o error for falso == 0

        ciclo += 1

        print('\n', ciclo, 'º Cicle\n')

        error = 0

        for i in range(len(T)):
            saidaCalculada = calculaSaida(np.asarray(X[i])) #Faz o calculo da saida com os pesos atuais

            comparacao = abs(T[i] - saidaCalculada) #Compara se o valor que saiu é o valor da saída esperada

            error += comparacao #Adiciona no erro para fazer a verificao no if e no loop



            print('Entrada ', i + 1 , ': f(w0 * x0 * + w1 * x1 + w2 * x2)', end="")


            if error != 0:

                print(' = ', saidaCalculada, ' != ', T[i])

                for p in range(len(pesos)):

                    pesoanterior = pesos[p]

                    pesos[p] = pesos[p] + (taxaAprendizado * (T[i] - saidaCalculada) * X[i][p])

                    print('w0 = w0+ ( t- sout ) * x0 = ', pesoanterior, ' + ', taxaAprendizado, '* ( ', T[i], ' - ',
                          saidaCalculada, ' ) x ', X[i][p], ' = ', pesos[p])
            else:
                print(' = ', T[i])


treinar()

#Rede Neural treinada!
for i in range(0, 4):
    print(calculaSaida(X[i]))



