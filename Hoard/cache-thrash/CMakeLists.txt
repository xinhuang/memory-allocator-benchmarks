project(cache-thrash)

add_executable(cache-thrash cache-thrash.cpp)

target_link_libraries(cache-thrash libhoard ${CMAKE_THREAD_LIBS_INIT})
