from flask import jsonify, request
from sqlalchemy import text
from sqlalchemy.orm import Query
from models.indice import Indice, IndiceByMunicipio
from common.database import db

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

def get_indice_municipio():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    sql_query = text('SELECT indi.ano, muni.nomemunicipio, indi.idh_educacao, indi.idh_renda FROM indices.indice as indi, indices.municipio as muni where indi.codmunicipio =  muni.codmunicipio')
    rows = db.session.execute(sql_query).all()
    
    i = 1
    list_query = []
    row_exemplo = {
        'ano': 2022,
        'codmunicipio': f'codigo_municipio {i}',
        'idh_educacao': 0.75,
        'idh_renda': 0.78,
    }
    i+=1
    for row in rows:
        list_query.append(IndiceByMunicipio(**row_exemplo))
    
    consulta = db.session.query(IndiceByMunicipio).filter(IndiceByMunicipio.codmunicipio.in_([objeto.codmunicipio for objeto in list_query]))
    paginated_query = consulta.all()

    a = 1

    # pagination = query.

    # with db.engine.connect() as conection:
    #     SQL = text('SELECT indi.ano, muni.nomemunicipio, indi.idh_educacao, indi.idh_renda FROM indices.indice as indi, indices.municipio as muni where indi.codmunicipio =  muni.codmunicipio')
    #     resu = conection.execute(SQL).paginate(page=page, per_page=per_page)

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
