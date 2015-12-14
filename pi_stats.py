#rPi CPU data

from subprocess import PIPE, Popen

def get_CPU_temp():
	p = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
	o, _error = p.communicate()
	return o[:]
	
def main():
	cpu_temp = get_CPU_temp()
	print(cpu_temp)

if __name__ == '__main__':
	main()

