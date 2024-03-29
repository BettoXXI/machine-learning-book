import unittest
import os
import subprocess
import sys


def run_py(path):

    py_dir = os.path.dirname(path)
    py_path = os.path.basename(path)
    orig_dir = os.getcwd()
    os.chdir(py_dir)

    args = ["python", py_path]
    subprocess.check_output(args)

    os.chdir(orig_dir)


class TestOptionalScripts(unittest.TestCase):

    def test_ch01(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch01/ch01.py'))

    def test_ch02(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch02/ch02.py'))

    def test_ch03(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch03/ch03.py'))

    def test_ch04(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch04/ch04.py'))

    def test_ch05(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch05/ch05.py'))

    def test_ch06(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch06/ch06.py'))

    def test_ch07(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch07/ch07.py'))

    def test_ch08(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))

        # run only on Py3, because of Py2 unicode handling
        if (sys.version_info >= (3, 0)):
            run_py(os.path.join(this_dir,
                                '../ch08/ch08.py'))

    def test_ch09(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))

        # run only on Py3, because of the Py3 specific pickle files
        if (sys.version_info >= (3, 0)):
            run_py(os.path.join(this_dir, '../ch09/ch09.py'))
        else:
            pass

    def test_ch10(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch10/ch10.py'))

    def test_ch11(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch11/ch11.py'))

    def test_ch12(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch12/ch12.py'))

    def test_ch13(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch13/ch13.py'))

    def test_ch14(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch14/ch14.py'))

    def test_ch15(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        run_py(os.path.join(this_dir,
                            '../ch15/ch15.py'))

    def test_ch16(self):
        this_dir = os.path.dirname(os.path.abspath(__file__))
        # run only on Py3, because of Py2 unicode handling
        if (sys.version_info >= (3, 0)):
            run_py(os.path.join(this_dir,
                                '../ch16/ch16.py'))


if __name__ == '__main__':
    unittest.main()
