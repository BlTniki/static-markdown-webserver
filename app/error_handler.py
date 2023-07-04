from . import app

from flask import abort

@app.errorhandler(Exception)
def handle_internal_error(e):
    app.logger.exception(e)
    if not app.debug:
        abort(500)
    else:
        raise e

@app.errorhandler(404)
def handle_not_found_error(error):

    return error