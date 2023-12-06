#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "RVCcontroller.c"
#include <gtest/gtest.h>

using namespace std;

TEST(ForwardStateTest, Test0000) {
    string line;
    ifstream fileIn;
    ofstream fileOut;
    vector<string> targets = {
        "청소기가 정상 출력입니다."
    };
    
    // Implement
    fileOut.open("log.txt");
    ControllerInput controllerInput;

    controllerInput.forwardState = 1;
    controllerInput.backwardState = 0;
    controllerInput.obstacleLocation = {0, 0, 0};
    controllerInput.dustExistence = {0};

    controller(controllerInput);
    fileOut.close();

    // Test
    fileIn.open("log.txt");
    for (int i=0; i<targets.size(); i++) {
        getline(fileIn, line);
        EXPECT_EQ(line.compare(targets[i]), 0);
    }
    fileIn.close();
}

TEST(ForwardStateTest, Test0010) {
    string line;
    ifstream fileIn;
    ofstream fileOut;
    vector<string> targets = {
        "청소기가 정상 출력입니다."
    };
    
    // Implement
    fileOut.open("log.txt");
    ControllerInput controllerInput;

    controllerInput.forwardState = 1;
    controllerInput.backwardState = 0;
    controllerInput.obstacleLocation = {0, 0, 1};
    controllerInput.dustExistence = {0};

    controller(controllerInput);
    fileOut.close();

    // Test
    fileIn.open("log.txt");
    for (int i=0; i<targets.size(); i++) {
        getline(fileIn, line);
        EXPECT_EQ(line.compare(targets[i]), 0);
    }
    fileIn.close();
}

TEST(ForwardStateTest, Test0100) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
      "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {0, 1, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test0110) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
      "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 1, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1000) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 정상 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 0, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1010) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 정상 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 0, 1};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1100) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 정상 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 1, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1110) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 정상 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기가 뒤로 이동합니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 1, 1};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test0001) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {0, 0, 0};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test0011) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {0, 0, 1};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test0101) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {0, 1, 0};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test0111) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {0, 1, 1};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1001) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 0, 0};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1011) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 0, 1};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1101) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 1, 0};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(ForwardStateTest, Test1111) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 강한 출력입니다.",
    "청소기가 앞으로 이동을 정지합니다.",
    "청소기의 출력이 종료되었습니다.",
    "청소기가 뒤로 이동합니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 1;
  controllerInput.backwardState = 0;
  controllerInput.obstacleLocation = {1, 1, 1};
  controllerInput.dustExistence = {1};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(BackwardStateTest, Test0110) {
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
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(BackwardStateTest, Test0010) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 뒤로 이동을 정지합니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 0;
  controllerInput.backwardState = 1;
  controllerInput.obstacleLocation = {0, 0, 1};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(BackwardStateTest, Test0000) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 뒤로 이동을 정지합니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기를 왼쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 0;
  controllerInput.backwardState = 1;
  controllerInput.obstacleLocation = {0, 0, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}

TEST(BackwardStateTest, Test0100) {
  string line;
  ifstream fileIn;
  ofstream fileOut;
  vector<string> targets = {
    "청소기가 뒤로 이동을 정지합니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기를 오른쪽으로 회전시킵니다.",
    "청소기가 앞으로 이동합니다.",
    "청소기가 정상 출력입니다."
  };
  
  // Implement
  fileOut.open("log.txt");
  ControllerInput controllerInput;

  controllerInput.forwardState = 0;
  controllerInput.backwardState = 1;
  controllerInput.obstacleLocation = {0, 1, 0};
  controllerInput.dustExistence = {0};

  controller(controllerInput);
  fileOut.close();

  // Test
  fileIn.open("log.txt");
  for (int i=0; i<targets.size(); i++) {
      getline(fileIn, line);
      EXPECT_EQ(line.compare(targets[i]), 0);
  }
  fileIn.close();
}