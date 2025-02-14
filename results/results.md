# Benchmark Results

## Accuracy Table

| Task | deepseek8b | deepseek8b_bf16_lora64 | deepseek8b_bf16_lora64_eos | deepseek8b_bf16_lora8 | deepseek8b_chuan_20250212 | deepseek8b_chuan_20250212_im_end | deepseek8b_david_20250205 | sky_32b | sky_32b_flash | unsloth_4bit_lora64 | unsloth_r1-8b-bf16_lora64 | unsloth_r1-8b-bf16_lora8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| aime | 0.3 | 0.0333 | 0.0333 | 0.2333 | 0.0667 | 0.0333 | 0.1667 | **0.3333** |   | 0.1333 | 0.0667 | 0.2333 |
| gpqa_diamond | 0.3737 |   | 0.3838 | 0.3687 | 0.3182 | 0.2778 | 0.298 | **0.5152** |   | 0.3081 | 0.3737 | 0.399 |
| livecodebench |   |   |   |   |   |   |   | 0.5225 | **0.5382** |   |   |   |
| math500 | 0.702 |   | 0.49 | 0.754 | 0.438 | 0.496 | 0.596 | **0.87** |   | 0.658 | 0.58 | 0.69 |
| mmlu_pro |   |   |   |   |   |   |   | **0.6587** | 0.6479 |   |   |   |
| olympiadbench_math_en |   |   |   |   |   |   |   | **0.5801** | 0.5727 |   |   |   |


## Cost Table

| Task | deepseek8b | deepseek8b_bf16_lora64 | deepseek8b_bf16_lora64_eos | deepseek8b_bf16_lora8 | deepseek8b_chuan_20250212 | deepseek8b_chuan_20250212_im_end | deepseek8b_david_20250205 | sky_32b | sky_32b_flash | unsloth_4bit_lora64 | unsloth_r1-8b-bf16_lora64 | unsloth_r1-8b-bf16_lora8 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| aime | **39118.033** | 77963.633 | 69876.733 | 54102.967 | 83409.8 | 77116.433 | 87693.667 | 53532.767 |   | 75092.5 | 78412.2 | 52685.767 |
| gpqa_diamond | 35468.283 |   | 38852.823 | 41495.273 | 47914.045 | 65199.01 | 72838.823 | **14317.02** |   | 50996.773 | 44829.253 | 35573.773 |
| livecodebench |   |   |   |   |   |   |   | 38932.546 | **26532.0** |   |   |   |
| math500 | 10590.028 |   | 22187.364 | 19471.62 | 25343.774 | 39946.042 | 31705.106 | 12860.152 |   | 14468.874 | 27629.932 | **9385.058** |
| mmlu_pro |   |   |   |   |   |   |   | 9836.03 | **5588.128** |   |   |   |
| olympiadbench_math_en |   |   |   |   |   |   |   | 27423.914 | **13530.951** |   |   |   |

