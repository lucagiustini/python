#include <iostream>
#include <chrono>
#include <thread>

int main()
{
    int SIZE = 10000000;
    // Allocate memory without freeing it
    int *myArray = new int[SIZE];

    // Access the memory to prevent optimization
    for (int i = 0; i < SIZE; ++i)
    {
        myArray[i] = i;
        // std::cout << myArray[i] << " ";
    }

    // Calculate the amount of memory allocated
    std::size_t totalMemory = SIZE * sizeof(int);

    std::cout << "Memory allocated: " << totalMemory << " bytes" << std::endl;

    // Introduce a delay of 5 seconds
    // std::this_thread::sleep_for(std::chrono::seconds(20));

    // Uncomment the following line to introduce a delay
    // std::cin.get();

    // Memory leak - no deletion of allocated memory

    // ############### WARNING !!!! ###############
    // Deallocate the memory
    delete[] myArray;

    return 0;
}
