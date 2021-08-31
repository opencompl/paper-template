from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

class MLIRLexer(RegexLexer):
    name = 'MLIR'
    aliases = ['mlir']
    filenames = ['*.mlir']

    tokens = {
        'root': [
            (r'//.*?\n', Comment),
            (r'%[^ ]*', Name.Variable),
            (r'@[^(]*', Name.Function),
            (r'\^[^(]*', Name.Label),
            (r'(=)( +)([a-z]+)(\.)([a-z]+)', bygroups(Operator, Text, Name.Namespace, Text, Keyword.Function)),
            (r'(!)([a-z]+)(\.)([a-z]+)', bygroups(Operator, Name.Namespace, Text, Keyword.Type)),
            (r'(\n|\s)+', Text),
            (r'[=<>{}:\[\]()*.,!]|x\b', Punctuation),
            (r'def', Keyword),
        ]
    }

# This Lexer is a hack that enables a custom style where only operation names
# are highlighted and comments as well as dialect names are printed in light
# gray.
class MLIRLexerOnlyOps(RegexLexer):
    name = 'MLIR'
    aliases = ['mlir']
    filenames = ['*.mlir']

    tokens = {
        'root': [
            (r'//.*?\n', Comment),
            (r'%[^ ]*', Text),
            (r'@[^(]*', Text),
            (r'\^[^(]*', Text),
            (r'(=)( +)([a-z]+)(\.)([a-z]+)', bygroups(Text, Text, Comment, Comment, Name.Function)),
            (r'(!)([a-z]+)(\.)([a-z]+)', bygroups(Text, Comment, Comment, Text)),
            (r'(\n|\s)+', Text),
            (r'[=<>{}:\[\]()*.,!]|x\b', Text),
            (r'def', Text),
        ]
    }
