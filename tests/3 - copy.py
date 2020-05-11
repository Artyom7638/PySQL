"""advanced into grammar test"""
import sqlite3
from src.py_sql import PySQL

connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
a[3 + 2], b[a + "b"] = py_sql.execute_select(""" """, var_count=2, bulk=False)
a[3 + func(None, a == b) + i] = py_sql.execute_select(""" """, var_count=1, bulk=False)
