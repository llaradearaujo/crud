#.txt
#banco de dados - SQLite
#SQL - linguagem de consulta estruturada
# SELECT * FROM CLIENTES
#NOME, SOBRENOME, IDADE
#ORM
#FORMA DE COLOCAR DENTRO DO CÓDIGO OS COMANDOS SQL

import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

#criando banco de dados
MEU_BANCO = create_engine("sqlite:///meubanco.db")

#criando conexao com banco de dados
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

#I = input (entrada)
#O = output (saida)

#criando tabela
Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    
    def __init__(self, nome: str, email:str, senha:str):
        self.nome = nome
        self.email = email
        self.senha = senha

#criando tabela no banco de dados
Base.metadata.create_all(bind=MEU_BANCO)
    
#SALVAR NO BANCO DE DADOS
usuario = Usuario(nome="marta", email="marta@gmail.com", senha="123")
session.add(usuario)
session.commit()

usuario = Usuario(nome = "maria", email="maria@gmail.com", senha="456")
session.add(usuario)
session.commit()

#listando usuarios do banco de dados
print("exibindo todos usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")
    
#fechando conexao
session.close()