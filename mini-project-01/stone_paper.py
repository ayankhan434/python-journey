""" import random

Cscore=0
Hscore=0

while True:
    print(f"current scores you- {Hscore} computer-{Cscore}")
    user = int (input( " 1 for stone , 2 for paper 3 for scissors choose : "))

    com = random.randint(1,3)

    if user ==1 and com ==3:
        Hscore+=1
        print("You won the round \n")

    elif user ==2 and com ==1 :
        Hscore+=1
        print("You won the round \n")

    elif user ==3 and com ==2:
        Hscore+=1
        print("You won the round \n")

    elif user ==com:
        print("this round is a draw")

    else:
        Cscore+=1
        print("computer has won this round")

    if Cscore==5:
        print("computer has won the game ")
        break
    elif Hscore==5:
        print(" you have won the match")
 """

import streamlit as st
import random

# Page settings
st.set_page_config(
    page_title="Stone Paper Scissors",
    page_icon="🎮",
    layout="centered"
)

# Title
st.title("🪨 Stone Paper Scissors ✂️")
st.subheader("First to 5 wins 🏆")

# Session scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

if "result" not in st.session_state:
    st.session_state.result = ""

if "user_choice" not in st.session_state:
    st.session_state.user_choice = ""

if "computer_choice" not in st.session_state:
    st.session_state.computer_choice = ""


choices = {
    1: "🪨 Stone",
    2: "📄 Paper",
    3: "✂️ Scissors"
}


# Score Board
col1, col2 = st.columns(2)

with col1:
    st.metric("👤 You", st.session_state.user_score)

with col2:
    st.metric("🤖 Computer", st.session_state.computer_score)


st.divider()

st.write("### Choose your move 👇")


def play_game(user):

    computer = random.randint(1, 3)

    st.session_state.user_choice = choices[user]
    st.session_state.computer_choice = choices[computer]

    if user == computer:

        st.session_state.result = "🤝 It's a Draw!"

    elif (
        (user == 1 and computer == 3)
        or
        (user == 2 and computer == 1)
        or
        (user == 3 and computer == 2)
    ):

        st.session_state.user_score += 1
        st.session_state.result = "🎉 You Won!"

    else:

        st.session_state.computer_score += 1
        st.session_state.result = "🤖 Computer Won!"


# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🪨 Stone", use_container_width=True):
        play_game(1)

with col2:
    if st.button("📄 Paper", use_container_width=True):
        play_game(2)

with col3:
    if st.button("✂️ Scissors", use_container_width=True):
        play_game(3)


# Result
if st.session_state.result:

    st.divider()

    st.subheader(st.session_state.result)

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"👤 You: **{st.session_state.user_choice}**")

    with col2:
        st.write(f"🤖 Computer: **{st.session_state.computer_choice}**")


# Game Over
if st.session_state.user_score >= 5:

    st.success("🏆 CONGRATULATIONS! YOU WON THE GAME!")

elif st.session_state.computer_score >= 5:

    st.error("🤖 COMPUTER WON THE GAME!")


# Reset button
st.divider()

if st.button("🔄 Reset Game", use_container_width=True):

    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.result = ""
    st.session_state.user_choice = ""
    st.session_state.computer_choice = ""

    st.rerun()