from sqlalchemy.orm import Mapped, mapped_column 
from ..extensions import db

class Expenses(db.Model):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    description: Mapped[str] 
    amount: Mapped[float]
    date: Mapped[str]


