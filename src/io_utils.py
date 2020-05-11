import ast
import os
import tokenize
from collections import namedtuple
from src.preprocessor import preprocessor

Query = namedtuple('Query', 'query_string start end indent')


def process_file(file_path, py_sql_var_name, dbms, print_result, save_as_copy=True):
    queries = find_sql_queries(file_path)
    with open(file_path, 'r') as r:
        lines = r.readlines()
    filename = generate_processed_file_name(file_path, ' - copy')
    with open(filename, 'w') as w:
        i = 0
        for query in queries:
            while i < query.start - 1:  # т.к. номера строк начинаются с единицы
                i = write_line(w, lines, i)
            processed_query = preprocessor.process_query(query.query_string, py_sql_var_name, dbms, print_result)
            w.write(query.indent + processed_query + '\n')
            i = query.end
        while i < len(lines):
            i = write_line(w, lines, i)


def find_sql_queries(file_path):
    with tokenize.open(file_path) as f:
        tokens = tokenize.generate_tokens(f.readline)
        tokens = list(tokens)
    query_tokens = get_query_tokens(tokens)
    queries = []
    for token, query_string, indent in query_tokens:
        preprocessor.check_syntax(token.line, query_string)
        # query_string = normalize_string(query_string)
        queries.append(Query(query_string, token.start[0], token.end[0], indent))
    return queries


def get_query_tokens(tokens):
    query_tokens = []
    for i, token in enumerate(tokens):
        if token.type != tokenize.STRING:
            continue
        string = ast.literal_eval(token.string)  # получить саму строку, без различий между ' и "
        string = normalize_string_beginning(string)
        if not preprocessor.is_sql_query(string):  # не sql запрос
            continue
        indent = find_indent(token, i, tokens)
        query_tokens.append((token, string, indent))
    return query_tokens


def normalize_string_beginning(query_string):
    """ убрать \n и пробелы в начале строки для проверки, что это не просто строка, а есть sql в начале строки """
    i = 0
    while query_string[i] == ' ' or query_string[i] == '\n':
        i += 1
    if i != 0:
        query_string = query_string[i:]
    return query_string


def find_indent(query_token, i, tokens):
    string_line = query_token.start[0]
    indent = ''
    while i > 0:
        possible_indent_token = tokens[i - 1]
        if possible_indent_token.start[0] != string_line:  # просмотрены все токены этой строки
            break
        if possible_indent_token.type == tokenize.INDENT:
            indent = possible_indent_token.string
            break
        i -= 1
    return indent


'''
def normalize_string(string):
    return string.replace('\n', ' ')
'''


def generate_processed_file_name(path, postfix):
    filename = os.path.basename(path)
    split = filename.rsplit('.', 1)
    name = split[0]
    extension = split[1]
    return os.path.join(os.path.dirname(path), name + postfix + '.' + extension)


def write_line(file, lines, index):
    file.write(lines[index])
    return index + 1
