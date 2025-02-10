#!/bin/bash

# Check if a model argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <model>"
    exit 1
fi

model="$1"
tp="$2"

declare -A model_map
model_map["deepseek8b"]="deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
model_map["deepseek8b_david_20250205"]="/shared/chuan/models/2_prepromptsbest2_64"
model_map["sky_32b"]="NovaSky-AI/Sky-T1-32B-Preview"
model_map["sky_32b_flash"]="NovaSky-AI/Sky-T1-32B-Flash"

# Validate model
if [[ -z "${model_map[$model]}" ]]; then
    echo "Error: Model '$model' is not recognized."
    exit 1
fi

model_name="${model_map[$model]}"


tasks=(
    # aime
    # gpqa_diamond
    # math500
    # mmlu_pro
    # livecodebench
    olympiadbench_math_en
)

mkdir -p results

for task in "${tasks[@]}"; do
    output_file="./results/${model}/${task}.txt"
    echo "Running evaluation for task: $task with model: $model_name"
    # Check if model_name is aime or gpqa_diamond
    if [[ "$model_name" == "aime" || "$model_name" == "gpqa_diamond" ]]; then
        python -m skythought_evals.eval --model $model_name --evals=$task --tp=$tp --output_file=$output_file --temperatures 0.7
    else
        python -m skythought_evals.eval --model $model_name --evals=$task --tp=$tp --output_file=$output_file
    fi
done