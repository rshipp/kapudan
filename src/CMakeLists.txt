set(kapudan_srcs kapudan.cpp)
message(${ui})
add_executable(kapudan ${kapudan_srcs} ${ui_hdrs})
target_link_libraries(kapudan KF5::ConfigCore KF5::ConfigGui Qt5::Widgets)
