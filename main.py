from generalknowledgedata import data
from question_format import QuestionFormat
from question_rules import QuestionAnswerRules
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

user_name = input("Whats your name? ")
"""this list will create a list of question and answer from the database provided in General Knowledge data"""
question_list = []

for i in data:
    question = (i['question'])
    answer = (i['correct_answer'])
    final_question = QuestionFormat(question, answer)
    question_list.append(final_question)

quiz = QuestionAnswerRules(question_list)

"""the while loop will continue the test , until its finish"""
while quiz.test_finish():
    quiz.following_question()
print(f"{user_name}, you have completed the test. ")
print(f"Your total score is {quiz.points}.")


"""this section will get you the result of the users"""
email_result = MIMEMultipart()
email_result["from"] = "QuizTime"
email_result["to"] = "email"
email_result["subject"] = "Test result"
email_result.attach(MIMEText(f"{user_name} total score is {quiz.points}."))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("email", "password")
    smtp.send_message(email_result)

