'''
### Test Programs ###

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

'''
f = open('input', 'r')

for line in f:
	program = line

program = list(map(int, program.split(',')))
og_program = program.copy()

for x in range(0,100):
	for y in range(0,100):
		#reset program
		program = og_program.copy()
		program[1] = x
		program[2] = y
		#print(x,y)
		i = 0
		while True:
			op = program[i]
			if op == 99:
				#print('HALT')
				#print(program)
				break
			elif op == 1:
				program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]] 
				i+=4
			elif op == 2:
				program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]] 
				i+=4
			#print(i)
	
		#print(program[0])
		if program[0] == 19690720:
			print('noun and verb:', x, y)
			print('sol:', 100*x+y)
			break
		
		
