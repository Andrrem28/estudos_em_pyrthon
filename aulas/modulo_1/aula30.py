'''
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
 <- Contagem de complexidade (ruim)
A \ (barra invertida) é usado para quebrar linha em uma expressão.
'''

velocidade = 61 # Velocidade atual do carro
local_carro = 101 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # A distância onde o radar pega

menor_dist_radar = (LOCAL_1 - RADAR_RANGE)
maior_dist_radar = (LOCAL_1 + RADAR_RANGE)

menor_dist_local_carro = local_carro >= menor_dist_radar
maior_dist_local_carro = local_carro <= maior_dist_radar

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_ultrapassou_radar_1 = menor_dist_local_carro and maior_dist_local_carro

if vel_carro_pass_radar_1:
    print('A velocidade do carro passou no Radar 1')

if carro_ultrapassou_radar_1:
    print('O carro passou no Radar 1')

if  carro_ultrapassou_radar_1 and vel_carro_pass_radar_1:
    print('O carro foi multado no Radar 1')