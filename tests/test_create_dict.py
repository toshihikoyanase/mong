import json
import os
import shutil
import tempfile
import unittest

import mong.create_dict


class TestCreateDict(unittest.TestCase):

    def setUp(self) -> None:

        self.tmp_dir = tempfile.mkdtemp()
        self.go_file = os.path.join(self.tmp_dir, 'namesgenerator.go')
        self.go_url = 'file://{}'.format(self.go_file)
        self.go_code = """
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

        with open(self.go_file, 'w') as fout:
            print(self.go_code, file=fout)

    def test_download_go_code(self) -> None:

        code = mong.create_dict.download_go_code(self.go_url)

        self.assertTrue('left =' in code)
        self.assertTrue('right =' in code)

    def test_extract_dict(self) -> None:

        moby_dict = mong.create_dict.extract_dict(self.go_code)

        self.assertTrue('left' in moby_dict)
        self.assertTrue('right' in moby_dict)
        self.assertEqual(moby_dict['left'], ['admiring', 'zen'])
        self.assertEqual(moby_dict['right'], ['albattani', 'allen'])

    def test_create_dict(self) -> None:

        tmp_file = os.path.join(self.tmp_dir, 'tmp_dict.json')
        mong.create_dict.create_dict(self.go_url, tmp_file)

        with open(tmp_file) as fin:
            moby_dict = json.load(fin)

        self.assertTrue('left' in moby_dict)
        self.assertTrue('right' in moby_dict)

    def tearDown(self) -> None:

        shutil.rmtree(self.tmp_dir)
