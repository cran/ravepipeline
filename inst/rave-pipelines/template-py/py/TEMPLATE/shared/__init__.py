# Automatically import all the modules from this folder.
# Feel free to modify the script, but be aware of that behavior might change
# on how main.Rmd calls the shared python functions

import os

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
    # filter and use python files only
    if module.lower() == '__init__.py' or module.lower()[-3:] != '.py':
        continue
    if not os.path.isfile(os.path.join(os.path.dirname(__file__), module)):
        continue
    __all__.append(module[:-3])
del module

