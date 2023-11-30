


SSMTimes = []
LLMTimes = []
a = 1
mod = 2
with open('./r4_filter','r') as f:
    line = f.readline()
    while line != "":
        line = line.strip().split(":")
        # print(line[-1][:-2])
        strNum = line[-1][:-2]
        pointNum = (float)(line[-1][:-2])
        # print(pointNum)
        if a % mod == 1:
            # SSMs
            SSMTimes.append(pointNum)
        else:
            # LLM
            LLMTimes.append(pointNum)
        line = f.readline()
        a = a+1
        
import numpy as np

meanSSMTimes = np.mean(SSMTimes)
meanLLMTimes = np.mean(LLMTimes)

print(SSMTimes)
print(LLMTimes)

print(f"mean SSM time: {meanSSMTimes}")
print(f"mean LLM time: {meanLLMTimes}")