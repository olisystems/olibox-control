
import os
import json

import toml


def get_locals():
    config = 'config.toml'

    try:
        with open(config) as file:

            f = toml.load(file)
            items = f.keys()
            unique_dict = {}

            for item in items:
                if type(f[item]) is not str:
                    for i in f[item].keys():
                        unique_dict[i] = f[item][i]
                else:
                    unique_dict[item] = f[item]

            locals().update(unique_dict)

            return locals()

    except Exception as e:
        print(e)
