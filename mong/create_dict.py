import json
import re
from typing import Dict
from typing import List
import urllib.request

GO_URL = 'https://raw.githubusercontent.com/moby/moby/master/pkg/namesgenerator/names-generator.go'


def download_go_code(url: str) -> str:

    with urllib.request.urlopen(url) as response:
        code = response.read()
    return code.decode('utf-8')


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


def create_dict(url: str, filepath: str) -> None:

    go_code = download_go_code(url)
    moby_dict = extract_dict(go_code)
    with open(filepath, 'w') as fout:
        json.dump(moby_dict, fout, indent=4)


if __name__ == '__main__':
    create_dict(GO_URL, 'mong/moby_dict.json')
