import matplotlib.pyplot as plt

init_lines = []
with open("./each_token_time",'r') as f:
    line = f.readline()
    while line!="":
        line = line.strip()
        init_lines.append(line)
        line = f.readline()
        
# print(lines[1].split(' '))
start = 0

beam_depth = 16
for j in range(10):
    
    ssm0 = []
    ssm1 = []
    lines = init_lines[j*beam_depth:(j+1)*beam_depth]
    min = int(lines[0].split()[-1])
    
    for i in range(0,beam_depth):
        line = lines[i]
        line = line.split(' ')
        if line[-6] == '0':
            ssm0.append(int(line[-1])-min)
        else:
            ssm1.append(int(line[-1])-min)

    print(ssm0)
    print(ssm1)
        
    plt.plot(ssm0, marker = 'o',label="ssm0",color="red")
    plt.plot(ssm1, marker = 'o',label="ssm1",color="blue")
    filename = "./test_" + str(j) + ".jpg"
    plt.savefig(filename)
    plt.clf()
