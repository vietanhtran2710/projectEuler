#include<iostream>

using namespace std;

bool sameCounter(int value1, int value2) {
    int countDigit1[10] = {0};
    int countDigit2[10] = {0};
    while (value1 != 0) {
        countDigit1[value1 % 10]++;
        value1 /= 10;
    }
    while (value2 != 0) {
        countDigit2[value2 % 10]++;
        value2 /= 10;
    }
    for (int i = 0; i < 10; i++)
        if (countDigit1[i] != countDigit2[i]) return false;
    return true;
}

int main() {
    bool found = false; int number = 1;
    while (!found) {
        bool isValid = true;
        for (int i = 2; i < 7; i++)
            if (!sameCounter(number, number * i)) {
                isValid = false;
                break;
            }
        if (isValid) {
            cout << number << endl;
            found = true;
        }
        number++;
    }
    return 0;
}
