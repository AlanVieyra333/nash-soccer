import statistics

movements = {}

movements['db'] = { 'id': 'db', 'name': 'pass ball', 'frecuency': 0.0, 'value': 34.85 }
movements['rb'] = { 'id': 'rb', 'name': 'run with ball ', 'frecuency': 0.0, 'value': 26.12 }
movements['cb'] = { 'id': 'cb', 'name': 'catch ball ', 'frecuency': 0.0, 'value': 22.1}
movements['tl'] = { 'id': 'tl', 'name': 'tackle the player', 'frecuency': 0.0, 'value': 22 }
movements['d10'] = { 'id': 'd10', 'name': 'First down got', 'frecuency': 0.0, 'value': 20.17 }
movements['adb'] = { 'id': 'adb', 'name': 'advance with ball', 'frecuency': 0, 'value': 15 }
movements['ob'] = { 'id': 'ob', 'name': 'stop the ball', 'frecuency': 0.0, 'value': 10 }
movements['kfb'] = { 'id': 'kfb', 'name': 'kick the ball', 'frecuency': 0.0, 'value': 5.06 }
movements['p'] = { 'id': 'p', 'name': 'punt', 'frecuency': 0.0, 'value': 4.73 }
movements['td'] = { 'id': 'td', 'name': 'touchdown', 'frecuency': 0.0, 'value': 2.55 }
movements['qs'] = { 'id': 'qs', 'name': 'quaterback sacks', 'frecuency': 0.0, 'value': 2.51 }
movements['ga'] = { 'id': 'ga', 'name': 'field goal', 'frecuency': 0.0, 'value': 1.56 }
movements['re'] = { 'id': 're', 'name': 'conversion', 'frecuency': 0, 'value': 0.13 }
movements['beo'] = { 'id': 'beo', 'name': 'roll back the adversary', 'frecuency': 0.0, 'value': 0.11 }
movements['sf'] = { 'id': 'sf', 'name': 'safety', 'frecuency': 0.0, 'value': 0.10 }
movements['dg'] = { 'id': 'dg', 'name': 'delay game', 'frecuency': 0.0, 'value': 0.05 }
movements['fs'] = { 'id': 'fs', 'name': 'false start', 'frecuency': 0.0, 'value': 0.01 }
movements['h'] = { 'id': 'h', 'name': 'holding', 'frecuency': 0.0, 'value': 0.005 }

# print(len(movements))

total_movements = 0
for movement in movements.items():
    total_movements += movement[1]['value']

for movement in movements.items():
    movement[1]['frecuency'] = movement[1]['value'] / total_movements
    print(movement[1]['frecuency'], movement[1]['name'])