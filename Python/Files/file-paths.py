#A module for portable operation system methods
import os

#Get file path of the currently executing file, not the path that you are executing from
file = os.path.realpath(__file__)
print('Executing file: ' + __file__)

#Same for folder only
folder = os.path.dirname(file)
print('Folder: ' + folder)