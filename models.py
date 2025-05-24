from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Session
from sqlalchemy.sql import func

Base = declarative_base()


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    freebies = relationship("Freebie", back_populates="dev", cascade="all, delete-orphan")

    def freebies_count(self, session: Session):
        """Return number of freebies this dev has received."""
        count = session.query(func.count(Freebie.id)).filter(Freebie.dev_id == self.id).scalar()
        return count or 0


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company", cascade="all, delete-orphan")

    def total_value_of_freebies(self, session: Session):
        """Return total value of all freebies this company has given out."""
        total = session.query(func.sum(Freebie.value)).filter(Freebie.company_id == self.id).scalar()
        return total or 0


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    dev_id = Column(Integer, ForeignKey('devs.id'), nullable=False)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

    def __repr__(self):
        return f"<Freebie {self.item_name} from {self.company.name} to {self.dev.name} worth {self.value}>"
