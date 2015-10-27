cmake_minimum_required(VERSION 3.1)

project(memory_allocator_benchmarks)

set(ALLOCATOR "" CACHE STRING "Allocator that is going to be used.")
set(ALLOCATOR_ROOT "" CACHE STRING "Allocator path to find the allocator. (-DALLOCATOR=<NAME>)")
if ("${ALLOCATOR}" STREQUAL "" OR "${ALLOCATOR_ROOT}" STREQUAL "")
  message(FATAL_ERROR "ALLOCATOR and ALLOCATOR_ROOT must be specified! (-DALLOCATOR_ROOT=<PATH>)")
else ()
  # if (NOT EXISTS "${ALLOCATOR_ROOT}/${ALLOCATOR}")
  #   message(FATAL_ERROR "${ALLOCATOR} cannot be found in ${ALLOCATOR_ROOT}!")
  # else ()
    message("Will use ${ALLOCATOR} in ${ALLOCATOR_ROOT} as memory allocator.")
  # endif ()
endif ()

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

file(COPY "${ALLOCATOR_ROOT}" DESTINATION "${CMAKE_RUNTIME_OUTPUT_DIRECTORY}")
message("Copying ${ALLOCATOR_ROOT} to ${CMAKE_RUNTIME_OUTPUT_DIRECTORY} done")

link_directories(${ALLOCATOR_ROOT})

if (UNIX)
elseif (MSVC)
  add_definitions(-DNOMINMAX)
endif ()

set(bitness 32)
if(CMAKE_SIZEOF_VOID_P EQUAL 8)
  set(bitness 64)
endif()

set(CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 11)

find_package(Threads REQUIRED)

add_subdirectory(Hoard)
add_subdirectory(LocklessInc)
