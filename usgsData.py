import hou

class UsgsCsv(object):
    def __init__(self, eqDataFilePath):
        self._eqDataFilePath = eqDataFilePath

    @property
    def eqDataFilePath(self):
        return self._eqDataFilePath

    @property
    def node(self):
        return hou.pwd()

    @property
    def geo(self):
        return self.node.geometry()

    def _addHouAttributes(self):
        self.geo.addAttrib(hou.attribType.Point, "lat", 0.0)
        self.geo.addAttrib(hou.attribType.Point, "lon", 0.0)
        self.geo.addAttrib(hou.attribType.Point, "mag", 0.0)
        self.geo.addAttrib(hou.attribType.Point, "day", '')
        self.geo.addAttrib(hou.attribType.Point, "time", '')
        self.geo.addAttrib(hou.attribType.Point, "frame", -1)

    def _setHouAttributes(self, point, lat, lon, mag, day, time):
        point.setAttribValue("lat", lat)
        point.setAttribValue("lon", lon)
        point.setAttribValue("mag", mag)
        point.setAttribValue("day", day)
        point.setAttribValue("time", time)

    def getData(self):
        # Add data point attributes
        self._addHouAttributes()
        import csv
        with open(self.eqDataFilePath, 'r') as f:
            reader = csv.reader(f)
            reader.next()
            for data in reader:
                # some data has non-proper or empty strings
                try:
                    day = data[0].split('T')[0]
                    _time = data[0].split('T')[1].split(':')
                    h = _time[0]
                    m = _time[1]
                    s = _time[2].split('.')[0]
                    time = '{}:{}:{}'.format(h, m, s)
                    lat = float(data[1])
                    lon = float(data[2])
                    mag = float(data[4])
                except Exception, e:
                    print 'Could not process the data - {}'.format(data)
                    continue
                # Create a point
                point = self.geo.createPoint()

                # Set data point attributs
                self._setHouAttributes(point, lat, lon, mag, day, time)
