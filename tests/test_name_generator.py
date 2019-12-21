import re
import unittest

import mong


class TestNameGenerator(unittest.TestCase):

    def setUp(self):
        self._re_number = re.compile(r'[0-9]+')
        self._moby_dicts = {
            'left': ['admiring', 'zen'],
            'right': ['albattani', 'allen']
        }

    def test_name_format(self):
        generator = mong.NameGenerator(self._moby_dicts)

        name = generator.get_random_name()
        assert '_' in name
        assert self._re_number.search(name) is None

        name = generator.get_random_name(0)
        assert '_' in name
        assert self._re_number.search(name) is None

    def test_name_retries(self):
        generator = mong.NameGenerator(self._moby_dicts)

        name = generator.get_random_name(1)
        assert '_' in name
        assert self._re_number.search(name) is not None

    def test_forbidden_name(self):
        with self.assertRaises(RecursionError):
            mong.NameGenerator({'left': ['boring'], 'right': ['wozniak']}).get_random_name()

        ng = mong.NameGenerator({'left': ['boring'], 'right': ['wozniak', 'tom']})
        for _ in range(4):
            assert ng.get_random_name() == 'boring_tom'

if __name__ == '__main__':
    unittest.main()
