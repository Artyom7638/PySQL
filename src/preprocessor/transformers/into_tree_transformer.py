from collections import namedtuple

from lark import v_args
from src.preprocessor.transformers.base_transformer import BaseTransformer

Node = namedtuple('Node', 'type value')


class IntoTreeTransformer(BaseTransformer):

    def start(self, nodes):
        result = {'identifiers': [], 'bulk': False, 'rest_of_the_query': ''}
        for node in nodes:
            if node.type == 'identifier':
                result['identifiers'].append(node.value)
            elif node.type == 'bulk':
                result['bulk'] = True
            elif node.type == 'rest_of_the_query':
                result['rest_of_the_query'] = node.value
        return result

    def high_level_identifier(self, items):
        return Node(type='identifier', value=''.join(items))

    @v_args(inline=True)
    def BULK(self, bulk):
        if bulk:
            return Node(type='bulk', value=True)
        return Node(type='bulk', value=False)

    @v_args(inline=True)
    def eof(self, eof):
        return self.rest_of_the_query(eof)

    @v_args(inline=True)
    def eof_one_var(self, eof):
        return self.rest_of_the_query(eof)

    def rest_of_the_query(self, rest):
        return Node(type='rest_of_the_query', value=str(rest))
