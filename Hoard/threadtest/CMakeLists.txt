project(threadtest)

add_executable(threadtest threadtest.cpp)

target_link_libraries(threadtest libhoard ${CMAKE_THREAD_LIBS_INIT})
