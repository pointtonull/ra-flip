#!/usr/bin/env python

from PyQt4 import QtCore, QtGui, QtSvg
from Ui_field import Ui_Form
from decoradores import Verbose
from functools import wraps
import icons_rc
import random
import sys

VERBOSE = 2
DELAY = 100
EXAMPLES = {

    "walls": "\n".join((
        r"      \  ",
        r"  |   /  ",
    )),

    "sluices": "\n".join((
        r"  >  v2 ",
        r" 5      ",
        r" 4^  <3 ",
    )),

    "generators": "\n".join((
        r"  2          4     ",
    )),

    "tarpits": "\n".join((
        r" > 2 + *  ",
    )),

    "unary": "\n".join((
        r" ' ' , ' ~ ",
    )),

    "arith_with_output": "\n".join((
        r" > 2 + *  p   ",
    )),

    "ascii_output": "\n".join((
        r" > 8 * P ",
    )),

    "terminate": "\n".join((
        r"   Q   ",
    )),

    "grille1": "\n".join((
        r"  2  #  p ",
    )),

    "grille2": "\n".join((
        r"     #  p ",
    )),

    "processor": "\n".join((
        r" 3   \  p   ",
        r"   / X  +   ",
        r"   \    X   ",
        r"   Q    /   ",
    )),

    "modifier": "\n".join((
        r" \   p  ",
        r" > 1 /  ",
        r"     .% ",
        r"     p  ",
    )),
        
    "modified_flippers": "\n".join((
        r"  \   \   \     \ ",
        r"   @   @   @      ",
        r"  2   3   4       ",
        r"p +   +   /     Q ",
    )),
                             
    "modified_sluices": "\n".join((
        r'  > 5  \   p ',
        r'   @      ~ @',
        r'       >   <1',
        r'          ~  ',
        r'  > 4  /   \ ',
        r'   @         ',
        r'  \         Q',
    )),
  
    "modified_sluices2": "\n".join((
        r"     @v",
        r"      ^",
    )),

    "modified_processor": "\n".join((
        r" >  \    p    /         \ ",
        r" '      ~ @               ",
        r" \  X    X                ",
        r"        ~\    >         / ",
    )),

    "primes": "\n".join((
        r" >3   >2p #./, #p                 *** PRIMEZ ***  ",
        r"  @  @p    0'- /\                                 ",
        r" \  5   >              	\                       ",
        r"  @     \X ~^	                      , .\          ",
        r"         \                                    \   ",
        r"         /                                    /   ",
        r"         /1 *       / 0     <                \    ",
        r" .      @2@                  @                    ",
        r"    / .  ^        / v                             ",
        r" v \      @       \ +   X\                        ",
        r"   */   - @                                       ",
        r"         X       +      ~ \                       ",
        r" '      -                 *<X\                    ",
        r" '          ^    X  ^     X  /                    ",
        r" '      @.@        @                              ",
        r"         \0 ^                                     ",
        r"         '  \  /\X  /     \   \                   ",
        r"   \     <,                   /                   ",
        r" \   >     > 0                      \		       	",
        r"            @		  /		       \                ",
        r"           \              v         v       0\    ",
        r"                                       @ 0  @ @	",
        r"	       	       /      +	       	X     	       	",
        r"       	       	             @ 	         +      ",
        r"       	       	     #.X +  0 <	~ \  	     	",
        r"                       \ /     	  X +  	   X   /",
        r"   	 	       	       	  \ ^.#	                ",
        r"		                     @    @#+               ",
        r"                          \             >  /      ",
        r"                                          @\ /    ",
    )),

    "fibonacci": "\n".join((
        r" r\   /     > <  ",
        r" /X   X  \  Q-p@ ",
        r" \'  >  \        ",
        r"     ^+ X/       ",
     )),
}



class s32int(int):
    @wraps(int.__new__)
    def __new__(cls, value):
        """
        >>> s32int(2 ** 31)
        0
        >>> s32int(2 ** 31 + 10)
        -10
        >>> s32int(-5)
        -5
        >>> s32int(-(2 ** 31 - 5))
        -2147483643
        """
        abs_value = value & (2 ** 31 - 1)
        if value & (2 ** 31):
            return int.__new__(cls, -abs_value)
        else:
            return int.__new__(cls, abs_value)

    @wraps(int.__add__)
    def __add__(self, y):
        """
        >>> s32int(2 ** 31 - 1) + 1
        0
        >>> s32int(2 ** 31 - 1) + 2
        -1
        >>> s32int(2 ** 31) - 1
        -1
        """
        return s32int(int.__add__(self, y))

    @wraps(int.__mul__)
    def __mul__(self, y):
        """
        >>> s32int(3) * 2 ** 29
        1610612736
        >>> s32int(3) * 2 ** 30
        -1073741824
        >>> s32int(10) * (-1)
        -10
        """
        return s32int(int.__mul__(self, y))

    @wraps(int.__mod__)
    def __mod__(self, y):
        return s32int(int.__mod__(self, y))

    @wraps(int.__neg__)
    def __neg__(self):
        return s32int(int.__neg__(self))


class FieldWidget(QtGui.QWidget):
    @Verbose(VERBOSE)
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        # Set up the UI from designer
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ex_name = random.choice(EXAMPLES.keys())
        ex_code = EXAMPLES[ex_name]
        self.setWindowTitle("ra-flip: %s" % ex_name)

        self.ui.field.output = self.ui.output
        self.field = Field(self.ui.field, data=ex_code)

        QtCore.QObject.connect(self.ui.zoomIn, QtCore.SIGNAL("clicked()"),
            self.zoomIn)
        QtCore.QObject.connect(self.ui.zoomOut, QtCore.SIGNAL("clicked()"),
            self.zoomOut)
        QtCore.QObject.connect(self.ui.play, QtCore.SIGNAL("clicked()"),
            self.play)
        QtCore.QObject.connect(self.ui.stop, QtCore.SIGNAL("clicked()"),
            self.stop)
        QtCore.QObject.connect(self.ui.pause, QtCore.SIGNAL("toggled(bool)"),
            self.pause)

        self.zoomIn()
        self.zoomIn()
        self.zoomIn()

        self.field.run()
        
    @Verbose(VERBOSE)
    def zoomIn(self):
        self.ui.field.scale(1.2, 1.2)

    @Verbose(VERBOSE)
    def zoomOut(self):
        self.ui.field.scale(1/1.2, 1/1.2)

    @Verbose(VERBOSE)
    def play(self):
        self.ui.play.setEnabled(False)
        self.ui.stop.setEnabled(True)
        self.ui.pause.setEnabled(True)
        self.field.balls = []
        Ball(self.field, 0, 0).setSpeed(1)
        self.field.run()

    @Verbose(VERBOSE)
    def stop(self):
        self.ui.play.setEnabled(True)
        self.ui.stop.setEnabled(False)
        self.ui.pause.setEnabled(False)
        for ball in self.field.balls:
            ball.kill()
        
    @Verbose(VERBOSE)
    def pause(self, checked):
        self.ui.play.setEnabled(False)
        self.ui.stop.setEnabled(True)
        self.ui.pause.setEnabled(True)
        if checked:
            self.field.terminate = True
        else:
            self.field.terminate = False
            self.field.run()
        
class Field(QtCore.QObject):
    @Verbose(VERBOSE)
    def __init__(self, widget, width = 15, height = 15, data = None):
        QtCore.QObject.__init__(self)
        self.scene = QtGui.QGraphicsScene()
        widget.setScene(self.scene)
        self.widget = widget
        self.balls = []
        self.terminate = False
        if not data:
            self.width = width
            self.height = height
            self.objects = [ [ None for x in range (0, self.width) ] for x in range(0, self.height)]
            self.setupBoard()
        else:
            self.loadData(data)

        
            
    @Verbose(VERBOSE)
    def output(self, data):
        self.widget.output.append(data)
            
    @Verbose(VERBOSE)
    def loadData(self, data):
        lines = data.split('\n')
        self.width = len(lines[0])
        self.height = len(lines)
        self.objects = [ [ None for y in range (0, self.height) ] for x in range(0, self.width)]
        self.setupBoard()
        y = 0
        for line in lines:
            x = 0
            for char in line:
                if char == '|':
                    VertWall(self, x, y, ":/vwall.svg")
                elif char == '-':
                    HorizWall(self, x, y, ":/hwall.svg")
                elif char == '\\':
                    BSlashWall(self, x, y, ":/bswall.svg")
                elif char == '/':
                    SlashWall(self, x, y, ":/swall.svg")
                elif char == '>':
                    RightSluice(self, x, y, ":/rsluice.svg")
                elif char == '<':
                    LeftSluice(self, x, y, ":/lsluice.svg")
                elif char == '^':
                    UpSluice(self, x, y, ":/usluice.svg")
                elif char == 'v':
                    DownSluice(self, x, y, ":/dsluice.svg")
                elif char in "123456789":
                    Generator(self, x, y, char)
                elif char == '0':
                    ZeroGen(self, x, y)
                elif char == '+':
                    PlusTarpit(self, x, y)
                elif char == '*':
                    MulTarpit(self, x, y)
                elif char == '~':
                    Negate(self, x, y)
                elif char == '\'':
                    Increment(self, x, y)
                elif char == ', ':
                    Decrement(self, x, y)
                elif char == '.':
                    Reset(self, x, y)
                elif char == 'p':
                    NumOut(self, x, y)
                elif char == 'P':
                    CharOut(self, x, y)
                elif char == 'Q':
                    Terminate(self, x, y)
                elif char == '#':
                    Grille(self, x, y)
                elif char == 'X':
                    Processor(self, x, y)
                elif char == '@':
                    Always(self, x, y, ":/always.svg")
                elif char == '~':
                    Odd(self, x, y)
                elif char == '%':
                    Random(self, x, y)
                else:
                    TextObject(self, x, y, char)
                x+= 1 
            y+= 1
            
        
        
    @Verbose(VERBOSE)
    def setupBoard(self):
        for i in range(0, self.width):
            for j in range(0, self.height):
                FlipObject(self, i, j)
                pass
        self.objects = [ [ None for y in range (0, self.height) ]
            for x in range(0, self.width)]
                
        
    @Verbose(VERBOSE)
    def addItem(self, item):
        if isinstance(item, Ball):
            self.balls.append(item)
        else:
            self.objects[item.x][item.y] = item
        self.scene.addItem(item.graphicsItem())
        
    @Verbose(VERBOSE)
    def ballCount(self):
        c = 0
        for ball in self.balls:
            if isinstance(ball, Ball):
                c+= 1
        return c
        
    @Verbose(VERBOSE)
    def run(self):
        if ( not self.terminate ) and self.ballCount():
            self.doMove()
            self.timer = QtCore.QTimer.singleShot(DELAY, self.run)
        
    @Verbose(VERBOSE)
    def doMove(self):
        print "doMove"
        for x in range(0, self.width):
            for y in range(0, self.height):
                object = self.objects[x][y]
                if object:
                    object.animated = False


        # Move them balls simultaneously
                    
        for ball in self.balls:
            if not ball: continue
            ball.animated = False
        
        for i in range(0, 10):
            for i in range(0, len(self.balls)):
                ball = self.balls[i]
                if not ball: continue
                ball.item.moveBy(ball.sx, ball.sy)
            QtGui.qApp.processEvents()

        for ball in self.balls:
            if not ball: continue
            ball.animate()

        for x in range(0, self.width):
            for y in range(0, self.height):
                object = self.objects[x][y]
                if object:
                    object.animate()

        for i in range(0, len(self.balls)):
            ball = self.balls[i]
            if not ball: continue
            obj = self.objects[ball.x][ball.y]
            if obj:
                obj.handle(ball)
                    
                    
class Modifier:
    @Verbose(VERBOSE)
    def mvalue(self, v):
        # Objects by default don't modify
        return 0
                    
class FlipObject:
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        self.animated = False
        self.field = field
        self.x = x
        self.y = y
        self.field.addItem(self)
    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtGui.QGraphicsRectItem(QtCore.QRectF(10*self.x, 10*self.y, 10, 10))
        self.item.setZValue(0)
        return self.item
        
    @Verbose(VERBOSE - 2)
    def animate(self):
        if self.animated:
            return
        self.animated = True
        
    @Verbose(VERBOSE)
    def handle(self, ball):
        return


class TextObject(FlipObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y, c):
        self.c = c
        FlipObject.__init__(self, field, x, y)

    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtGui.QGraphicsSimpleTextItem(self.c)
        br = self.item.boundingRect()
        sf = 9/br.height()
        self.item.scale(sf, sf)
        self.item.setZValue(1)
        self.item.setPos(10*self.x+.5, 10*self.y+.5)
        return self.item

class SVGObject(FlipObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y, fname):
        self.fname = fname
        FlipObject.__init__(self, field, x, y)

    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtSvg.QGraphicsSvgItem(self.fname)
        self.item.setZValue(1)
        self.item.scale(0.009, 0.009)
        self.item.setPos(10*self.x+.5, 10*self.y+.5)
        return self.item


        
class Ball(FlipObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y, value = 0):
        self.value = value
        FlipObject.__init__(self, field, x, y)

    @Verbose(VERBOSE)
    def setValue(self, v):
        self.item2.setText(str(v))
        self.value = v
        
    @Verbose(VERBOSE)
    def kill(self):
        self.item.scene().removeItem(self.item)    
        self.item = None
        self.item2 = None
        self.field.balls[self.field.balls.index(self)] = None
        
    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtGui.QGraphicsItemGroup()
        self.item.setZValue(3)
        self.item1 = QtSvg.QGraphicsSvgItem(":/ball.svg")
        self.item1.setZValue(1)
        self.item1.scale(0.009, 0.009)
        self.item1.setPos(10*self.x+.5, 10*self.y+.5)

        self.item2 = QtGui.QGraphicsSimpleTextItem()
        self.item2.setText(str(self.value))
        br = self.item2.boundingRect()
        self.item2.setPos(10*self.x+2.5, 10*self.y+.5)
        sf = 10/br.height()
        self.item2.scale(sf, sf)
        self.item2.setZValue(2)
        
        self.item.addToGroup(self.item1)
        self.item.addToGroup(self.item2)
        
        return self.item
        
    @Verbose(VERBOSE)
    def setSpeed(self, sx = 0, sy = 0):
        self.sx = sx
        self.sy = sy
        
    @Verbose(VERBOSE - 2)
    def animate(self):
        if self.animated:
            return
        self.animated = True
        self.moveTo(self.x+self.sx, self.y+self.sy)

    @Verbose(VERBOSE)
    def moveTo(self, x, y):
        if x >= self.field.width or y >= self.field.height or x<0 or y < 0:
            self.kill()
            return            
        self.x = x
        self.y = y


        
class VertWall(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        ball.sx =-ball.sx

class HorizWall(SVGObject, Modifier):

    @Verbose(VERBOSE)
    def handle(self, ball):
        ball.sy =-ball.sy

    @Verbose(VERBOSE)
    def mvalue(self, value):
        """
        True if value < 0 or value > 2 ** 31
        """
        if value < 0 or value > 2 ** 31:
            return 1
        return 0
        
class SlashWall(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        sy =-ball.sx
        sx =-ball.sy
        ball.sx = sx
        ball.sy = sy
        mods = []
        if self.y>0 and self.x<self.field.width-1:
            m = self.field.objects[self.x-1][self.y-1]
            if m and isinstance(m, Modifier):
                mods.append(m)
        if self.y<self.field.height-1 and self.x>0:
            m = self.field.objects[self.x+1][self.y+1]
            if m and isinstance(m, Modifier):
                mods.append(m)
        if not mods:
            return
        mval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in mods ]))
        if mval:
            # Flip to BSlashWall
            for i in range(0, 90):
                self.item.rotate(1)
                self.item.moveBy(9./90., 0)
                QtGui.qApp.processEvents()
            BSlashWall(self.field, self.x, self.y, ":/swall.svg")
            self.item.scene().removeItem(self.item)    

class BSlashWall(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        sy = ball.sx
        sx = ball.sy
        ball.sx = sx
        ball.sy = sy
        
        mods = []
        if self.y>0 and self.x>0:
            m = self.field.objects[self.x-1][self.y-1]
            if m and isinstance(m, Modifier):
                mods.append(m)
        if self.y<self.field.height-1 and self.x<self.field.width-1:
            m = self.field.objects[self.x+1][self.y+1]
            if m and isinstance(m, Modifier):
                mods.append(m)
        if not mods:
            return
        mval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in mods ]))
        if mval:
            # Flip to SlashWall
            for i in range(0, 90):
                self.item.rotate(1)
                self.item.moveBy(9./90., 0)
                QtGui.qApp.processEvents()
            SlashWall(self.field, self.x, self.y, ":/swall.svg")
            self.item.scene().removeItem(self.item)    

class RightSluice(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        if ball.sx>0: #Pass ball
            return
        elif ball.sx<0: #Bounce ball
        
            # Evaluate top modifiers
            tval = 0
            tmods = []
            if self.y>0:
                if self.x>0:
                    m = self.field.objects[self.x-1][self.y-1]
                    if m and isinstance(m, Modifier): tmods.append(m)
                if self.x<self.field.width-1:
                    m = self.field.objects[self.x+1][self.y-1]
                    if m and isinstance(m, Modifier): tmods.append(m)
            if tmods:
                tval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in tmods ]))
                
            # Evaluate bottom modifiers
            bval = 0
            bmods = []
            if self.y<self.field.height-1:
                if self.x>0:
                    m = self.field.objects[self.x-1][self.y+1]
                    if m and isinstance(m, Modifier): bmods.append(m)
                if self.x<self.field.width-1:
                    m = self.field.objects[self.x+1][self.y+1]
                    if m and isinstance(m, Modifier): bmods.append(m)
            if bmods:
                bval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in bmods ]))
            
            if bval == tval: # Equal: bounce ball
                ball.sx =-ball.sx
            elif bval: # Go down
                ball.setSpeed(0, 1)
            else: # Go up
                ball.setSpeed(0, -1)
                
        else: # Turn ball
            ball.sy = 0
            ball.sx = 1

class LeftSluice(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        if ball.sx<0: # Pass ball
            return
        elif ball.sx>0:
        
            # Evaluate top modifiers
            tval = 0
            tmods = []
            if self.y>0:
                if self.x>0:
                    m = self.field.objects[self.x - 1][self.y - 1]
                    if m and isinstance(m, Modifier): tmods.append(m)
                if self.x < self.field.width - 1:
                    m = self.field.objects[self.x + 1][self.y - 1]
                    if m and isinstance(m, Modifier): tmods.append(m)
            if tmods:
                tval = eval('^'.join([str(mod.mvalue(ball.value))
                    for mod in tmods ]))
                
            # Evaluate bottom modifiers
            bval = 0
            bmods = []
            if self.y < self.field.height - 1:
                if self.x > 0:
                    m = self.field.objects[self.x - 1][self.y + 1]
                    if m and isinstance(m, Modifier):
                        bmods.append(m)
                if self.x<self.field.width - 1:
                    m = self.field.objects[self.x + 1][self.y + 1]
                    if m and isinstance(m, Modifier):
                        bmods.append(m)
            if bmods:
                bval = eval('^'.join([str(mod.mvalue(ball.value))
                    for mod in bmods]))
            
            print tval, bval, tmods, bmods, self.x, self.field.width
            print "bmods: %s" % bmods
                
            if bval == tval: # Equal: bounce ball
                ball.sx = -ball.sx
            elif bval: # Go down
                ball.setSpeed(0, 1)
            else: # Go up
                ball.setSpeed(0, -1)
                
        else: # Turn ball
            ball.sy = 0
            ball.sx =-1


class DownSluice(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        if ball.sy>0:
            return
        elif ball.sy<0:

            # Evaluate left modifiers
            lval = 0
            lmods = []
            if self.x>0:
                if self.y>0:
                    m = self.field.objects[self.x-1][self.y-1]
                    if m and isinstance(m, Modifier): lmods.append(m)
                if self.y<self.field.height-1:
                    m = self.field.objects[self.x-1][self.y+1]
                    if m and isinstance(m, Modifier): lmods.append(m)
            if lmods:
                lval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in lmods ]))
                
            # Evaluate right modifiers
            rval = 0
            rmods = []
            if self.x<self.field.width-1:
                if self.y>0:
                    m = self.field.objects[self.x+1][self.y-1]
                    if m and isinstance(m, Modifier): rmods.append(m)
                if self.y<self.field.height-1:
                    m = self.field.objects[self.x+1][self.y+1]
                    if m and isinstance(m, Modifier): rmods.append(m)
            if rmods:
                rval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in rmods ]))
            
            if lval == rval: # Equal: bounce ball
                ball.sy =-ball.sy
            elif lval: # Go left
                ball.setSpeed(-1, 0)
            else: # Go right
                ball.setSpeed(1, 0)
        else:
            ball.sy = 1
            ball.sx = 0


class UpSluice(SVGObject):
    @Verbose(VERBOSE)
    def handle(self, ball):
        if ball.sy<0:
            return
        elif ball.sy>0:

            # Evaluate left modifiers
            lval = 0
            lmods = []
            if self.x>0:
                if self.y>0:
                    m = self.field.objects[self.x-1][self.y-1]
                    if m and isinstance(m, Modifier): lmods.append(m)
                if self.y<self.field.height-1:
                    m = self.field.objects[self.x-1][self.y+1]
                    if m and isinstance(m, Modifier): lmods.append(m)
            if lmods:
                lval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in lmods ]))
                
            # Evaluate right modifiers
            rval = 0
            rmods = []
            if self.x<self.field.width-1:
                if self.y>0:
                    m = self.field.objects[self.x+1][self.y-1]
                    if m and isinstance(m, Modifier): rmods.append(m)
                if self.y<self.field.height-1:
                    m = self.field.objects[self.x+1][self.y+1]
                    if m and isinstance(m, Modifier): rmods.append(m)
            if rmods:
                rval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in rmods ]))
            
            if lval == rval: # Equal: bounce ball
                ball.sy =-ball.sy
            elif lval: # Go left
                ball.setSpeed(-1, 0)
            else: # Go right
                ball.setSpeed(1, 0)
        else:
            ball.sy =-1
            ball.sx = 0
            
class Generator(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y, n):
        TextObject.__init__(self, field, x, y, n)
        self.n = int(n)
        
    @Verbose(VERBOSE)
    def handle(self, ball):
        sx = ball.sx
        sy = ball.sy
        b = Ball(self.field, self.x, self.y, value = self.n)
        b.setSpeed(sx, sy)
        ball.setSpeed(-sx, -sy)
        
class ZeroGen(Generator, Modifier):            
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        Generator.__init__(self, field, x, y, '0')
        self.n = 0
        
    @Verbose(VERBOSE)
    def mvalue(self, v):
        if v == 0:
            return 1
        return 0
            
class PlusTarpit(TextObject, Modifier):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        self.value = None
        TextObject.__init__(self, field, x, y, '+')
    
    @Verbose(VERBOSE)
    def handle(self, ball):
        if self.value == None:
            self.value = ball.value
            ball.kill()
            self.item.setText("+%d"%self.value)
        else:
            ball.setValue(ball.value+self.value)
            self.item.setText("+")
            self.value = None
    @Verbose(VERBOSE)
    def mvalue(self, v):
        if v>0:
            return 1
        return 0

class MulTarpit(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        self.value = None
        TextObject.__init__(self, field, x, y, '*')
    
    @Verbose(VERBOSE)
    def handle(self, ball):
        if self.value == None:
            self.value = ball.value
            ball.kill()
            self.item.setText("*%d"%self.value)
        else:
            ball.setValue(ball.value*self.value)
            self.item.setText("*")
            self.value = None
    
class Negate(TextObject, Modifier):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '~')
    @Verbose(VERBOSE)
    def handle(self, ball):
            ball.setValue(-ball.value)
    @Verbose(VERBOSE)
    def mvalue(self, v): return v%2

class Increment(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '++')
    @Verbose(VERBOSE)
    def handle(self, ball):
            ball.setValue(ball.value+1)

class Decrement(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '--')
    @Verbose(VERBOSE)
    def handle(self, ball):
            ball.setValue(ball.value-1)
    
class Reset(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '.')
    @Verbose(VERBOSE)
    def handle(self, ball):
            ball.setValue(0)

class NumOut(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, 'p')
    @Verbose(VERBOSE)
    def handle(self, ball):
            self.field.output(str(ball.value))
            ball.kill()

class CharOut(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, 'P')
    @Verbose(VERBOSE)
    def handle(self, ball):
            self.field.output(chr(ball.value))
            ball.kill()

class Terminate(FlipObject):
    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtSvg.QGraphicsSvgItem(':/terminate.svg')
        self.item.setZValue(1)
        self.item.scale(0.009, 0.009)
        self.item.setPos(10*self.x+.5, 10*self.y+.5)
        return self.item
    @Verbose(VERBOSE)
    def handle(self, ball):
        ball.kill()
        self.field.terminate = True

class Grille(TextObject):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '#')
    @Verbose(VERBOSE)
    def handle(self, ball):
        if ball.value <= 0:
            ball.kill()
class Processor(FlipObject):
    @Verbose(VERBOSE)
    def graphicsItem(self):
        self.item = QtSvg.QGraphicsSvgItem(':/processor.svg')
        self.item.setZValue(1)
        self.item.scale(0.009, 0.009)
        self.item.setPos(10*self.x+.5, 10*self.y+.5)
        return self.item
    @Verbose(VERBOSE)
    def handle(self, ball):
        v = ball.value

        # Evaluate top modifiers
        tval = 1
        tmods = []
        if self.y>0:
            if self.x>0:
                m = self.field.objects[self.x-1][self.y-1]
                if m and isinstance(m, Modifier): tmods.append(m)
            if self.x<self.field.width-1:
                m = self.field.objects[self.x+1][self.y-1]
                if m and isinstance(m, Modifier): tmods.append(m)
        if tmods:
            tval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in tmods ]))
            
        # Evaluate bottom modifiers
        bval = 1
        bmods = []
        if self.y<self.field.height-1:
            if self.x>0:
                m = self.field.objects[self.x-1][self.y+1]
                if m and isinstance(m, Modifier): bmods.append(m)
            if self.x<self.field.width-1:
                m = self.field.objects[self.x+1][self.y+1]
                if m and isinstance(m, Modifier): bmods.append(m)
        if bmods:
            bval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in bmods ]))


        # Evaluate left modifiers
        lval = 1
        lmods = []
        if self.x>0:
            if self.y>0:
                m = self.field.objects[self.x-1][self.y-1]
                if m and isinstance(m, Modifier): lmods.append(m)
            if self.y<self.field.height-1:
                m = self.field.objects[self.x-1][self.y+1]
                if m and isinstance(m, Modifier): lmods.append(m)
        if lmods:
            lval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in lmods ]))
            
        # Evaluate right modifiers
        rval = 1
        rmods = []
        if self.x<self.field.width-1:
            if self.y>0:
                m = self.field.objects[self.x+1][self.y-1]
                if m and isinstance(m, Modifier): rmods.append(m)
            if self.y<self.field.height-1:
                m = self.field.objects[self.x+1][self.y+1]
                if m and isinstance(m, Modifier): rmods.append(m)
        if rmods:
            rval = eval('^'.join([ str(mod.mvalue(ball.value)) for mod in rmods ]))
        
        
        print lval, rval, tval, bval
        
        if ball.sx<>0:
            print "x-ball"
            # left or right ball
            if tval: # new top ball
                Ball(self.field, self.x, self.y, ball.value).setSpeed(0, -1)
            if bval: # new bottom ball
                Ball(self.field, self.x, self.y, ball.value).setSpeed(0, 1)
        else:
            print "y-ball"
            # up or down ball
            if lval:
                Ball(self.field, self.x, self.y, ball.value).setSpeed(-1, 0)
            if rval:
                Ball(self.field, self.x, self.y, ball.value).setSpeed(1, 0)

        ball.kill()
                
class Always(SVGObject, Modifier):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y, fname):
        SVGObject.__init__(self, field, x, y, ':/always.svg')
    @Verbose(VERBOSE)
    def mvalue(self, v):
        return 1
        
class Random(TextObject, Modifier):
    @Verbose(VERBOSE)
    def __init__(self, field, x, y):
        TextObject.__init__(self, field, x, y, '%')
    @Verbose(VERBOSE)
    def mvalue(self, v):
        v = random.randint(0, 1)
        print v
        return v
            
@Verbose(VERBOSE)
def main():
    app = QtGui.QApplication(sys.argv)
    window = FieldWidget()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

