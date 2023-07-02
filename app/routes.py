from . import app
from app.filesystem_accounter import dirtree_accounter
from app.render_markdown import render_page

from flask import render_template, redirect, url_for, send_file, abort
from os.path import abspath, exists, sep


@app.route('/')
def index():
    return redirect(url_for("serve_url_for_md_static"))

@app.route('/md_static/')
@app.route('/md_static/<path:url>')
def serve_url_for_md_static(url="index.md"):
    # get abs path
    PATH = abspath(app.config["PATH_TO_VAULT"] + sep + url)

    # check for existing
    if not exists(PATH):
        return abort(404)

    # if it's not markdown file return as file
    if url[-3:] != ".md":
        return send_file(PATH)

    # get markdown file and render it
    html = render_page(PATH)

    # get vault_tree
    vault_tree = dirtree_accounter.get_file_tree()

    return render_template("base.html", vault_tree=vault_tree, content=html)
