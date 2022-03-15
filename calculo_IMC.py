def calculo_IMC():
    altura = float(input('Digite sua altura (m): '))
    peso = float(input('Digite seu peso (kg): '))
    IMC = round(peso / (altura ** 2), 2)

    '''
    Tabela de resultados - IMC
    O IMC pode trazer os seguintes resultados:

    IMC	                Resultado
    Menos do que 18,5	Abaixo do peso
    Entre 18,5 e 24,9	Peso normal
    Entre 25 e 29,9	    Sobrepeso
    Entre 30 e 34,9	    Obesidade grau 1
    Entre 35 e 39,9	    Obesidade grau 2
    Mais do que 40	    Obesidade grau 3
    '''

    if IMC < 18.5:
        print(f'\nIMC é: {IMC} | Abaixo do peso')
    elif 18.5 <= IMC <= 24.9:
        print(f'\nIMC é: {IMC} | Peso Normal')
    elif 25.0 <= IMC <= 29.9:
        print(f'\nIMC é: {IMC} | Sobrepeso')
    elif 30.0 <= IMC <= 34.9:
        print(f'\nIMC é: {IMC} | Obesidade grau 1')
    elif 35.0 <= IMC <= 39.9:
        print(f'\nIMC é: {IMC} | Obesidade grau 2')
    else:
        print(f'\nIMC é: {IMC} | Obesidade grau 3')

calculo_IMC()