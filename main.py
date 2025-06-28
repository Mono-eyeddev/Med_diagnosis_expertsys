# MYCIN-style expert system for Cold, Flu, and COVID-19

def get_symptoms():
    print("Welcome to the MYCIN-style Medical Diagnosis System")
    print("Please answer the following questions with yes or no.\n")

    symptoms = {}
    symptoms["fever"] = input("Do you have a fever? ").lower() == "yes"
    symptoms["cough"] = input("Do you have a cough? ").lower() == "yes"
    symptoms["sore_throat"] = input("Do you have a sore throat? ").lower() == "yes"
    symptoms["fatigue"] = input("Do you feel fatigued? ").lower() == "yes"
    symptoms["body_aches"] = input("Do you have body aches? ").lower() == "yes"
    symptoms["loss_of_smell"] = input("Have you lost your sense of smell or taste? ").lower() == "yes"
    symptoms["sneezing"] = input("Are you sneezing? ").lower() == "yes"
    symptoms["headache"] = input("Do you have a headache? ").lower() == "yes"

    return symptoms


def diagnose(symptoms):
    # Rule-based diagnosis
    if symptoms["fever"] and symptoms["cough"] and symptoms["loss_of_smell"] and symptoms["fatigue"]:
        return "Diagnosis: You may have COVID-19."
    elif symptoms["fever"] and symptoms["body_aches"] and symptoms["headache"] and symptoms["fatigue"]:
        return "Diagnosis: You may have the Flu."
    elif symptoms["sneezing"] and symptoms["sore_throat"] and not symptoms["fever"]:
        return "Diagnosis: You may have a Common Cold."
    else:
        return "Diagnosis: Your symptoms do not match Cold, Flu, or COVID-19. Please consult a healthcare professional."


# Run the expert system
if __name__ == "__main__":
    user_symptoms = get_symptoms()
    result = diagnose(user_symptoms)
    print("\n" + result)