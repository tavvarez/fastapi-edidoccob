from sqlalchemy import Column, Integer, ForeignKey
from app.models.base import Base

class UserInputCTELink(Base):
    __tablename__ = 'user_input_cte_link'

    id = Column(Integer, primary_key=True, index=True)
    user_input_id = Column(Integer, ForeignKey('user_input.id'), nullable=False)
    cte_info_id = Column(Integer, ForeignKey('cte_info.id'), nullable=False)