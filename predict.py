import joblib

model = joblib.load("models/model.pkl")

house = [[
    1,
    2500,
    4,
    3,
    2,
    2015,
    0,
    2,
    1
]]

prediction = model.predict(house)

print("Predicted Price:", prediction[0])