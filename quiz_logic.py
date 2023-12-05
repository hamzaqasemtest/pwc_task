def check_answer(index, user_choice, quiz_data):
    correct_answer = quiz_data[index]["answer"]
    return user_choice == correct_answer

