
# Usage

```
virtualenv venv -p /usr/bin/python venv-skythought
source venv-skythought/bin/activate

git clone https://github.com/LambdaLabsML/SkyThought.git
cd SkyThought
git checkout lambda
pip install -e .

# see run_bash.sh for more details
# e.g. ./run_bash.sh deepseek8b 8
./run_bash.sh $model $tp 

# compile results
# markdown table will be saved to ./results/results.md
python compile_results.py ./results
```