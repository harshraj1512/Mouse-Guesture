from tkinter import *


b1 = "up"
xold, yold = None, None
display_width = '500'
display_height = '500'
canvas_width = '500'
canvas_height = '500'
def main():
    root = Tk()
    root.geometry((display_width+"x"+display_height))


    drawing_area = Canvas(root,width=canvas_width,height=canvas_height,bg="white")
    drawing_area.bind("<Motion>", motion)
    drawing_area.bind("<ButtonPress-1>", b1down)
    drawing_area.bind("<ButtonRelease-1>", b1up)
    drawing_area.pack(side=RIGHT)
    root.mainloop()

def b1down(event):
    global b1
    x1, y1 = ( event.x - 4 ), ( event.y - 4 )
    x2, y2 = ( event.x + 4 ), ( event.y + 4 )
    event.widget.create_oval( x1, y1, x2, y2, fill = "black" )
    b1 = "down"           # you only want to draw when the button is down
                          # because "Motion" events happen -all the time-

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x + 4 ), ( event.y + 4 )
        event.widget.create_oval( x1, y1, x2, y2, fill = "black" )
        if xold is not None and yold is not None:
            python_green = "#476042"
            x1, y1 = ( event.x - 4 ), ( event.y - 4 )
            x2, y2 = ( event.x + 4 ), ( event.y + 4 )
            event.widget.create_oval( x1, y1, x2, y2, fill = "black" )
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE,width=9)
    # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y

if __name__ == "__main__":
    main()