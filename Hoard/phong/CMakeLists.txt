project(phong)

add_executable(phong phong.c)

target_link_libraries(phong libhoard ${CMAKE_THREAD_LIBS_INIT})
