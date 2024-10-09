#!/usr/bin/env python3

import io
import re

import argparse
import pypandoc
import panflute

# store command definitions
cmd_defs: dict[str, str] = {}


def extract_cmds(latex_content):
    """Extract LaTeX command definitions."""

    pattern = r'\\newdelimitedcommand{(\w+)}{(.+?)}'
    matches = re.finditer(pattern, latex_content)

    commands = {}

    for match in matches:
        command_name = match.group(1)
        definition = match.group(2)
        commands[command_name] = definition

    return commands


def find_and_replace_cmds(elem: panflute.Element, _):
    """Find and replace LaTeX command definitions."""
    if isinstance(elem, panflute.RawInline) and elem.format == "latex":
        for command, definition in cmd_defs.items():
            pattern = r'\\' + command + r'{}'
            text = re.sub(pattern, definition, elem.text)

            if elem.text != text:
                return panflute.Str(text)

    return elem


def extract_abstract_from_meta(doc):
    """Extract the abstract from metadata."""
    if 'abstract' in doc.metadata:
        abstract = doc.metadata['abstract']

        # MetaBlocks are a list of block elements (e.g., Para, BulletList, etc.)
        if isinstance(abstract, panflute.MetaBlocks):
            return abstract.content
        elif isinstance(abstract, panflute.MetaInlines):
            return [panflute.Para(abstract)]

    return None


def finalize(doc):
    """Replace document content with abstract when used a panflute filter finalize
    function."""
    abstract_blocks = extract_abstract_from_meta(doc)
    if abstract_blocks:
        # Replace document content with abstract blocks
        doc.content = abstract_blocks
    else:
        doc.content = [panflute.Para(panflute.Str("No abstract found."))]


def noop(elem, doc):
    """Noop for block-level filtering in a panflute filter action."""
    return None


def main():
    """
    Export abstract as markdown from a LaTeX file with some support for replacing custom
    LaTeX commands.
    """
    parser = argparse.ArgumentParser(
        description=r'Export abstract from LaTeX file to markdown with \\newdelimitedcommand replaced'
    )
    parser.add_argument('-i', "--input_file", help='input LaTeX file')
    parser.add_argument('-o', "--output_file", help='output abstract as markdown file')
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            content = file.read()
            global cmd_defs
            cmd_defs = extract_cmds(content)
    except Exception as exc:
        print(exc)
        return

    data = pypandoc.convert_file(
        args.input_file, 'json', extra_args=['--from=latex+raw_tex']
    )
    content = io.StringIO(data)
    doc = panflute.load(content)
    doc = panflute.run_filter(noop, finalize=finalize, doc=doc)
    doc = panflute.run_filter(find_and_replace_cmds, doc=doc)
    md_content = panflute.convert_text(doc, 'panflute', 'markdown')

    try:
        with open(args.output_file, 'w', newline='', encoding='utf-8') as file:
            file.write(str(md_content))
    except Exception as exc:
        print(exc)
        return


if __name__ == "__main__":
    main()
