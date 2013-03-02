kde4_install_auth_actions(org.chakraproject.kapudan org.chakraproject.kapudan.daemon.actions)

kde4_add_executable(daemon_helper  daemon_helper.cpp)
find_package(Qt4 COMPONENTS QtCore QtDBus REQUIRED)
target_link_libraries(daemon_helper ${KDE4_KDECORE_LIBS})
install(TARGETS daemon_helper DESTINATION ${LIBEXEC_INSTALL_DIR} ${QT_QTDBUS_LIBRARY})
 
kde4_install_auth_helper_files(daemon_helper org.chakraproject.kapudan.daemon root)
