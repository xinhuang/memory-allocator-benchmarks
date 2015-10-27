project(linux-scalability)

add_executable(linux-scalability linux-scalability.c ptbarrier.h)

target_link_libraries(linux-scalability libhoard ${CMAKE_THREAD_LIBS_INIT})

if (UNIX)
  target_link_libraries(linux-scalability m)
endif ()
