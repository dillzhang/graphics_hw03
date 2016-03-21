from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    filer = open(fname, 'r')
    data = filer.read()
    filer.close()
    lines = data.split("\n")
    counter = 0
    while counter < len(lines):
        print lines[counter]
        if lines[counter] == "line":
            counter += 1
            parameters = lines[counter].split(" ")
            add_edge(points, int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3]), int(parameters[4]), int(parameters[5]))
        elif lines[counter] == "circle" or lines[counter] == "c":
            counter += 1
            parameters = lines[counter].split(" ")
            add_circle(points, int(parameters[0]), int(parameters[1]), 0, int(parameters[2]), 64)
        elif lines[counter] == "hermite" or lines[counter] == "h":
            counter += 1
            parameters = lines[counter].split(" ")
            add_curve(points, int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3]), int(parameters[4]), int(parameters[5]), int(parameters[6]), int(parameters[7]), 32, 0)
        elif lines[counter] == "bezier" or lines[counter] == "b":
            counter += 1
            parameters = lines[counter].split(" ")
            add_curve(points, int(parameters[0]), int(parameters[1]), int(parameters[2]), int(parameters[3]), int(parameters[4]), int(parameters[5]), int(parameters[6]), int(parameters[7]), 32, 1)
        elif lines[counter] == "ident":
            ident(transform)
        elif lines[counter] == "scale":
            counter += 1
            parameters = lines[counter].split(" ")
            matrix_mult(make_scale(float(parameters[0]), float(parameters[1]), float(parameters[2])), transform)
        elif lines[counter] == "translate":
            counter += 1
            parameters = lines[counter].split(" ")
            matrix_mult(make_translate(int(parameters[0]), int(parameters[1]), int(parameters[2])), transform)
        elif lines[counter] == "xrotate":
            counter += 1
            matrix_mult(make_rotX(int(lines[counter])), transform)
        elif lines[counter] == "yrotate":
            counter += 1
            matrix_mult(make_rotY(int(lines[counter])), transform)
        elif lines[counter] == "zrotate":
            counter += 1
            matrix_mult(make_rotZ(int(lines[counter])), transform)
        elif lines[counter] == "apply":
            matrix_mult(transform, points)
        elif lines[counter] == "display":
            color = [0, 255, 0]
            screen = new_screen()
            draw_lines(points, screen, color)
            display(screen)
        elif lines[counter] == "save":
            counter += 1
            save_extension(screen, lines[counter])
        else:
            print "Invalid command: " + lines[counter]
        counter += 1
