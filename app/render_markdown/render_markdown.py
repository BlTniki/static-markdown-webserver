from external.markdown_extensions.markdown_mark.markdown_mark import MarkdownMark

from markdown import Markdown

def get_markdown_page(ABSPATH: str):
    with open(ABSPATH, "r", encoding="UTF") as f:
        md = f.read()
    return md


def render_page(ABSPATH: str):
    # get markdown file and render it
    md_str = get_markdown_page(ABSPATH)

    md = Markdown(extensions=['fenced_code', 'tables', 'nl2br', 'markdown_katex', MarkdownMark()])

    return md.convert(md_str)


if __name__ == "__main__":
    print(render_page(r"D:\!Important\Progrog\Python\static-markdown-webserver\app\md_static\index.md"))