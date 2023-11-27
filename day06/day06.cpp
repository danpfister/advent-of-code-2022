#include <file_utils.h>
#include <cstdint>
#include <bit>

void part1(std::vector<std::string> input) {
    std::string buffer = input[0];

    std::uint32_t values = 0;
    int currentIndex = 0;
    // iterate until there are 4 ones in the binary representation of the window
    while (std::popcount(values) != 4) {
        std::string window =  buffer.substr(currentIndex, 4);
        values = 0;
        for (const int & symbol : window) {
            // each letter getts mapped to a different position in the 32bit int
            values |= 0b1 << (symbol - 97);
        }
        currentIndex++;
    }

    std::cout << "The location of the marker is at: " << currentIndex + 3 << std::endl;
}

void part2(std::vector<std::string> input) {
    std::string buffer = input[0];

    std::uint32_t values = 0;
    int currentIndex = 0;
    while (std::popcount(values) != 14) {
        std::string window =  buffer.substr(currentIndex, 14);
        values = 0;
        for (const int & symbol : window) {
            values |= 0b1 << (symbol - 97);
        }
        currentIndex++;
    }
    
    std::cout << "The location of the marker is at: " << currentIndex + 13 << std::endl;
}

int main() {
    std::vector<std::string> input = FileReader::readFile("C:/Users/Daniel/Github/advent-of-code-2022/day06/input.txt");

    part1(input);
    part2(input);

    return 0;
}