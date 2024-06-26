
from flask import jsonify, request
from models.regiao import Regiao

def get_regiao_all():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    pagination = Regiao.query.paginate(page=page, per_page=per_page)
    schema = Regiao.Schema()
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