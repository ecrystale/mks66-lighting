import math
from display import *


  # IMPORANT NOTE

  # Ambient light is represeneted by a color value

  # Point light sources are 2D arrays of doubles.
  #      - The fist index (LOCATION) represents the vector to the light.
  #      - The second index (COLOR) represents the color.

  # Reflection constants (ka, kd, ks) are represened as arrays of
  # doubles (red, green, blue)

AMBIENT = 0
DIFFUSE = 1
SPECULAR = 2
LOCATION = 0
COLOR = 1
SPECULAR_EXP = 4


#lighting functions
def get_lighting(normal, view, ambient, light, areflect, dreflect, sreflect ):
    color=[0,0,0]
    A=calculate_ambient(ambient,areflect)
    S=calculate_specular(light,sreflect,view,normal)
    D=calculate_diffuse(light,dreflect,normal)
    for i in range(len(color)):
        color[i]=A[i]+S[i]+D[i]
    return limit_color(color)
    #pass

def calculate_ambient(alight, areflect):
    color=[0,0,0]
    for i in range(len(color)):
        color[i]=alight[i]*areflect[i]
#    dot_product(alight, areflect)
    return limit_color(color)


def calculate_diffuse(light, dreflect, normal):
    color=[0,0,0]
    normalize(normal)
    L=light[LOCATION]
    normalize(L)
    for i in range(len(color)):
        color[i]=light[1][i]*dreflect[i]*dot_product(L,normal)
    return limit_color(color)
    #pass


def calculate_specular(light, sreflect, view, normal):
    color=[0,0,0]
    #print(light[LOCATION])
    L=light[0]
    normalize(L)
    #print(light[LOCATION])
    normalize(normal)
    #print(normal)
    #normalize(sreflect)
    #print(sreflect)
    normalize(view)
    #print(view)
    A=[0,0,0]
    for i in range(len(A)):
        A[i]=(2*dot_product(normal,L)*normal[i]-L[i])
    #print(A)
    for i in range(len(color)):
        color[i]=light[1][i]*sreflect[i]*dot_product(A,view) ** SPECULAR_EXP
    return limit_color(color)
    #pass

def limit_color(color):
    for i in range(len(color)):
        c=color[i]
        if c>255:
            color[i]=255
        if c<0:
            color[i]=0
    return color
        
    #pass

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    magnitude = math.sqrt( vector[0] * vector[0] +
                           vector[1] * vector[1] +
                           vector[2] * vector[2])
    for i in range(3):
        vector[i] = vector[i] / magnitude

#Return the dot porduct of a . b
def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):

    A = [0, 0, 0]
    B = [0, 0, 0]
    N = [0, 0, 0]

    A[0] = polygons[i+1][0] - polygons[i][0]
    A[1] = polygons[i+1][1] - polygons[i][1]
    A[2] = polygons[i+1][2] - polygons[i][2]

    B[0] = polygons[i+2][0] - polygons[i][0]
    B[1] = polygons[i+2][1] - polygons[i][1]
    B[2] = polygons[i+2][2] - polygons[i][2]

    N[0] = A[1] * B[2] - A[2] * B[1]
    N[1] = A[2] * B[0] - A[0] * B[2]
    N[2] = A[0] * B[1] - A[1] * B[0]

    return N
