import tkinter as tk
from tkinter import messagebox
import pickle
import numpy as np

try:
    with open(r'E:\Work\Programs\Python\AI\Machine Learning\Projects\House Price Predictator\model\cityhome.pkl', 'rb') as file:
        data = pickle.load(file)
        model = data['model']
except FileNotFoundError:
    print("Error: cityhome.pkl not found. Please run your training script first.")
    exit()

def predict_price():
    try:
        size = float(entry_size.get())
        beds = int(entry_beds.get())
        baths = int(entry_baths.get())
        year = int(entry_year.get())
        
       
        loc_map = {"Downtown": 0, "Rural": 1, "Suburban": 2}
        loc_val = loc_map.get(variable_loc.get())
        
        
        cond_map = {"Excellent": 0, "Fair": 1, "Good": 2, "Needs Renovation": 3}
        cond_val = cond_map.get(variable_cond.get())

        
        features = np.array([[size, beds, baths, loc_val, cond_val, year]])
        prediction = model.predict(features)[0]

        
        label_result.config(text=f"Estimated Price: ${prediction:,.2f}", fg="green")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")


root = tk.Tk()
root.title("CityHome Price Predictor")
root.geometry("400x500")

tk.Label(root, text="House Price Predictor", font=("Arial", 16, "bold")).pack(pady=10)

fields = [
    ("Size (SqFt):", "entry_size"),
    ("Bedrooms:", "entry_beds"),
    ("Bathrooms:", "entry_baths"),
    ("Year Built:", "entry_year")
]

entries = {}
for text, name in fields:
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=20, pady=5)
    tk.Label(frame, text=text, width=15, anchor="w").pack(side="left")
    ent = tk.Entry(frame)
    ent.pack(side="right", expand=True, fill="x")
    entries[name] = ent

entry_size = entries["entry_size"]
entry_beds = entries["entry_beds"]
entry_baths = entries["entry_baths"]
entry_year = entries["entry_year"]


tk.Label(root, text="Location:", anchor="w").pack(padx=20, fill="x")
variable_loc = tk.StringVar(root)
variable_loc.set("Downtown") # Default
tk.OptionMenu(root, variable_loc, "Downtown", "Rural", "Suburban").pack(padx=20, fill="x", pady=5)

tk.Label(root, text="House Condition:", anchor="w").pack(padx=20, fill="x")
variable_cond = tk.StringVar(root)
variable_cond.set("Good") # Default
tk.OptionMenu(root, variable_cond, "Excellent", "Fair", "Good", "Needs Renovation").pack(padx=20, fill="x", pady=5)


btn_predict = tk.Button(root, text="Predict Price", command=predict_price, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
btn_predict.pack(pady=20)


label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack()

root.mainloop()