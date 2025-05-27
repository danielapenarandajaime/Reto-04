import math
class Point:    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def compute_distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
    def __str__(self):
        return f"({self.x}, {self.y})"
        

class Line:
    lenght: float
    slope: float

    def __init__(self, start: Point, end: Point): 
        self.start = start
        self.end = end

    def compute_length(self) -> float:
        self.lenght = self.start.compute_distance(self.end)
        return self.lenght
    
    def compute_slope(self) -> float:
        self.slope = (self.start.y - self.end.y) / (self.start.x - self.end.x)
        return self.slope

    def compute_horizontal_cross(self) -> bool:
        if self.start.y>0 and self.end.y<0:
            return True
        elif self.start.y<0 and self.end.y>0:
            return True
        else: return False
    
    def compute_vertical_cross(self) -> bool:
        if self.start.x>0 and self.end.x<0:
            return True
        elif self.start.x<0 and self.end.x>0:
            return True
        else: return False


class Shape:
    _is_regular: bool
    
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        self._vertices = vertices 
        
        if edges is None:
            # Generar automáticamente los edges
            self._edges = []
            for i in range(len(vertices)):
                start = vertices[i]
                end = vertices[(i+1) % len(vertices)]
                self._edges.append(Line(start, end))
        else:
            self._edges = edges
            
    def get_vertices(self):
        return self._vertices
    
    def get_edges(self):
        return self._edges
    
    def get_inner_angles(self):
        return self._inner_angles
    
    def get_is_bool(self):
        return self._is_regular

    def set_vertices(self, new_vertices):
        if new_vertices:
            self._vertices = new_vertices
    
    def set_edges(self, new_edges):
        if new_edges:
            self._edges = new_edges

    def set_inner_angles(self, new_inner_angles):
        if new_inner_angles:
            self._inner_angles = new_inner_angles    


class Rectangle(Shape):
    _is_regular = False
    
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)  
        
        self.line1 = self._edges[0]
        self.line2 = self._edges[1]
        self.line3 = self._edges[2]
        self.line4 = self._edges[3]
        
        len1 = self.line1.compute_length()
        len2 = self.line2.compute_length()
        len3 = self.line3.compute_length()
        len4 = self.line4.compute_length()
        
        if not (math.isclose(len1, len3) and math.isclose(len2, len4)):
            raise ValueError("Los lados opuestos deben ser iguales en un rectángulo")
            
        self.width = min(len1, len2)
        self.height = max(len1, len2)
        
        x_coords = [p.x for p in self._vertices]
        y_coords = [p.y for p in self._vertices]
        self.center = Point(sum(x_coords)/4, sum(y_coords)/4)

    def compute_area(self):
        return (self.width * self.height)
    
    def compute_perimeter(self):
        return (2*self.width +  2* self.height)
    
    def compute_interference_point(self, point: "Point"):

        x_derecha = self.center.x + (self.width/2)
        x_izquierda = self.center.x - (self.width/2)
        y_arriba = self.center.y + (self.height/2)
        y_abajo = self.center.x - (self.height/2)

        if point.x<x_derecha and point.x>x_izquierda and point.y<y_arriba and point.y>y_abajo:
                return "The point is inside the rectangle."
        else: return "The point is outside the rectangle."

    def compute_inner_angles(self):
        return [90, 90, 90, 90]

    

class Square(Rectangle):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        super().__init__(vertices, edges)
        
        lengths = [edge.compute_length() for edge in self._edges]
        if not all(math.isclose(l, lengths[0]) for l in lengths):
            raise ValueError("A square must have all the sides of the same size.")
            
        self._is_regular = True


class Triangle(Shape):
    def __init__(self, vertices: list[Point], edges: list[Line] = None):
        if len(vertices) != 3:
            raise ValueError("Un triángulo debe tener exactamente 3 vértices")
            
        super().__init__(vertices, edges)

        self.line1 = self._edges[0]
        self.line2 = self._edges[1]
        self.line3 = self._edges[2]
        
        self.len1 = self.line1.compute_length()
        self.len2 = self.line2.compute_length()
        self.len3 = self.line3.compute_length()
        
        self._is_regular = math.isclose(self.len1, self.len2) and math.isclose(self.len2, self.len3)
        self._inner_angles = self.compute_inner_angles()
    def compute_inner_angles(self):

        angleA = math.degrees(math.acos((self.len3 ** 2 + self.len1 ** 2 - self.len2 ** 2)/(2 * self.len3 * self.len1)))
        angleB = math.degrees(math.acos((self.len2 ** 2 + self.len1 ** 2 - self.len3 ** 2)/(2 * self.len2 * self.len1)))
        angleC = 180 - angleA - angleB
        
        return [angleA, angleB, angleC]
    
    def compute_area(self):
        # Fórmula de Herón
        s = (self.len1 + self.len2 + self.len3) / 2
        return math.sqrt(s * (s - self.len1) * (s - self.len2) * (s - self.len3))
    
    def compute_perimeter(self):
        return self.len2 + self.len1 + self.len3

class Isosceles(Triangle):

    def __init__(self, vertices: list[Point], edges: list[Line] = None):

        super().__init__(vertices, edges)

        lengths = [edge.compute_length() for edge in self._edges]
        if lengths[0] != lengths[1] and lengths[1] != lengths[2] and lengths[2] != lengths[0]:
            raise ValueError("A isosceles must have two sides of the same size.")


class Equilateral(Triangle):

    def __init__(self, vertices: list[Point], edges: list[Line] = None):

        super().__init__(vertices, edges)
        lengths = [edge.compute_length() for edge in self._edges]
        if lengths[0] != lengths[1] or lengths[1] != lengths[2] or lengths[2] != lengths[0]:
            raise ValueError("A equilatetral must have all its sides of the same size.")


class Scalene(Triangle):

    def __init__(self, vertices: list[Point], edges: list[Line] = None):

        super().__init__(vertices, edges)
        lengths = [edge.compute_length() for edge in self._edges]
        if lengths[0] == lengths[1] or lengths[1] == lengths[2] or lengths[2] == lengths[0]:
            raise ValueError("A scalene must have all its sides of diferent sizes.")
        

class TriRectangle(Triangle):

    def __init__(self, vertices: list[Point], edges: list[Line] = None):

        super().__init__(vertices, edges)

        self.angulos: list[float] = self.compute_inner_angles()

        if self.angulos[0] != 90 and self.angulos[1] != 90 and self.angulos[2] != 90:
            raise ValueError("A trirectangle must have one angle of 90 degrees.")
        

if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 2)
    p4 = Point(0, 2)

    rect = Rectangle([p1, p2, p3, p4])
    print("Área del rectángulo:", rect.compute_area())  # 8 
    print("Perímetro del rectángulo:", rect.compute_perimeter())  # 12 
    print("Ángulos internos:", rect.compute_inner_angles())  

    p_test1 = Point(2, 1)
    p_test2 = Point(5, 3)
    print(rect.compute_interference_point(p_test1))  # Inside
    print(rect.compute_interference_point(p_test2))  # Outside

    p10 = Point(0, 0)
    p20 = Point(2, 0)
    p30 = Point(2, 2)
    p40 = Point(0, 2)

    square = Square([p10, p20, p30, p40], None)
    print("Área del cuadrado:", square.compute_area())  # 4
    print("Perímetro del cuadrado:", square.compute_perimeter())  # 8

    p11 = Point(0, 0)
    p21 = Point(3, 0)
    p31 = Point(1.5, 2.6)

    triangle = Triangle([p11, p21, p31], None)
    print("Área del triángulo:", triangle.compute_area())
    print("Perímetro del triángulo:", triangle.compute_perimeter())
    print("Ángulos internos:", triangle.compute_inner_angles())

    p12 = Point(0, 0)
    p22 = Point(2, 0)
    p32 = Point(1, 2)

    isosceles = Isosceles([p12, p22, p32], None)
    print("Es isósceles válido?", isosceles._is_regular)  # False 

    p13 = Point(0, 0)
    p23 = Point(2, 0)
    p33 = Point(1, math.sqrt(3))

    equilateral = Equilateral([p13, p23, p33], None)
    print("Es equilátero válido?", equilateral._is_regular)  # True

    p14 = Point(0, 0)
    p24 = Point(3, 0)
    p34 = Point(1, 2)

    scalene = Scalene([p14, p24, p34], None)
    print("Es escaleno válido?", scalene._is_regular)  # True

    p15 = Point(0, 0)
    p25 = Point(3, 0)
    p35 = Point(0, 4)

    tri_rect = TriRectangle([p15, p25, p35], None)
    print("Área del triángulo rectángulo:", tri_rect.compute_area())  # 6 
    print("Es triángulo rectángulo válido?", 90 in tri_rect.compute_inner_angles())  # True


