import json
import os
import random
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple


class NameGenerator(object):

    def __init__(self,
                 moby_dicts: Optional[Dict[str, List[str]]] = None) -> None:

        if moby_dicts is None:
            path = os.path.join(os.path.dirname(__file__), 'moby_dict.json')
            self._left, self._right = self._load_dict(path)
        else:
            self._left = moby_dicts['left']
            self._right = moby_dicts['right']

    def _load_dict(self, path: str) -> Tuple[List[str], List[str]]:

        with open(path) as fin:
            moby_dict = json.load(fin)
        return moby_dict['left'], moby_dict['right']

    def get_random_name(self, retry: int = 0) -> str:
        """
        Generate a random name.

        See `get_random_name` doc for further details.
        """

        name = '{}_{}'.format(random.choice(self._left), random.choice(self._right))

        # Steve Wozniak is not boring.
        if name == 'boring_wozniak':
            return self.get_random_name(retry)

        if retry > 0:
            name = '{}{}'.format(name, random.randint(0, 9))
        return name


_name_generator = NameGenerator()


def get_random_name(retry: int = 0) -> str:
    """
    Generate a random name.

    This function corresponds to GetRandomName() in moby's namegenerator in the following file:
    https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go.

    It returns a string which is formatted as "<left>_<right>".
    Please note that a random integer between 0 to 10 will be added to the end of the name if
    retry is specified.

    Args:
        retry:
            A flag to add a random integer at the end of the name. If ``retry`` > 0, the integer
            will be added. The default is 0.
    """

    return _name_generator.get_random_name(retry)
