# Estadisticas sacadas de https://es.whoscored.com/Regions/206/Tournaments/4/Seasons/7889/Stages/17702/TeamStatistics/Espa%C3%B1a-LaLiga-2019-2020
# Alan Fernando Rincon Vieyra
# 26/06/2020

import statistics

players = [
    {'name': 'Portero', 'players': 1, },
    {'name': 'Defensa', 'players': 4},
    {'name': 'Medio', 'players': 4},
    {'name': 'Delantero', 'players': 2},
]

movements = [
    # Defensivo
    { 'id': 'ib', 'name': 'Intercepta el balón', 'frecuency': 0.0, 'value': 9.9,
      'players': [0.05, 0.45, 0.3, 0.2]},
    { 'id': 'fap', 'name': 'Realiza falta con el balón', 'frecuency': 0.0, 'value': 14.5,
      'players': [0.02, 0.2, 0.3, 0.48]},
    { 'id': 'farb', 'name': 'Recibe falta con balón', 'frecuency': 0.0, 'value': 10,
      'players': [0.03, 0.2, 0.3, 0.47]},
    { 'id': 'far', 'name': 'Recibe falta sin balón', 'frecuency': 0.0, 'value': 3,
      'players': [0.01, 0.15, 0.49, 0.35]},
    { 'id': 'sdu', 'name': 'Recibe tarjeta amarilla', 'frecuency': 0.0, 'value': 2.7,
      'players': [0.02, 0.48, 0.3, 0.2]},
    { 'id': 'sdd', 'name': 'Recibe doble tarjeta amarilla', 'frecuency': 0.0, 'value': 0.6,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'sf', 'name': 'Recibe tarjeta roja', 'frecuency': 0.0, 'value': 0.1,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'sa', 'name': 'Recibe tarjeta roja luego de 2 amonestaciones', 'frecuency': 0.0, 'value': 0.05,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'per', 'name': 'Pierde el balón con tarjeta amarilla', 'frecuency': 0.0, 'value': 1.0,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'fuj', 'name': 'Comete fuera de lugar.', 'frecuency': 0.0, 'value': 2.3,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'db', 'name': 'Despeja el balón', 'frecuency': 0.0, 'value': 18.2,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'blce', 'name': 'Bloquea el balón con éxito', 'frecuency': 0.0, 'value': 11.7,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'blse', 'name': 'Bloquea el balón sin éxito', 'frecuency': 0.0, 'value': 14.0,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'bl', 'name': 'Bloquea disparo', 'frecuency': 0.0, 'value': 5.8,
      'players': [0.01, 0.49, 0.3, 0.2]},    # Jugador(3) y portero(2.8)
    # Ofensivo
    { 'id': 'gl', 'name': 'Anota gol', 'frecuency': 0.0, 'value': 1.4,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'tr', 'name': 'Realiza tiro', 'frecuency': 0.0, 'value': 12.0,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'rta', 'name': 'Acierta regate', 'frecuency': 0.0, 'value': 10.0,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'rtf', 'name': 'Falla regate', 'frecuency': 0.0, 'value': 6.5,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'perb', 'name': 'Pierde el balón', 'frecuency': 0.0, 'value': 23.8,
      'players': [0.01, 0.49, 0.3, 0.2]}, # Toque no exitoso(14.8) y desposeido(9)
    { 'id': 'rb', 'name': 'Recupera el balón', 'frecuency': 0.0, 'value': 8.0,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'pn', 'name': 'Comete penalti', 'frecuency': 0.0, 'value': 0.2,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'repnb', 'name': 'Recibe penalti con balón', 'frecuency': 0.0, 'value': 0.18,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'repn', 'name': 'Recibe penalti sin balón', 'frecuency': 0.0, 'value': 0.02,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    # Distribucion
    { 'id': 'pl', 'name': 'Realiza pase largo', 'frecuency': 0.0, 'value': 30.0,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'pc', 'name': 'Realiza pase corto', 'frecuency': 0.0, 'value': 350.0,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'as', 'name': 'Asiste a otro jugador', 'frecuency': 0.0, 'value': 0.9,
      'players': [0.01, 0.49, 0.3, 0.2]},
    { 'id': 'cn', 'name': 'Realiza centro', 'frecuency': 0.0, 'value': 4.3,
      'players': [0.01, 0.49, 0.3, 0.2]},
    # Otro
    { 'id': 'fubc', 'name': 'Saca el balón del campo de juego', 'frecuency': 0.0, 'value': 10.0,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'mac', 'name': 'Comete mano', 'frecuency': 0.0, 'value': 0.7,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'adv', 'name': 'Recibe advertencia', 'frecuency': 0.0, 'value': 1.0,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
    { 'id': 'exp', 'name': 'Expulsión del juego', 'frecuency': 0.0, 'value': 0.12,
      'players': [0.01, 0.49, 0.3, 0.2]}, #*
]

movements = sorted(movements, key=lambda movement : movement['value'], reverse=True)

# print(len(movements), movements)

total_movements = 0
for movement in movements:
    total_movements += movement['value']

for movement in movements:
    movement['frecuency'] = movement['value'] / total_movements
    print(movement['frecuency'], movement['name'])

def payoff(player, movement):
  if player['name'] == 'Portero':
    if movement['id'] == 'bl':
      return movement['frecuency']
    elif movement['id'] == 'bl':
      return movement['frecuency']