# Travelling Salesman Problem

**Greedy algorithm**
makes the best choice in each step pretending that it will be the best solution globally.

This **won´t** solve completely the problem, but it **will** provide a way better solution than just randomize the points as we will see.

# How it works
It uses **turtle** module to draw the points and draw the paths.

The function **fill_Places(number)** fill the places array with random points (user inputs the number). After that function **draw_Points()** is called and draw all the random points on the screen.

After that **draw_path()** is called to draw an alleatory path, without using any algorithm.

When the drawing is done, function **proximity_Algo()** is called to make the magic:

```python
for i in range(1,len(places)-1):
        for d in range(i,len(places)-1):
        total_iterations += 1
             if get_distance(places[d],places[i-1]) < get_distance(places[i],places[i-1]):
                places[i], places[d] = places[d], places[i]
```

> **Note:** The path will ever start and begin at the same point! And the path will ever begin with the first element of the array, which has an immutable position, the same for the last element.

It starts comparing the second element of the array (index = 1) **and** and every element beyond it (index > i, defined in "d" loop) to the previous one. Than it follows the same logic until the element at the position **len(places)-1** (remeber that the last element is immutable because it is the return of the path).


# Results

|                |Randomize Points               |Solution Provided            |
|----------------|-------------------------------|-----------------------------|
|50 points       |dist:22750                     |dist:7683 -it: 1176          |
|300 points      |dist:157941                    |dist:15948 -it: 44551        |
|1000 points     |dist:499865                    |dist:29293 -it: 498501       |
|5000 points     |dist:2595147                   |dist:64640 -it: 12492501     |
|10000 points    |dist:5234931                   |dist:89350 -it: 49985001     |

> **Note:** The distance will change every time because the points are generated randomly.

> **Note:**
**dist:distance**
**it:iterations**
