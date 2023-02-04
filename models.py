from datetime import datetime

from sqlalchemy import Column, INT, VARCHAR, BOOLEAN, ForeignKey, DECIMAL, create_engine, SMALLINT, TIMESTAMP, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    # engine = URL.create("postgresql+psycopg2",
    #                     username="db_test_user",
    #                     password="123",
    #                     host="localhost",
    #                     database="belhard")

    # engine = create_engine('sqlite:///alchemy.sqlite3')
    engine = create_engine(
        'postgresql+psycopg2://db_test_user:123@localhost:5432/belhard?options=-csearch_path%3Dpublic')
    _Session = sessionmaker(bind=engine)

    # 'postgresql://db_test_user:123@localhost:5432/belhard?options=-csearch_path%3Dpublic'

    @staticmethod
    def create_session(func):
        def wrapper(*args, **kwargs):
            with Base._Session() as session:
                return func(*args, **kwargs, session=session)

        return wrapper

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk, session: Session = None):
        return session.get(cls, pk)

    @create_session
    def delete(self, session: Session = None):
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def all(cls, order_by: int = 'id', limit: int = None, offset: int = None, session: Session = None, **kwargs):
        query = session.scalars(
            select(cls)
            .filter_by(**kwargs)
            .limit(limit)
            .offset(offset)
            .order_by(order_by)
        )
        return query.all()

    def dict(self):
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data


class Category(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(64), unique=True, nullable=False)
    is_published = Column(BOOLEAN, default=True)

    # @classmethod
    # def values(cls):
    #     return [cls.name, cls.is_published]


class Product(Base):
    __tablename__ = 'products'

    name = Column(VARCHAR(64), nullable=False)
    descr = Column(VARCHAR(1024), nullable=True)
    price = Column(DECIMAL(8, 2), nullable=False)
    is_published = Column(BOOLEAN, default=True)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class Status(Base):
    __tablename__ = 'statuses'

    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(15), unique=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    username = Column(VARCHAR(128), nullable=False)
    email = Column(VARCHAR(128), unique=True, nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    status_id = Column(SMALLINT, ForeignKey('statuses.id', ondelete='RESTRICT'), nullable=False)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow)


class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)

# Base.metadata.create_all(bind=Base.engine)
# Base.metadata.drop_all(bind=Base.engine)
