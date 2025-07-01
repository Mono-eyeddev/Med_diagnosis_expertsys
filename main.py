import tkinter as tk
from tkinter import messagebox

# Diagnosis function (same logic as before)
def diagnose(symptoms):
    if symptoms["fever"] and symptoms["cough"] and symptoms["loss_of_smell"] and symptoms["fatigue"]:
        return "Diagnosis: You may have COVID-19."
    elif symptoms["fever"] and symptoms["body_aches"] and symptoms["headache"] and symptoms["fatigue"]:
        return "Diagnosis: You may have the Flu."
    elif symptoms["sneezing"] and symptoms["sore_throat"] and not symptoms["fever"]:
        return "Diagnosis: You may have a Common Cold."
    else:
        return "Diagnosis: Your symptoms do not match Cold, Flu, or COVID-19. Please consult a healthcare professional."

# GUI logic
def on_diagnose():
    # Collect symptom states
    symptoms = {
        "fever": fever_var.get(),
        "cough": cough_var.get(),
        "sore_throat": sore_throat_var.get(),
        "fatigue": fatigue_var.get(),
        "body_aches": body_aches_var.get(),
        "loss_of_smell": loss_of_smell_var.get(),
        "sneezing": sneezing_var.get(),
        "headache": headache_var.get()
    }

    result = diagnose(symptoms)
    messagebox.showinfo("Medical Diagnosis", result)

# Initialize the main window
root = tk.Tk()
root.title("MYCIN-style Medical Expert System")
root.geometry("420x450")
root.resizable(False, False)

# Title
tk.Label(root, text="Medical Diagnosis System (MYCIN-style)", font=("Arial", 14, "bold")).pack(pady=15)

# Instructions
tk.Label(root, text="Select all symptoms that apply:", font=("Arial", 12)).pack(pady=5)

# Symptom checkboxes
fever_var = tk.BooleanVar()
cough_var = tk.BooleanVar()
sore_throat_var = tk.BooleanVar()
fatigue_var = tk.BooleanVar()
body_aches_var = tk.BooleanVar()
loss_of_smell_var = tk.BooleanVar()
sneezing_var = tk.BooleanVar()
headache_var = tk.BooleanVar()

symptoms_frame = tk.Frame(root)
symptoms_frame.pack(pady=10)

tk.Checkbutton(symptoms_frame, text="Fever", variable=fever_var).grid(row=0, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Cough", variable=cough_var).grid(row=1, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Sore Throat", variable=sore_throat_var).grid(row=2, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Fatigue", variable=fatigue_var).grid(row=3, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Body Aches", variable=body_aches_var).grid(row=4, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Loss of Smell or Taste", variable=loss_of_smell_var).grid(row=5, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Sneezing", variable=sneezing_var).grid(row=6, column=0, sticky='w', padx=10, pady=2)
tk.Checkbutton(symptoms_frame, text="Headache", variable=headache_var).grid(row=7, column=0, sticky='w', padx=10, pady=2)

# Diagnose button
tk.Button(root, text="Diagnose", command=on_diagnose, bg="#007BFF", fg="white", font=("Arial", 12), width=20).pack(pady=20)

# Start the GUI loop
root.mainloop()

