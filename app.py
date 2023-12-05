import streamlit as st
from langchain_integration import generate_questions
from quiz_logic import check_answer

if 'quiz_data' not in st.session_state:
    st.session_state.quiz_data = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0

def display_preferences_form():
    with st.form(key='preferences_form'):
        topic = st.text_input("Enter the topic for the quiz:")
        num_questions = st.number_input("How many questions do you want?", min_value=1, max_value=10, value=5)
        submit_button = st.form_submit_button(label='Generate Quiz')
        if submit_button:

            st.session_state.quiz_data = generate_questions(topic, num_questions)
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.experimental_rerun()

def display_question():
    current_data = st.session_state.quiz_data[st.session_state.current_question]
    st.write(current_data["question"])
    options = current_data["choices"]
    with st.form(key='question_form'):
        answer = st.radio("Choose one:", options)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            if check_answer(st.session_state.current_question, answer, st.session_state.quiz_data):
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error("Wrong answer!")
            st.session_state.current_question += 1
            if st.session_state.current_question == len(st.session_state.quiz_data):
                st.write(f"Quiz completed! Your score is {st.session_state.score}/{len(st.session_state.quiz_data)}")
            else:
                st.experimental_rerun()

def main():
    st.title("PWC TASK MCQ Quiz")
    if not st.session_state.quiz_data:
        display_preferences_form()
    else:
        display_question()
    st.write(f"Your current score is {st.session_state.score}")

if __name__ == "__main__":
    main()
