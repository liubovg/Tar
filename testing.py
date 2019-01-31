import unittest
from tar import create_directory_db, get_records_for_table
import os


class Testing(unittest.TestCase):
    def test_create_dir(self):
        create_directory_db(os.getcwd()+'\db_test')
        result = os.path.exists(os.getcwd()+'\db_test')
        expected = True
        self.assertEqual(expected, result)
        os.rmdir(os.getcwd()+'\db_test')

    def test_get_records(self):
        result = get_records_for_table("test.csv")
        expected = [('test.csv', 'q;w;e;r;t'), ('test.csv', 'g;f;d;s;a'), ('test.csv', 'z;x;c;v;b')]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
