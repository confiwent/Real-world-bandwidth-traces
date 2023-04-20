import numpy as np
import datetime


FILE_PATH = './video_sent_2021-12-30T11_2021-12-31T11.csv'
OUTPUT_PATH = './cooked_puffer_211230_new/'
NUM_LINES = np.inf
NUM_FILES = 500
TIME_ORIGIN = datetime.datetime.utcfromtimestamp(0)
MINI_LENS = 50
B_IN_MB = 1000000
MILLISECOND = 1e3
NANOSECOND = 1e9
VALUE_UPPER = 4.0
VALUE_LOWER = 0.3
BITS_IN_BYTES = 8


bw_measurements = {}
timestamp_measurements = {}
def main():
	line_counter = 0
	with open(FILE_PATH, 'r') as f:
		for line in f:
			if line_counter > 0:
				parse = line.split(',')

				dtime = float(parse[0]) # nanoseconds 1e-9
				# dtime = (datetime.datetime.strptime(parse[1],'%Y-%m-%d %H:%M:%S') 
				# 	- TIME_ORIGIN).total_seconds()
				session_id = parse[1]
				index = parse[2]
				throughput = float(parse[13])  # bytes per second


				k = (session_id, index)

				if k in bw_measurements:
					bw_measurements[k].append(float(throughput/B_IN_MB))
					# bw_measurements[k].append(float(throughput))
					timestamp_measurements[k].append(float(dtime/NANOSECOND))
				else:
					bw_measurements[k] = [float(throughput/B_IN_MB)]
					# bw_measurements[k] = [float(throughput)]
					timestamp_measurements[k] = [float(dtime/NANOSECOND)]
					# start_timestamp = dtime

			line_counter += 1
			if line_counter >= NUM_LINES:
				break

	file_counter = 0
	for k in bw_measurements:
		mean_bw = np.mean(bw_measurements[k])
		if len(bw_measurements[k]) >= MINI_LENS and np.mean(bw_measurements[k]) >= VALUE_LOWER and np.mean(bw_measurements[k]) < VALUE_UPPER:
			out_file = 'trace' + '_'.join(k)
			out_file = out_file.replace(':', '-')
			out_file = out_file.replace('/', '-')
			out_file = OUTPUT_PATH + out_file
			# with open(out_file, 'wb') as exf:
			# 	for i in bw_measurements[k]:
			# 		f.write(str(i) + '\n')
			with open(out_file, 'w') as f:
				for i in range(len(bw_measurements[k])):
					f.write(str(float((timestamp_measurements[k][i] - timestamp_measurements[k][0]))) + '\t' + str(bw_measurements[k][i]) + '\n')
			file_counter += 1
		if file_counter >= NUM_FILES:
			break


if __name__ == '__main__':
	main()

