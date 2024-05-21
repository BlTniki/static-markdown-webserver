from .markdown_strikethrough.markdown_strikethrough import MarkdownStrikethrough
from .markdown_mark.markdown_mark import MarkdownMark
from .markdown_obsidian_katex import makeExtension as katexMakeExtension

# init list with unofficial extensions entities
unof_extensions = [MarkdownStrikethrough(), MarkdownMark(), katexMakeExtension()]
