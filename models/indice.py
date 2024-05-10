from sqlalchemy import Column, Integer, Numeric, ForeignKey, String
from common.database import db
from common.marshmallow import add_schema


@add_schema
class Indice(db.Model):
    __tablename__ = 'indice'
    __table_args__ = {"schema": "indices"}
    
    codmunicipio = Column(Integer, primary_key=True, nullable=False)
    ano = Column(Numeric, primary_key=True)
    idh_geral = Column(Numeric(precision=8, scale=3), nullable=False)
    idh_renda = Column(Numeric(precision=8, scale=3), nullable=False)
    idh_longevidade = Column(Numeric(precision=8, scale=3), nullable=False)
    idh_educacao = Column(Numeric(precision=8, scale=3), nullable=False)

@add_schema
class IndiceByMunicipio(db.Model):
    
    ano = Column(Numeric, primary_key=True)
    codmunicipio = Column(String, nullable=False)
    idh_educacao = Column(Numeric(precision=8, scale=3), nullable=False)
    idh_renda = Column(Numeric(precision=8, scale=3), nullable=False)

    
