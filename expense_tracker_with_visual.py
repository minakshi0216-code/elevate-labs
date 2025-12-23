import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Button, Label, filedialog, messagebox

def load_expenses():
    global df

    file_path = filedialog.askopenfilename(
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return

    try:
        df = pd.read_csv(file_path)
        total = df["Amount"].sum()
        total_label.config(text=f"Total Expense: ₹{total}")
        messagebox.showinfo("Success", "Expense file loaded successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_bar_chart():
    if df is None:
        messagebox.showwarning("Warning", "Please load expense file first!")
        return

    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="bar", title="Category-wise Expenses")

    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()


def show_pie_chart():
    if df is None:
        messagebox.showwarning("Warning", "Please load expense file first!")
        return

    category_sum = df.groupby("Category")["Amount"].sum()
    category_sum.plot(kind="pie", autopct="%1.1f%%", title="Expense Distribution")

    plt.ylabel("")
    plt.tight_layout()
    plt.show()


# --------- Tkinter GUI ---------
df = None

root = Tk()
root.title("Expense Tracker")
root.geometry("350x300")

Label(root, text="Expense Tracker with Visuals", font=("Arial", 14)).pack(pady=10)

Button(root, text="Load Expense CSV", command=load_expenses).pack(pady=10)
Button(root, text="Show Bar Chart", command=show_bar_chart).pack(pady=10)
Button(root, text="Show Pie Chart", command=show_pie_chart).pack(pady=10)

total_label = Label(root, text="Total Expense: ₹0", font=("Arial", 12))
total_label.pack(pady=20)

root.mainloop()
