#! /usr/bin/env python
import os

os.mkdir('_testing')
os.chdir('_testing')

import pymt.components

components = pymt.components.__all__
print('found {num} components'.format(num=len(components)))

for cls in components:
    print('instantiate: {name}'.format(name=cls.__name__))
    model = cls()

    for default in model.defaults:
        print('{name}: {val} {units}'.format(
            name=default[0], val=default[1][0], units=default[1][1]))
