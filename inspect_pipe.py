import pickle
from pathlib import Path
from pprint import pprint

path = Path('pipe.pkl')
print('pipe exists:', path.exists(), 'size:', path.stat().st_size if path.exists() else None)
with path.open('rb') as f:
    pipe = pickle.load(f)

print('pipe type:', type(pipe))
print('pipe repr:', pipe)
print('pipe steps:')
try:
    pprint(pipe.steps)
except Exception as e:
    print('steps error:', repr(e))

try:
    print('named_steps:', pipe.named_steps.keys())
except Exception as e:
    print('named_steps error:', repr(e))

try:
    for name, step in pipe.steps:
        print('step', name, type(step))
        if hasattr(step, 'get_feature_names_out'):
            print('feature_names_out sample:', step.get_feature_names_out(['a','b','c']))
        if hasattr(step, 'transformers_'):
            print('transformers_ keys:', [t[0] for t in step.transformers_])
        if hasattr(step, 'get_params'):
            print('params keys length', len(step.get_params()))
except Exception as e:
    print('inspect error:', repr(e))
