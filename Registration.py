import tkinter as tk

root = tk.Tk()
root.title("Registration")
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
tk.Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0,column=3)

#Field Name
name =tk.Label(root, text="Name")
phone =tk.Label(root, text="Phone")
gender =tk.Label(root, text="Gender")
emergency=tk.Label(root, text="Emergency")
paymentmood =tk.Label(root, text="Payment Mood")

#Packing Field
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#Variable for Storing Data
namevalue =tk.StringVar
phonevalue =tk.StringVar
gendervalue =tk.StringVar
paymentmoodvalue =tk.StringVar
emergencyvalue =tk.StringVar
checkvalue =tk.IntVar

#Creating entry Field
nameentry =tk.Entry(root, textvariable = namevalue)
genderentry=tk.Entry(root, textvariable =gendervalue)
phonerentry=tk.Entry(root, textvariable =phonevalue)
paymentmoodentry=tk.Entry(root, textvariable =paymentmoodvalue)
emergencyentry=tk.Entry(root, textvariable =emergencyvalue)

#Packing entry Field
nameentry.grid(row=1, column=3)
genderentry.grid(row=2, column=3)
phonerentry.grid(row=3, column=3)
paymentmoodentry.grid(row=4, column=3)
emergencyentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn=tk.Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submit button
tk.Button(text="submit", command=getvals).grid(row=7, column=3) 

root.mainloop()

