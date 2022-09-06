from pygments.lexer import RegexLexer, bygroups
from pygments.token import *


class MLIRLexer(RegexLexer):
    name = 'MLIR'
    aliases = ['mlir']
    filenames = ['*.mlir']

    tokens = {
        'root': [
            (r'//.*?\n', Comment),
            (r'%[^[ )]*]*', Name.Variable),
            (r'@[^(]*', Name.Function),
            (r'\^[^(:\]]*', Name.Label),
            (r'(=)( +)([a-z_]+)(\.)([a-z_]+)',
             bygroups(Operator, Text, Name.Namespace, Text, Keyword.Function)),
            (r'([a-z_]+)(\.)([a-z_]+)',
             bygroups(Name.Namespace, Text, Keyword.Function)),
            (r'(!)([a-z_]+)(\.)([a-z0-9_]+)',
             bygroups(Operator, Name.Namespace, Text, Keyword.Type)),
            (r'(!)([a-z0-9]+)', bygroups(Operator, Keyword.Type)),
            (r'(\n|\s)+', Text),
            (r'([{\[])([a-z_]+)( = +)([a-z0-9">=]+)',
             bygroups(Text, Name.Attribute, Text, Name.Tag)),
            (r'(\[)([a-z]+)', bygroups(Text, Name.Variable)),
            (r'(, +)([a-z_]+)( = +)([a-z0-9">=]+)',
             bygroups(Text, Name.Attribute, Text, Name.Tag)),
            (r'(, +)([a-z_]+)( = +)', bygroups(Text, Name.Attribute, Text)),
            (r'[=<>{}:\[\]()*.,!]|x\b', Punctuation),
            (r'(...)', Text),
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
            (r'(=)( +)([a-z]+)(\.)([a-z]+)',
             bygroups(Text, Text, Comment, Comment, Name.Function)),
            (r'(!)([a-z]+)(\.)([a-z]+)', bygroups(Text, Comment, Comment,
                                                  Text)),
            (r'(\n|\s)+', Text),
            (r'[=<>{}:\[\]()*.,!]|x\b', Text),
            (r'def', Text),
        ]
    }
