project(larson)

add_executable(larson larson.cpp)

target_link_libraries(larson ${ALLOCATOR} ${CMAKE_THREAD_LIBS_INIT})
