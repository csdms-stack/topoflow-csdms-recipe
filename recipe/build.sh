#! /bin/bash

python setup.py install
bmi babelize ./.bmi/channels_diffusive_wave --prefix=$PREFIX
