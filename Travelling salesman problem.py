#salesman problem
#Gabriel Rocco

import turtle
import math as m
import random


tl = turtle.Turtle()
screen = turtle.Screen()
points = turtle.Turtle()

screen.setworldcoordinates(0,0,1000,1000)


tl.begin_fill()
points.speed(0)
tl.speed(3)


tl.fillcolor('')




places = []
#Fill the array with random numbers
def fill_Places(number):
    for i in range(0,number):
        cordenada = []
        cordenada.append(random.randint(0, 999))
        cordenada.append(random.randint(0, 999))
        places.append(cordenada)
    places[len(places)-1] = places[0]
   


#Draw points before begin
def draw_Points():
    points.begin_fill
    for i in range(1,len(places)):
        points.penup()
        points.goto(places[i][0],places[i][1])
        points.pendown()
        points.dot(5,'blue')
        points.end_fill
    

#Helps to compare distances
def get_distance(p1,p2):
    return m.sqrt( abs((pow(p1[0]-p2[0],2)) + (pow(p1[1]-p2[1],2))))



    

#greedy algorithm
def proximity_Algo():
    total_iterations = 0
    
    temp_index = 0
    menor_d_temp = get_distance(places[0],places[1])
    
    
    for i in range(1,len(places)-1):
        for d in range(i,len(places)-1):
             total_iterations += 1
             if get_distance(places[d],places[i-1]) < get_distance(places[i],places[i-1]):
                places[i], places[d] = places[d], places[i]
     
   
    print("Iterations: ", total_iterations)
  
    
    
    

#Draw any path
distancia = 0
def draw_path():
    tl.penup()
    tl.goto(places[0][0], places[0][1])
    tl.pendown() 
    global distancia 
    distancia = 0
    tl.clear()
    for i in range(1,len(places)):
       tl.goto(places[i][0],places[i][1])
       distancia += m.sqrt((pow(places[i][0]-places[i-1][0],2)) + (pow(places[i][1]-places[i-1][1],2))    )
    print("Distance: ", int(distancia))
   
    







#Handles output and function call
x = input("Input the number of random points to be generated: ")   
fill_Places(int(x)) 
print("Drawing the points now!")
draw_Points() 
print("Drawing the path without any algo, just random choices")       
draw_path()  
dist_base = distancia
print("Running greedy algorithm")    
proximity_Algo()
print("Redrawing the path using results")
tl.speed(3)
draw_path()
print("Now the path is ", dist_base/distancia, " faster")   
    


   


    




tl.end_fill()




