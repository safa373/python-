
from rectangle import rectangle as rectangle_area
from circle import circle as circle_area
from three_d import cube as cube_volume
from three_d import sphere as sphere_volume

def main():

    rect_length = 5
    rect_width = 3
    print(f"Area of rectangle: {rectangle_area(rect_length, rect_width)}")


    circ_radius = 7
    print(f"Area of circle: {circle_area(circ_radius)}")


    cube_side = 4
    print(f"Volume of cube: {cube_volume(cube_side)}")


    sphere_radius = 6
    print(f"Volume of sphere: {sphere_volume(sphere_radius)}")

if __name__ == "__main__":
    main()
