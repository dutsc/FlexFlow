import os
from transformers import AutoModelForCausalLM
import torch

def convert_hf_model(model, dst_folder):
    os.makedirs(dst_folder, exist_ok=True)
    for name, params in model.named_parameters():
        name = (
            name.replace(".", "_")
            .replace("self_attn", "attention")
            .replace("q_proj", "wq")
            .replace("k_proj", "wk")
            .replace("v_proj", "wv")
            .replace("o_proj", "wo")
            .replace("mlp", "feed_forward")
            .replace("gate_proj", "w1")
            .replace("down_proj", "w2")
            .replace("up_proj", "w3")
            .replace("input_layernorm", "attention_norm")
            .replace("post_attention_layernorm", "ffn_norm")
            .replace("embed_tokens", "tok_embeddings")
            .replace("lm_head", "output")
            .replace("model_", "")
        )
        params.detach().cpu().numpy().tofile(f"{dst_folder}/{name}")


# 对于每个模型，下载（如果还没有下载），然后转换
# models = ["/models/llama-68m", "/models/llama-160m"]
# models = ["/models/llama/llama-7b-hf"]
models = ["/share/llama2/model/llama-2-7b-hf"]
for model_name in models:
    model = AutoModelForCausalLM.from_pretrained(model_name)
    # 为每个模型设置目标文件夹路径
    dst_folder = os.path.join(model_name, "half-precision")
    convert_hf_model(model, dst_folder)
