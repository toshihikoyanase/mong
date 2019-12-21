import json
import re
from typing import Dict
from typing import List
import urllib.request


def download_go_code() -> str:
    url = \
        'https://raw.githubusercontent.com/moby/moby/master/pkg/namesgenerator/names-generator.go'

    with urllib.request.urlopen(url) as response:
       code = response.read()
    return code.decode('utf-8')


def read_go_code() -> str:
    with open('./names-generator.go') as fin:
        code = fin.read()
    return code


def extract_dict(code: str) -> Dict[str, List[str]]:
    is_left = False
    is_right = False

    left = []
    right = []

    re_name = re.compile('^"([a-z]+)",$')

    for line in map(lambda l: l.strip(), code.split('\n')):
        if line.startswith('left ='):
            is_left = True
            continue

        if line.startswith('right ='):
            is_right = True
            continue

        if is_left:
            if line.startswith('}'):
                is_left = False
                continue
            mobj = re_name.match(line)
            if mobj:
                left.append(mobj.group(1))

        if is_right:
            if line.startswith('}'):
                is_right = False
                continue
            mobj = re_name.match(line)
            if mobj:
                right.append(mobj.group(1))
    return {
        'left': left,
        'right': right
    }


if __name__ == '__main__':
    import pprint
    # go_code = read_go_code()
    go_code = download_go_code()
    moby_dict = extract_dict(go_code)
    pprint.pprint(moby_dict)
    path = 'mong/moby_dict.json'
    with open(path, 'w') as fout:
        json.dump(moby_dict, fout, indent=4)
    print('Save moby dict to {}.'.format(path))
