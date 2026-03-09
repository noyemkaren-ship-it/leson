from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"


# Создаем таблицы
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create(name: str, age: int) -> User:
    new_user = User(name=name, age=age)
    session.add(new_user)
    session.commit()
    return new_user

def delete(user_id: int) -> None:
    user_to_delete = session.query(User).filter_by(id=user_id).first()
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        print(f"Пользователь с ID {user_id} удален")
    else:
        print(f"Пользователь с ID {user_id} не найден")
users = session.query(User).all()

def searches(name: str, age: int):
    user = session.query(User).filter_by(name=name, age=age).first()
    if user:
        return user
    else:
        return None

session.close()