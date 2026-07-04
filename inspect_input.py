import pickle
from pathlib import Path
path = Path('pipe.pkl')
with path.open('rb') as f:
    pipe = pickle.load(f)
print('pipeline type:', type(pipe))
print('steps:', pipe.steps)
step1 = pipe.named_steps['step1']
print('step1 type:', type(step1))
print('feature_names_in_ exists:', hasattr(step1, 'feature_names_in_'))
if hasattr(step1, 'feature_names_in_'):
    print('feature_names_in_:', step1.feature_names_in_)
else:
    print('no feature_names_in_')
print('transformers_:', step1.transformers_)
print('remainder:', step1.remainder)
try:
    print('remainder_:', step1.remainder_)
except Exception as e:
    print('remainder_ error', e)
print('transformers:', [t[2] for t in step1.transformers_])
print('transformers names:', [t[0] for t in step1.transformers_])
print('transformer types:', [type(t[1]) for t in step1.transformers_])
print('named_steps keys:', pipe.named_steps.keys())
