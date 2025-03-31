import streamlit as st
import time
import random

# Set page title
st.title("Eidi Time!")

# Set a background color (you can customize the color as per your choice)
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #f5f5f5;
    }
    </style>
    """, unsafe_allow_html=True
)

# Display a fun greeting message
st.header("Welcome to Eidi Predictor App 🎉")

# Let user input their name
name = st.text_input("Enter your name:", "")

# Let user input LinkedIn URL (if they wish to share)
linkedin_url = st.text_input("Enter your LinkedIn URL (optional):", "")

# Set mood options
mood_options = ["Happy 😄", "Excited 🎉", "Sleepy 😴", "Nervous 😬", "Relaxed 😌"]
mood = st.selectbox("Aap kaise feel kar rahe ho?", mood_options)

# Get Eidi amount prediction
eidi_amount = random.randint(50, 5000)  # Random Eidi amount between 50 to 5000
st.write(f"🎁 Eidi Prediction: ₹{eidi_amount}")

# Add a message from the user
message = st.text_area("Send a message with your Eidi:", "")
if not message:
    st.warning("Aapko apna message zarur bhejna chahiye!")

# Countdown timer - dynamic duration
countdown_duration = st.slider("Set countdown duration (seconds)", min_value=5, max_value=60, step=5, value=10)
st.write(f"⏳ Countdown started! {countdown_duration} seconds left for Eidi!")

# Display countdown timer
for i in range(countdown_duration, 0, -1):
    time.sleep(1)
    st.write(f"⏳ {i} seconds left for Eidi!")

# Display Eidi celebration with a GIF or animation
st.image("farida.jpg", caption="Eidi Time Celebration!", use_container_width=True)

# Display a final message after countdown
st.write("🎉 EIDI TIME IS HERE!! 🎉")
st.write(f"🎁 Your Eidi is ₹{eidi_amount}!")
st.write(f"Feeling: {mood}")
st.write(f"Message: {message}")

# Social media sharing
if st.button("Share Your Eidi Experience!"):
    twitter_url = f"https://twitter.com/intent/tweet?text=I just got my Eidi! Feeling {mood} & got ₹{eidi_amount} today! #EidiTime"
    st.write(f"Share it on [Twitter](<{twitter_url}>)!")

# LinkedIn sharing (if the user inputs their LinkedIn URL)
if linkedin_url:
    st.write(f"Share your Eidi joy on LinkedIn: [Your LinkedIn]({linkedin_url})")

# End of the app
st.write("Thank you for using the Eidi Time App! Enjoy your Eidi and have a wonderful celebration! 🎉")
