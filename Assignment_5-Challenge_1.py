# Challenge 1: Square Numbers and Return Their Sum

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        square_x = self.x ** 2
        square_y = self.y ** 2
        square_z = self.z ** 2
        return square_x + square_y + square_z

x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))
z = int(input("Enter the value for z: "))
point_instance  = Point(x, y, z)

sum_of_squares = point_instance .sqSum()
print(f"The sum of the squares is: {sum_of_squares}")
