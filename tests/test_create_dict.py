import unittest

import mong.create_dict


class TestCreateDict(unittest.TestCase):

    def test_download_go_code(self):

        code = mong.create_dict.download_go_code()

        self.assertTrue('left =' in code)
        self.assertTrue('right =' in code)

    def test_extract_dict(self):

        code = """
var (
	left = [...]string{
		"admiring",
		"zen",
	}
	right = [...]string{
		// Muhammad ibn Jābir al-Ḥarrānī al-Battānī
		"albattani",

		// Frances E. Allen
		"allen",
	}
)
        """

        moby_dict = mong.create_dict.extract_dict(code)

        self.assertTrue('left' in moby_dict)
        self.assertTrue('right' in moby_dict)
        self.assertEqual(moby_dict['left'], ['admiring', 'zen'])
        self.assertEqual(moby_dict['right'], ['albattani', 'allen'])
