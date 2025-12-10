from sqlalchemy import Column,Integer,String,Boolean,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    is_done = Column(Boolean,default=False)


engine = create_engine("sqlite:///todos.db")


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)