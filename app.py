from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load hospital data
with open("hospital_data.json") as f:
    data = json.load(f)

# Chatbot function
def chatbot(query):
    query = query.lower()

    if any(word in query for word in ["location", "address", "where"]):
        return f"The hospital is located at {data['address']}"

    elif any(word in query for word in ["time", "timing", "open"]):
        return f"Our hospital is open from {data['timing']}"

    elif any(word in query for word in ["service", "treatment"]):
        return "We provide services like " + ", ".join(data["services"])

    elif any(word in query for word in ["doctor", "specialist"]):
        return "Our doctors are " + ", ".join([doc["name"] for doc in data["doctors"]])

    elif any(word in query for word in ["appointment", "book"]):
        return data["appointment"]

    elif any(word in query for word in ["emergency", "24"]):
        return data["emergency"]

    elif any(word in query for word in ["contact", "phone"]):
        return data["contact"]

    else:
        return "I can help with location, timing, services, doctors, and appointments."

@app.route("/chat", methods=["POST"])
def chat():
     user_input = request.json["message"]
     response = chatbot(user_input)
     return jsonify({"reply": response})

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=10000)
	 