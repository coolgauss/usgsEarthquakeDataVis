#ifndef __EARTHQUAKE2__
#define __EARTHQUAKE2__

#define blend(a, b, x) ((a) * (1 - (x)) + (b) * (x))

struct Mercator{
  float zoom = 1.0;
  float magUnit = 31.6227; // unit = pow(10, 1.5);
  int timelapseGroupFrames = 50; // good number for a month data
  int maxAnimFrames = 24;

  float _tilezoom() {
    return (256 / PI) * pow(2, this.zoom);
  }

  float getX(float lon) {
    lon = radians(lon);
    return this->_tilezoom() * (lon + PI);
  }

  float getY(float lat) {
    lat = radians(lat);
    float x = tan(PI / 4 + lat / 2);
    // negate per houdini y up is +
    return this->_tilezoom() * (PI - log(x)) * -1;
  }

  float getLinearMag(float mag) {
    // Calcualate linear magnitude
    float lmag = pow(this.magUnit, mag);
    return sqrt(lmag);
  }

  float getNormalizedAnimFrames(int ptnum; float currentFrame) {
    // Create grouped points to animate together
    float frame = ptnum/this.timelapseGroupFrames;
    // Get the time diff current sampple to current frame
    int deltaf = int(currentFrame) - frame;
    // Get normalized delta frames
    return clamp(float(deltaf)/this.maxAnimFrames, 0, 1);
  }
}
#endif
