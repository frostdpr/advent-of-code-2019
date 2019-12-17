f = open('input', 'r')

for line in f:
	program = line

program = list(map(int, program.split(',')))

print('num instructions:', len(program))
		
i = 0
while True:
	instr = program[i]
	op = str(instr)[-1:]
	print(instr)
	mode = str(instr).rstrip(op.zfill(2)).zfill(3)
	print('opcode', op, 'mode', mode, 'PC', i)
	op = int(op)

	C_mode = mode[2]
	B_mode = mode[1]
	A_mode = mode[0]

	
	if op == 99:
		print('HALT')
		#print(program)
		break
	#print(program[i + 1])
	param_1 = program[i + 1] if C_mode == 1 else  program[program[i + 1]] 
	param_2 = program[i + 2] if B_mode == 1 else  program[program[i + 2]] 
	param_3 = i + 3 if A_mode == 1 else  program[i + 3]

	param_1 = int(param_1)
	param_2 = int(param_2)
	if op == 1: # add
		program[param_3] = param_1 + param_2
		i+=4
	elif op == 2: # mul
		program[param_3] = param_1 * param_2 
		i+=4
	elif op == 3: # write to program
		program[program[i+1]] = input()
		i+=2
	elif op == 4: # print to stdout
		print('Print:', program[program[i+1]])
		i+=2
			#print(i)
	
print('Program Output:', program[0])
		
		
		