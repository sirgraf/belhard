
from sqlalchemy import Column, INT, VARCHAR, ForeignKey, create_engine, select
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
            with Base._Session() as ssession:
                return func(*args, **kwargs, session=session)

        return wrapper

    # @staticmethod
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


class Role(Base):
    __tablename__ = 'role'

    name = Column(VARCHAR(15), unique=True, nullable=False)


class User(Base):
    __tablename__ = 'user'

    username = Column(VARCHAR(255), unique=True, nullable=False)
    email = Column(VARCHAR(255), unique=True, nullable=False)
    role_id = Column(INT, ForeignKey('role.id', ondelete='CASCADE'), nullable=False)


class Topic(Base):
    __tablename__ = 'topic'

    author_id = Column(INT, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete='CASCADE'), nullable=False)


class Category(Base):
    __tablename__ = 'category'

    name = Column(VARCHAR(255), unique=True, nullable=False)


class Comment(Base):
    __tablename__ = 'comment'

    user_id = Column(INT, ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    topic_id = Column(INT, ForeignKey('topic.id', ondelete='CASCADE'), nullable=False)
    parent_id = Column(INT, ForeignKey('comment.id', ondelete='CASCADE'), nullable=False)

# Base.metadata.create_all(bind=Base.engine)
# Base.metadata.drop_all(bind=Base.engine)
