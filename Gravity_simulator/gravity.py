import tkinter as tk
from tkinter import HORIZONTAL,CURRENT,END
from matplotlib import pyplot as plt

#Define function and variables
time = 0
data = {}
for i in range(1,5):
    data['data_%d' % i] = []

def move(event):
    #Restricting the movement of only cicles on canvas using gettags
    if "BALL" in canvas.gettags(CURRENT):
        #Store the x1 and x2 coordinate of the circles:
        x1 = canvas.coords(CURRENT)[0]
        x2 = canvas.coords(CURRENT)[2]
        
        canvas.coords(CURRENT,x1,event.y,x2,event.y+10)
        #limiting the movement of each circles
        if canvas.coords(CURRENT)[3] < 15:
            canvas.coords(CURRENT,x1,5,x2,15)
        elif canvas.coords(CURRENT)[3] > 415:
            canvas.coords(CURRENT,x1,405,x2,415)

    update_height()

def update_height():
    for i in range(1,5):
        heights['height_%d' %i].config(text="Height: " + str(round(415 - canvas.coords(circles['circle_%d' %i])[3],2)))

def step(t):
    global time

    #Actual movment of circles
    for i in range(1,5):
        #convert acceleration and velocity in negative first as the height of canvas is from top to bottom
        a = -1*float(accelerations['acceleration_%d' %i].get())
        v = -1*float(velocities['velocity_%d' % i].get())
        d = v*t + .5*a*t**2

        x1 = canvas.coords(circles['circle_%d' % i])[0]
        x2 = canvas.coords(circles['circle_%d' % i])[2]
        #moving the circle one step ahead after checking the movement into the canvas
        if canvas.coords(circles['circle_%d' % i])[3] + d <= 415:           
            canvas.move(circles['circle_%d' % i],0 , d)
            y2 = canvas.coords(circles['circle_%d' % i])[3]           
            canvas.create_line(x1,y2,x2,y2,tags="DASH")
        else:
            canvas.coords(circles['circle_%d' % i],x1,405,x2,415)

        vf = v + a*t
        velocities['velocity_%d' % i].delete(0,END)
        velocities['velocity_%d' % i].insert(0, str(round(-1*vf, 2)))

        data['data_%d' %i].append((time, 415 - canvas.coords(circles['circle_%d' %i])[3]))

    #update height after every loop
    update_height()
    #update time after every loop
    time += t
        
def run():
    #before begin of loof use a step method one time
    step(time_scale.get())

    while 15 < canvas.coords(circles['circle_1'])[3] < 415 or 15 < canvas.coords(circles['circle_2'])[3] < 415 or 15 < canvas.coords(circles['circle_3'])[3] < 415 or 15 < canvas.coords(circles['circle_4'])[3] < 415:
        step(time_scale.get())

def graph():
    #define colors for each line
    colors = ['red','green','blue','yellow']

    for i in range(1,5):
        #creating blank list for x and y axes
        x = []
        y = []
        for data_list in data['data_%d' % i]:
            #adding data to both list
            x.append(data_list[0])
            y.append(data_list[1])
        plt.plot(x, y, color=colors[i-1])

    plt.title('Distance vs time')
    plt.xlabel('time')
    plt.ylabel('distance')
    plt.show()

def reset():
    global time

    time = 0
    canvas.delete("DASH")

    for i in range(1,5):
        velocities['velocity_%d' %i].delete(0,END)
        velocities['velocity_%d' %i].insert(0,'0')
        accelerations['acceleration_%d' %i].delete(0,END)
        accelerations['acceleration_%d' %i].insert(0,'0')
        canvas.coords(circles['circle_%d' %i],45+(i-1)*100,405,55+(i-1)*100,415)

        data['data_%d' %i].clear()

    update_height()
    time_scale.set(1)


     




#Define window
root = tk.Tk()
root.title("Gravity Simulator")
root.iconbitmap("images/earth.ico")
root.geometry("450x650")
root.resizable(0,0)

#Define frames
Canvas_frame = tk.Frame(root)
input_frame = tk.Frame(root)
Canvas_frame.pack()
input_frame.pack(padx=20)

#Define layout
#Define Canvas_Frame
canvas = tk.Canvas(Canvas_frame,width=400,height=415,bg="#ffffff")
canvas.pack(padx=20,pady=20)

#create_shapes
#creating lines on canvas
canvas.create_line(2,0,2,415)
canvas.create_line(100,0,100,415)
canvas.create_line(200,0,200,415)
canvas.create_line(300,0,300,415)
canvas.create_line(400,0,400,415)

#creating circles on canvas
#creating a dictionary to store coordinates of it before creating the circle
circles = {}
circles['circle_1'] = canvas.create_oval(45,405,55,415,fill="#ff0000",tags="BALL")
circles['circle_2'] = canvas.create_oval(145,405,155,415,fill="#00ff00",tags="BALL")
circles['circle_3'] = canvas.create_oval(245,405,255,415,fill="#0000ff",tags="BALL")
circles['circle_4'] = canvas.create_oval(345,405,355,415,fill="#ffff00",tags="BALL")

#Define input_frame
#Define labels
tk.Label(input_frame,text="d").grid(row=0,column=0)
tk.Label(input_frame,text="vi").grid(row=1,column=0)
tk.Label(input_frame,text="a").grid(row=2,column=0)
tk.Label(input_frame,text="t").grid(row=3,column=0)

#creating height labels and storing its value in a dictionary named height
heights = {}
for i in range(1,5):
    heights['height_%d' % i] = tk.Label(input_frame,text="Height: " + str(415 - canvas.coords(circles['circle_%d' %i])[3]))
    heights['height_%d' % i].grid(row=0,column=i)
    

#creating velocity input box and storing its value in dictionary
velocities = {}
for i in range(1,5):
    velocities['velocity_%d' % i] = tk.Entry(input_frame,width=15)
    velocities['velocity_%d' % i].grid(row=1,column=i,padx=1)
    velocities['velocity_%d' % i].insert(0,"0")

#creating acceleration input box and storing its value in dictionary
accelerations = {}
for i in range(1,5):
    accelerations['acceleration_%d' % i] = tk.Entry(input_frame,width=15)
    accelerations['acceleration_%d' % i].grid(row=2,column=i,padx=1)
    accelerations['acceleration_%d' % i].insert(0,"0")

#creating a scale for time interval

time_scale = tk.Scale(input_frame,from_=0,to=1,tickinterval=.1,resolution=.01,orient=HORIZONTAL)
time_scale.grid(row=3,column=1,columnspan=4,sticky="WE")

#Create buttons
step_button = tk.Button(input_frame,text="Step",command=lambda: step(time_scale.get()))
run_button = tk.Button(input_frame,text="Run",command=run)
graph_button = tk.Button(input_frame,text="Graph",command=graph)
reset_button = tk.Button(input_frame,text="Reset",command=reset)
quit_button = tk.Button(input_frame,text="Quit",command=root.destroy)

step_button.grid(row=4,column=1,padx=1,sticky="WE")
run_button.grid(row=4,column=2,padx=1,sticky="WE")
graph_button.grid(row=4,column=3,padx=1,sticky="WE")
reset_button.grid(row=4,column=4,padx=1,sticky="WE")
quit_button.grid(row=5,column=1,columnspan=4,sticky="WE")


root.bind("<B1-Motion>",move)

root.mainloop()
#Run mainloop
