#!/usr/bin/python3


"""define class inheritance from base"""

from models.base import Base


class Rectangle(Base):
    """inherites from class base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """args list
            width
            height
            x
            y
            """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the attribute width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """"gets the attribute height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""

        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the attribute x"""

        return self.__x

    @x.setter
    def x(self, value):
        """gets the value of x"""

        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """gets the attribute y"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the value for y"""

        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """sets the method area"""

        return self.__height * self.__width

    def display(self):
        """define display method to print #"""

        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """used to print in strings"""

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """method for arbituary arguments"""

        n = len(args)
        kw = len(kwargs)
        if args and n != 0:
            count = 0
            for i in args:
                if count == 0:
                    if i is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = i
                elif count == 1:
                    self.width = i
                elif count == 2:
                    self.height = i
                elif count == 3:
                    self.x = i
                elif count == 4:
                    self.y = i
                count += 1

        elif kwargs and kw != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """define method for dictionary"""

        dict = {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
        return dict
