from gooey import Gooey, GooeyParser
import pandas as pd
import tkinter as tk
from tkinter import ttk

# GUI decorator
@Gooey(program_name="CSV Importer", required_cols=1, default_size=(600, 400))
def main():
    parser = GooeyParser(description="Select a CSV file to import")
    parser.add_argument(
        "csv_file",
        help="Choose a CSV file",
        widget="FileChooser",
        type=str
    )
    
    args = parser.parse_args()
    
    if args.csv_file:
        try:
            df = pd.read_csv(args.csv_file)
            display_csv(df)
        except Exception as e:
            print(f"Error reading CSV file: {e}")

def display_csv(df):
    """ Display CSV contents in a simple Tkinter window """
    root = tk.Tk()
    root.title("CSV Preview")
    
    frame = ttk.Frame(root)
    frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")
    
    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    for _, row in df.head(5).iterrows():
        tree.insert("", "end", values=list(row))
    
    tree.pack(fill="both", expand=True)
    
    root.mainloop()

if __name__ == "__main__":
    main()
