# how to run:
#   python3 multiGpuTrace
#   ctrl + C to generate plot

import psutil
import datetime
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
import time
import numpy as np
import sys

DISPLAY_FLAG = True

def convertTime(t):
    tt = t.split(":")
    tHour = float(tt[0])
    tMin = float(tt[1])
    tSec = float(tt[2])
    tOutput = 3600 * tHour + 60 * tMin + tSec
    return tOutput

p = Popen(["nvidia-smi" ,"--query-gpu=utilization.gpu,temperature.gpu,fan.speed,power.draw,power.limit", "--format=csv,noheader,nounits"], stdout=PIPE)
pout, _ = p.communicate()

tmp = (pout.decode('utf-8').rstrip().split('\n'))
print(tmp)
num_gpu = len(tmp)
print(num_gpu)

f = []
# for i in range(num_gpu):
    # filename = './loss_and_acc_gpuutil/bs_8/{}_{}_log-gpu-{}.txt'.format(network,idx,i)
filename = '/workspace/FlexFlow/sclog/gpuutil_w_wait'
f.append(open(filename, 'w'))

time_array = []

cpu_dict = dict()
cpu_dict['cpu_percent'] = []

gpu_dict = dict()
for i in range(num_gpu):
    gpu_dict['gpu-%d' % i] = []

cur_time = datetime.datetime.now()
start_time = convertTime(str(cur_time).split()[1])

try:
    while True:
        cur_time = datetime.datetime.now()
        tt = convertTime(str(cur_time).split()[1])

        ttt = tt-start_time
        time_array.append(ttt)

        cpu_percent = psutil.cpu_percent()
        cpu_dict['cpu_percent'].append(float(cpu_percent))

        p = Popen(["nvidia-smi" ,"--query-gpu=utilization.gpu,temperature.gpu,fan.speed,power.draw,power.limit", "--format=csv,noheader,nounits"], stdout=PIPE)
        pout, _ = p.communicate()

        # for i in range(num_gpu):
        tmp = str(pout.decode('utf-8').rstrip().split('\n')[0]).split(', ')  # 0表示第一块GPU
        gpu_utilization = tmp[0]
        # gpu_dict['gpu-%d' % i].append(float(gpu_utilization))

        f[0].write("%s\n" % gpu_utilization) # 0表示第一块GPU

        time.sleep(0.1)

except KeyboardInterrupt:
    print("output log in log-gpu-*.txt!")
    # print(cpu_dict)
    # print(gpu_dict)

    if (DISPLAY_FLAG):
        total_len = len(gpu_dict['gpu-%d'  % (num_gpu - 1)])

        plt.subplot(num_gpu + 1, 1, 1)
        plt.plot(time_array[:total_len], cpu_dict['cpu_percent'][:total_len])
        plt.ylabel('cpu_percent')
        plt.ylim([0, 100])
        plt.yticks(np.arange(0, 101, 20))

        for i in range(num_gpu):
            plt.subplot(num_gpu + 1, 1, 2 + i)
            plt.plot(time_array[:total_len], gpu_dict['gpu-%d' % i][:total_len])
            plt.ylabel('gpu_utilization for gpu %d' % i)
            plt.ylim([0, 100])
            plt.yticks(np.arange(0, 101, 20))

        plt.show()