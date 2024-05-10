from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from common.database import db
from common.marshmallow import add_schema


@add_schema
class Estado(db.Model):
    __tablename__ = "estado"
    __table_args__ = {"schema": "indices"}

    codestado = Column(Integer, primary_key=True, nullable=False)
    nomeestado = Column(String(20), nullable=False)
    siglaestado = Column(String(2), nullable=False)
    codregiao = Column(Integer, ForeignKey('indices.regiao.codregiao'), nullable=False)

    ForeignKeyConstraint(
        [codregiao],
        ['indices.regiao.codregiao'],
        name='fk_estado_pk_regiao',
        onupdate='NO ACTION',
        ondelete='NO ACTION'
    )