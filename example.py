import tkinter as tk

root = tk.Tk()
w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=tk.X, pady=10)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill= tk.X, pady=10)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X, pady=10)



 
# Creating master Tkinter window
# master = tk.Tk()
 
# # Creating object of photoimage class
# # Image should be in the same folder
# # in which script is saved
# p1 = tk.PhotoImage(file = 'Images/MP3.jpg')
 
# # Setting icon of master window
# master.iconphoto(False, p1)
 
# # Creating button
# b = tk.Button(master, text = 'Click me !')
# b.pack(side = tk.TOP)
 

tk.mainloop()