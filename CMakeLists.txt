file( GLOB LIB_SOURCES RELATIVE medium/*.cpp hard/*.cpp )
file( GLOB LIB_HEADERS RELATIVE medium/*.h hard/*.cpp)
add_library( Leetcode ${LIB_SOURCES} ${LIB_HEADERS} )
# If necessary, use the RELATIVE flag, otherwise each source file may be listed
# with full pathname. RELATIVE may makes it easier to extract an executable name
# automatically.
# file( GLOB APP_SOURCES RELATIVE app/*.cxx )
file( GLOB APP_SOURCES RELATIVE medium/*.cpp hard/*.cpp)
foreach( testsourcefile ${APP_SOURCES} )
    # I used a simple string replace, to cut off .cpp.
    string( REPLACE ".cpp" "" testname ${testsourcefile} )
    add_executable( ${testname} ${testsourcefile} )
    # Make sure YourLib is linked to each app
    target_link_libraries( ${testname} Leetcode )
endforeach( testsourcefile ${APP_SOURCES} )