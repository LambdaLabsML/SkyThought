# Benchmark Results

## Accuracy Table

| Task | deepseek8b | deepseek8b_chuan_20250212 | deepseek8b_david_20250205 | deepseek8b_unsloth | sky_32b | sky_32b_flash |
|---|---|---|---|---|---|---|
| aime | 0.3 | 0.0667 | 0.1667 |   | **0.3333** |   |
| gpqa_diamond | 0.3737 | 0.3182 | 0.298 |   | **0.5152** |   |
| livecodebench | 0.3875 |   |   |   | 0.5225 | **0.5382** |
| math500 | 0.702 | 0.438 | 0.596 |   | **0.87** |   |
| mmlu_pro | 0.4132 |   |   |   | **0.6587** | 0.6479 |
| olympiadbench_math_en |   |   |   |   | **0.5801** | 0.5727 |


## Cost Table

| Task | deepseek8b | deepseek8b_chuan_20250212 | deepseek8b_david_20250205 | deepseek8b_unsloth | sky_32b | sky_32b_flash |
|---|---|---|---|---|---|---|
| aime | **39118.033** | 83409.8 | 87693.667 |   | 53532.767 |   |
| gpqa_diamond | 35468.283 | 47914.045 | 72838.823 |   | **14317.02** |   |
| livecodebench | 55943.978 |   |   |   | 38932.546 | **26532.0** |
| math500 | **10590.028** | 25343.774 | 31705.106 |   | 12860.152 |   |
| mmlu_pro | 18926.791 |   |   |   | 9836.03 | **5588.128** |
| olympiadbench_math_en |   |   |   |   | 27423.914 | **13530.951** |

