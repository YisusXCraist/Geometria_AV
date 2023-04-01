# Line.py

from Vector import Vector


class Line:
    def __init__(self, point1, point2):
        self.v1 = Vector(point1[0], point1[1], point1[2])
        self.v2 = Vector(point2[0], point2[1], point2[2])

    def direction_vector(self):
        return self.v2 - self.v1

    def point(self, t):
        return self.v1 + self.direction_vector() * t

    def __str__(self):
        return "Line: {} + t{}".format(self.v1, self.direction_vector())
    
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Plot the two points defining the line as a red dot and a blue line connecting them
        ax.scatter(self.v1.x, self.v1.y, self.v1.z, color='red')
        ax.plot([self.v1.x, self.v2.x], [self.v1.y, self.v2.y], [self.v1.z, self.v2.z], color='blue')

        # Compute the direction vector and plot it as a green line starting from the first point
        direction = self.direction_vector()
        ax.plot([self.v1.x, self.v1.x + direction.x], [self.v1.y, self.v1.y + direction.y], [self.v1.z, self.v1.z + direction.z], color='green')

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        plt.show()


