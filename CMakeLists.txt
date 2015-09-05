cmake_minimum_required (VERSION 3.0)
project (Kapudan)
set(CMAKE_EXPORT_COMPILE_COMMANDS "ON")

find_package(ECM REQUIRED NO_MODULE)
set(CMAKE_MODULE_PATH ${ECM_MODULE_PATH})
include(KDEInstallDirs)
include(KDECompilerSettings)
kde_enable_exceptions()
include(ECMEnableSanitizers)
include(KDECMakeSettings)


# Find includes in corresponding build directories
set(CMAKE_INCLUDE_CURRENT_DIR ON)
include_directories(src/kapudan)
find_package(Qt5 COMPONENTS Widgets Core Concurrent)
find_package(KF5Config)
# Instruct CMake to run moc automatically when needed.
set(CMAKE_AUTOMOC ON)
add_definitions(-std=c++14)


# add_executable(dupfinder ${dupfinder_SRCS} ${UIS_HDRS})
# target_link_libraries(dupfinder ${xxHash_LIBRARY} Qt5::Widgets Qt5::Concurrent)
# set_property( TARGET dupfinder APPEND_STRING PROPERTY COMPILE_FLAGS)
# qt5_use_modules(dupfinder Widgets)


file(GLOB  ui_files "ui/*.ui")
message("ui files: ${ui_files}")
qt5_wrap_ui(ui_hdrs ${ui_files})
set(kapudan_srcs src/kapudan.cpp src/progress_pie.cpp)
set(kapudan_screen_srcs
  src/kapudan/screens/scrWelcome.cpp
  src/kapudan/screens/scrFolder.cpp
  )
add_executable(kapudan ${kapudan_srcs} ${kapudan_screen_srcs} ${ui_hdrs})
target_link_libraries(kapudan KF5::ConfigCore KF5::ConfigGui Qt5::Widgets)

# install(TARGETS dupfinder RUNTIME DESTINATION bin)
