#rPi CPU data

import os

def get_CPU_temp():
	p = os.popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
	output, _error = p.communicate()
	return float(output[output.index('=') + 1:output.rindex("'")])
	
def main():
	cpu_temp = get_CPU_temp()
	print(cpu_temp)
