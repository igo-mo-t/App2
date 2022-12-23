from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:test@db/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://test:test@127.0.0.1:5433/test'
app.config['JSON_AS_ASCII'] = False

db=SQLAlchemy()
db.init_app(app)
migrate=Migrate(app, db)
    
from . import views    

    
  

    



