import pygame
import sys
from tkinter import simpledialog
import tkinter as tk

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

# Convert the integers in plates to color names
plates = [colorarr[i] for i in plates]

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
CUP_WIDTH, CUP_HEIGHT = 20, 40
PLATE_WIDTH, PLATE_HEIGHT = 24, 5
MARGIN = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define the colors
colors = {
    "red": (255, 0, 0),
    "orange": (255, 165, 0),
    "blue": (0, 0, 255),
    "pink": (255, 192, 203),
    "brown": (165, 42, 42),
    "purple": (128, 0, 128),
    "yellow": (255, 255, 0),
    "green": (0, 128, 0),
    "cyan": (0, 255, 255),
    "black": (0, 0, 0)
}

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the cups and plates
    for i, cups in enumerate(cupcolors):
        for j, cup in enumerate(cups):
            pygame.draw.rect(screen, colors[cup], pygame.Rect(j * (CUP_WIDTH + MARGIN), i * (CUP_HEIGHT + PLATE_HEIGHT + MARGIN), CUP_WIDTH, CUP_HEIGHT))
            pygame.draw.rect(screen, colors[plates[j]], pygame.Rect(j * (PLATE_WIDTH + MARGIN), i * (CUP_HEIGHT + PLATE_HEIGHT + MARGIN) + CUP_HEIGHT, PLATE_WIDTH, PLATE_HEIGHT))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()