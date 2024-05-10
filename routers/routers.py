from flask import Flask, jsonify
from api.regiao import get_regiao_all
from api.estago import get_estado_all
from api.indice import get_indice_all, get_indice_municipio

def get_root():
    return jsonify({
        'return': 'API IDH regiões'
        }), 200


def register_routes(app: Flask) -> None:
    app.add_url_rule('/', 'root', get_root, methods=['GET'])
    app.add_url_rule('/regioes', 'get_regioes', get_regiao_all, methods=['GET'])
    app.add_url_rule('/estados', 'get_estados', get_estado_all, methods=['GET'])
    app.add_url_rule('/indices', 'get_indices', get_indice_all, methods=['GET'])
    app.add_url_rule('/indices-mun', 'get_indices_mun', get_indice_municipio, methods=['GET'])
