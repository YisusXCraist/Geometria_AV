### Vectores ### 

# Clase Vector
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# Operaciones con vectores
    # Suma
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    # Resta
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    # Producto punto
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)
    # Producto cruz
    def __rmul__(self, scalar):
        return self.__mul__(scalar)

# Funciones
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)
    