#rPi CPU data

from subprocess import PIPE, Popen
import psutil

#returns cpu temp
def get_CPU_temp():
	p = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
	o, _error = p.communicate()
	return float(o[5:-2])
	
#returns core volatage
def get_core_voltage():
	p  = Popen(['vcgencmd', 'measure_volts', 'core'], stdout=PIPE)
	o, _error = p.communicate()
	return o

def main():
	cpu_temp = get_CPU_temp()
	core_voltage = get_core_voltage()
	print(cpu_temp)
	print(core_voltage)

if __name__ == '__main__':
	main()

