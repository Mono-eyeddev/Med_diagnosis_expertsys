import flet as ft
from experta import *

# Step 1: Create a simple expert system class
class PatientSymptoms(Fact):
    pass

class MedicalExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnosis = "No diagnosis yet."

    @Rule(PatientSymptoms(fever='yes', cough='yes', sore_throat='yes'))
    def flu(self):
        self.diagnosis = "You might have the **Flu**."

    @Rule(PatientSymptoms(cough='yes', sore_throat='yes', runny_nose='yes'))
    def cold(self):
        self.diagnosis = "You might have the **Common Cold**."

    @Rule(PatientSymptoms(fever='yes', diarrhea='yes'))
    def gi(self):
        self.diagnosis = " You might have a **Gastrointestinal Infection**."

    @Rule(PatientSymptoms(fever='yes', headache='yes', fatigue='yes'))
    def malaria(self):
        self.diagnosis = " Possible **Malaria**. Get tested."

    @Rule(AS.fact << PatientSymptoms())
    def unknown(self, fact):
        self.diagnosis = "Diagnosis unclear. Please consult a doctor."


# Step 2: Flet UI
def main(page: ft.Page):
    page.title = "MediHelper - Expert Diagnosis"
    page.theme_mode = "light"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.scroll = "auto"

    title = ft.Text("MediHelper - Medical Diagnosis", size=24, weight="bold")

    # Inputs
    inputs = {}
    questions = {
        "fever": "Do you have a fever?",
        "cough": "Do you have a cough?",
        "sore_throat": "Do you have a sore throat?",
        "runny_nose": "Do you have a runny nose?",
        "headache": "Do you have a headache?",
        "fatigue": "Do you feel fatigue?",
        "diarrhea": "Do you have diarrhea?"
    }

    for key, question in questions.items():
        inputs[key] = ft.Dropdown(
            label=question,
            options=[ft.dropdown.Option("yes"), ft.dropdown.Option("no")],
            width=300
        )

    result = ft.Text(value="", size=20, color="#2196f3")


    # Button
    def diagnose(e):
        symptoms = {key: dropdown.value or "no" for key, dropdown in inputs.items()}

        # Run expert system
        engine = MedicalExpertSystem()
        engine.reset()
        engine.declare(PatientSymptoms(**symptoms))
        engine.run()

        result.value = engine.diagnosis
        page.update()

    btn = ft.ElevatedButton("🩺 Diagnose", on_click=diagnose)

    # Add all to the page
    page.add(title)
    page.add(*inputs.values())
    page.add(btn, result)

ft.app(target=main)
