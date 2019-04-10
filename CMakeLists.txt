cmake_minimum_required(VERSION 3.13)
 project(Leetcode)
 set (CMAKE_CXX_STANDARD 11)
 # add_library( Leetcode ${LIB_SOURCES})
# If necessary, use the RELATIVE flag, otherwise each source file may be listed
# with full pathname. RELATIVE may makes it easier to extract an executable name
# automatically.
# file( GLOB APP_SOURCES RELATIVE app/*.cxx )
file(GLOB APP_SOURCES "${CMAKE_CURRENT_SOURCE_DIR}/HuaHua/*/*/*.cpp")
foreach( testsourcefile ${APP_SOURCES} )
    # I used a simple string replace, to cut off .cpp.
    string( REPLACE ".cpp" "" testname ${testsourcefile} )
    get_filename_component(barename ${testname} NAME)
    message(STATUS ${barename})
    add_executable( ${barename} ${testsourcefile} )
#    target_link_libraries( ${testname} Leetcode )
endforeach( testsourcefile ${APP_SOURCES} )