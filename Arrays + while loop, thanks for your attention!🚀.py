Carcolor=[0,1,2,3,4,5,6]
Carcolor[0]="Green"
Carcolor[1]="Black"
print("I want to repaint my car:",Carcolor[0],sep="")
print("Right now my car is",Carcolor[1], "in color")
print("The cars come in different colors such as:",Carcolor[0],sep="",)
print("What color car do I have now?")
ColorNow = True
while ColorNow:
    if input("Enter:") == "Black":
        ColorNow=False
        print("You entered it correctly, bro)")
