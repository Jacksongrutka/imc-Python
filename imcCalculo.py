peso = input("Digite o seu peso em quilogramas: ")
altura = input("Digite sua altura em metros: ")

peso = peso.replace(',', '.')
altura = altura.replace(',', '.')

try:
    peso = float(peso)
    altura = float(altura)

    imc = peso / (altura * altura)

    if imc < 18.5:
        print("Você está com o peso abaixo do recomendado.")
    elif 18.5 <= imc <= 24.9:
        print("Você está com o peso recomendado. Parabéns!")
    elif 25.0 <= imc <= 29.9:
        print("Você está com o peso acima do recomendado!")
    else:
        print("Você está com o peso muito acima do recomendado. Procure um médico.")
except ValueError:
    print("Entrada inválida. Por favor, digite valores de peso e altura válidos.")
