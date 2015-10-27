project(t-test1)

add_executable(t-test1 t-test1.c)

target_link_libraries(t-test1 ${ALLOCATOR} ${CMAKE_THREAD_LIBS_INIT})
