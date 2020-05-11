import os
import re
import sys
import warnings

from lark import Lark
from src.preprocessor.transformers.into_tree_transformer import IntoTreeTransformer
from src.preprocessor.transformers.variables_tree_transformer import VariablesTreeTransformer

into_regex = re.compile(r'(\$\s*into)|(into_py)', re.IGNORECASE)
# variables_regex = re.compile(r'\$\s*\b(?!into)\b', re.IGNORECASE)
# variables_regex = re.compile(r'\$\s*((?!into).)*', re.IGNORECASE)
variables_regex = re.compile(r'\$\s*(?!into)', re.IGNORECASE)
grammars_folder = os.path.join(sys.path[0], 'grammars')
into_grammar_path = os.path.join(grammars_folder, 'into_grammar.lark')
into_parser = Lark.open(into_grammar_path)
variables_grammar_path = os.path.join(grammars_folder, 'variables_grammar.lark')
variables_parser = Lark.open(variables_grammar_path)


def is_sql_query(string):
    if string.lower().startswith('sql'):
        return True
    return False


def check_syntax(line, query_string):
    """
    отсутствие, например, присваивания строки переменной, иначе после препроцессинга получится некорректный синтаксис
    """
    line = line.replace('\\', '')  # иначе следующая строчка не сработает если использовался \ в строке
    result = line.replace(query_string, '')
    allowed_chars = [' ', '\n', "'", '"']
    for char in result:
        if char not in allowed_chars:
            raise SyntaxError("Lines that contain an SQL query should only contain the query itself. "
                              "Comments, assignments etc. are not supported.")


def process_query(query, py_sql_var_name, dbms, print_result):
    query = query[3:]  # убирает слово sql в начале строки
    query, into_parse_dict = parse_intos(query, print_result)
    query, expressions = parse_variables(query, print_result)
    resulting_line = ''
    if into_parse_dict:  # есть into_py/$into
        resulting_line += generate_identifiers_string(into_parse_dict['identifiers'])
    resulting_line += py_sql_var_name + '.'
    resulting_line += 'execute_select' if into_parse_dict else 'execute'
    resulting_line += '("""' + query + '"""'
    if into_parse_dict:  # есть into_py/$into
        bulk = into_parse_dict['bulk']
        identifiers = into_parse_dict['identifiers']
        resulting_line += ', var_count=' + str(len(identifiers)) + ', bulk=' + str(bulk)
    if expressions:  # использовались какие-либо переменные
        resulting_line += ', variables_list=['
        resulting_line += expressions[0]
        i = 1
        while i < len(expressions):
            expression = expressions[i]
            i += 1
            resulting_line += ', ' + expression
        resulting_line += ']'
    resulting_line += ')'
    return resulting_line


def parse_intos(query, print_result):
    into_matches = into_regex.finditer(query)
    intos = list(into_matches)
    if len(intos) > 1:
        raise SyntaxError('PySQL\'s "into" keyword cannot appear twice in one query')
    if len(intos) < 1:
        return query, None
    start = intos[0].start()
    query_beginning = query[:start]
    string_for_parsing = query[start:]
    try:
        tree = into_parser.parse(string_for_parsing)
        parse_dict = IntoTreeTransformer(visit_tokens=True).transform(tree)
        if print_result:
            print(query, '\n', tree.pretty(), '\n', parse_dict, '\n\n')
    except Exception as e:
        '''print(e)
        return "there was an exception while parsing this query", None'''
        raise e
    if parse_dict['bulk'] and len(parse_dict['identifiers']) != 1:
        raise SyntaxError("When using PySQL's \"bulk\" keyword, query's result can be stored in one variable only")
    resulting_query = query_beginning + parse_dict['rest_of_the_query']
    return resulting_query, parse_dict


def parse_variables(query, print_result):
    expressions = []
    while True:
        variable = variables_regex.search(query)
        if not variable:
            break
        query, expression = parse_variable(query, variable, print_result)
        expressions.append(expression)
    return query, expressions


def parse_variable(query, variable, print_result):
    start = variable.start()
    final_query = query[:start]
    string_for_parsing = query[start:]
    tree = variables_parser.parse(string_for_parsing)
    expression, eof = VariablesTreeTransformer(visit_tokens=True).transform(tree)
    final_query += '?' + eof
    if print_result:
        print(query, '\n', tree.pretty(), '\n', expression, '\n\n')
    return final_query, expression


def generate_identifiers_string(identifiers):
    resulting_line = identifiers[0]
    used_identifiers = {identifiers[0]}
    i = 1
    while i < len(identifiers):
        identifier = identifiers[i]
        i += 1
        resulting_line += ', ' + identifier
        if identifier in used_identifiers:
            warnings.warn('Variable "' + identifier + '" reassigned without usage', RuntimeWarning)
        used_identifiers.add(identifier)
    return resulting_line + ' = '
