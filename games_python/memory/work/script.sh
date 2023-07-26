#!/bin/bash

# Compile the application with debug symbols
g++ -g your_application.cpp -o your_application

# Run the application tests
./your_application_tests

# Check for memory leaks using Valgrind
valgrind --leak-check=full ./your_applicatio
