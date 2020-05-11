"""
тест всех случаев для into - несколько переменных, bulk как в конце строки, так и в середине (то есть дальше ещё что-то)
"""
import sqlite3
from src.py_sql import PySQL


connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
res, res2, a[5].fdfd.fds[4][5].ffff = py_sql.execute_select(""" select *  from users""", var_count=3, bulk=False)
res = py_sql.execute_select(""" select * from users """, var_count=1, bulk=True)
res = py_sql.execute_select(""" select *  from users""", var_count=1, bulk=True)
if 1:
    if 2:
        res, b[1] = py_sql.execute_select(""" select * from users """, var_count=2, bulk=False)
res = py_sql.execute_select(""" select *
from users
""", var_count=1, bulk=False)
test['ind'], test["ind2"], test['''ind3'''], test["""ind4"""] = py_sql.execute_select(""" select * from users """, var_count=4, bulk=False)
test[i], test[t.t[i].t] = py_sql.execute_select(""" select * from users """, var_count=2, bulk=False)
