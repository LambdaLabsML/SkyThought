# Benchmark Results

## Accuracy Table

| Task | deepseek8b | deepseek8b_chuan_20250212 | deepseek8b_chuan_20250212_im_end | deepseek8b_david_20250205 | sky_32b | sky_32b_flash | unsloth_4bit_lora | unsloth_4bit_lora_run1 | unsloth_r1-8b-bf16 |
|---|---|---|---|---|---|---|---|---|---|
| aime | 0.3 | 0.0667 | 0.0333 | 0.1667 | **0.3333** |   | 0.1333 | 0.1333 | 0.2333 |
| gpqa_diamond | 0.3737 | 0.3182 | 0.2778 | 0.298 | **0.5152** |   | 0.3081 | 0.3081 | 0.399 |
| livecodebench | 0.3875 |   |   |   | 0.5225 | **0.5382** |   |   |   |
| math500 | 0.702 | 0.438 | 0.496 | 0.596 | **0.87** |   | 0.658 | 0.658 | 0.69 |
| mmlu_pro | 0.4132 |   |   |   | **0.6587** | 0.6479 |   |   |   |
| olympiadbench_math_en |   |   |   |   | **0.5801** | 0.5727 |   |   |   |


## Cost Table

| Task | deepseek8b | deepseek8b_chuan_20250212 | deepseek8b_chuan_20250212_im_end | deepseek8b_david_20250205 | sky_32b | sky_32b_flash | unsloth_4bit_lora | unsloth_4bit_lora_run1 | unsloth_r1-8b-bf16 |
|---|---|---|---|---|---|---|---|---|---|
| aime | **39118.033** | 83409.8 | 77116.433 | 87693.667 | 53532.767 |   | 75092.5 | 75092.5 | 52685.767 |
| gpqa_diamond | 35468.283 | 47914.045 | 65199.01 | 72838.823 | **14317.02** |   | 50996.773 | 50996.773 | 35573.773 |
| livecodebench | 55943.978 |   |   |   | 38932.546 | **26532.0** |   |   |   |
| math500 | 10590.028 | 25343.774 | 39946.042 | 31705.106 | 12860.152 |   | 14468.874 | 14468.874 | **9385.058** |
| mmlu_pro | 18926.791 |   |   |   | 9836.03 | **5588.128** |   |   |   |
| olympiadbench_math_en |   |   |   |   | 27423.914 | **13530.951** |   |   |   |

