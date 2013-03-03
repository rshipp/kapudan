cmake_minimum_required(VERSION 2.8)
project(kapudan_daemon_helper)

include(CheckLibraryExists)
find_package( KDE4 REQUIRED ) 
include(MacroLibrary)

add_definitions(${QT_DEFINITIONS} ${KDE4_DEFINITIONS})
include_directories(${KDE4_INCLUDES})

kde4_add_executable(daemon_helper  daemon_helper.cpp)
find_package(Qt4 COMPONENTS QtCore QtDBus REQUIRED)
target_link_libraries(daemon_helper ${KDE4_KDECORE_LIBS} ${QT_QTDBUS_LIBRARY})
install(TARGETS daemon_helper DESTINATION ${LIBEXEC_INSTALL_DIR})
 
kde4_install_auth_helper_files(daemon_helper org.chakraproject.kapudan.daemon root)
kde4_install_auth_actions(org.chakraproject.kapudan org.chakraproject.kapudan.daemon.actions)
