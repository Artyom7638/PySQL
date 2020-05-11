import contextlib
from enum import Enum

from src import io_utils


class SupportedDBMS(Enum):
    sqlite = 'SQLITE'


class PySQL:

    @property
    def var_name(self):
        return self._var_name

    @var_name.setter
    def var_name(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Invalid PySQL variable name")
        self._var_name = value

    @property
    def dbms(self):
        return self._dbms

    @dbms.setter
    def dbms(self, value):
        if value not in SupportedDBMS:
            raise ValueError("DBMS not supported")
        self._dbms = value

    def __init__(self, var_name, connection, dbms=SupportedDBMS.sqlite):
        self.var_name = var_name  # название переменной-экземпляра данного класса, нужно для вызова функций экземпляра
        self.connection = connection  # подключение к БД, через которое будет идти запрос
        self.dbms = dbms  # СУБД, по идее ни на что не влияет, но в теории что-то может отличаться

    def process_file(self, file_path):
        io_utils.process_file(file_path, self.var_name, self.dbms)

    def _execute(self, query, variables_list):
        if variables_list:
            return self.connection.execute(query, tuple(variables_list))
        else:
            return self.connection.execute(query)

    def execute_select(self, query, var_count, bulk, variables_list=None):
        cursor = self._execute(query, variables_list)
        with contextlib.closing(cursor):
            if bulk:
                return cursor.fetchall()
            values = cursor.fetchmany(var_count + 1)
            if len(values) < var_count:
                raise ValueError("Too few values. Expected " + str(var_count) + ", got " + str(len(values))
                                 + '. The misbehaving query was ' + query + '".')
            elif len(values) > var_count:
                remaining_values = cursor.fetchall()  # учитывая, что будет Exception, производительность не очень важна
                raise ValueError("Too many values. Expected " + str(var_count) + ", got "
                                 + str(len(values) + len(remaining_values))
                                 + '. The misbehaving query was ' + query + '".')
            return values

    def execute(self, query, variables_list=None):
        cursor = self._execute(query, variables_list)
        cursor.close()
