
import os

import toml

snap_userdata = os.environ['SNAP_USER_DATA']


def get_locals():
    if os.path.isfile(snap_userdata + '/config.toml'):

        f = toml.load(snap_userdata + '/config.toml')
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

    else:
        print('file not found')
