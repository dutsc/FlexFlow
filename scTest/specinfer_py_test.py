import flexflow.serve as ff
import datasets
import time

ff.init(
        num_gpus=4,
        memory_per_gpu=22048,
        zero_copy_memory_per_node=20000,
        tensor_parallelism_degree=4,
        pipeline_parallelism_degree=1
    )

# Specify the LLM
llm = ff.LLM("/models/opt-13b")

# Specify a list of SSMs (just one in this case)
ssms=[]
ssm = ff.SSM("/models/opt-125m")
ssms.append(ssm)

# Create the sampling configs
generation_config = ff.GenerationConfig(
    do_sample=False, temperature=0.9, topp=0.8, topk=1
)

# Compile the SSMs for inference and load the weights into memory
for ssm in ssms:
    ssm.compile(generation_config)

# Compile the LLM for inference and load the weights into memory
compiled = llm.compile(generation_config, ssms=ssms)

prompts = ["What's the best way to cook an egg?\n"] * 10
start_time = time.time()
result = llm.generate(prompts)
print("--- %s seconds ---" % (time.time() - start_time))