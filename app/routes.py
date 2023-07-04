from . import app
from app.filesystem_accounter import dirtree_accounter
from app.render_markdown import md_render

from flask import render_template, redirect, url_for, send_file, abort
from os.path import abspath, exists, sep


@app.route('/')
def index():
    return redirect(url_for("serve_url_for_md_static"))

@app.route('/md_static/')
@app.route('/md_static/<path:url>')
def serve_url_for_md_static(url="index.md"):
    # get abs path
    ABSPATH = abspath(app.config["PATH_TO_VAULT"] + sep + url)

    # check for existing
    if not exists(ABSPATH):
        return abort(404)

    # if it's not markdown file return as file
    if url[-3:] != ".md":
        return send_file(ABSPATH)

    # get markdown file and render it
    html = md_render.render_page(ABSPATH)

    return render_template("markdown_page.html", vault_tree=vault_tree, payload=html)
