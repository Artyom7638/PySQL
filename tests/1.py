"""
тест всех случаев для into - несколько переменных, bulk как в конце строки, так и в середине (то есть дальше ещё что-то)
"""
import sqlite3
from src.py_sql import PySQL


connection = sqlite3.connect('database.db')
py_sql = PySQL('py_sql', connection)
"""sql select * into_py res, res2, a[5].fdfd.fds[4][5].ffff from users"""
"""sql select * from users into_py res bulk"""
"""sql select * into_py res bulk from users"""
if 1:
    if 2:
        """sql select * from users into_py res, b[1]"""
"""sql select *
from users
into_py
res"""
"""sql select * from users into_py test['ind'], test["ind2"], test['''ind3'''], test[""\"ind4\"\"\"]"""
"""sql select * from users into_py test[i], test[t.t[i].t]"""
