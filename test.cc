#include <fstream>
#include <iostream>
#include <vector>
#include "RVCcontroller.c"

using namespace std;

int main() {
    string line;
    ifstream fileIn;
    ofstream fileOut;
    vector<string> targets = {
        ""
    };
    
    // Implement
    fileOut.open("log.txt");
    ControllerInput controllerInput;

    controllerInput.forwardState = 0;
    controllerInput.backwardState = 1;
    controllerInput.obstacleLocation = {0, 1, 1};
    controllerInput.dustExistence = {0};

    controller(controllerInput);
    fileOut.close();

    // Test
    fileIn.open("log.txt");
    for (int i=0; i<targets.size(); i++) {
        getline(fileIn, line);
        cout << line.compare(targets[i]) << endl;
    }
    fileIn.close();
    
    return 0;
}