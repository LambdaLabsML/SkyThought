import os
import json
import argparse
import pandas as pd


def extract_accuracy(file_path):
    """Extracts accuracy value from a given benchmark result file."""
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if '"acc"' in line:
                    data = json.loads(line.strip())
                    return data.get("acc", None)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None


def extract_cost(file_path):
    """Extracts avg_completion_tokens from a given cost JSON file."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("avg_completion_tokens", None)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None


def compile_results(input_path, task_list):
    models = sorted([d for d in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, d))])
    
    accuracy_data = {task: {} for task in task_list}
    cost_data = {task: {} for task in task_list}
    
    for model in models:
        model_path = os.path.join(input_path, model)
        token_usage_path = os.path.join(model_path, "token_usage", "token_usage")
        
        for task in task_list:
            acc_file = os.path.join(model_path, f"{task}.txt")
            if os.path.exists(acc_file):
                accuracy_data[task][model] = extract_accuracy(acc_file)
            
            if os.path.exists(token_usage_path):
                cost_files = [f for f in os.listdir(token_usage_path) if f"_{task}_" in f and f.endswith(".json")]
                if cost_files:
                    cost_file = os.path.join(token_usage_path, cost_files[0])  # Assuming only one matching file
                    cost_data[task][model] = extract_cost(cost_file)
    
    return models, accuracy_data, cost_data


def format_markdown_table(models, data, highlight_max=True):
    """Formats a markdown table from the data dictionary, highlighting max/min values appropriately."""
    df = pd.DataFrame.from_dict(data, orient='index', columns=models)
    df = df.sort_index()
    df = df.where(pd.notna(df), "")  # Ensure NaN values are replaced with empty strings
    
    md_table = "| Task | " + " | ".join(models) + " |\n"
    md_table += "|---" + "|---" * len(models) + "|\n"
    
    for task, row in df.iterrows():
        row_values = row.to_dict()
        values = [v for v in row_values.values() if v != ""]
        
        if not values:
            md_table += f"| {task} | " + " | ".join(["" for _ in models]) + " |\n"
            continue
        
        if highlight_max:
            best_value = max(v for v in values if v is not None)
        else:
            best_value = min(v for v in values if v is not None)
        
        row_str = []
        for model in models:
            value = row_values.get(model, "")
            if value == "":
                row_str.append(" ")
            elif value == best_value:
                row_str.append(f"**{value}**")
            else:
                row_str.append(str(value))
        
        md_table += f"| {task} | " + " | ".join(row_str) + " |\n"
    
    return md_table


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str, help="Path to the benchmark results folder")
    parser.add_argument("--tasks", type=str, default="aime,gpqa_diamond,math500,mmlu_pro,livecodebench,olympiadbench_math_en", 
                        help="Comma-separated list of tasks")
    args = parser.parse_args()
    
    task_list = args.tasks.split(',')
    models, accuracy_data, cost_data = compile_results(args.input_path, task_list)
    
    accuracy_table = format_markdown_table(models, accuracy_data, highlight_max=True)
    cost_table = format_markdown_table(models, cost_data, highlight_max=False)
    
    markdown_output = "# Benchmark Results\n\n## Accuracy Table\n\n" + accuracy_table + "\n\n## Cost Table\n\n" + cost_table + "\n"
    
    with open(os.path.join(args.input_path, "results.md"), "w") as f:
        f.write(markdown_output)
    
    print("Markdown results saved to results.md")


if __name__ == "__main__":
    main()
