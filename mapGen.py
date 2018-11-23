import hou

class MapBoxHandler(object):
    CAM_NAME = 'map_cam'
    MAPBOX_TOKEN_FILE_PARMNAME = 'mapbox_token_file'
    USE_PICKLED_TOKEN_PARMNAME = 'use_pickled_token'
    MAPBOX_TOKEN_STR_PARMNAME  = 'mapbox_token_string'
    LAT_CENTER_PARMNAME        = 'lat_center'
    LON_CENTER_PARMNAME        = 'lon_center'
    ZOOM_PARMNAME              = 'zoom'
    RESOLUTION_PARMNAME        = 'resolution'
    MAPPATH_PARMNAME           = 'mappath'

    def __init__(self):
        pass

    @property
    def node(self):
        return hou.pwd()

    def _getPickledMapboxToken(self):
        import cPickle as pickle
        pickledTokenPath = hou.evalParm(self.MAPBOX_TOKEN_FILE_PARMNAME)
        #import os
        #pickledTokenPath = os.path.join(hou.getenv('HIP'), 'pickledToken.tok')
        with open(pickledTokenPath, 'r') as f:
            token = pickle.load(f)
        return token

    def _getMapboxToken(self):
        if hou.evalParm(self.USE_PICKLED_TOKEN_PARMNAME):
            return self._getPickledMapboxToken()
        return hou.evalParm(self.MAPBOX_TOKEN_STR_PARMNAME)

    def _getLatCenter(self):
        return hou.evalParm(self.LAT_CENTER_PARMNAME)

    def _getLonCenter(self):
        return hou.evalParm(self.LON_CENTER_PARMNAME)

    def _getZoom(self):
        return hou.evalParm(self.ZOOM_PARMNAME)

    def _getResolution(self):
        return hou.evalParmTuple(self.RESOLUTION_PARMNAME)

    def generateMap(self):
        token = self._getMapboxToken()
        lat = self._getLatCenter()
        lon = self._getLonCenter()
        zoom = self._getZoom()
        res = self._getResolution()
        # XXX: Currently, we only consider the simple style map
        urlPrefix = 'https://api.mapbox.com/styles/v1/mapbox/streets-v8/static'
        #urlPrefix = 'https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v10/static
        url = '{}/{},{},{},0/{}x{}?access_token={}'.format(urlPrefix, lon, \
            lat, zoom, res[0], res[1], token)

        import requests
        # get a world map
        print 'requesting url - {}'.format(url)
        res = requests.get(url, stream=True)
        outmap = hou.evalParm(self.MAPPATH_PARMNAME)
        with open(outmap, 'wb') as f:
            f.write(res.content)
        print 'wrote an image - {}'.format(outmap)

    def setCurrentViewportCam(self):
        import toolutils
        cam = hou.node('{}/{}'.format(self.node.path(), self.CAM_NAME))
        sceneViewer = toolutils.sceneViewer()
        viewport = sceneViewer.curViewport()
        viewport.setCamera(cam)

def refreshGlCache():
    hou.hscript('glcache -c')
