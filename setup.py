import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python36\tcl\tk8.6'

executables_ = [ cx_Freeze.Executable( 'Main.py' ) ]

cx_Freeze.setup(
    name = "Giant Robot Super Battles!",
    options={ "build_exe" : { "packages" : [ "pygame" ],
                              "include_files":["Red Bot Icon.png",
                                                "Yellow Bot Icon.png",
                                                "ReadMe.txt",
                                                "RadC.png",
                                                "Press H For Help.png",
                                                "MountC.png",
                                                "KO.png",
                                                "GushF.png",
                                                "GushB.png",
                                                "GuiScreen.png",
                                                "Green Bot Icon.png",
                                                "Explosion.png",
                                                "DefaultBack.png",
                                                "Default.png",
                                                "Default.jpg",
                                                "Cursor.png",
                                                "CityC.png",
                                                "Choose Your Robot.png",
                                                "Choose Stage.png",
                                                "Blue Bot Icon.png",
                                                "Battary.png",
                                                "Bar.png",
                                                "AltR.png",
                                                "AltM.png",
                                                "AltC.png",
                                                "2Player.png",
                                                "2Palt.png",
                                                "1Player.png",
                                                "1Palt.png",
                                                "Yellow Bot/Robot_ArmB.png",
                                                "Yellow Bot/Robot_ArmF.png",
                                                "Yellow Bot/Robot_JumpingB.png",
                                                "Yellow Bot/Robot_JumpingF.png",
                                                "Yellow Bot/Robot_StandB.png",
                                                "Yellow Bot/Robot_StandF.png",
                                                "Red Bot/Robot_ArmB.png",
                                                "Red Bot/Robot_ArmF.png",
                                                "Red Bot/Robot_JumpingB.png",
                                                "Red Bot/Robot_JumpingF.png",
                                                "Red Bot/Robot_StandB.png",
                                                "Red Bot/Robot_StandF.png",
                                                "Blue Bot/Robot_ArmB.png",
                                                "Blue Bot/Robot_ArmF.png",
                                                "Blue Bot/Robot_JumpingB.jpg",
                                                "Blue Bot/Robot_JumpingF.jpg",
                                                "Blue Bot/Robot_StandB.jpg",
                                                "Blue Bot/Robot_StandF.jpg",
                                                "Green Bot/Robot_ArmB.png",
                                                "Green Bot/Robot_ArmF.png",
                                                "Green Bot/Robot_JumpingB.png",
                                                "Green Bot/Robot_JumpingF.png",
                                                "Green Bot/Robot_StandB.png",
                                                "Green Bot/Robot_StandF.png",
                                                "Radioactive/Back.png",
                                                "Radioactive/Cloud.png",
                                                "Radioactive/Foreground.png",
                                                "Moutain/Back.png",
                                                "Moutain/Cloud.png",
                                                "Moutain/Foreground.png",
                                                "City/Back.png",
                                                "City/Cloud.png",
                                                "City/Foreground.png",
                                                "Sounds/KO.wav",
                                                "Sounds/Boom.wav",
                                                "Sounds/66951__benboncan__boxing-bell.wav",
                                                "Sounds/Hit/MetalHit0.wav",
                                                "Sounds/Hit/MetalHit1.wav",
                                                "Sounds/Hit/MetalHit2.wav",
                                                "Sounds/Hit/MetalHit3.wav",
                                                "Sounds/Jump/Jump.wav",
                                                "Sounds/Jump/Land.wav",
                                                "Sounds/Robo/Walk.wav",
                                                "Sounds/Wind/Gush.wav", 
                                                "Sprite_Object.py"
                                                ] } }, executables = executables_ )
