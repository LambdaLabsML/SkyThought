

### Quality Benchmark

| task_name            | deepseek8b  | deepseek8b_david_20250205   | skyt1_32b  | skyt1_32b_flash |
|:---------------------|:------------|:----------------------------|:-----------|:----------------|
| aime                 | 0.3         | 0.1667                      | **0.3333** |                 |
| gpqa_diamond         | 0.3737      | 0.298                       | **0.5152** |                 |
| math500              | 0.702       | 0.596                       | **0.87**   |                 |  
| livecodebench        |             |                             | 0.5225     |   **0.5382**    |
| mmlu_pro             |             |                             | **0.6587** |     0.6479      |
| olympiadbench_math_en|             |                             |            |     0.5727      |

### Cost (output tokens)

| task_name            | deepseek8b | deepseek8b_david_20250205   | skyt1_32b   | skyt1_32b_flash |
|:---------------------|:-----------|:----------------------------|:------------|:----------------|
| aime                 | 39118      | 87693                       | 53532       |                 |
| gpqa_diamond         | 35468      | 72838                       | 14317       |                 |
| math500              | 10590      | 31705                       | 12860       |                 |
| livecodebench        |            |                             | 38932       |     26532       |
| mmlu_pro             |            |                             | 9836        |     5588        |
| olympiadbench_math_en|            |                             |             |     13530       |
