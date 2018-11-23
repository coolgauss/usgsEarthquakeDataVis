#!/usr/bin/python

# ---------------------------------------
# Global imports
# ---------------------------------------
import sys
import os
import argparse

# ---------------------------------------
# Defaults
# ---------------------------------------
VERBOSE = False

# ---------------------------------------
# Arg parse
# ---------------------------------------

def _ParseArg():
    parser = argparse.ArgumentParser(description='TBD')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='output more description')
    parser.add_argument('-rootDir', dest='rootDir', action='store',
                        default='',
                        help='root directory to set up data vis dir/files.')
    args = parser.parse_args()
    if args.verbose is True:
        global VERBOSE
        VERBOSE = True
    return args

# ---------------------------------------
# Utility Functions
# ---------------------------------------

class Project(object):
    RMAN_TEX_DIRNAME = 'data/tex'
    def __init__(self, rootDir):
        self._rootDir = rootDir

    @property
    def rootDir(self):
        return self._rootDir

    @property
    def texDir(self):
        if not os.path.isdir(self.rootDir):
            return None
        return os.path.join(self.rootDir, self.RMAN_TEX_DIRNAME)

    def Setup(self):
        if not self.texDir:
            print 'error: {} is not a directory.'.format(self.rootDir)
            return 1
        if not os.path.exists(self.texDir):
            print 'making dirs: {}'.format(self.texDir)
            os.makedirs(self.texDir)
        return 0

# ---------------------------------------
# Main Function
# ---------------------------------------

def main():
    parser = _ParseArg()
    rootDir = parser.rootDir
    
    project = Project(rootDir)
    res = project.Setup()
    return res

if __name__ == '__main__':
    sys.exit(main())
