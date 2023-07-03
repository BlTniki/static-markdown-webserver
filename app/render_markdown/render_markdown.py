from external.markdown_extensions import unof_extensions
from config import Config

from markdown import Markdown
import os


def get_filename(file_path):
    file_name = os.path.basename(file_path)
    file_name = file_name[0: file_name.rfind(".")]
    return file_name

def get_markdown_page(ABSPATH: str):
    with open(ABSPATH, "r", encoding="UTF") as f:
        md = f.read()
    return md


class MarkdownRenderer:

    def __init__(self, config: Config):
        # Load official extensions list
        of_extensions = config.OFFICIAL_EXTENSIONS_TO_USE

        # Make list with official and unofficial extensions
        extensions = [*of_extensions, *unof_extensions]

        # Init markdown
        self.md = Markdown(extensions=extensions)

    def render_page(self, ABSPATH: str):
        # get markdown file
        md_str = get_markdown_page(ABSPATH)
        # append filename as header
        md_str = f"# {get_filename(ABSPATH)}\n" + md_str
        # and render it
        return self.md.convert(md_str)


if __name__ == "__main__":
    p = "D:\\!Important\\Progrog\\Python\\static-markdown-webserver\\app\\render_markdown\\render_markdown.py"
    p1 = "/lol/kek.md"
    print(get_filename(p))
    # md = Markdown(extensions=unof_extensions)
    # print(md.convert("kekDimalovelylox\n$\\frac{1}{0}$\n$$\n\\frac{1}{0}\n$$\ndawdaw\n"))
