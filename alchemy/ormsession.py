from sqlalchemy.orm import DeclarativeBase
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from dataclasses import dataclass
from sqlalchemy.orm import Session
from sqlalchemy import text

class Store(DeclarativeBase):
    pass


@dataclass
class User(Store):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
@dataclass
class Address(Store):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"


engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
Store.metadata.create_all(engine)
pk = User(id=1, name="Praveen", fullname="Praveen Singh", addresses=([Address(id=1, email_address="pk@hey.com"),]))
with Session(engine) as session:
    session.add(pk)
    session.commit()
    
    
with engine.connect() as conn:
    rs = conn.execute(text("select * from user_account"))
    print(rs.all())