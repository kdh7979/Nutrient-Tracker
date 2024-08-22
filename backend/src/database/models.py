from sqlalchemy import Integer, String, DateTime, Boolean, Float
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from src.database.database import Base


# class 명은 마음대로 바꿔도 됨
class Users(Base):
    __tablename__ = "users" # 여기에 테이블 이름
    # 이건 건들지 말기
    id = Column(Integer, primary_key=True, index=True)

    # 아래 원하는 컬럼 추가
    # user_id = Column(Integer, primary_key=True)
    # summoner_id = Column(String, nullable=False, unique=True, index=True)
    # puuid = Column(String, nullable=True, index=True)




class Foods(Base):
    __tablename__ = "foods"
    food_id = Column(Integer, primary_key=True, index=True)
    eater_id = Column(Integer, ForeignKey('users.id'))
    food_category = Column(String)
    intake_time = Column(DateTime, default=current_timestamp())
    img_path = Column(String, nullable=True)
    nutrient = relationship("Nutrients", back_populates="foods")



class Nutrients(Base):
    '''
    [열량, 탄수화물, 당류, 단백질, 지방, 포화지방, 트랜스지방, 클레스테롤, 나트륨]
    '''
    __tablename__ = "nutrients"
    food_id = Column(Integer, ForeignKey('foods.food_id'), primary_key=True)
    calorie = Column(Float(2))
    carbohydrates = Column(Float(2))
    sugar = Column(Float(2))
    protein = Column(Float(2))
    fat = Column(Float(2))
    saturated_fat = Column(Float(2))
    trans_fat = Column(Float(2))
    cholesterol = Column(Float(2))
    sodium = Column(Float(2))
    foods = relationship("Foods", back_populates="nutrient")