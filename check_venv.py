import sys
import pathlib
import pickle
import importlib
print('python:', sys.executable)
print('sys.prefix:', sys.prefix)
try:
    import sklearn
    print('sklearn version:', sklearn.__version__)
    from sklearn.compose import _column_transformer as ct
    print('_RemainderColsList present:', hasattr(ct, '_RemainderColsList'))
    print('composer attrs:', [a for a in dir(ct) if 'Remainder' in a])
except Exception as e:
    print('sklearn inspect exception:', repr(e))
path = pathlib.Path('pipe.pkl')
print('pipe exists:', path.exists(), 'size:', path.stat().st_size if path.exists() else None)
try:
    loader = pickle.load(open(path, 'rb'))
    print('pipe loaded type:', type(loader))
except Exception as e:
    print('pickle load exception:', repr(e))
