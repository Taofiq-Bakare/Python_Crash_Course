from survey import AnonymousSurvey as ans

# define a question, and make as survey.

question = "What language did you first learn to speak? "
my_survey = ans(question)

my_survey.show_question()
print("Enter 'q' to exit the program.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# show the result of the survey.

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
