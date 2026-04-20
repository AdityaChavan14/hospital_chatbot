import streamlit as st
import json

# Load hospital data
with open("hospital_data.json") as f:
    data = json.load(f)

# Chatbot function
def chatbot(query):
    query = query.lower()
    
    if any(word in query for word in ["hi", "hello", "hey"]):
        return f"Hello! welcome to {data['name']}. How can I assist you today?"

    elif any(word in query for word in["location","address","where"]):
        return f"The hospital is located at {data['address']}"

    elif any(word in query for word in["time","timing","open"]):
        return f"Our hospital is open from {data['timing']}"

    elif any(word in query for word in ["service", "treatment"]):
        return "We provide services like " + ", ".join(data["services"])

    elif any(word in query for word in ["doctor", "specialist"]):
        return "Our doctors are " + ", ".join([doc["name"] for doc in data["doctors"]])

    elif any(word in query for word in ["appointment", "book"]):
        return data["appointment"]

    elif any(word in query for word in ["contact", "phone"]):
        return data["contact"]

    else:
        return "I can help with location, timing, services, doctors and appointments."

# UI Title
st.title("Hospital Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.text_input("You:")

# Button click
if st.button("Send"):
    response = chatbot(user_input)

    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("Bot", response))

# Show chat
for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")