#Include nessesary files.
import pygame, sys, pygame.mixer
from pygame.locals import *
import math
import random
import os



#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



#Initilize pygame
pygame.init()
Window=pygame.display.set_mode((600,400),0,32)



#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



#A sprite class makes everything easier.
class Sprite_Object:
        def __init__( self, file ):
                self._Sprite=pygame.image.load(file).convert_alpha()
                self._file = file
                self._x = 0
                self._y = 0
                self._angle = 0
        def getFile( self ):
                return self._file
        def setFile( self, value ):
                self._file = value
        def delFile( self ):
                del self._file
        def Update_Properties( self ):
                self._Sprite=pygame.image.load(self._file).covert()
        def getSprite( self ):
                return self._Sprite
        def setSprite( self, value ):
                self._Sprite = Value
        def delSprite( self ):
                del self._Sprite
        def Draw( self, PosX, PosY ):
                Window.blit(self._Sprite,(PosX, PosY))
        def Draw():
                Window.blit( self._Sprite, ( self._x, self._y ) )
        def SetPosition( self, x, y ):
                self._x = x
                self._y = y
        def getX( self ):
                return self._x
        def getY( self ):
                return self._y
        def setX( self, value ):
                self._x = value
                
        def setY( self, value ):
                self._y = value
        def delX( self ):
                del self._x
        def delY( self ):
                del self._y
        def getAngle( self ):
                return self._angle
        def Rotate( self, angle ):
                self._Sprite = pygame.transform.rotate( self._Sprite, angle )
                #self._angle = 0
        def Scale( self, X, Y ):
                self._Sprite = pygame.transform.smoothscale( self._Sprite, ( X, Y ) )
        File = property( getFile, setFile, delFile, "Image File" )
        sprite = property( getSprite, setSprite, delSprite, "The Sprite" )
        x = property( getX, setX, delX, "X position" )
        y = property( getY, setY, delY, "Y psoition" )
        angle = property( getAngle, "Get the angle." )




#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



#Vector class.
class Vector:
        def __init__( self ):
                self._x = 0
                self._y = 0
                self._scaler = 1
                self._x2 = 0
                self._y2 = 0
                self._Mag = 0
        def Magn( self ):
                if self._x != self._x2:
                        self._x -= self._x2
                else:
                        self._x = 0
                if self._y != self._y2:
                        self._y -= self._y2
                else:
                        self._y = 0
        def Pythag( self ):
                self._Mag = self._x + self._x * self._y * self._y
                if self._Mag < 0:
                        self._Mag *= -1
                self._Mag = math.sqrt( self._Mag )
        def Round( self ):
                round( self._x, 200 )
                round( self._y, 200 )
        def Round_M( self ):
                round( self._Mag )
        def setDestination( self, x, y ):
                self._x2 = x
                self._y2 = y
        def setBegin( self, x, y ):
                self._x = x
                self._y = y
        def setSpeed( self, Speed ):
                self._scaler = Speed
        def getVx( self ):
                return self._x
        def getVy( self ):
                return self._y
        def setVx( self, x ):
                self._x = x
        def setVy( self, y ):
                self._y = y
        def getSpeed( self ):
                return self._scaler
        def getMag( self ):
                return self._Mag
        def getdx( self ):
                return self._x2
        def getdy( self ):
                return self._y2
        x = property( getVx, setVx, "X element of the vector." )
        y = property( getVy, setVy, "Y element of the vector." )
        speed = property( getSpeed, setSpeed, "The scaler of the vector." )
        mag = property( getMag, "The magnitude of the vector." )
        dx = property( getdx, "The x destination." )
        dy = property( getdy, "The y destination." )

#################################

#Calculate a vector

def Calc( Vector, Position ):
        Vector.Magn()
        if Position.x > Vector.dx:
                if Vector.x < 0:
                        Vector.x = Vector.x * -1
        if Position.y > Vector.dy:
                if Vector.y < 0:
                        Vector.y = Vector.y * -1
        Vector.Pythag()
        if Vector.mag != 0:
                if Vector.x != 0:
                        Vector.x = Vector.x / Vector.mag
                if Vector.y != 0:
                        Vector.y = Vector.y / Vector.mag
        Vector.x = Vector.x * Vector.speed
        Vector.y = Vector.y * Vector.speed
        return Vector

#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################


class XY:
        def __init__( self ):
                self._x = 0
                self._y = 0
        def getX( self ):
                return self._x
        def getY( self ):
                return self._y
        def setX( self, value ):
                self._x = value
        def setY( self, value ):
                self._y = value
        x = property( getX, setX, "X position." )
        y = property( getY, setY, "Y position." )

#################################

def Move( vector, Position ):
        Position.x = Position.x + vector.x
        Position.y = Position.y + vector.y
        return Position

#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################


#Colors.
Blue = ( 0, 0, 255 )
Red = ( 255, 0, 0 )
Green = ( 0, 255, 0 )
Black = ( 0, 0 , 0 )
White = ( 255, 255, 255 )


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





#For collision.
class Bounding_Box:
        def __init__( self ):
                self.xo = 10
                self.yo = 10
                self.Position = XY()
        def setPosition( self, value ):
                self.Position = value
        def getPosition( self ):
                return self.Position
        def setXOffset( self, value ):
                self.xo = value
        def setYOffset( self, value ):
                self.yo = value
        def getXOffset( self ):
                return self.xo
        def getYOffset( self ):
                return self.yo
        position = property( getPosition, setPosition, "The position." )
        x_offset = property( getXOffset, setXOffset, "The x offset." )
        y_offset = property( getYOffset, setYOffset, "The y offset." )



#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




class Collision_Manager:
        #Calculate the reaction to a collision.
        def React( self, Vector, Collision_Scale, P1, P2 ):
                Vector.x = Vector.x - Vector.x * Collision_Scale
                Vector.y = Vector.y - Vector.y * Collision_Scale
                return Vector
        #Update Reactions to the collision.
        def Update_Physics( self, Robot, OtherBot ):
                if Robot.collision == True:
                        Robot.vector = self.React( Robot.vector, Robot.reaction, Robot.position, OtherBot.position )
                        Robot.collision = False
                        Robot.stop = False
                if Robot.arm_col == True:
                        t = Robot.vector
                        Robot.vector = self.React( OtherBot.arm_vector, Robot.reaction, Robot.position, OtherBot.position )
                        Robot.vector.x = -Robot.vector.x
                        Robot.vector.y = -Robot.vector.y
                        Robot.position = Move( Robot.vector, Robot.position )
                        Robot.vector = t
                        Robot.arm_col = False
                        Robot.stop = True
                if Robot.collision_frames < Robot.collision_time:
                        Robot.collision_frames += 1
                else:
                        Robot.collision_frames = 0
                        Robot.vector.x = 0
                        Robot.vector.y = 0
                        Robot.stop = True
                return Robot
        #Detect collisions.
        def Check_Collision( self, A, B ):
                X = False
                Y = False
                if A.position.x + A.x_offset > B.position.x - B.x_offset and A.position.x - A.x_offset < B.position.x + B.x_offset:
                        X = True
                if A.position.y + A.y_offset > B.position.y - B.y_offset and A.position.y - A.y_offset < B.position.y + B.y_offset:
                        Y = True
                if X == Y and Y == True:
                        return True
                return False
CM = Collision_Manager()






#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





#AI and player base class.
class Robot_Base:
        def __init__( self, F, B, AF, AB, JF, JB ):
                self.Initilize( F, B, AF, AB, JF, JB )
        def Initilize( self, F, B, AF, AB, JF, JB ):
                self._ReactM = 2
                self._Col = False
                self.ColFR = 0
                self.Box = Bounding_Box()
                self._Foward = Sprite_Object( F )
                self._Back = Sprite_Object( B )
                self._ArmF = Sprite_Object( AF )
                self._ArmB = Sprite_Object( AB )
                self._JumpF = Sprite_Object( JF )
                self._JumpB = Sprite_Object( JB )
                self._Fwd = True
                self._Bkwd = False
                self._Jump = False
                self._Punch = False
                self._Vector = Vector()
                self._Position = XY()
                self._ArmPos = XY()
                self._ArmVect = Vector()
                self._ArmDis = XY()
                self._JmpF = False
                self.jc = 0
                self._coltime = 4
                self._Stop = True
                self._ReactM = 4
                self._ArmBox = Bounding_Box()
                self._ArmTime = 0
                self._ArmColl = False
                self._Health = 100
        def getAT( self ):
                return self._ArmTime
        def setAT( self, value ):
                self._ArmTime = value
        def getCL( self ):
                return self._coltime
        def setCL( self, value ):
                self._coltime = value
        def getR( self ):
                return self._ReactM
        def setR( self, value ):
                self._ReactM = value
        def getCollision( self ):
                return self._Col
        def getCollisionFrames( self ):
                return self.ColFR
        def setCollision( self, value ):
                self._Col = value
        def setCollisionFrames( self, value ):
                self.ColFR = value
        def SetBotPosition( self, X, Y ):
                self._Position.x = X
                self._Position.y = Y
                self._ArmPos.x = X + 10
                self._ArmPos.y = Y + 30
                self.Box.position.x = X
                self.Box.position.y = Y
        def getBox( self ):
                return self.Box
        def setBox( self, value ):
                self.Box = value
        def ArmCalc( self ):
                self._ArmDis.x = self._Position.x - self._ArmPos.x
                self._ArmDis.y = self._Position.y - self._ArmPos.y
        def Walk( self ):
                self._Position = Move( self._Vector, self._Position )
        def Walk( self, x, y ):
                self._Vector.setBegin( self._Position.x, self._Position.y )
                self._Vector.setDestination( x, y )
                self._Vector.Calc()
                Position = Move( self._Vector, self._Position )
        def getV( self ):
                return self._Vector
        def getP( self ):
                return self._Position
        def setP( self, value ):
                self._Position = value
                self.Box.position = value
        def setV( self, value ):
                self._Vector = value
        def getAV( self ):
                return self._ArmVect
        def getAP( self ):
                return self._ArmPos
        def setAV( self, value ):
                self._ArmVect = value
        def setAP( self, value ):
                self._ArmPos = value
        def setFwd( self, value ):
                if self._Bkwd == True and value == True:
                        self._Bkwd = False
                else:
                        self._Bkwd = True
                self._Fwd = value
        def setBkwd( self, value ):
                if self._Fwd == True and value == True:
                        self._Fwd = False
                else:
                        self._Fwd = True
                self._Bkwd = value
        def setJump( self, value ):
                self._Jump = value
        def getFwd( self ):
                return self._Fwd
        def getBkwd( self ):
                return self._Bkwd
        def getJump( self ):
                return self._Jump
        def Draw( self ):
                if self._Fwd == True:
                        if self._Jump == False:
                                Window.blit( self._Foward.sprite, (self._Position.x, self._Position.y) )
                        else:
                                Window.blit( self._JumpF.sprite, (self._Position.x, self._Position.y) )
                        Window.blit( self._ArmF.sprite, (self._ArmPos.x, self._ArmPos.y ) )
                else:
                        if self._Jump == False:
                                Window.blit( self._Back.sprite, (self._Position.x, self._Position.y) )
                        else:
                                Window.blit( self._JumpB.sprite, (self._Position.x, self._Position.y) )
                        Window.blit( self._ArmB.sprite, (self._ArmPos.x, self._ArmPos.y ) )
        def Update_Arms( self ):
                self._ArmPos.x = self._Position.x
                self._ArmPos.x -= self._ArmDis.x
                self._ArmPos.y = self._Position.y
                self._ArmPos.y -= self._ArmDis.y
        def Jump( self ):
                if self._Jump == True:
                        self.jc += 1
                        if self.jc >= 100:
                                self._JF = True
                                self._Position.y += 2
                                if self._Position.y > 270:
                                        self.jc = 0
                                        self._JF = False
                                        self._Jump = False
                        else:
                                self._Position.y -= 3
                else:
                        self._jc = 0
        def getStop( self ):
                return self._Stop
        def setStop( self, value ):
                self._Stop = value
        def getAB( self ):
                return self._ArmBox
        def setAB( self, value ):
                self._ArmBox = value
        def setACll( self, value ):
                self._ArmColl = value
        def getACll( self ):
                return self._ArmColl
        def Punch( self ):
                pass
        def CheckPunch( self ):
                pass
        def getHealth( self ):
                return self._Health
        def setHealth( self, value ):
                self._Health = value
        def SetFowardRaw( self, value ):
                self._Fwd = value
        def SetBackwardRaw( self, value ):
                self._Bkwd = value
        def Punch( self ):
                if self._ArmTime >= 1:
                        pass
                else:
                        self._ArmVect.setBegin( self._ArmPos.x, self._ArmPos.y )
                        if self._Fwd == True:
                                self._ArmVect.setDestination( self._ArmPos.x + 10, self._ArmPos.y )
                                self._ArmVect = Calc( self._ArmVect, self._ArmPos )
                                self._ArmTime = 1
                        else:
                                self._ArmVect.setDestination( self._ArmPos.x - 10, self._ArmPos.y )
                                self._ArmVect = Calc( self._ArmVect, self._ArmPos )
                                self._ArmTime = 1
        def CheckPunch( self ):
                if self._ArmTime >= 1:
                        self._ArmTime += 1
                        self._ArmPos = Move( self._ArmVect, self._ArmPos )
                        self._ArmBox.position.x = self._ArmPos.x
                        self._ArmBox.position.y = self._ArmPos.y
                        self._ArmBox.x_offset = 32
                        self._ArmBox.y_offset = 16
                if self._ArmTime > 20:
                        self._ArmTime = 0
                        self._ArmVect.x = 0
                        self._ArmVect.y = 0
                        self._ArmPos.x = self._Position.x + 10
                        self._ArmPos.y = self._Position.y + 30
        vector = property( getV, setV, "The vector." )
        position = property( getP, setP, "The position." )
        arm_position = property( getAP, setAP, "The arms position." )
        arm_vector = property( getAV, setAV, "The arms vector." )
        foward = property( getFwd, setFwd )
        back = property( getBkwd, setBkwd )
        jump = property( getJump, setJump )
        box = property( getBox, setBox, "A box for bounding box collision." )
        collision = property( getCollision, setCollision, "A bool that tells if there is a collision or not." )
        collision_frames = property( getCollisionFrames, setCollisionFrames, "Count how many frames after a collision.")
        reaction = property( getR, setR, "How much to multiply the vector from a collision by." )
        collision_time = property( getCL, setCL, "How much time the reaction for a collision should last." )
        stop = property( getStop, setStop, "Should the robot sease to move?" )
        arm_box = property( getAB, setAB, "The bounding box for the arm." )
        arm_col = property( getACll, setACll, "Did we collide with a robots arm?" )
        health = property( getHealth, setHealth, "The robot's health." )
        arm_time = property( getAT, setAT, "To tell if the robot is punching" )


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



class PlayerBase( Robot_Base ):
        def Controle( self ):
                pass


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



#Input varibles.
Up = False
Down = False
Left = False
Right = False
W = False
A = False
S = False
D = False
Z = False
X = False
RShift = False
RControle = False
R = False


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




#The player 1 and player 2 class will be slightly diffrent.
class Player1( PlayerBase ):
        def Controle( self ):
                        if self._Stop == True:
                                if A == True:
                                        self._Vector.setBegin( self._Position.x, self._Position.y )
                                        self._Vector.setDestination( self._Position.x + 1, self._Position.y )
                                        self._Vector = Calc( self._Vector, self._Position )
                                        self._Fwd = True
                                        self._Bkwd = False
                                if D == True:
                                        self._Vector.setBegin( self._Position.x, self._Position.y )
                                        self._Vector.setDestination( self._Position.x - 1, self._Position.y )
                                        self._Vector = Calc( self._Vector, self._Position )
                                        self._Fwd = False
                                        self._Bkwd = True
                                if W == True:
                                        self._Jump = True


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





#The player 2 and player 1 classes are slightly diffrent.
class Player2( PlayerBase ):
        def Controle( self ):
                        if self._Stop == True:
                                if Left == True:
                                        self._Vector.setBegin( self._Position.x, self._Position.y )
                                        self._Vector.setDestination( self._Position.x + 1, self._Position.y )
                                        self._Vector = Calc( self._Vector, self._Position )
                                        self._Fwd = True
                                        self._Bkwd = False
                                if Right == True:
                                        self._Vector.setBegin( self._Position.x, self._Position.y )
                                        self._Vector.setDestination( self._Position.x - 1, self._Position.y )
                                        self._Vector = Calc( self._Vector, self._Position )
                                        self._Fwd = False
                                        self._Bkwd = True
                                if Up == True:
                                        self._Jump = True

#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################






def Combat( Robot, Punch ):#, Kick ):
        if Punch == True:
                Robot.Punch()
        Robot.CheckPunch()
        return Robot






#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




#Makes sure the robot does not exit the level.
def KeepInLevel( Robot ):
        if Robot.position.x > 600:
                Robot.vector.x = -1
                Robot.vector.y = 0
                t = Robot.vector
                while Robot.position.x > 560:
                        Robot.position = Move( Robot.vector, Robot.position )
                Robot.vector = t
        if Robot.position.x < 0:
                Robot.vector.x = 1
                Robot.vector.y = 0
                t = Robot.vector
                while Robot.position.x < 40:
                        Robot.position = Move( Robot.vector, Robot.position )
                Robot.vector = t
        return Robot



#If the robot gets "punched" its health will be decromented."
def Hurt( Robot, OtherBot ):
        if Robot.arm_col == True and OtherBot.arm_time >= 1:
                Robot.health = Robot.health - 1
        return Robot

#Manages all the collisions.
def ManageCollision( Robot, OtherBot ):
        Robot.collision = CM.Check_Collision( Robot.box, OtherBot.box )
        Robot.arm_col = CM.Check_Collision( OtherBot.arm_box, Robot.box )
        Robot = Hurt( Robot, OtherBot )
        return Robot

#Refreshes the players.
def Refresh_Bot( Robot, OtherBot, Punch ):
        Robot.Controle()
        Robot.position = Move( Robot.vector, Robot.position )
        Robot.Update_Arms()
        Robot = Combat( Robot, Punch )
        Robot.Draw()
        Robot = ManageCollision( Robot, OtherBot )
        Robot = CM.Update_Physics( Robot, OtherBot )
        if Robot.jump == True:
                Robot.Jump()
        Robot = KeepInLevel( Robot )
        return Robot


#Gets events
def getEvents():
        for event in pygame.event.get():
                global W
                global A
                global S
                global D
                global Left
                global Right
                global Up
                global Down
                global Z
                global X
                global RShift
                global RControle
                if event.type == QUIT:
                        pygame.quit()
                if event.type == KEYDOWN:
                        if event.key == K_r:
                                R = True
                        if event.key == K_w:
                                W = True
                        if event.key == K_a:
                                A = True
                        if event.key == K_s:
                                S = True
                        if event.key == K_d:
                                D = True
                        if event.key == K_UP:
                                Up = True
                        if event.key == K_DOWN:
                                Down = True
                        if event.key == K_LEFT:
                                Left = True
                        if event.key == K_RIGHT:
                                Right = True
                        if event.key == K_z:
                                Z = True
                        if event.key == K_x:
                                X = True
                        if event.key == K_RSHIFT:
                                RShift = True
                        if event.key == K_RCTRL:
                                RControle = True
                if event.type == KEYUP:
                        if event.key == K_r:
                                R = False
                        if event.key == K_w:
                                W = False
                        if event.key == K_a:
                                A = False
                        if event.key == K_s:
                                S = False
                        if event.key == K_d:
                                D = False
                        if event.key == K_UP:
                                Up = False
                        if event.key == K_DOWN:
                                Down = False
                        if event.key == K_LEFT:
                                Left = False
                        if event.key == K_RIGHT:
                                Right = False
                        if event.key == K_z:
                                Z = False
                        if event.key == K_x:
                                X = False
                        if event.key == K_RSHIFT:
                                RShift = False
                        if event.key == K_RCTRL:
                                RControle = False







#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################

class GameThread:
        def __init__(self, KO, kop, back ):
                self.bg = Sprite_Object( back )
                self.ko = Sprite_Object( KO )
                self.KOP = kop
        def MainGameThreadBegin( self ):
                Window.blit( self.bg.sprite, (0, 0) )
                getEvents()
        def MainGameThreadEnd( self ):
                pygame.display.update()
        def getKO( self ):
                return self.ko
        def setKO( self, value ):
                self.ko = value
        def getKOP( self ):
                return self.KOP
        def setKOP( self, value ):
                self.KOP = value
        koP = property( getKOP, setKOP )
        kO = property( getKO, setKO, "Knock out sprite." )

#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





class Exploader:
        def __init__( self, x, y ):
                self.booms = []
                self.all_coords = []
                self.X = x
                self.Y = y
                self.random = 0
                self.size = 0
        def Randomize_R( self ):
                self.random = random.randint( 0, 100 )
        def Create( self ):
                if self.random >= 10 and self.random <= 15:
                        if self.size >= 10:
                                i = 9
                                while i >= 0:
                                        del self.booms[i]

                                        del self.all_coords[i]
                                        i -= 1
                                self.size = 0
                        self.size += 1
                        self.booms.append( Sprite_Object( "Explosion.png" ) )
                        self.all_coords.append( XY() )
                        self.all_coords[self.size - 1].x = random.uniform( self.X, self.X + 32 )
                        self.all_coords[self.size - 1].y = random.uniform( self.Y, self.Y + 128 )
        def Refresh( self ):
                self.Randomize_R()
                self.Create()
                i = 0
                i2 = 0
                while i < self.size:
                        Window.blit( self.booms[i].sprite, (self.all_coords[i].x, self.all_coords[i].y) )
                        i += 1
        def setX( self, value ):
                self.X = value
        def setY( self, value ):
                self.Y = value



#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################



##############---Currently Unused---##############
class Returner:
        def __init__( self ):
                self._position = XY()
                self._foward = True
                self._back = False
                self._vector = Vector()
        def setPosition( self, value ):
                self._position = value
        def setFoward( self, value ):
                self._foward = value
        def setBack( self, value ):
                self._back = value
        def setVector( self, value ):
                self._vector = value
        def getPosition( self ):
                return self._position
        def getFoward( self ):
                return self._foward
        def getBack( self ):
                return self._back
        def getVector( self ):
                return self._vector
        def DefaultAll( self ):
                self._position = XY()
                self._foward = True
                self._back = False
                self._vector = Vector()
        def DefaultDirection( self ):
                self._foward = True
                self._back = False
        position = property( getPosition, setPosition, "The position." )
        foward = property( getFoward, setFoward, "Are we going foward?" )
        back = property( getBack, setBack, "Are we going backwords?" )
        vector = property( getVector, setVector, "The objects vector." )





#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





#AI behavor base class.
class Behavor:
        def __init__( self ):
                self._position = XY()
                self._behavorDeterminBox = Bounding_Box()
                self._punchBox = Bounding_Box()
                self._foward = False
                self._back = True
                self._otherFront = True
                self._otherBack = False
                self._otherFace = True
                self._bbbCollided = False
                self._pbbCollided = False
                self._vector = Vector()
                self._targate = Player1( "Blue Bot/Robot_StandF.jpg", "Blue Bot/Robot_StandB.jpg", "Blue Bot/Robot_ArmF.png", "Blue Bot/Robot_ArmB.png", "Blue Bot/Robot_JumpingF.jpg", "Blue Bot/Robot_JumpingB.jpg" )
                self._otherJumping = False
                self._speed = .01
                self._combat = False
                self._jump = False
                self._jt = 0
        def UpdateParams( self, AI, Other ):
                self._position = AI.position
                self._foward = AI.foward
                self._back = AI.back
                self._targate = Other
                self._behavorDeterminBox.x_offset = 200
                self._behavorDeterminBox.y_offset = 200
                self._punchBox.x_offset = 10
                self._punchBox.y_offset = 70
                self._behavorDeterminBox.position.x = self._position.x
                self._behavorDeterminBox.position.y = self._position.y
                self._punchBox.position.x = self._position.x
                self._punchBox.position.y = self._position.y
        def IsFacing( self, Other ):
                if Other.foward == self._foward or Other.back == self._back:
                        self._otherFace = False
                else:
                        self._otherFace = True
        def Which_Side( self, Other ):
                if Other.position.x > self._position.x:
                        self._otherFront = False
                        self._otherBack = True
                else:
                        self._otherFront = True
                        self._otherBack = False
                if Other.position.y < self._position.y:
                        self._otherJumping = True
                else:
                        self._otherJumping = False
        def Manage_Collision( self, boundingBox ):
                self._bbbCollided = CM.Check_Collision( self._behavorDeterminBox, boundingBox )
                self._pbbCollided = CM.Check_Collision( self._punchBox, boundingBox )
                if self._bbbCollided == True and self._pbbCollided == True:
                        self._bbbCollided = False
        def FowardAlt( self ):
                pass
        def BackAlt( self ):
                pass
        def FowardDecision( self ):
                pass
        def BackDecision( self ):
                pass
        def Default( self ):
                pass
        def DefaultAll( self ):
                pass
        def Decision( self ):
                self.IsFacing( self._targate )
                self.Which_Side( self._targate )
                self.Manage_Collision( self._targate.box )
                if self._bbbCollided == True:
                        if self._otherFront == True:
                                self.FowardDecision()
                        else:
                                self.BackDecision()
                if self._pbbCollided == True:
                        if self._otherFront == True:
                                self.FowardAlt()
                        else:
                                self.BackAlt()
                else:
                        self.Default()
                self.DefaultAll()
        def Refresh( self ):
                pass
        def DefaultAll( self ):
                pass
        def Notify( self, AI ):
                AI.position = self._position
                AI.SetFowardRaw( self._foward )
                AI.SetBackwardRaw( self._back )
                AI.vector = self._vector
                AI.jump = self._jump
                AI.Jump()
                AI = Combat( AI, self._combat )
                return AI





#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################






class Agressive( Behavor ):
        def Default( self ):
                t = Vector()
                t.setBegin( self._position.x, self._position.y )
                self._combat = False
                if self._otherFront == True:
                        t.setDestination( self._position.x + self._speed, self._position.y )
                        self._back = False
                        self._foward = True
                else:
                        t.setDestination( self._position.x - self._speed, self._position.y )
                        self._back = True
                        self._foward = False
                t = Calc( t, self._position )
                self._vector.x = t.x
                self._position = Move( self._vector, self._position )
        def FowardAlt( self ):
                self._vector.x = 0
                self._vector.y = 0
                self._back = False
                self._foward = True
                self._combat = True
        def BackAlt( self ):
                self._vector.x = 0
                self._vector.y = 0
                self._back = True
                self._foward = False
                self._combat = True
        def FowardDecision( self ):
                self._vector.setBegin( self._position.x, self._position.y )
                self._vector.setDestination( self._position.x + .05, self._position.y )
                self._back = False
                self._foward = True
                self._combat = False
                self._vector = Calc( self._vector, self._position )
                self._position = Move( self._vector, self._position )
        def BackDecision( self ):
                self._vector.setBegin( self._position.x, self._position.y )
                self._vector.setDestination( self._position.x - .05, self._position.y )
                self._back = True
                self._foward = False
                self._combat = False
                self._vector = Calc( self._vector, self._position )
                self._position = Move( self._vector, self._position )
        def DefaultAll( self ):
                if self._otherJumping == True:
                        if self._jt >= 25:
                                self._jump = True
                        else:
                                self._jt += 1
                else:
                        self._jt -= 1
                        self._jump = False
                        if self._position.y <= 270:
                                self._position.y += 3


#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################








class ArtificalIntelegence( Robot_Base ):
        def BehavorDecide( self ):
                #if self._Health < 50:
                #        return "pass"
                #else:
                #        return "agress"
                return "agress"




#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################






#Makes it so there is no long constructor for a robot.
class Robot_Factory:
        def __init__( self, F, B ,AF, AB, JF, JB ):
                self._sds = [ F, B, AF, AB, JF, JB ]
        def GetSpriteDirectories( self ):
                return self._sds
        def CreatePlayer1( self ):
                player1 = Player1( self._sds[0], self._sds[1], self._sds[2], self._sds[3], self._sds[4], self._sds[5] )
                player1.SetBotPosition( 100, 270 )
                player1.ArmCalc()
                player1.box.x_offset = 32
                player1.box.y_offset = 30
                return player1
        def CreatePlayer2( self ):
                player2 = Player2( self._sds[0], self._sds[1], self._sds[2], self._sds[3], self._sds[4], self._sds[5] )
                player2.SetBotPosition( 100, 270 )
                player2.ArmCalc()
                player2.box.x_offset = 32
                player2.box.y_offset = 30
                return player2
        def CreateAI( self ):
                AI = ArtificalIntelegence( self._sds[0], self._sds[1], self._sds[2], self._sds[3], self._sds[4], self._sds[5] )
                AI.SetBotPosition( 300, 273 )
                AI.ArmCalc()
                AI.box.x_offset = 8
                AI.box.y_offset = 20
                return AI
        spriteDirectories = property( GetSpriteDirectories, "All the sprite directories." )








#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################









class AI_Controler:
        def __init__( self, AI, targate ):
                self._ag = Agressive()
                self._targate = targate
                self._ai = AI
        def UpdateParamiters( self, AI, targate ):
                self._targate = targate
                self._ai = AI
        def Refresh( self ):
                ManageCollision( self._ai, self._targate )
                self._ai = CM.Update_Physics( self._ai, self._targate )
                if self._ai.BehavorDecide() == "agress":
                        self._ag.UpdateParams( self._ai, self._targate )
                        self._ag.Decision()
                        self._ai = self._ag.Notify( self._ai )
                        self._ai = KeepInLevel( self._ai )
                self._ai.Draw()
                self._ai.Update_Arms()
                return self._ai

        




def Wait():
        w = 0
        while w < 10000:
                w += 1

#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





#More will be implemented.
class GamePackage:
        def __init__( self, levelDir, ko_object ):
                self._thread = GameThread( ko_object, XY(), levelDir + "\Back.png" )
                self._foreground = Sprite_Object( levelDir + "\Foreground.png" )
                self._cloudDir = levelDir + "\Cloud.png"
                self._thread.koP.x = 200
                self._thread.koP.y = 400
                self._clouds = self.InitClouds()
        def InitClouds( self ):
                t = Sprite_Object( self._cloudDir )
                clouds = [t]
                del clouds[0]
                return clouds
        def getThread( self ):
                return self._thread
        def BeginThread( self ):
                self._thread.MainGameThreadBegin()
        def EndThread( self ):
                self._thread.MainGameThreadEnd()
        def setKOposition( self ):
                if self._thread.koP.y > 80:
                        self._thread.koP.y -= 1
        thread = property( getThread, "Main game thread." )






#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################






#Base class for a level, so its not so messy.
class Level:
        def __init__( self, Package, Obj1, Obj2, AI):
                self._player = Obj1
                self._robot = Obj2
                self._package = Package
                self._exploader = Exploader( 100.1, 100.1 )
                self._gameOver = False
                self._end = False                
                if AI == True:
                        self._controller = AI_Controler( Obj2, Obj1 )
                self.Initilize()
        def Draw( self ):
                pass
        def EndGame( self ):
                self._player.Draw()
                self._robot.Draw()
                if self._player.health <= 0:
                        self._exploader.setX( self._player.position.x )
                        self._exploader.setY( self._player.position.y )
                if self._robot.health <= 0:
                        self._exploader.setX( self._robot.position.x )
                        self._exploader.setY( self._robot.position.y )
                self._exploader.Refresh()
                self._package.setKOposition()
                Window.blit( self._package.thread.kO.sprite, (self._package.thread.koP.x, self._package.thread.koP.y) )
                if W == True:
                        self._gameOver = False
                        self._robot.health = 100
                        self._player.health = 100
                        self.Initilize()
                if R == True:
                        self._end = True
                        self.CleanUp()
        def RunLevel( self ):
                pass
        def Initilize( self ):
                pass
        def CleanUp( self ):
                del self._player
                del self._robot
                del self._package
                del self._gameOver
                del self._exploader
        def Logic( self ):
                getEvents()
                self._package.BeginThread()
                if self._gameOver == False:
                        self.RunLevel()
                else:
                        self.EndGame()
                self.Draw()
                self._package.EndThread()
        def getKO( self ):
                return self._package.kO
        def Notify( self ):
                return self._end
        KO = property( getKO )





#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################





class TwoPlayerLevel( Level ):
        def Initilize( self ):
                self._player.SetBotPosition( 100, 270 )
                self._player.ArmCalc()
                self._player.box.x_offset = 32
                self._player.box.y_offset = 30
                self._robot.SetBotPosition( 200, 270 )
                self._robot.ArmCalc()
                self._robot.box.x_offset = 12
                self._robot.box.y_offset = 20
        def RunLevel( self ):
                self._player = Refresh_Bot( self._player, self._robot, Z )
                self._robot = Refresh_Bot( self._robot, self._player, RShift )
                self._player.Update_Arms()
                self._robot.Update_Arms()
                if self._robot.health <= 0 or self._player.health <= 0:
                        self._gameOver = True
        def Draw( self ):        
                        self._package.EndThread()




#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




class OnePlayerLevel( Level ):
        def Initilize( self ):
                self._player.SetBotPosition( 100, 270 )
                self._player.ArmCalc()
                self._player.box.x_offset = 32
                self._player.box.y_offset = 30
                self._robot.SetBotPosition( 200, 270 )
                self._robot.ArmCalc()
                self._robot.box.x_offset = 8
                self._robot.box.y_offset = 20
        def RunLevel( self ):
                self._player = Refresh_Bot( self._player, self._robot, Z )
                self._controller.UpdateParamiters( self._robot, self._player )
                self._robot = self._controller.Refresh()
                self._player.Update_Arms()
                self._robot.Update_Arms()
                if self._robot.health <= 0 or self._player.health <= 0:
                        self._gameOver = True
        def Draw( self ):        
                        self._package.EndThread()





#################################
#                               #
#                               #
#                               #
#                               #
#                               #
#################################




#class ButtonActions:
#        def __init__( self ):
#                self._RunWhat = ""
#        def RunTPL( self, back ):
#                level = TwoPlayerLevel( back, "KO.png" )
#                while level.Notify == False:
#                        level.Logic()
#        def RunOPL( self, back ):
#                level
#        def Run( self, what ):
                

#############MAIN PROECDURE#############


def main():
        os.system( "COLOR 9" )
        print( "Giant Robot Super Battles: \n\n \t Created by Christopher Greeley: \n\n\t Programed With:\n\n\t Python Version 3.22, and Pygame Version 1.92." )
        Game = GamePackage( "City", "KO.png" )
        BlueBot = Robot_Factory( "Blue Bot/Robot_StandF.jpg", "Blue Bot/Robot_StandB.jpg", "Blue Bot/Robot_ArmF.png", "Blue Bot/Robot_ArmB.png", "Blue Bot/Robot_JumpingF.jpg", "Blue Bot/Robot_JumpingB.jpg" )
        RedBot = Robot_Factory( "Red Bot/Robot_StandF.png", "Red Bot/Robot_StandB.png", "Red Bot/Robot_ArmF.png", "Red Bot/Robot_ArmB.png", "Red Bot/Robot_JumpingF.png", "Red Bot/Robot_JumpingB.png" )
        YellowBot = Robot_Factory( "Yellow Bot/Robot_StandF.png", "Yellow Bot/Robot_StandB.png", "Yellow Bot/Robot_ArmF.png", "Yellow Bot/Robot_ArmB.png", "Yellow Bot/Robot_JumpingF.png", "Yellow Bot/Robot_JumpingB.png" )
        GreenBot = Robot_Factory( "Green Bot/Robot_StandF.png", "Green Bot/Robot_StandB.png", "Green Bot/Robot_ArmF.png", "Green Bot/Robot_ArmB.png", "Green Bot/Robot_JumpingF.png", "Green Bot/Robot_JumpingB.png" )
        level = OnePlayerLevel( Game, BlueBot.CreatePlayer1(), GreenBot.CreateAI(), True )
        while level.Notify() == False:
                level.Logic()
        
main()
