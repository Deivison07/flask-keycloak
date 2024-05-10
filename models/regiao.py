from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, schema
from common.database import db
from common.marshmallow import add_schema


@add_schema
class Regiao(db.Model):
  __tablename__ = 'regiao'
  __table_args__ = {"schema": "indices"}

  codregiao = Column(Integer, primary_key=True)
  nomeregiao = Column(String(20), nullable=False)
