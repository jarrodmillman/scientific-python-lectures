from distutils.core import Extension, setup

import numpy

# define the extension module
cos_module_np = Extension(
    "cos_module_np", sources=["cos_module_np.c"], include_dirs=[numpy.get_include()]
)

# run the setup
setup(ext_modules=[cos_module_np])
