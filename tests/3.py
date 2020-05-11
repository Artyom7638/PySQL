"""advanced into grammar test"""
import sqlite3
from src.py_sql import PySQL

connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
"""sql into_py a[3 + 2], b[a + "b"]"""
"""sql into_py a[3 + func(None, a == b) + i]"""
