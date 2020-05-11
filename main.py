import os
from src.py_sql import PySQL


if __name__ == '__main__':
    dir_name = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_name, 'tests', '2.py')
    py_sql = PySQL('py_sql', None)
    py_sql.process_file(file_path)
