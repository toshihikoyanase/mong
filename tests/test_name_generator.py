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
        for moby_dict in [None, self._moby_dicts]:
            with self.subTest(moby_dict=moby_dict):
                generator = mong.NameGenerator(moby_dict)

                name = generator.get_random_name()
                self.assertTrue('_' in name)
                self.assertTrue(self._re_number.search(name) is None)

                name = generator.get_random_name(0)
                self.assertTrue('_' in name)
                self.assertTrue(self._re_number.search(name) is None)

    def test_name_retries(self):
        for moby_dict in [None, self._moby_dicts]:
            with self.subTest(moby_dict=moby_dict):
                generator = mong.NameGenerator(moby_dict)

                name = generator.get_random_name(1)
                self.assertTrue('_' in name)
                self.assertTrue(self._re_number.search(name) is not None)

    def test_forbidden_name(self):
        with self.assertRaises(RecursionError):
            mong.NameGenerator({'left': ['boring'], 'right': ['wozniak']}).get_random_name()

        ng = mong.NameGenerator({'left': ['boring'], 'right': ['wozniak', 'tom']})
        for _ in range(4):
            self.assertEqual(ng.get_random_name(), 'boring_tom')


if __name__ == '__main__':
    unittest.main()
