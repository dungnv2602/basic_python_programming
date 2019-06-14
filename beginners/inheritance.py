class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Lastname: "+self.last_name+"; Eye Color: "+self.eye_color)

class Child(Parent): #Inherit Parent class
    def __init__(self, last_name, eye_clor, number_of_toys):
        Parent.__init__(self, last_name, eye_clor)
        self.number_of_toys = number_of_toys

    def show_info(self):
        Parent.show_info(self)
        print("Number of Toys: "+str(self.number_of_toys))
