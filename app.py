from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the saved model
with open("kings_county_model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)


@app.route("/isAlive")
def index():
    return "true"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    new_data = np.array(data["data"]).reshape(-1, 1)
    prediction = loaded_model.predict(new_data)
    return jsonify(prediction.tolist())


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
