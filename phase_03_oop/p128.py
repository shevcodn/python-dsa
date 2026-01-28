class Shape:                                                                                                                          
    def __init__(self, color):                                                                                                        
        self.color = color                                                                                                            
                                                                                                                                        
    def area(self):                                                                                                                   
        return 0                                                                                                                      
                                                                                                                                        
class Rectangle(Shape):                                                                                                               
    def __init__(self, color, width, height):                                                                                         
        self.color = color                                                                                                            
        self.width = width                                                                                                            
        self.height = height                                                                                                          
                                                                                                                                        
    def area(self):                                                                                                                   
        return self.width * self.height                                                                                               
                                                                                                                                        
class Circle(Shape):                                                                                                                  
    def __init__(self, color, radius):                                                                                                
        self.color = color                                                                                                            
        self.radius = radius                                                                                                          
                                                                                                                                        
    def area(self):                                                                                                                   
        return 3.14 * self.radius * self.radius                                                                                       
                                                                                                                                        
                                                                                                                                        
rect = Rectangle("red", 5, 3)                                                                                                         
circ = Circle("blue", 4)                                                                                                              
                                                                                                                                        
print(rect.color)                                                                                                                     
print(rect.area())                                                                                                                    
print(circ.area())        
