# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

def calcular_area_base(r):
    area = 3.14*r**2
    return area

def calcular_volume_cilindro(r, h):
    area = calcular_area_base(r)
    volume = area*h
    return volume

raio = float(input("Digite o raio da base "))
altura = float(input("Digite a altura do cilindro "))
volume = calcular_volume_cilindro(raio, altura)
print(f'o volume do cilindro é {volume}')