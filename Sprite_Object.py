import pygame, sys
from pygame.locals import *

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
