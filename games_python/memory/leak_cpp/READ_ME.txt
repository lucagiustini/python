g++ -g create_leak.cpp -o create_leak
valgrind --leak-check=full ./create_leak