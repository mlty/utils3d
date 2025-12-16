from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

setup(
    name="mesh_inpaint_processor",
    ext_modules=[
        Pybind11Extension(
            "mesh_inpaint_processor",
            ["mesh_inpaint_processor.cpp"],
        )
    ],
    cmdclass={"build_ext": build_ext},
)