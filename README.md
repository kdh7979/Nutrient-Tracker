# Nutrient-Tracker
## 주제
gemini API를 활용해 식품과 영양정보표가 보이는 이미지로부터 영양정보(나트륨, 탄수화물, 당류 등) 수치를 추출하고, 해당 식품의 유형을 추론하여 하루동안 섭취한 식품의 유형, 권장 영양소, 섭취 시간대 등을 기록할 수 있는 웹페이지 개발

![structure_fig](https://github.com/user-attachments/assets/b390528c-8c2a-4d98-b7a8-5d8dacfff54d)
## 주요 기능
- 이미지 내의 영양정보 표로부터 각 영양 성분 수치(g / mg 단위)를 추출하여 하루 총 섭취 영양 정보를 표시
- 섭취한 식품들을 식품 유형별로 분류하여 기록
- 하루 영양소 섭취 기준 권장량과 하루 총 섭취 영양소를 비교
- 일별 영양 섭취량 비교 그래프 시각화
- 시간대별 섭취 식품 개수, 유형, 열량 등을 시각화
- AI의 오류 가능성, 영양정보표의 부재를 고려하여 직접 내용 추가, 수정, 삭제 기능

## DB, 컨트롤러 설계
어떤 DB를 쓸까? -> 관계형 데이터베이스 (SQLite / MySQL / PostgreSQL etc.)

### DB에 저장할 값들

- 유저 아이디 - string
- 유저 패스워드 - string
- 유저명 - string

- 이미지 주소 - string
- 식품 유형 - enum (int)
- 섭취 시각 - datetime
- 영양정보(총 9가지) - (unsigned) float

```javascript
exports.makeAccount = (userID, userPW) => {
    // ID 중복 여부 확인
    // PW 복잡성 확인 (~글자 이상, 대문자 포함 등)
    // user db에 uid, userID, PW 등의 정보 추가 (uid 할당 방식)
}

exports.login = (userID, userPW) => {
    // userID, userPW 일치하는 회원 정보 확인
    // 로그인 성공시 userName 변수에 유저명 할당, db에 저장된 userid uid 변수에 할당
    // userName = ...
    // uid = ...
}

exports.addFoodData = (uid, food_category, intake_time, img_path, essential_nutrients) => {
    // db에 섭취한 음식의 이미지, API를 통해 인식한 식품 유형, 영양소 수치 등을 DB에 저장하는 코드
}

exports.findDailyNutrient = (uid, date) => {
    // 특정 uid를 가지는 유저의 db에서 특정 날짜(date)로 필터링한 결과 반환
    // 이 함수의 결과로 그래프 시각화, 하루 섭취 영양소 총량, 시간대 별 섭취 음식 등 시각화
    // db = findUserDB(uid)
    // dailyNutrients = db.find(date)
    // return dailyNutrients
}
```
