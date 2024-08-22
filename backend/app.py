from flask import Flask, json, request, g

from src.middleware.cors import cors
from src.database.database import init_db, Base
from config import config

from src.database.controller import create_user, get_user_by_id, addFoodData, get_nutrient_from_food, findDailyNutrient
from src.database.models import Users, Foods, Nutrients


def init_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY

    # app에 뭔가 더 추가하고 싶은게 있으면 여기에 추가
    cors.init_app(app)
    
    @app.before_request
    def before_request():
        g.db_session = get_db()


    return app

app = init_app()
engine, get_db = init_db(config.DATABASE_URI)

# 데이터베이스 생성
Base.metadata.create_all(engine)

# 연결이 끊어질때 db close
@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/status')
def status():
    return json.jsonify({'status': 'ok'})

@app.route("/users/foods", methods=["GET", "POST"])
def handle_food_data():
    # 여기에 로직을 추가해주세요.
    request_data = request.get_json()
    print(request_data)
    db = get_db()
    if request.method == "GET":
        res = get_nutrient_from_food(db, request_data["foodId"])
        return json.jsonify({
                                "foodId": res[0].food_id,
                                "calorie": res[0].calorie,
                                "carbohydrates": res[0].carbohydrates,
                                "sugar": res[0].sugar,
                                "protein": res[0].protein,
                                "fat": res[0].fat,
                                "saturated_fat": res[0].saturated_fat,
                                "trans_fat": res[0].trans_fat,
                                "cholesterol": res[0].cholesterol,
                                "sodium": res[0].sodium,
                            })
    elif request.method == "POST":
        # foodInfo = Foods(request_data["foodInfo"])
        res = addFoodData(db, request_data['foodInfo'], request_data['nutrients'])
        return json.jsonify({"commit": res})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=13242)