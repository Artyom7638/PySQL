"""
тест использования переменных, потом просто запросов, потом переменных и into одновременно, потом логические операции и сравнения
"""
import sqlite3
from src.py_sql import PySQL


connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
"""sql INSERT INTO users (name, surname) VALUES($ name, $54)"""
"""sql INSERT INTO users (name) VALUES($ gfd + function(g444, f32, *args, e=3, d=5, **kwargs) + -44, $test.test[4].test(2 + 3 / 3 - 2 * 2));"""
"""sql UPDATE users SET name=$new_name, surname = 'Doe' WHERE id=$i;"""
"""sql UPDATE users SET name='John', surname = 'Doe' WHERE id=1;"""
"""sql SELECT * into_py res, res2 WHERE id <= $2 from users"""
"""sql INSERT INTO users (name, surname) VALUES($ test['ind'], $test[i])"""
"""sql INSERT INTO users (name, surname) VALUES($ 'test', $ 'test' + 'test', $ test + test, $ 'test' + i + 'test')"""
"""sql VALUES($ True, $ func(False, None), $not a or b and not c)"""
"""sql VALUES($ a == b, $ a < b >= c)"""
"""sql VALUES($ a[3 + 2], $ b['a' + 'b'])"""
"""sql VALUES($ a[3 + func(None, a == b) + b])"""
