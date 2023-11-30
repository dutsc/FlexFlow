#/bin/bash
# MODELNAME=("opt-13b" "opt-6.7b" "opt-1.3b" "opt-350m" "opt-125m")
# MODELNAME=("opt-6.7b" "opt-1.3b" "opt-125m")
MODELNAME=("opt-6.7b")

for model in "${MODELNAME[@]}"
do
    /workspace/FlexFlow/build/inference/incr_decoding/incr_decoding \
        -ll:gpu 1 \
        -ll:fsize 22000 \
        -ll:zsize 30000 \
        -llm-model /models/$model/ \
        -prompt /workspace/FlexFlow/prompts/prompt.json \
        -tensor-parallelism-degree 1 \
        --fusion > /workspace/FlexFlow/sclog/prefill/1GPU_incre_decoding_$model
done