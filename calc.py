base, space = 1 << 8, 1 << 5
modules = [
    (lambda _, __, ___: _(_, __, ___))(
        lambda _, __, ___:
            chr(___ % __) + _(_, __, ___ // __) if ___ else
            chr(space)[:-1],
        base,
        545200826904043625543027),
    (lambda _, __, ___: _(_, __, ___))(
        lambda _, __, ___:
            chr(___ % __) + _(_, __, ___ // __) if ___ else
            chr(space)[:-1],
        base,
        7567731),
]
subprocess, sys = map(__import__, modules)
_, __ = getattr, globals

expr = _(sys, 'argv')[1]
popen = _(subprocess, 'Popen')

args = ['python3', '-c', _('print({})', 'format')(expr)]
kwargs = {'stdout': _(subprocess, 'PIPE')}
result, ___ = _(popen(args, **kwargs), 'communicate')()
x = _(_(result, 'decode')('utf-8'), 'strip')()

try:
    _(__()['__builtins__'], 'float')(x)
except:
    _(sys, 'exit')(1)
else:
    _(__()['__builtins__'], 'print')(x)
