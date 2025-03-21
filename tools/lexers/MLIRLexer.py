from pygments.lexer import RegexLexer, bygroups
from pygments.token import (
    Name,
    Keyword,
    Number,
    Operator,
    Comment,
    Text,
    Punctuation,
    Literal,
)

comment_rule = (r'//.*?\n', Comment)
ssa_value_rule = (r'%[a-zA-Z0-9_][a-zA-Z0-9_$.]*', Name.Variable)
symbol_rule = (r'@[^(]*', Name.Function)
basic_block_rule = (r'\^[^(:\]]*', Name.Label)
operation_rule = (
    r'(=)( +)([a-z_]+)(\.)([a-z_\.]+)',
    bygroups(Operator, Text, Name.Namespace, Text, Keyword.Function),
)
non_assign_operation_rule = (
    r'([a-z_]+)(\.)([a-z_\.]+)',
    bygroups(Name.Namespace, Text, Keyword.Function),
)
builtin_type_rule = (
    r'(#)([a-z_]+)(\.)([a-z0-9_]+)',
    bygroups(Operator, Name.Namespace, Text, Keyword.Type),
)
type_rule = (
    r'(!)([a-z_]+)(\.)([a-z0-9_]+)',
    bygroups(Operator, Name.Namespace, Text, Keyword.Type),
)
abbrev_type_tule = (r'(!)([a-z0-9]+)', bygroups(Operator, Keyword.Type))
first_attribute_rule = (
    r'([{\[])([a-z_A-Z]+)( = +)([@a-z0-9">=]+)',
    bygroups(Text, Name.Attribute, Text, Name.Tag),
)
following_attribute_rule = (
    r'(, +)([a-z_]+)( = +)([a-z0-9">=@]+)',
    bygroups(Text, Name.Attribute, Text, Name.Tag),
)
abbrev_following_attribute_rule = (
    r'(, +)([a-z_]+)( = +)',
    bygroups(Text, Name.Attribute, Text),
)


class MLIRLexer(RegexLexer):
    name = 'MLIR'
    aliases = ['mlir']
    filenames = ['*.mlir']

    tokens = {
        'root': [
            comment_rule,
            ssa_value_rule,
            symbol_rule,
            basic_block_rule,
            operation_rule,
            non_assign_operation_rule,
            builtin_type_rule,
            type_rule,
            # float and integer types (e.g. f32, i64) potetially preceded by 'x' for shape dimeqnsions
            (r'(x)?([fi]([0-9]+))', bygroups(Text, Keyword.Type)),
            (r'false', Number),
            (r'true', Number),
            (r'(-?[0-9]+(?:\.[0-9]+)?)', Number),
            abbrev_type_tule,
            (r'(\n|\s)+', Text),
            first_attribute_rule,
            (r'(\[)([a-z]+)', bygroups(Text, Name.Variable)),
            following_attribute_rule,
            abbrev_following_attribute_rule,
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
            (
                r'(=)( +)([a-z_]+)(\.)([a-z_\.]+)',
                bygroups(Text, Text, Comment, Comment, Name.Function),
            ),
            (
                r'([a-z_]+)(\.)([a-z_\.]+)',
                bygroups(Comment, Comment, Name.Function),
            ),
            (r'([!#])([a-z_]+)(\.)([a-z_]+)', bygroups(Text, Comment, Comment, Text)),
            (r'(\n|\s)+', Text),
            (r'([a-zA-Z0-9"_\?])+', Text),
            (r'(-)', Text),
            (r'[=<>{}:\[\]()*.,!]|x\b', Text),
            (r'def', Text),
            (
                r'([{\[])([a-z_A-Z]+)( = +)([@a-z0-9">=]+)',
                bygroups(Text, Name.Attribute, Text, Name.Tag),
            ),
        ]
    }
