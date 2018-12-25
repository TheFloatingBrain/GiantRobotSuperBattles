import pygame, sys, pygame.mixer
from pygame.locals import *
import math
import random
import os
from Sprite_Object import Sprite_Object
import socket
import threading

GAME_PORT = 27020
LOCAL_IP = "127.0.0.1"

#pygame.init()
#Window=pygame.display.set_mode((600,400),0,32)

def PollEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
                        pygame.quit()

#guiBack = Sprite_Object( "GuiScreen.png" )


def Client():
    global GAME_PORT
    global LOCAL_IP
    client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    client.connect( ( LOCAL_IP, GAME_PORT ) )
    client.send( input( "What do you want to say?! ---> " ) )
    print( "Got back " + client.recv( 256 ) )


def Server():
    global GAME_PORT
    global LOCAL_IP
    numHello = 0
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.bind( ( LOCAL_IP, LOCAL_PORT ) )
    server.listen()
    while True:
        ( client, address ) = server.accept()
        print( "Hello from: " + address )
        print( "Client says: " + client.recv( 256 ) )
        print( "Sending hello " + str( numHello ) )
        numHello += 1
        server.send( "hello" + str( numHello ) )



#while True:
 #   Window.blit( guiBack.sprite, ( 0, 0 ) )
  #  PollEvents()
   # pygame.display.update()
