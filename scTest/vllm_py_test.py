from vllm import LLM, SamplingParams
import time

prompts = ["What's the best way to cook an egg?\n"] * 10
sampling_params = SamplingParams(temperature=0.8, top_p=0.95, max_tokens=256)

llm = LLM(model="decapoda-research/llama-7b-hf", tokenizer='hf-internal-testing/llama-tokenizer')
start_time = time.time()
outputs = llm.generate(prompts, sampling_params)
print("--- %s seconds ---" % (time.time() - start_time))

# Print the outputs.
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")