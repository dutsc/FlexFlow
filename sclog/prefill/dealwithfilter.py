



file_names = ["filter_incre_decoding_opt-13b","filter_incre_decoding_opt-6.7b",
              "filter_incre_decoding_opt-1.3b","filter_incre_decoding_opt-125m"]


for file in file_names:
    LLMTimes = []
    a = 1
    mod = 2
    with open(file,'r') as f:
        line = f.readline()
        while line != "":
            line = line.strip().split(":")
            # print(line[-1][:-2])
            strNum = line[-1][:-2]
            pointNum = (float)(line[-1][:-3])
            # print(pointNum)
            LLMTimes.append(pointNum*1000)
            line = f.readline()
            a = a+1
            
    import numpy as np

    meanLLMTimes = np.mean(LLMTimes)

    print(file)
    # print(LLMTimes)
    print(f"mean LLM time: {meanLLMTimes} ms.")