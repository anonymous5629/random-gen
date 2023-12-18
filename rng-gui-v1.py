from random import uniform
import tkinter as tk

def rng():
	amount, upperb, lowerb, decimal, print_to_file = amot.get(), float(upb.get()), float(lowb.get()), deci.get(), ptf.get()
	numlist = []
	for x in range(amount):
		number = round(uniform(lowerb, upperb), decimal)
		numlist.append(number)
	numlst = ("\n".join(map(str, numlist)))
	if print_to_file == True:
		filename = filenm.get()
		with open(filename, "a") as f:
			f.write(numlst)
	print_gui(numlst)

def print_gui(numlst):
	num_label = tk.Label(gui, text=("Numbers:\n"+numlst), font=("arial semibold", 14)).grid(row=9, rowspan=3, column=0, columnspan=2)

gui = tk.Tk()
gui.geometry("700x650")
gui.title("rng-gui-v1")

gui.columnconfigure(0, weight=1)
gui.columnconfigure(1, weight=1)

for x in range(12):
	gui.rowconfigure(x, weight=1)

label = tk.Label(gui, text="Random Number Generator V1\nGUI Version", font=("Arial Black", 19)).grid(row=0, column=0, columnspan=2, sticky="nwes")

upb, lowb, deci, amot, ptf, filenm = tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.IntVar(), tk.BooleanVar(), tk.StringVar()

ub_lable = tk.Label(gui, text="Upper Bound: ", font=("arial semibold", 14)).grid(row=1, column=0, sticky="e")
ub = tk.Entry(gui, textvariable = upb, font=("arial", 13)).grid(row=1, column=1, sticky="w")

lb_lable = tk.Label(gui, text ="Lower Bound: ", font=("arial semibold", 14)).grid(row=2, column=0, sticky="e")
lb = tk.Entry(gui, textvariable = lowb, font=("arial", 13)).grid(row=2, column=1, sticky="w")

dec_lable = tk.Label(gui, text ="Amount of Decimals: ", font=("arial semibold", 14)).grid(row=3, column=0, sticky="e")
dec = tk.Entry(gui, textvariable = deci, font=("arial", 13)).grid(row=3, column=1, sticky="w")

amt_lable = tk.Label(gui, text ="Amount of Numbers: ", font=("arial semibold", 14)).grid(row=4, column=0, sticky="e")
amt = tk.Entry(gui, textvariable = amot, font=("arial", 13)).grid(row=4, column=1, sticky="w")

prttf_lable = tk.Label(gui, text ="Print to File: ", font=("arial semibold", 14)).grid(row=5, column=0, sticky="e")
prttf = tk.Checkbutton(gui, variable=ptf, text=" ").grid(row=5, column=1, sticky="w")

flnm_label = tk.Label(gui, text = "File Name: ", font=("arial semibold", 14)).grid(row=6, column=0, sticky="e")
flnm = tk.Entry(gui, textvariable = filenm, font=("arial", 13)).grid(row=6, column=1, sticky="w")

gen_button = tk.Button(gui, text = "Generate", command=lambda:rng(),  font=("arial bold", 18)).grid(row=7, column=0, columnspan=2, sticky="n")

gui.mainloop()