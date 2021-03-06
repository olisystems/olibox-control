
import json
import os

snap_userdata = os.environ['SNAP_USER_DATA']


def write_values(file, new_data):
    """
    The function uses json.dump method to write the data object to a file.
    """

    file_to_write = os.path.join(f'{snap_userdata}/{file}')

    if os.path.isfile(file_to_write) and os.stat(file_to_write).st_size !=0:
        with open(file_to_write) as f:
            data = json.load(f)
            # get existing data keys
            keys = data.keys()
            for k in keys:
                # update keys only if they exists in new data
                if k in new_data.keys():
                    data[k].update(new_data[k])

            with open(file_to_write, 'w+', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
    else:
        with open(file_to_write, 'w+', encoding='utf-8') as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
