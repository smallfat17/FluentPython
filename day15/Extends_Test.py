#
# class A:
#     def ping(self):
#         print('ping in A')
#
# class B(A):
#     def pong(self):
#         print('pong in B')
#
# class C(A):
#     def pong(self):
#         print('pong in C')
#
# class D(B, C):
#     def ping(self):
#         super().ping()
#         print('ping in D')
#
#     def pingpong(self):
#         self.ping()
#         super().ping()
#         self.pong()
#         super().pong()
#         C.pong(self)


class Root:
    def draw(self, cls=None):
        # the delegation chain stops here
        assert not hasattr(super(), 'draw')
        print('mysuper',super())
        # pass

class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting shape to:', self.shapename)
        super().draw()
        #Root.draw(self)

class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)
    def draw(self):
        print('Drawing.  Setting color to:', self.color)
        super().draw()
        #Shape.draw(self)

class Moveable:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print('Drawing at position:', self.x, self.y)

class MoveableAdapter(Root):
    def __init__(self, x, y, **kwds):
        self.movable = Moveable(x, y)
        super().__init__(**kwds)

    def draw(self):
        self.movable.draw()
        print(super())
        print(MoveableAdapter.__mro__) #(<class '__main__.MoveableAdapter'>, <class '__main__.Root'>, <class 'object'>)
        super().draw()


class MovableColoredShape(ColoredShape, MoveableAdapter):
    pass



if __name__ == '__main__':
    # d = D()
    # d.ping()
    # # d.pong()
    # # C.pong(d)
    # d.pong()
    # d.pingpong()
    # cs = ColoredShape(color='blue', shapename='square')
    # cs.draw()
    MovableColoredShape(color='red', shapename='triangle',
                    x=10, y=20).draw()
    print(MovableColoredShape.__mro__)

    #super()根据MRO的顺序查找方法

