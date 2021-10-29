import tkinter

root = tkinter.Tk()
root.title("Josiah BMI Calculator V2")
root.iconbitmap(r'C:\Users\Dessalegn\Downloads\icon for BMI calculator.ico')

def calculate_bmi():
    kg = float(entry_kg.get())
    height = float(entry_height.get())
    bmi = round(kg / (height ** 2), 2)
    label_result['text'] = f"BMI: {bmi}"

    if bmi > 30:
        label_kg = tkinter.Label(root, text="your obese LOL")
        label_kg.pack()
        label_kg.clear()
        label_kg.pack()

    if bmi > 25:
        label_kg = tkinter.Label(root, text="your overweight")
        label_kg.pack()
        label_kg.clear()
        label_kg.pack()

    if bmi > 18:
        label_kg = tkinter.Label(root, text="your normal weight")
        label_kg.pack()
        label_kg.clear()
        label_kg.pack()

    if bmi < 18:
        label_kg = tkinter.Label(root, text="your underweight")
        label_kg.pack()
        label_kg.pack()


label_kg = tkinter.Label(root, text="KG: ")
label_kg.pack()


entry_kg = tkinter.Entry(root)
entry_kg.pack()

label_height = tkinter.Label(root, text="Height:" )
label_height.pack()

entry_height = tkinter.Entry(root)
entry_height.pack()

button_calculate = tkinter.Button(root, text='Calculate', command=calculate_bmi)
button_calculate.pack()

label_result = tkinter.Label(root, text="BMI: ")
label_result.pack()

root.mainloop()

root.quit()