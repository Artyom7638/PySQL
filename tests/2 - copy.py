"""
тест использования переменных, потом просто запросов, потом переменных и into одновременно, потом логические операции и сравнения
"""
import sqlite3
from src.py_sql import PySQL


connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
py_sql.execute(""" INSERT INTO users (name, surname) VALUES(?, ?)""", variables_list=[name, 54])
py_sql.execute(""" INSERT INTO users (name) VALUES(?, ?);""", variables_list=[gfd + function(g444, f32, *args, e=3, d=5, **kwargs) + -44, test.test[4].test(2 + 3 / 3 - 2 * 2)])
py_sql.execute(""" UPDATE users SET name=?, surname = 'Doe' WHERE id=?;""", variables_list=[new_name, i])
py_sql.execute(""" UPDATE users SET name='John', surname = 'Doe' WHERE id=1;""")
res, res2 = py_sql.execute_select(""" SELECT *  WHERE id <= ? from users""", var_count=2, bulk=False, variables_list=[2])
py_sql.execute(""" INSERT INTO users (name, surname) VALUES(?, ?)""", variables_list=[test['ind'], test[i]])
py_sql.execute(""" INSERT INTO users (name, surname) VALUES(?, ?, ?, ?)""", variables_list=['test', 'test' + 'test', test + test, 'test' + i + 'test'])
py_sql.execute(""" VALUES(?, ?, ?)""", variables_list=[True, func(False, None), not a or b and not c])
py_sql.execute(""" VALUES(?, ?)""", variables_list=[a == b, a < b >= c])
py_sql.execute(""" VALUES(?, ?)""", variables_list=[a[3 + 2], b['a' + 'b']])
py_sql.execute(""" VALUES(?)""", variables_list=[a[3 + func(None, a == b) + b]])
