from pygments.lexer import RegexLexer, bygroups
from pygments.token import Name, Keyword, Operator, Comment, Text, Punctuation, Literal

comment_rule = (r'//.*?\n', Comment)
ssa_value_rule = (r'%[^[ )]*]*', Name.Variable)
symbol_rule = (r'@[^(]*', Name.Function)
basic_block_rule = (r'\^[^(:\]]*', Name.Label)
operation_rule = (r'(=)( +)([a-z_]+)(\.)([a-z_]+)',
                  bygroups(Operator, Text, Name.Namespace, Text,
                           Keyword.Function))
non_assign_operation_rule = (r'([a-z_]+)(\.)([a-z_]+)',
                             bygroups(Name.Namespace, Text, Keyword.Function))
type_rule = (r'(!)([a-z_]+)(\.)([a-z0-9_]+)',
             bygroups(Operator, Name.Namespace, Text, Keyword.Type))
abbrev_type_tule = (r'(!)([a-z0-9]+)', bygroups(Operator, Keyword.Type))
first_attribute_rule = (r'([{\[])([a-z_A-Z]+)( = +)([@a-z0-9">=]+)',
                        bygroups(Text, Name.Attribute, Text, Name.Tag))
following_attribute_rule = (r'(, +)([a-z_]+)( = +)([a-z0-9">=@]+)',
                            bygroups(Text, Name.Attribute, Text, Name.Tag))
abbrev_following_attribute_rule = (r'(, +)([a-z_]+)( = +)',
                                   bygroups(Text, Name.Attribute, Text))


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
            type_rule,
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
            (r'(=)( +)([a-z]+)(\.)([a-z]+)',
             bygroups(Text, Text, Comment, Comment, Name.Function)),
            (r'(!)([a-z]+)(\.)([a-z]+)', bygroups(Text, Comment, Comment,
                                                  Text)),
            (r'(\n|\s)+', Text),
            (r'[=<>{}:\[\]()*.,!]|x\b', Text),
            (r'def', Text),
        ]
    }
