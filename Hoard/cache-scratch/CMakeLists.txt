project(cache-scratch)

add_executable(cache-scratch cache-scratch.cpp)

target_link_libraries(cache-scratch libhoard ${CMAKE_THREAD_LIBS_INIT})
