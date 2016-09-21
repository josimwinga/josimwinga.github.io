import zellegraphics as zg
import time
'''
A graphics class adapted from Zellegraphics
Used for the Artemis Project at Brown University

Created on Jul 4, 2015
Updated Aug 1, 2015

@author: Joanna Simwinga
'''

class Point(zg.Point):
    def __init__(self, x,y):
        zg.Point.__init__(self, x, y)
    
class Rectangle(zg.Rectangle):
    '''Inherited methods from Zellegraphcis Rectangle class:
    
    move(dx,dy) --> None
    getAnchor() --> Point
    '''
    
    def __init__(self, centerPoint, width, height):
        
        x1 = centerPoint.getX() - width/2
        y1 = centerPoint.getY() - height/2
        x2 = centerPoint.getX() + width/2
        y2 = centerPoint.getY() + height/2
        
        p1 = zg.Point(x1,y1)
        p2 = zg.Point(x2,y2)
        
        zg.Rectangle.__init__(self, p1, p2)
        
        self._fill = None
        self._outline = 'black'
        
    #override
    def setFill(self, color):
        zg.Rectangle.setFill(self, color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    #override
    def setOutline(self, color):
        zg.Rectangle.setOutline(self, color)
        self._outline = color
        
    def getOutline(self):
        return self._outline

class Text(zg.Text):
    '''
    Inherited methods from Zellegraphcis Text class:
    
    setText(string) --> None
    getText() --> String
    getAnchor() --> Point
    setFace(family) --> None 
        Changes font
        Possible Values: 'helvetica', 'courier'
                    'times roman', 'arial'
    setSize(point) --> None
        Changes font size 
        Possible Vales: 5-36 points
    setStyle(style) --> None
        Changes font style
        Possible Values: 'normal', 'bold', 
                    'italic', 'bold italic'
    setTextColor(color)/setFill(color) --> None
    '''  
    
    def __init__(self, centerPoint, text):
        zg.Text.__init__(self, centerPoint, text)
        
        self._size = 12
        self._Face = 'times roman'
        self._Style = 'normal'
        self._fill = 'black'
        self._outline = 'black'  
    
    #override
    def setSize(self, size):
        zg.Text.setSize(self, size)
        self._size = size
        
    def getSize(self):
        return self._size
    
    #override
    def setFace(self, family):
        zg.Text.setFace(self, family)
        self._Face = family
        
    def getFace(self):
        return self._Face
    
    #override
    def setStyle(self, style):
        zg.Text.setStyle(self, style)
        self._Style = style
        
    def getStyle(self):
        return self._Style
    
    #override
    def setFill(self, color):
        zg.Text.setFill(self, color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    #override
    def setOutline(self, color):
        zg.Text.setOutline(self, color)
        self._outline = color
        
    def getOutline(self):
        return self._outline
    
class Circle(zg.Circle):
    
    def __init__(self, centerPoint, radius):
        zg.Circle.__init__(self, centerPoint, radius)
        
        self._fill = None
        self._outline = 'black'
    
    #override
    def setFill(self, color):
        zg.Circle.setFill(self, color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    #override
    def setOutline(self, color):
        zg.Circle.setOutline(self, color)
        self._outline = color
        
    def getOutline(self):
        return self._outline 

class Triangle(zg.Polygon):
    
    def __init__(self, p1,p2,p3):
        points = [p1,p2,p3]
        zg.Polygon.__init__(self, points)
        self._fill = None
        self._outline = 'black'
        
    #override
    def setFill(self, color):
        zg.Polygon.setFill(self, color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    #override
    def setOutline(self, color):
        zg.Polygon.setOutline(self, color)
        self._outline = color
        
    def getOutline(self):
        return self._outline

class EquilateralTri(Triangle):
    
    def __init__(self, p1, width):
        
        p2 = zg.Point(p1.getX()+width/2, p1.getY()+ width)
        p3 = zg.Point(p1.getX() - width/2, p1.getY() +width)
        Triangle.__init__(self, p1, p2, p3)
                                   
class Window(zg.GraphWin):
    
    def __init__(self, title, width, height):
        zg.GraphWin.__init__(self, title, width, height, autoflush= True)
                                          

class Image(zg.Image):
    
    def __init__(self, centerPoint, fileName):
        zg.Image.__init__(self, centerPoint, fileName)

class LabeledObject():
    '''base class'''
    def __init__(self, centerPoint, width, height, text):
        
        self._height = height
        self._width = width
        self._centerPoint = centerPoint
        self._text = Text(centerPoint, text)
        self._currentPlacement = 'center'
        
    def undraw(self):
        self._text.setText('')

    def setWidth(self, width):
        self._width = width
    
    
    def getWidth(self):
        return self._width
    
    def setHeight(self, height):
        self._height = height
    
    def getHeight(self):
        return self._height
    
    def setTextSize(self, size):
        self._text.setSize(size)
        
    def setTextPlacement(self, placement):
        if placement == 'center':
            if self._currentPlacement == 'bottom':
                self._text.move(0, self.getHeight()/2)
            elif self._currentPlacement == 'top':
                self._text.move(0, -(self.getHeight()/2)) 
            self._currentPlacement = placement
        
        elif placement == 'top':
            if self._currentPlacement == 'center':
                self._text.move(0, (-(self.getHeight()/2))+ 20)
            elif self._currentPlacement == 'bottom':
                self._text.move(0, (-self.getHeight())+ 20)
            self._currentPlacement = placement    
        
        elif placement == 'bottom':
            if self._currentPlacement == 'center':
                self._text.move(0, self.getHeight()/2 - 10)
            elif self._currentPlacement == 'top':
                self._text.move(0, -(self.getHeight()/2) - 10)
            self._currentPlacement = placement
        
        else:
            raise InvalidInputException("Error: invalid placement\nLegal placement values: 'top', 'bottom', and 'center'")
    
    def setFill(self, color):
        return
    
    def setTextColor(self, color):
        return
    
    def setText(self, text):
        self._text.setText(text)
    
    def draw(self, graphwin):
        return

class LabeledCircle(LabeledObject):
    
    def __init__(self, centerPoint, radius, text):
        width = radius
        height = radius
        LabeledObject.__init__(self, centerPoint, width, height, text)
        
        self._circle = zg.Circle(centerPoint, radius)
        self._text = Text(centerPoint, text)
    
    def undraw(self):
        self._circle.undraw()
        self._text.setText('')
    
    #override
    def setFill(self, color):
        self._circle.setFill(color) 
    
    #override    
    def setTextColor(self, color):
        self._text.setFill(color)  
    
    #override
    def draw(self, graphwin):
        self._circle.draw(graphwin)
        self._text.draw(graphwin)

class LabeledRect(LabeledObject):
    
    def __init__(self, centerPoint, width, height, text):
        LabeledObject.__init__(self, centerPoint, width, height, text)
        
        self._rect = Rectangle(centerPoint, width, height)
        self._text = Text(centerPoint, text)
    
    def undraw(self):
        self._rect.undraw()
        self._text.setText('')
        
    #override
    def setFill(self, color):
        self._rect.setFill(color) 
    
    #override    
    def setTextColor(self, color):
        self._text.setFill(color)  
           
    #override
    def draw(self, graphwin):
        self._rect.draw(graphwin)
        self._text.draw(graphwin)

class LabeledImage():
    
    def __init__(self, centerPoint, img, text):
        
        self._img = zg.Image(centerPoint, img)
        self._text = Text(centerPoint, text)
        self._originalPoint = centerPoint
        self._x = centerPoint.getX()
        self._y = centerPoint.getY()
        self._currentPlacement = 'center'
        
        #text Placement
        self._height = self._img.getPixmap().getHeight()
        self._imgTop = self._height/2 - self._y + 12
        self._imgBottom = self._height/2 +self._y -12
        self._textPlacement = centerPoint
        
    def unDraw(self):
        self._text.setText('')
        self._img.undraw()
    def setTextSize(self, size):
        height = self._img.getHeight()
        self._imgTop = height/2 - self._y + self._text.getSize()
        self._imgBottom = height/2 + self._y - self._text.getSize()
        
    def setTextPlacement(self, placement):

        if placement == 'center':
            if self._currentPlacement == 'bottom':
                self._text.move(0, (self._height/2))
            elif self._currentPlacement == 'top':
                self._text.move(0, -(self._height/2)) 
            self._currentPlacement = 'center'
        
        elif placement == 'top':
            if self._currentPlacement == 'center':
                self._text.move(0, (-self._height/2)+20)
            elif self._currentPlacement == 'bottom':
                self._text.move(0, (-(self._height))+20)
            self._currentPlacement = 'top'    
        
        elif placement == 'bottom':
            if self._currentPlacement == 'center':
                self._text.move(0, self._height/2 -10)
            elif self._currentPlacement == 'top':
                self._text.move(0, -(self._height/2)-10)
            self._currentPlacement = 'bottom'
    
    #override    
    def setTextColor(self, color):
        self._text.setFill(color) 
    
    def draw(self, graphwin):
        self._img.draw(graphwin)
        self._text.draw(graphwin)    

class Button:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, center, width, height, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 
        
        self._center = center
        self._textColor = 'black'
        self._fill = None
        self._center = center
        self._width = width
        self._height = height
        
        #Rect placement
        w,h = width/4.0, height/4.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        
        #text and rect
        self.rect = Rectangle(center, width, height)
        self.label = Text(center, label)
        self.activate()

    def undraw(self):
        self.rect.undraw()
        self.label.setText('')
    
    def clicked(self, p):
        """ RETURNS true if button active and p is inside"""

        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        """RETURNS the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill(self._textColor)
        self.rect.setWidth(2)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = 0
    
    def setLabel(self, label):
        self.label.setText(label)
        
    def setFill(self, color):
        self.rect.setFill(color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    def setTextColor(self, color):
        self.label.setFill(color)
        
    def getTextColor(self):
        return self.label.getFill()
    
    def draw(self, win):
        self.rect.draw(win)
        self.label.draw(win)
    
    def waitForClick(self):
        clicked = False
        while clicked == False:
            clicked = self.clicked(self._win.getMouse())
            return self.getLabel()
        
class CircularButton:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, center, radius, label):
        """ Creates a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """ 
        
        self._center = center
        self._textColor = 'black'
        self._fill = None
        self._radius = radius
        
        #text and rect
        self.circle = Circle(center, radius)
        self.label = Text(center, label)
        self.activate()

    def undraw(self):
        self.circle.undraw()
        self.label.setText('')
        
    def clicked(self, p):
        """ RETURNS true if button active and p is inside"""
        return self.active and \
               self._center.getX() - self._radius <= self._center.getX() <= self._center.getX() + self._radius and \
               self._center.getY() <= p.getY() <= self._center.getY()+self._radius

    def getLabel(self):
        """RETURNS the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill(self._textColor)
        self.circle.setWidth(2)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = 0
    
    def setLabel(self, label):
        self.label.setText(label)
        
    def setFill(self, color):
        self.circle.setFill(color)
        self._fill = color
    
    def getFill(self):
        return self._fill
    
    def setTextColor(self, color):
        self.label.setFill(color)
        
    def getTextColor(self):
        return self.label.getFill()
    
    def draw(self, win):
        self.circle.draw(win)
        self.label.draw(win)
        
    def waitForClick(self):
        clicked = False
        while clicked == False:
            clicked = self.clicked(self._win.getMouse())
            return self.getLabel()
        
class ImageButton:

    """An image button is an image in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, center, fileName, label):
        
        self._center = center
        self._textColor = 'black'
        
        #text and rect
        self.img = Image(center, fileName)
        self.label = Text(center, label)
        self.activate()
        
        pm = self.img.getPixmap()
        w,h = pm.getWidth()/2.0, pm.getHeight()/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h

    def undraw(self):
        self.img.undraw()
        self.label.setText('')
        
    def clicked(self, p):
        """ RETURNS true if button active and p is inside"""
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        """RETURNS the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill(self._textColor)
        self.active = 1

    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('darkgrey')
        self.active = 0
    
    def setLabel(self, label):
        self.label.setText(label)
    
    def setTextColor(self, color):
        self.label.setFill(color)
        
    def getTextColor(self):
        return self.label.getFill()
    
    def draw(self, win):
        self.img.draw(win)
        self.label.draw(win)
        
    def waitForClick(self):
        clicked = False
        while clicked == False:
            clicked = self.clicked(self._win.getMouse())
            return self.getLabel()


class ButtonList():
    def __init__(self, center, numberOfButtons, orientation, width, height,win):
        '''
        auto arrangement is horizontal 
        center is center of first button
        '''
        x = center.getX()
        y = center.getY()

        self._numberOfButtons = numberOfButtons
        self._win = win
        self._reaction = None
        
        labels = [None, None, None, None, None]
        if orientation == 'horizontal':
            self._b1 = Button(center, width, height, labels[0],self._win)
            self._b2 = Button(zg.Point(x+width,y), width, height, labels[1], self._win)
            self._b3 = Button(zg.Point(x+width*2, y), width, height, labels[2], self._win)
            self._b4 = Button(zg.Point(x+width*3, y), width, height, labels[3], self._win)
            self._b5 = Button(zg.Point(x+width*4, y), width, height, labels[4], self._win)  

        elif orientation == 'vertical':
            self._b1 = Button(center, width, height, labels[0], self._win)
            self._b2 = Button(zg.Point(x, y+height), width, height, labels[1], self._win)
            self._b3 = Button(zg.Point(x, y+height*2), width, height, labels[2], self._win)
            self._b4 = Button(zg.Point(x, y+height*3), width, height, labels[3], self._win)
            self._b5 = Button(zg.Point(x, y+height*4), width, height, labels[4], self._win)
    
        self._buttons = [self._b1, self._b2, self._b3, self._b4, self._b5]
    
    def setLabels(self, textList):
        labels = [None, None, None, None, None]
        
        for i in range(len(textList)):
            labels[i] = textList[i]
        
        self._b1.setLabel(labels[0])
        self._b2.setLabel(labels[1])
        self._b3.setLabel(labels[2])
        self._b4.setLabel(labels[3])
        self._b5.setLabel(labels[4])
    
    def setTextColor(self, color):
        self._b1.setTextColor(color)
        self._b2.setTextColor(color)
        self._b3.setTextColor(color)
        self._b4.setTextColor(color)
        self._b5.setTextColor(color)
    
    def setFill(self, color):
        self._b1.setFill(color)
        self._b2.setFill(color)
        self._b3.setFill(color)
        self._b4.setFill(color)
        self._b5.setFill(color)
    
    def draw(self):
        for i in range(0, self._numberOfButtons):
            self._buttons[i].draw(self._win)
    
    def undraw(self):
        for i in range(0, self._numberOfButtons):
            self._buttons[i].undraw(self._win)
    
    def waitForClick(self):
        clicked = False
        while clicked == False:
            if self._b1.clicked(self._win.getMouse()):
                clicked = True
                button = self._b1
            elif self._b2.clicked(self._win.getMouse()):
                clicked = True
                button = self._b2
            elif self._b3.clicked(self._win.getMouse()):
                clicked = True
                button = self._b3
            elif self._b4.clicked(self._win.getMouse()):
                clicked = True
                button = self._b4
            elif self._b5.clicked(self._win.getMouse()):
                clicked = True
                button = self._b5
        return button.getLabel()
            
    def checkClick(self, point):
        if self._b1.clicked(point):
            self._reaction = self._b1.getLabel()
            return True
        elif self._b2.clicked(point):
            self._reaction = self._b2.getLabel()
            return True
        elif self._b3.clicked(point):
            self._reaction = self._b3.getLabel()
            return True
        elif self._b4.clicked(point):
            self._reaction = self._b4.getLabel()
            return True
        elif self._b5.clicked(point):
            self._reaction = self._b5.getLabel()
            return True
        else:
            return False
    
    def getReaction(self):
        return self._reaction

class Timer():

    def __init__(self, centerPoint, width, height, win):
        self._increment = 1
        self._win = win
        self._time = 10
        self._timer = LabeledRect(centerPoint,width, height,'10')
        self._timeUp = False
        self._center = centerPoint
        self._width = width
        self._height = height
        self._fColor = None
        self._tColor = 'black'

    def undraw(self):
        self._timer.undraw()
    
    def draw(self, win):
        self._timer.draw(win)

    def setIncrement(self, i):
        self._increment = i

    def setTime(self, time):
        self._time = time
        self._timer.setText(time)
        
    def start(self):
        self._timeUp = False
        x = self._time
        while x>0:
            x-=1
            self._timer.setText(x)
            time.sleep(1)

        self._timeUp = True

    def setFill(self, color):
        self._fColor = color
        self._timer.setFill(color)

    def setTextColor(self, color):
        self._tColor = color
        self._timer.setTextColor(color)

    def timeOver(self):
        return self._timeUp

    def startButton(self):
        b = Button(Point(self._center.getX(), self._center.getY()+self._height), self._width, self._height/2, 'Start')
        b.setFill(self._fColor)
        b.setTextColor(self._tColor)
        b.draw(self._win)
        clicked = False

        while clicked == False:
            point = self._win.getMouse()
            if b.clicked(point):
                self.start()
                clicked = True

class Entry(zg.Entry):
    def __init__(self, p, width):
        zg.Entry.__init__(self,p,width)
        self._point = p

    def enterButton(self, centerPoint,width, height, label, win):
        b = Button(centerPoint, width, height, label)
        b.draw(win)
        clicked = False
        while clicked == False:
            point = win.getMouse()
            if b.clicked(point):
                clicked = True
        return self.getText()
        
            
class InvalidInputException(Exception): 
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
     
        
