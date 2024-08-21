from sqlalchemy.orm import Session
from src.database.models import Users, Foods, Nutrients, DateTime

# 아래 설계한 컨트롤러를 만들어 넣기
def create_user(db: Session, user: Users, commit : bool = True):
    db.add(user)
    if commit:
        db.commit()
    return user

def get_user_by_id(db: Session, user_id: int):
    return db.query(Users).filter(Users.id == user_id).first()

def addFoodData(db: Session, foodInfo: Foods, nutrients: Nutrients, commit: bool = True):
    db.add(foodInfo)
    db.add(nutrients)
    if commit:
        db.commit()
    return commit

def get_nutrient_from_food(db: Session, foodId: int):
    return db.query(Nutrients).filter(Nutrients.food_id == foodId)

def findDailyNutrient(db: Session, date: DateTime):
    return db.query(Foods).filter(Foods.intake_time == date)