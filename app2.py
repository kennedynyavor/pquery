import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

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

        result_label.config(text=f"Annual Premium: ${premium:.2f}", foreground="green")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for age and coverage.")

# Create the main application window
root = tk.Tk()
root.title("Actuarial Calculator")
root.geometry("600x400")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use('default')  # Use default theme for customization
style.configure("TNotebook", background="#f0f0f0", borderwidth=0)  # Tab control styling
style.configure("TNotebook.Tab", background="#d1e0f0", foreground="black", padding=[20, 8], font=("Arial", 12))
style.map("TNotebook.Tab", background=[("selected", "#a3c9f7")])  # Change tab color when selected
style.configure("TButton", font=("Arial", 12), background="#4caf50", foreground="white", relief="flat")
style.map("TButton", background=[("active", "#45a049")])
style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
style.configure("TEntry", font=("Arial", 12))

# Create a Notebook (Tab Control)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

# Tab 1: Premium Calculator
tab1 = ttk.Frame(notebook, style="TFrame")
notebook.add(tab1, text="Premium Calculator")

# Title Label for Tab 1
title_label = ttk.Label(tab1, text="Actuarial Premium Calculator", font=("Arial", 16, "bold"), background="#f0f0f0")
title_label.pack(pady=10)

# Age Input
age_label = ttk.Label(tab1, text="Age:")
age_label.pack(pady=(10, 0))
age_entry = ttk.Entry(tab1)
age_entry.pack(pady=(0, 10))

# Gender Selection
gender_label = ttk.Label(tab1, text="Gender:")
gender_label.pack()
gender_combo = ttk.Combobox(tab1, values=["Male", "Female"], state="readonly")
gender_combo.current(0)  # Default selection
gender_combo.pack(pady=10)

# Coverage Input
coverage_label = ttk.Label(tab1, text="Coverage Amount ($):")
coverage_label.pack(pady=(10, 0))
coverage_entry = ttk.Entry(tab1)
coverage_entry.pack(pady=(0, 10))

# Calculate Button
calculate_button = ttk.Button(tab1, text="Calculate Premium", command=calculate_premium)
calculate_button.pack(pady=10)

# Result Label
result_label = ttk.Label(tab1, text="", font=("Arial", 14, "bold"), background="#f0f0f0")
result_label.pack(pady=10)

# Tab 2: Actuarial Information
tab2 = ttk.Frame(notebook, style="TFrame")
notebook.add(tab2, text="Actuarial Info")

info_label = ttk.Label(tab2, text="Actuarial Information", font=("Arial", 16, "bold"), background="#f0f0f0")
info_label.pack(pady=10)

info_text = """This calculator uses simplified actuarial logic to estimate insurance premiums based on age, gender, and coverage amount. 
The rates used are illustrative and may not reflect real-world scenarios."""
info_display = tk.Text(tab2, wrap=tk.WORD, height=10, width=50, font=("Arial", 12), bg="#f9f9f9", bd=0)
info_display.insert(tk.END, info_text)
info_display.config(state=tk.DISABLED)  # Make the text read-only
info_display.pack(pady=10)

# Tab 3: Settings
tab3 = ttk.Frame(notebook, style="TFrame")
notebook.add(tab3, text="Settings")

settings_label = ttk.Label(tab3, text="Settings", font=("Arial", 16, "bold"), background="#f0f0f0")
settings_label.pack(pady=10)

theme_label = ttk.Label(tab3, text="Theme:")
theme_label.pack(pady=(10, 0))
theme_combo = ttk.Combobox(tab3, values=["Light", "Dark"], state="readonly")
theme_combo.current(0)  # Default selection
theme_combo.pack(pady=10)

# Run the application
root.mainloop()