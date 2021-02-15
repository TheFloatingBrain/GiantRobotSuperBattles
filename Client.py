#import pygame, sys, pygame.mixer
#from pygame.locals import *
import math
import random
import os
#from Sprite_Object import Sprite_Object
import socket
import _thread
import time

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
    while True:
        client = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
        client.connect( ( LOCAL_IP, GAME_PORT ) )
        client.send( bytes( input( "What do you want to say?! ---> " ).encode( 'utf-8' ) ) )
        print( "Got back " + str( client.recv( 256 ).decode() ) )


def Server():
    global GAME_PORT
    global LOCAL_IP
    numHello = 0
    server = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    server.bind( ( LOCAL_IP, GAME_PORT ) )
    server.listen()
    while True:
        ( client, address ) = server.accept()
        print( "Hello from: " + str( address ) )
        print( "Client says: " + str( client.recv( 256 ).decode() ) )
        print( "Sending hello " + str( numHello ) )
        client.send( bytes( ( "hello" + str( numHello ) ).encode( 'utf-8' ) ) )
        numHello += 1

_thread.start_new_thread( Server, () )
_thread.start_new_thread( Client, () )

while True:
    pass

#while True:
 #   Window.blit( guiBack.sprite, ( 0, 0 ) )
  #  PollEvents()
   # pygame.display.update()
