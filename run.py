from datetime import datetime

def read_history_file(filename):
	file = open(filename, 'r')
	return file

def write_history_file(filename, lst):
	with open(filename, 'w') as file:
		for str in lst:
			if str[0] == '#':
				timestamp = int(str[1:])
				dt = datetime.fromtimestamp(timestamp)
				date_string = '%02d.%02d.%02d %02d:%02d\n' %(dt.day, dt.month, dt.year, dt.hour, dt.minute)
				print('%s %s' %(timestamp, date_string))
				file.write('#%s' %(date_string))
			else:
				file.write(str + '\n')
	file.close()

def timestamps_rewrite(file_obj):
	lst = [i for i in file_obj.readlines()]
	file_obj.close()
	write_history_file('/tmp/bash_history', lst)

if __name__ == "__main__":
	timestamps_rewrite(read_history_file('/home/white/tmp/mikepero/root_bash_history'))

