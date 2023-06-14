from math import pow


def calcula_juros_composto(capital, juros, tempo):
    # Função para calcular o montante final usando juros compostos
    return capital * pow((1 + juros), tempo)


capital = float(input("Qual o capital que você irá investir? "))
juros = float(input("Qual o juros anual em porcentagem (%)? "))
tempo = int(input("Quantos meses o seu dinheiro ficará rendendo? "))

juros = juros / 100
tempo = int(tempo / 12)

valor_final = calcula_juros_composto(capital, juros, tempo)

print(f"O montante final será de: {valor_final:,.2f}")
print(f"Os juros do rendimento foram de: {valor_final - capital:,.2f}")
