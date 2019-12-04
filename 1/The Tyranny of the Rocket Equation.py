import math

def fuel_requirement(mass):
	return math.floor(mass/3) - 2


### PART 1 ###

f = open('input' , 'r')
total_fuel_requirement = 0

for line in f:
	total_fuel_requirement += fuel_requirement(int(line))

print('Total Fuel Requirement:', total_fuel_requirement)

### PART 2 ###

f = open('input' , 'r')
new_total_fuel_req = 0

for line in f:
	cur_fuel_req = fuel_requirement(int(line))
	cur_total_fuel = 0
	
	while cur_fuel_req > 0:
		cur_total_fuel += cur_fuel_req
		cur_fuel_req = fuel_requirement(cur_fuel_req)
	
	new_total_fuel_req += cur_total_fuel


print('Updated Fuel Req:', new_total_fuel_req)