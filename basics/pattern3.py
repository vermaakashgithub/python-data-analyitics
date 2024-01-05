from turtle import*
bgcolor('black')
speed('fastest')
colors=['red','purple','blue','green','orange','yellow','black','pink',]
for x in range(180):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
mainloop()