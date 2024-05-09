from flask import Flask


def register_routes(app: Flask) -> None:
    app.add_url_rule('/', 'root', )
