__author__ = 'ratcave'

# First import pyglet and turn off the debug_gl option.  This is great for performance!
import pyglet
pyglet.options['debug_gl'] = False

from .core import transformations, utils
import resources
from .core import utils
from .core.camera import Camera
from .core.mesh import Mesh
from .core.scene import Scene
from .core.window import Window
from .core.wavefront import WavefrontReader
from .core.mixins import Physical


# Create the projector
def __build_projector():
    import pickle
    import appdirs
    from os import path

    proj_file = path.join(appdirs.user_data_dir("ratCAVE"), "projector_data.pickle")  # TODO: Use relative import to get data_dir from ratCAVE.__init__.py
    if path.exists(proj_file):
        projector_data = pickle.load(open(proj_file))
        projector = Camera(position=projector_data['position'],
                           rotation=projector_data['rotation'],
                           fov_y=projector_data['fov_y'])
    else:
        print("Cannot auto-create projector until opti_projector_calibration script is run.  projector object will be set to None.")
        projector = None

    return projector

projector = __build_projector()



__all__ = ['Camera', 'Mesh', 'Physical', 'Scene', 'Window', 'WavefrontReader', 'projector']

