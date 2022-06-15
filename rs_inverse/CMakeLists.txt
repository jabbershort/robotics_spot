cmake_minimum_required(VERSION 2.8.3)
project(rs_inverse)

find_package(catkin REQUIRED COMPONENTS)

catkin_package()

catkin_install_python(
	PROGRAMS
	    scripts/Bezier.py
      scripts/env_tester.py
      scripts/gui_spot.py
      scripts/LegKinematics.py
      scripts/LieAlgebra.py
      scripts/SpotKinematics.py
      scripts/stand_mode_spot.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
