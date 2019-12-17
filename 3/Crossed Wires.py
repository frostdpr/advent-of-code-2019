
'''
Test Wiring

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159

R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
'''


size = 200
wiring = [ ['.' for _ in range(size)]for _ in range(size)]

wires = ['R8,U5,L5,D3', 'U7,R6,D4,L4']


central_port = size // 2

X_locations = []
cur_x = central_port
cur_y = central_port

for wire in wires: 
	instructions = wire.split(',')
	cur_x = central_port
	cur_y = central_port
	for i in instructions:
		op = i[0]
		travel = int(i[1:]) + 1
		for j in range(travel):
			if wiring[cur_y][cur_x] == '-' or wiring[cur_y][cur_x] == '|' :
				wiring[cur_y][cur_x] = 'X'
				X_locations.append((cur_x, cur_y))
			elif op == 'R':
				wiring[cur_y][cur_x] = '-'
				cur_x += 1
			elif op == 'L':
				wiring[cur_y][cur_x] = '-'
				cur_x -= 1
			elif op == 'U':
				wiring[cur_y][cur_x] = '|'
				cur_y -= 1
			elif op == 'D':
				wiring[cur_y][cur_x] = '|'
				cur_y += 1

wiring[central_port][central_port] = 'O'

formatted_wiring = []

for row in wiring:
	formatted_wiring.append(''.join(row))

print ('\n'.join(formatted_wiring))