from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class AgriMarketModel(BaseModel, Base):
    """ Your AgriMarket model class """
    # Define the class attributes for SQLALchemy
    __tablename__='agrimarket_models'
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
