from sqlalchemy import create_engine , Column , Integer , String , Float , ForeignKey
from sqlalchemy.orm import declarative_base , relationship , sessionmaker

Base = declarative_base()

# Banco de dados aqui
# Tabela curso

class Curso(Base):
    __tablename__ = "cursos"

#colunas da tabela do curso
id = Column(Integer,primary_key=True , autoincrement=True)
nome = Column(String(100) , nullable=False)
duracao_dias = Column(Integer)
descricao = Column(String(100))



#Tabela aluno

class Aluno(Base):
    __tablename__ = "alunos"

    #colunas da tabela cursos
    id = Column(Integer,primary_key=True , autoincrement=True)
    nome = Column(String(100) , nullable=False)
    email = Column(String(100) , unique=False)
    idade = Column(Integer)