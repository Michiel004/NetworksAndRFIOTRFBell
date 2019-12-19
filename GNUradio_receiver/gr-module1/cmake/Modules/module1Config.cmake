INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_MODULE1 module1)

FIND_PATH(
    MODULE1_INCLUDE_DIRS
    NAMES module1/api.h
    HINTS $ENV{MODULE1_DIR}/include
        ${PC_MODULE1_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    MODULE1_LIBRARIES
    NAMES gnuradio-module1
    HINTS $ENV{MODULE1_DIR}/lib
        ${PC_MODULE1_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(MODULE1 DEFAULT_MSG MODULE1_LIBRARIES MODULE1_INCLUDE_DIRS)
MARK_AS_ADVANCED(MODULE1_LIBRARIES MODULE1_INCLUDE_DIRS)

