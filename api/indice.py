from flask import jsonify, request
from models.indice import Indice, IndiceByMunicipio
from common.initial import keycloak_openid


def get_indice_all():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = Indice.query.paginate(page=page, per_page=per_page)
    schema = Indice.Schema()
    rows = pagination.items

    pagination_info = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total
    }

    response = {
        'data': schema.dump(rows, many=True),
        'pagination': pagination_info
    }
    return jsonify(response), 200


@keycloak_openid.role_in_client( request=request, role='casa')
def get_indice_municipio():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = IndiceByMunicipio.query.paginate(page=page, per_page=per_page)
    schema = IndiceByMunicipio.Schema()
    rows = pagination.items

    pagination_info = {
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
        'total_items': pagination.total
    }

    response = {
        'data': schema.dump(rows, many=True),
        'pagination': pagination_info
    }

    return jsonify(response), 200




