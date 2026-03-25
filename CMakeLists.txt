cmake_minimum_required(VERSION 3.21...3.28)
project(flowstab LANGUAGES C CXX)

find_package(Python REQUIRED COMPONENTS Interpreter Development.Module NumPy)

# Define common compile options for all Cython modules
add_library(flowstab_compile_options INTERFACE)
target_compile_options(flowstab_compile_options INTERFACE -O3)
target_compile_definitions(flowstab_compile_options INTERFACE NPY_NO_DEPRECATED_API=NPY_1_7_API_VERSION)

function(add_cython_cpp_module TARGET_NAME CYTHON_SOURCE)
    set(GENERATED_CXX_FILE "${CMAKE_CURRENT_BINARY_DIR}/${TARGET_NAME}.cxx")
    
    # Extract the directory path of the Cython source file (e.g., src/flowstab)
    get_filename_component(CYTHON_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/${CYTHON_SOURCE}" DIRECTORY)
    
    add_custom_command(
        OUTPUT "${GENERATED_CXX_FILE}"
        COMMAND "${Python_EXECUTABLE}" -m cython -3 --cplus "${CMAKE_CURRENT_SOURCE_DIR}/${CYTHON_SOURCE}" -o "${GENERATED_CXX_FILE}"
        DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/${CYTHON_SOURCE}"
        COMMENT "Generating C++ source from Cython definition: ${CYTHON_SOURCE}"
    )
    
    # Create the Python extension module
    # We only pass the generated .cxx file because sparse_accumulator.cpp is 
    # included via the #include directive injected by Cython from the .pxd
    Python_add_library(${TARGET_NAME} MODULE WITH_SOABI "${GENERATED_CXX_FILE}")
    target_link_libraries(${TARGET_NAME} PRIVATE Python::NumPy flowstab_compile_options)
    
    # Map the source directory to the compiler's include path so it can find 
    # "sparse_accumulator.cpp" and "sparse_accumulator.h" during compilation
    target_include_directories(${TARGET_NAME} PRIVATE "${CYTHON_SOURCE_DIR}")
    
    # Install the compiled module into the flowstab package directory
    install(TARGETS ${TARGET_NAME} DESTINATION flowstab)
endfunction()

# Define the modules to be built
add_cython_cpp_module(_cython_fast_funcs "src/flowstab/_cython_fast_funcs.pyx")
add_cython_cpp_module(_cython_sparse_stoch "src/flowstab/_cython_sparse_stoch.pyx")
