import numpy as np
import tkinter as tk
from tkinter import messagebox

# --------------------------
# Functions for operations
# --------------------------
def get_matrix(entries, rows, cols):
    try:
        mat = []
        for i in range(rows):
            row = []
            for j in range(cols):
                val = float(entries[i][j].get())
                row.append(val)
            mat.append(row)
        return np.array(mat)
    except:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")
        return None

def create_entries(frame, rows, cols):
    entries = []
    for i in range(rows):
        row_entries = []
        for j in range(cols):
            e = tk.Entry(frame, width=5)
            e.grid(row=i, column=j, padx=2, pady=2)
            row_entries.append(e)
        entries.append(row_entries)
    return entries

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# --------------------------
# Matrix Operation Functions
# --------------------------
def addition():
    clear_frame(result_frame)
    rows = int(rows_var.get())
    cols = int(cols_var.get())
    A = get_matrix(entries_A, rows, cols)
    B = get_matrix(entries_B, rows, cols)
    if A is not None and B is not None:
        result = A + B
        display_result(result)

def subtraction():
    clear_frame(result_frame)
    rows = int(rows_var.get())
    cols = int(cols_var.get())
    A = get_matrix(entries_A, rows, cols)
    B = get_matrix(entries_B, rows, cols)
    if A is not None and B is not None:
        result = A - B
        display_result(result)

def multiplication():
    clear_frame(result_frame)
    rows_A = int(rows_var.get())
    cols_A = int(cols_var.get())
    rows_B = int(rows_var_B.get())
    cols_B = int(cols_var_B.get())
    A = get_matrix(entries_A, rows_A, cols_A)
    B = get_matrix(entries_B, rows_B, cols_B)
    if A is not None and B is not None:
        if cols_A != rows_B:
            messagebox.showerror("Error", "Columns of A must equal rows of B")
            return
        result = np.dot(A, B)
        display_result(result)

def transpose(matrix_entries, frame, rows, cols):
    clear_frame(result_frame)
    M = get_matrix(matrix_entries, rows, cols)
    if M is not None:
        result = M.T
        display_result(result)

def determinant(matrix_entries, frame, rows, cols):
    clear_frame(result_frame)
    M = get_matrix(matrix_entries, rows, cols)
    if M is not None:
        if M.shape[0] != M.shape[1]:
            messagebox.showerror("Error", "Determinant can only be calculated for square matrices")
            return
        result = np.linalg.det(M)
        lbl = tk.Label(result_frame, text=f"Determinant: {result}", font=("Arial", 14))
        lbl.pack()

def display_result(result):
    for i in range(result.shape[0]):
        row_frame = tk.Frame(result_frame)
        row_frame.pack()
        for j in range(result.shape[1]):
            lbl = tk.Label(row_frame, text=str(round(result[i,j],2)), width=5, borderwidth=1, relief="solid")
            lbl.pack(side="left", padx=2, pady=2)

# --------------------------
# GUI Setup
# --------------------------
root = tk.Tk()
root.title("Matrix Operations Tool")

# Variables for size
rows_var = tk.StringVar(value="2")
cols_var = tk.StringVar(value="2")
rows_var_B = tk.StringVar(value="2")
cols_var_B = tk.StringVar(value="2")

# Frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

matrixA_frame = tk.LabelFrame(input_frame, text="Matrix A")
matrixA_frame.grid(row=0, column=0, padx=10)
matrixB_frame = tk.LabelFrame(input_frame, text="Matrix B")
matrixB_frame.grid(row=0, column=1, padx=10)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Size input
size_frame = tk.Frame(root)
size_frame.pack(pady=5)
tk.Label(size_frame, text="Rows A:").grid(row=0,column=0)
tk.Entry(size_frame, textvariable=rows_var, width=3).grid(row=0,column=1)
tk.Label(size_frame, text="Cols A:").grid(row=0,column=2)
tk.Entry(size_frame, textvariable=cols_var, width=3).grid(row=0,column=3)

tk.Label(size_frame, text="Rows B:").grid(row=0,column=4)
tk.Entry(size_frame, textvariable=rows_var_B, width=3).grid(row=0,column=5)
tk.Label(size_frame, text="Cols B:").grid(row=0,column=6)
tk.Entry(size_frame, textvariable=cols_var_B, width=3).grid(row=0,column=7)

# Create initial entries
entries_A = create_entries(matrixA_frame, int(rows_var.get()), int(cols_var.get()))
entries_B = create_entries(matrixB_frame, int(rows_var_B.get()), int(cols_var_B.get()))

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Addition", command=addition).grid(row=0,column=0,padx=5)
tk.Button(button_frame, text="Subtraction", command=subtraction).grid(row=0,column=1,padx=5)
tk.Button(button_frame, text="Multiplication", command=multiplication).grid(row=0,column=2,padx=5)
tk.Button(button_frame, text="Transpose A", command=lambda: transpose(entries_A, result_frame, int(rows_var.get()), int(cols_var.get()))).grid(row=0,column=3,padx=5)
tk.Button(button_frame, text="Transpose B", command=lambda: transpose(entries_B, result_frame, int(rows_var_B.get()), int(cols_var_B.get()))).grid(row=0,column=4,padx=5)
tk.Button(button_frame, text="Determinant A", command=lambda: determinant(entries_A, result_frame, int(rows_var.get()), int(cols_var.get()))).grid(row=1,column=0,padx=5, pady=5)
tk.Button(button_frame, text="Determinant B", command=lambda: determinant(entries_B, result_frame, int(rows_var_B.get()), int(cols_var_B.get()))).grid(row=1,column=1,padx=5, pady=5)
tk.Button(button_frame, text="Exit", command=root.destroy).grid(row=1,column=2,padx=5, pady=5)

root.mainloop()
