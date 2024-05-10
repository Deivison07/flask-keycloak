from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from common.database import db
from common.marshmallow import add_schema



@add_schema
class Municipio(db.Model):
    __tablename__ = "municipio"
    __table_args__ = {"schema": "indices"}

    codmunicipio = Column(Numeric(precision=6, scale=0), primary_key=True)
    nomemunicipio = Column(String(50), nullable=False)
    codestado = Column(Integer,  nullable=False)
    
