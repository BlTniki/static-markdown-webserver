from .render_markdown import MarkdownRenderer
from configs import ConfigHandler

md_render = MarkdownRenderer(ConfigHandler.get_config())
