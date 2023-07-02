import markdown

def get_markdown_page(ABSPATH: str):
    with open(ABSPATH, "r", encoding="UTF") as f:
        md = f.read()
    return md


def render_page(ABSPATH: str):
    # get markdown file and render it
    md = get_markdown_page(ABSPATH)
    return markdown.markdown(md, extensions=['fenced_code', 'tables', 'nl2br', 'markdown_katex'])


if __name__ == "__main__":
    print(render_page(r"D:\!Important\Progrog\Python\static-markdown-webserver\app\md_static\index.md"))