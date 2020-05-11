from lark import v_args
from src.preprocessor.transformers.base_transformer import BaseTransformer


class VariablesTreeTransformer(BaseTransformer):

    def start(self, items):
        expr = items[0]
        eof = items[1] if len(items) > 1 else ''
        return str(expr), str(eof)

    @v_args(inline=True)
    def eof(self, rest_of_the_query):
        return str(rest_of_the_query)
