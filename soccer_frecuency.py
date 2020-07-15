# Estadisticas sacadas de https://es.whoscored.com/Regions/206/Tournaments/4/Seasons/7889/Stages/17702/TeamStatistics/Espa%C3%B1a-LaLiga-2019-2020
# Alan Fernando Rincon Vieyra
# 26/06/2020
#
# N : Número de jugadores.
#
# S_k^î : Estrategia (acción) k-ésima del jugador i.
#     Ej: Anotar gol, etc.
# 
# D_i : Conjunto de estrategias del jugador i.
#     D_i = {S_1^î, ..., S_k^î, ..., S_p^î}
#     |D_i| = p
# 
# D : Perfiles de estrategias.
#     D = D_1 x D_2 x ... x D_N
# 
# d : Perfil de estrategia.
#     d in D
#     Ej: d = (S_m^1, S_n^2, ..., S_r^N)
#         donde:
#         m : m-ésima jugada del jugador 1.
#         n : n-ésima jugada del jugador 2.
#         ...
#         r : r-ésima jugada del jugador N.
# 
# U_i : Función de utilidad del jugador i.
#     (Funcion suma de prob. ... ver  pdf)
# 
# D_l,i : Distancia Manhattan entre jugadores.
#
import statistics
import sys

roles = [
  {'name': 'Portero', 'movements': []},
  {'name': 'Defensa', 'movements': []},
  {'name': 'Medio', 'movements': []},
  {'name': 'Delantero', 'movements': []},
]

players = [0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]

movements = [
    # Defensivo
    { 'id': 'ib', 'name': 'Intercepta el balón', 'frecuency': 0.0, 'times': 9.9,
      'players': [0.05, 0.40, 0.35, 0.20], 'gain': 0.7},
    { 'id': 'fap', 'name': 'Realiza falta con el balón', 'frecuency': 0.0, 'times': 14.5,
      'players': [0.01, 0.35, 0.40, 0.24], 'gain': 0.0},
    # { 'id': 'farb', 'name': 'Recibe falta con balón', 'frecuency': 0.0, 'times': 10,
    #   'players': [0.03, 0.2, 0.3, 0.47], 'gain': 0.5},
    # { 'id': 'far', 'name': 'Recibe falta sin balón', 'frecuency': 0.0, 'times': 3,
      # 'players': [0.01, 0.35, 0.49, 0.15], 'gain': 0.5},
    { 'id': 'sdu', 'name': 'Recibe tarjeta amarilla', 'frecuency': 0.0, 'times': 2.7,
      'players': [0.02, 0.48, 0.30, 0.20], 'gain': 0.0},
    # { 'id': 'sdd', 'name': 'Recibe doble tarjeta amarilla', 'frecuency': 0.0, 'times': 0.6,
      # 'players': [0.01, 0.49, 0.3, 0.2], 'gain': 0.0},
    # { 'id': 'sf', 'name': 'Recibe tarjeta roja', 'frecuency': 0.0, 'times': 0.1,
      # 'players': [0.01, 0.40, 0.39, 0.20], 'gain': 0.0},
    # { 'id': 'sa', 'name': 'Recibe tarjeta roja luego de 2 amonestaciones', 'frecuency': 0.0, 'times': 0.05,
      # 'players': [0.01, 0.4, 0.2, 0.39], 'gain': 0.0},
    # { 'id': 'per', 'name': 'Pierde el balón con tarjeta amarilla', 'frecuency': 0.0, 'times': 0.5,
      # 'players': [0.01, 0.4, 0.2, 0.39], 'gain': 0.0}, #*
    { 'id': 'fuj', 'name': 'Comete fuera de lugar.', 'frecuency': 0.0, 'times': 2.3,
      'players': [0.01, 0.15, 0.19, 0.45], 'gain': 0.0},
    { 'id': 'db', 'name': 'Despeja el balón', 'frecuency': 0.0, 'times': 18.2,
      'players': [0.70, 0.25, 0.03, 0.02], 'gain': 0.8},
    # { 'id': 'blce', 'name': 'Bloquea el balón con éxito', 'frecuency': 0.0, 'times': 11.7,
      # 'players': [0.30, 0.25, 0.24, 0.21], 'gain': 0.6},
    # { 'id': 'blse', 'name': 'Bloquea el balón sin éxito', 'frecuency': 0.0, 'times': 14.0,
      # 'players': [0.30, 0.25, 0.24, 0.21], 'gain': 0.0}, #*
    { 'id': 'bl', 'name': 'Bloquea disparo', 'frecuency': 0.0, 'times': 5.8,
      'players': [0.30, 0.25, 0.24, 0.21], 'gain': 0.9},    # Jugador(3) y portero(2.8)
    # Ofensivo
    { 'id': 'gl', 'name': 'Anota gol', 'frecuency': 0.0, 'times': 1.4,
      'players': [0.01, 0.18, 0.21, 0.60], 'gain': 1.0},
    { 'id': 'tr', 'name': 'Realiza tiro', 'frecuency': 0.0, 'times': 12.0,
      'players': [0.01, 0.20, 0.29, 0.50], 'gain': 0.9},
    { 'id': 'rta', 'name': 'Acierta regate', 'frecuency': 0.0, 'times': 10.0,
      'players': [0.01, 0.39, 0.35, 0.25], 'gain': 0.8},
    # { 'id': 'rtf', 'name': 'Falla regate', 'frecuency': 0.0, 'times': 6.5,
      # 'players': [0.01, 0.39, 0.35, 0.25], 'gain': 0.0},
    { 'id': 'perb', 'name': 'Pierde el balón', 'frecuency': 0.0, 'times': 23.8,
      'players': [0.01, 0.2, 0.39, 0.4], 'gain': 0.0}, # Toque no exitoso(14.8) y desposeido(9)
    { 'id': 'rb', 'name': 'Recupera el balón', 'frecuency': 0.0, 'times': 8.0,
      'players': [0.01, 0.39, 0.35, 0.25], 'gain': 0.7}, #*
    { 'id': 'pn', 'name': 'Comete penalti', 'frecuency': 0.0, 'times': 0.2,
      'players': [0.01, 0.15, 0.19, 0.65], 'gain': 0.0},
    { 'id': 'repnb', 'name': 'Recibe penalti con balón', 'frecuency': 0.0, 'times': 0.18,
      'players': [0.01, 0.15, 0.19, 0.65], 'gain': 0.8}, #*
    # { 'id': 'repn', 'name': 'Recibe penalti sin balón', 'frecuency': 0.0, 'times': 0.02,
      # 'players': [0.01, 0.15, 0.19, 0.65], 'gain': 0.8}, #*
    # Distribucion
    { 'id': 'pl', 'name': 'Realiza pase largo', 'frecuency': 0.0, 'times': 30.0,
      'players': [0.10, 0.25, 0.35, 0.30], 'gain': 0.4},
    { 'id': 'pc', 'name': 'Realiza pase corto', 'frecuency': 0.0, 'times': 350.0,
      'players': [0.05, 0.37, 0.32, 0.26], 'gain': 0.5},
    # { 'id': 'as', 'name': 'Asiste a otro jugador', 'frecuency': 0.0, 'times': 0.9,
      # 'players': [0.01, 0.49, 0.4, 0.1], 'gain': 0.8},
    { 'id': 'cn', 'name': 'Realiza centro', 'frecuency': 0.0, 'times': 4.3,
      'players': [0.01, 0.21, 0.46, 0.32], 'gain': 0.8},
    # Otro
    # { 'id': 'fubc', 'name': 'Saca el balón del campo de juego', 'frecuency': 0.0, 'times': 10.0,
      # 'players': [0.01, 0.25, 0.44, 0.30], 'gain': 0.0}, #*
    # { 'id': 'mac', 'name': 'Comete mano', 'frecuency': 0.0, 'times': 0.1,
      # 'players': [0.01, 0.44, 0.30, 0.25], 'gain': 0.0}, #*
    # { 'id': 'adv', 'name': 'Recibe advertencia', 'frecuency': 0.0, 'times': 1.0,
      # 'players': [0.01, 0.42, 0.37, 0.2], 'gain': 0.0}, #*
    # { 'id': 'exp', 'name': 'Expulsión del juego', 'frecuency': 0.0, 'times': 0.12,
      # 'players': [0.01, 0.45, 0.34, 0.2], 'gain': 0.0}, #*
]

movements = sorted(movements, key=lambda movement : movement['times'], reverse=True)
movements_len = len(movements)
print('Jugadas:', len(movements))

# Calcular la frecuencia de cada jugada.
total_mov_in_play = 0
for movement in movements:
    total_mov_in_play += movement['times']

for movement in movements:
    movement['frecuency'] = movement['times'] / total_mov_in_play
    #print(movement['frecuency'], movement['name'])

##########################################################
N = len(players)

def get_idx_rol(idx_player):
  if idx_player == 0:
    return 0
  elif idx_player >= 1 and idx_player <= 4:
    return 1
  elif idx_player >= 5 and idx_player <= 7:
    return 2
  elif idx_player >= 8 and idx_player <= 10:
    return 3
  return 0

# Funcion para determinar los movimientos de cada jugador (rol).
def determine_movements_rol():
  for movement in movements:

    max_frec_mov_rol = 0
    for idx_rol in range(len(roles)):
      if movement['players'][idx_rol] > max_frec_mov_rol:
        max_frec_mov_rol = movement['players'][idx_rol]

    for idx_rol in range(len(roles)):
      # Agregar solo las jugadas que realiza mas del 80% de las veces
      # con respecto al rol que mas la realiza.
      if movement['players'][idx_rol] / max_frec_mov_rol > 0.80:
        roles[idx_rol]['movements'].append(movement)

  for role in roles:
    print(len(role['movements']))

# Función que devuelve el promedio de la ocurrencia de una jugada
# realizada por todos sus jugadores.
def PM(movement):
  return movement['times'] / N

# Función que devuelve la ocurrencia de una jugada en el estado actual.
def p(movement):
  return PM(movement) / movements_len

# Función que devuelve la factibilidad de que un rol (jugador) realice
# una jugada.
def PMr(idx_rol, movement):
  return movement['players'][idx_rol] * movement['frecuency'] * 100.0

# Función que devuelve la distancia Manhattan entre dos jugadores (roles).
def Dli(l, idx_rol):
  return abs(l - idx_rol) + 1

# Funcion de utilidad de un jugador (rol), dado un perfil de estrategia.
def Ui(idx_rol, strategy):
  sum = 0.0

  for l in range(N):
    aux = PMr(idx_rol, strategy[l]) * p(strategy[l])  # * strategy[i]['gain']
    sum += aux / Dli(l, idx_rol)
  
  return sum

# Función que encuentra los perfiles de estrategia no dominados de todos
# los jugadores (roles).
# Estrategias totales: 2× 7×7×7×7× 8×8×8× 7×7×7 = 8.4x10^8
def strategy_filter(mov_ini, mov_end):
  # print(mov_ini, mov_end)
  ui_max = -10000
  best_strategy = {}

  # Generar perfiles de estrategia
  for m1 in roles[players[0]]['movements']:
    for m2 in roles[players[1]]['movements']:
      for m3 in roles[players[2]]['movements']:
        for m4 in roles[players[3]]['movements']:
          for m5 in roles[players[4]]['movements']:
            for m6 in roles[players[5]]['movements'][mov_ini : mov_end]:
              for m7 in roles[players[6]]['movements']:
                for m8 in roles[players[7]]['movements']:
                  for m9 in roles[players[8]]['movements']:
                    for m10 in roles[players[9]]['movements']:
                      for m11 in roles[players[10]]['movements']:
                        strategy = [m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11]
                        uo = Ui(0, strategy)  # Portero
                        u1 = Ui(1, strategy)  # Defensa
                        u2 = Ui(2, strategy)  # Medio
                        u3 = Ui(3, strategy)  # Delantero
TODO
                        if ui > ui_max:
                          ui_max = ui
                          best_strategy = strategy
  print('\n>>>>> Rol:', roles[idx_rol],', ui_max: ', ui_max, best_strategy)

##########################################################

mov_ini = int(sys.argv[1])
mov_end = int(sys.argv[2])
print(mov_ini, mov_end)

determine_movements_rol()
# strategy_filter(mov_ini, mov_end)






# Funcion para calcular la mejor estrategia del equipo 1 dada
# una estrategia del equipo 2.
def get_best_strategy_team1(strategy_team2):
  mov_num = len(movements)
  # mov_num = 2

  best_gain = 0.0
  best_strategy = []

  for m1_1 in range(mov_num):
    for m1_2 in range(mov_num):
      for m1_3 in range(mov_num):
        for m1_4 in range(mov_num):
          for m1_5 in range(mov_num):
            for m1_6 in range(mov_num):
              for m1_7 in range(mov_num):
                for m1_8 in range(mov_num):
                  for m1_9 in range(mov_num):
                    for m1_10 in range(mov_num):
                      for m1_11 in range(mov_num):
                        strategy_team1 = [movements[m1_1], movements[m1_2], movements[m1_3], movements[m1_4], movements[m1_5], movements[m1_6], movements[m1_7], movements[m1_8], movements[m1_9], movements[m1_10], movements[m1_11]]
                        gain = f1(strategy_team1, strategy_team2)

                        if gain > best_gain:
                          best_gain = gain
                          best_strategy = strategy_team1
  return best_strategy

# Funcion para calcular la mejor estrategia del equipo 2 dada
# una estrategia del equipo 1.
def get_best_strategy_team2(strategy_team1):
  mov_num = len(movements)
  # mov_num = 2

  best_gain = 0.0
  best_strategy = []

  for m2_1 in range(mov_num):
    for m2_2 in range(mov_num):
      for m2_3 in range(mov_num):
        for m2_4 in range(mov_num):
          for m2_5 in range(mov_num):
            for m2_6 in range(mov_num):
              for m2_7 in range(mov_num):
                for m2_8 in range(mov_num):
                  for m2_9 in range(mov_num):
                    for m2_10 in range(mov_num):
                      for m2_11 in range(mov_num):
                        strategy_team2 = [movements[m2_1], movements[m2_2], movements[m2_3], movements[m2_4], movements[m2_5], movements[m2_6], movements[m2_7], movements[m2_8], movements[m2_9], movements[m2_10], movements[m2_11]]
                        gain = f2(strategy_team1, strategy_team2)

                        if gain > best_gain:
                          best_gain = gain
                          best_strategy = strategy_team2
  return best_strategy

# Funcion para calcular el equilibrio de Nash para escoger la
# mejor estrategia de ambos equipos.
def calc_nash_equilibrium():
  mov_num = len(movements)
  # mov_num = 2
  nash_equilibrium = ()

  for m2_1 in range(mov_num):
    for m2_2 in range(mov_num):
      for m2_3 in range(mov_num):
        for m2_4 in range(mov_num):
          for m2_5 in range(mov_num):
            for m2_6 in range(mov_num):
              for m2_7 in range(mov_num):
                for m2_8 in range(mov_num):
                  for m2_9 in range(mov_num):
                    for m2_10 in range(mov_num):
                      for m2_11 in range(mov_num):
                        strategy_team2 = [movements[m2_1], movements[m2_2], movements[m2_3], movements[m2_4], movements[m2_5], movements[m2_6], movements[m2_7], movements[m2_8], movements[m2_9], movements[m2_10], movements[m2_11]]
                        best_strategy_team1 = get_best_strategy_team1(strategy_team2)
                        best_strategy_team2 = get_best_strategy_team2(best_strategy_team1)

                        if strategy_team2 == best_strategy_team2:
                          nash_equilibrium = (best_strategy_team1, best_strategy_team2)
                          return nash_equilibrium

  return nash_equilibrium

# nash_equilibrium = calc_nash_equilibrium()
# gain_1 = f1(nash_equilibrium[0], nash_equilibrium[1])
# gain_2 = f2(nash_equilibrium[0], nash_equilibrium[1])
# print('Nash equilibrium:')
# print('Costo-beneficio equipo 1:', gain_1)
# print('Costo-beneficio equipo 2:', gain_2)
# print('Estrategia equipo 1:')
# for i in range(len(nash_equilibrium[0])):
#   print(players[i]['name'], nash_equilibrium[0][i]['name'])
# print('Estrategia equipo 2:')
# for i in range(len(nash_equilibrium[1])):
#  print(players[i]['name'], nash_equilibrium[1][i]['name'])
