# MYCIN-style expert system for Cold, Flu, and COVID-19
def get_boolean_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer with yes or no.")

def get_symptoms():
    print("Welcome to the MYCIN-style Medical Diagnosis System")
    print("Please answer the following questions with yes or no.\n")

    symptoms = {}
    symptoms["fever"] = get_boolean_input("Do you have a fever? ")
    symptoms["cough"] = get_boolean_input("Do you have a cough? ")
    symptoms["sore_throat"] = get_boolean_input("Do you have a sore throat? ")
    symptoms["fatigue"] = get_boolean_input("Do you feel fatigued? ")
    symptoms["body_aches"] = get_boolean_input("Do you have body aches? ")
    symptoms["loss_of_smell"] = get_boolean_input("Have you lost your sense of smell or taste? ")
    symptoms["sneezing"] = get_boolean_input("Are you sneezing? ")
    symptoms["headache"] = get_boolean_input("Do you have a headache? ")

    return symptoms

def diagnose(symptoms):
    if symptoms["fever"] and symptoms["cough"] and symptoms["loss_of_smell"] and symptoms["fatigue"]:
        return "Diagnosis: You may have COVID-19."
    elif symptoms["fever"] and symptoms["body_aches"] and symptoms["headache"] and symptoms["fatigue"]:
        return "Diagnosis: You may have the Flu."
    elif symptoms["sneezing"] and symptoms["sore_throat"] and not symptoms["fever"]:
        return "Diagnosis: You may have a Common Cold."
    else:
        return "Diagnosis: Your symptoms do not match Cold, Flu, or COVID-19. Please consult a healthcare professional."

if __name__ == "__main__":
    user_symptoms = get_symptoms()
    result = diagnose(user_symptoms)
    print("\n" + result)
