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
os.system("cls || clear")

#create
print("solicitando dados para o usuario")
inserir_nome = input("digite seu nome: ")
inserir_email = input("digite seu email : ")
inserir_senha = input("digite sua senha: ")


usuario = Usuario(nome=inserir_nome, email=inserir_email, senha=inserir_senha)
session.add(usuario)
session.commit()


#listando usuarios do banco de dados
print("exibindo todos usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#delete
print("\nexcluindo um usuário. ")
email_usuario = input("informe o email do usuario para ser excluido: ")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()
session.delete(usuario)
session.commit()
print(f"{usuario.nome} excluido com sucesso")


#listando usuarios do banco de dados
print("exibindo todos usuários do banco de dados")
lista_usuarios = session.query(Usuario).all()

#read
for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.senha}")

#update
print("atualizando dados do  usuario")
usuario = session.query(Usuario).filter_by(email = email_usuario).first()

novos_dados = Usuario(
    nome = input("digite seu nome: ")
    email = input("digite seu email : ")
    senha = input("digite sua senha: ")

)

usuario = novos_dados
session.add(usuario)
session.commit()

#fechando conexao
session.close()