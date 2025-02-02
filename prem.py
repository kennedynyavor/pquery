import tkinter as tk
from tkinter import ttk, messagebox

# Function to calculate the premium based on actuarial logic
def calculate_premium():
    try:
        age = int(age_entry.get())
        gender = gender_combo.get().lower()
        coverage = float(coverage_entry.get())

        # Example actuarial logic (simplified)
        if gender == 'male':
            if age < 30:
                premium = coverage * 0.02
            elif 30 <= age < 50:
                premium = coverage * 0.03
            else:
                premium = coverage * 0.05
        elif gender == 'female':
            if age < 30:
                premium = coverage * 0.015
            elif 30 <= age < 50:
                premium = coverage * 0.025
            else:
                premium = coverage * 0.04
        else:
            messagebox.showerror("Error", "Invalid gender selected.")
            return

        result_label.config(text=f"Annual Premium: ${premium:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for age and coverage.")

# Create the main application window
root = tk.Tk()
root.title("Actuarial Calculator")
root.geometry("800x500")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12))
style.configure("TLabel", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))

# Title Label
title_label = ttk.Label(root, text="Actuarial Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Age Input
age_label = ttk.Label(root, text="Age:")
age_label.pack(pady=(10, 0))
age_entry = ttk.Entry(root)
age_entry.pack(pady=(0, 10))

# Gender Selection
gender_label = ttk.Label(root, text="Gender:")
gender_label.pack()
gender_combo = ttk.Combobox(root, values=["Male", "Female"], state="readonly")
gender_combo.current(0)  # Default selection
gender_combo.pack(pady=10)

# Coverage Input
coverage_label = ttk.Label(root, text="Coverage Amount ($):")
coverage_label.pack(pady=(10, 0))
coverage_entry = ttk.Entry(root)
coverage_entry.pack(pady=(0, 10))

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate Premium", command=calculate_premium)
calculate_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()