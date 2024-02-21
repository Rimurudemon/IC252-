# import important libraries
import tkinter as tk
from tkinter import Canvas, Scrollbar
from PIL import Image, ImageTk
# swapping the value function
def swap(cups,i,j):
    cups[i],cups[j]=cups[j],cups[i]
# total permutation calculating function 
def perm(cups,i,n,ans,k):
    if(i>=n):
        ans.add(tuple(cups))
        return 
    for m in range(i,n):
        if cups[m]==i//k:
            continue
        swap(cups,i,m)
        perm(cups,i+1,n,ans,k)
        swap(cups,i,m)
# function initialising values
def initialiser(n,k):
    cups=[]
    ans=set()
    plates=[]
    for i in range(n):
        cups.append(i//k)
        plates.append(i//k)
    perm(cups,0,n,ans,k)
    return ans,plates
import tkinter as tk
from tkinter import simpledialog
# function to take user input from dailogue box
def get_user_input(str):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring("Input", f"Enter number of {str} :")
    root.destroy()  # Destroy the root window
    return user_input
n=int(get_user_input("saucers"))
k=int(get_user_input("saucers with same color"))
ans,plates=initialiser(n,k)
size=len(ans)
print("Total number of such permutations=",size)
colorarr=["red","orange","blue","pink","brown","purple","yellow","green","cyan","black"]
cupcolors=[]
ans=list(ans)
for i in ans:
    i=list(i)
for i in range(len(ans)):
    arr=[]
    for j in range(len(ans[i])):
        arr.append(colorarr[ans[i][j]])
    cupcolors.append(arr)


def create_side_view_cup(color, canvas, x, y):
    cup_width = 50
    cup_height = 80
    cup_top_width = 60

    # Draw the cup body
    canvas.create_polygon(x, y + cup_height, x, y, x + cup_top_width, y, x + cup_width, y + cup_height,
                          fill=color, outline='black')

    # Draw the handle
    handle_width = 12
    handle_height = 30
    canvas.create_arc(x - handle_width, y, x, y + cup_height,
                      start=0, extent=180, style=tk.ARC, outline='black')
    canvas.create_arc(x - handle_width, y, x, y + cup_height,
                      start=180, extent=180, style=tk.ARC, outline='black')
                      
# creating plate 
def create_plate(color, canvas, x, y):
    plate_width = 56
    plate_height = 10

    # Draw the plate
    canvas.create_rectangle(x, y, x + plate_width, y + plate_height, fill=color, outline='black')
# displaying cups and plates
def display_cups_and_plates(array1, array2):
    root = tk.Tk()
    root.title("Side View Cup and Plate Arrangement")

    max_array_length = len(array2)
    total_width = max_array_length * 80 

    canvas = tk.Canvas(root, width=total_width, height=500000)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    colors=dict()
    for i in range(n//2):
        colors[i]=colorarr[i]
    # ...
    colors = dict()
    for i in range(n):
        colors[i] = colorarr[i % len(colorarr)]

    x_position = 10
    y_position1 = 10
    scrollbar = Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(yscrollcommand=scrollbar.set)
    for i in range (0,len(array1)):
        for num in array1[i]:
            color = colors.get(num, 'white')
            create_side_view_cup(color, canvas, x_position, y_position1)
            x_position += 80 

        x_position = 7  

        for num in array2:
            color = colors.get(num, 'white')
            create_plate(color, canvas, x_position, y_position1+82)
            x_position += 80
        x_position=10
        y_position1+=102
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()
# calling display cups and plates  
display_cups_and_plates(ans,plates)