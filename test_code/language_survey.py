from survey import AnonymousSurvey

#定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time if you want to quit.\n")
while True:
    response = input("Language:")
    if response == 'q':
        break   
    else:
        my_survey.store_response(response)
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
