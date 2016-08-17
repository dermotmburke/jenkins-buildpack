#!/usr/bin/env python

import yaml

with open("../plugins/data.yaml", 'r') as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)
