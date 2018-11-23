'''
# We assume the pythonrc.py has,
import os
USER = os.getenv('USER')
sys.path.append(<usgsEarthquakeDataVis_PROJECT_PATH>)

# Macos pythonrc.py location example:
/Applications/Houdini/Houdini17.0.352/Frameworks/Houdini.framework/Versions/Current/Resources/houdini/python2.7libs/pythonrc.p
'''

from eqDataVisLib import mapGen
reload(mapGen)

mapBoxHandle = mapGen.MapBoxHandler()

def genMap():
    mapBoxHandle.generateMap()

def refreshGlCache():
    mapGen.refreshGlCache()
        
def setCurrentViewportCam():
    mapBoxHandle.setCurrentViewportCam()
    
