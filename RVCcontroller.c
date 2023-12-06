#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef struct ObstacleLocation // 장애물 유무 struct
{
    short F;
    short L;
    short R;
} ObstacleLocation;

typedef struct DustExistence // 먼지 유무 sturct
{
    short Dust;
} DustExistence;

typedef struct ControllerInput
{
    ObstacleLocation obstacleLocation;
    DustExistence dustExistence;
    short forwardState;
    short backwardState;
} ControllerInput;

typedef struct CleanerCommand // 먼지 유무 & 정지 유무에 struct
{
    short On;
    short Off;
    short Up;
} CleanerCommand;

typedef struct CleanerInterfaceInput // 먼지 유무 & 정지 유무에 struct
{
    short On;
    short Off;
    short Up;
} CleanerInterfaceInput;

typedef struct MotorInterfaceInput // Controller에서 센서 데이터 취합해서 만드는 interface Input
{
    short enableMoveForward;
    short disableMoveForward;
    short enableMoveBackward;
    short disableMoveBackward;
    short turnLeft;
    short turnRight;
} MotorInterfaceInput;

void controller(ControllerInput);
short fronSensorInterface();
short leftSensorInterface();
short rightSensorInterface();
short dustSensorInterface();
ObstacleLocation determineObstacleLocation();
DustExistence determineDustExistence();
void moveForward(short enable);
void turnLeft();
void turnRight();
void moveBackward(short enable);
void cleanerCommand(CleanerCommand command);
void motorInterface(MotorInterfaceInput input);
void cleanerInterface(CleanerInterfaceInput input);

int main_(void)
{
    short forwardState = 1;
    short backwardState = 0;
    ObstacleLocation obstacleLocation;
    DustExistence dustExistence;
    ControllerInput controllerInput;

    moveForward(1);
    CleanerCommand cleanerInput = {1, 0, 0};
    cleanerCommand(cleanerInput);
    

    while (1)
    {
        obstacleLocation = determineObstacleLocation();
        dustExistence = determineDustExistence();

        controllerInput.forwardState = forwardState;
        controllerInput.backwardState = backwardState;
        controllerInput.obstacleLocation = obstacleLocation;
        controllerInput.dustExistence = dustExistence;

        controller(controllerInput);

        sleep(1);
    }
}

void controller(ControllerInput controllerInput) {
    short forwardState = controllerInput.forwardState;
    short backwardState = controllerInput.backwardState;
    ObstacleLocation obstacleLocation = controllerInput.obstacleLocation;
    DustExistence dustExistence = controllerInput.dustExistence;

    CleanerCommand cleanerInput = {0, 0, 0};

    if (forwardState)
        {
            if (dustExistence.Dust)
            {
                cleanerInput.Up = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.Up = 0;
            }
            else
            {
                cleanerInput.On = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.On = 0;
            }

            if (obstacleLocation.F && !obstacleLocation.L)
            {
                // Turn left
                forwardState = 0;
                moveForward(0);
                cleanerInput.Off = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.Off = 0;
                
                turnLeft();
                forwardState = 1;
                moveForward(1);
                cleanerInput.On = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.On = 0;
            }
            else if (obstacleLocation.F && obstacleLocation.L && !obstacleLocation.R)
            {
                // Turn right
                forwardState = 0;
                moveForward(0);
                cleanerInput.Off = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.Off = 0;
                
                turnRight();
                forwardState = 1;
                moveForward(1);
                cleanerInput.On = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.On = 0;
            }
            else if (obstacleLocation.F && obstacleLocation.L && obstacleLocation.R)
            {
                // Move backward
                forwardState = 0;
                moveForward(0);
                cleanerInput.Off = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.Off = 0;

                backwardState = 1;
                moveBackward(1);
            }
        }
        else if (backwardState)
        {
            if (!obstacleLocation.L)
            {
                // Turn left
                backwardState = 0;
                moveBackward(0);
                
                turnLeft();
                forwardState = 1;
                moveForward(1);
                cleanerInput.On = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.On = 0;
            }
            if (obstacleLocation.L && !obstacleLocation.R)
            {
                // Turn right
                backwardState = 0;
                moveBackward(0);
                
                turnRight();
                forwardState = 1;
                moveForward(1);
                cleanerInput.On = 1;
                cleanerCommand(cleanerInput);
                cleanerInput.On = 0;
            }
        }
}

short fronSensorInterface()
{
    return 0;
}

short leftSensorInterface()
{
    return 0;
}

short rightSensorInterface()
{
    return 0;
}

short dustSensorInterface()
{
    return 0;
}

ObstacleLocation determineObstacleLocation() // FLR 장애물 struct 받아오고 리턴
{
    struct ObstacleLocation obstacleLocation;
    obstacleLocation.F = fronSensorInterface();
    obstacleLocation.L = leftSensorInterface();
    obstacleLocation.R = rightSensorInterface();
    return obstacleLocation;
}

DustExistence determineDustExistence() // dust Existence struct 받아오고 리턴
{
    struct DustExistence dustExistence;
    dustExistence.Dust = dustSensorInterface();
    return dustExistence;
}

void moveForward(short enable)
{
    MotorInterfaceInput input = {0, 0, 0, 0, 0, 0};
    if (enable)
    {
        input.enableMoveForward = 1;
    }
    else
    {
        input.disableMoveForward = 1;
    }
    motorInterface(input);
}

void turnLeft()
{
    MotorInterfaceInput input = {0, 0, 0, 0, 1, 0};
    short i;

    for (i = 0; i < 5; i++)
    {
        motorInterface(input);
        sleep(1);
    }
}

void turnRight()
{
    MotorInterfaceInput input = {0, 0, 0, 0, 0, 1};
    short i;

    for (i = 0; i < 5; i++)
    {
        motorInterface(input);
        sleep(1);
    }
}

void moveBackward(short enable)
{
    MotorInterfaceInput input = {0, 0, 0, 0, 0, 0};
    if (enable)
    {
        input.enableMoveBackward = 1;
    }
    else
    {
        input.disableMoveBackward = 1;
    }
    motorInterface(input);
}

void cleanerCommand(CleanerCommand command)
{
    CleanerInterfaceInput input = {0, 0, 0};

    if (command.On)
    {
        input.On = 1;
    }
    else if (command.Off)
    {
        input.Off = 1;
    }
    else if (command.Up)
    {
        input.Up = 1;
    }

    cleanerInterface(input);
}

void motorInterface(MotorInterfaceInput input)
{
    short forwardState;
    short backwardState;

    FILE *logFile = fopen("log.txt", "a");
    char *log;

    if (input.enableMoveForward)
    {
        log = "청소기가 앞으로 이동합니다.";
        forwardState = 1;
    }
    else if (input.disableMoveForward)
    {
        log = "청소기가 앞으로 이동을 정지합니다.";
        forwardState = 0;
    }
    else if (input.turnLeft)
    {
        log = "청소기를 왼쪽으로 회전시킵니다.";
    }
    else if (input.turnRight)
    {
        log = "청소기를 오른쪽으로 회전시킵니다.";
    }
    else if (input.enableMoveBackward)
    {
        log = "청소기가 뒤로 이동합니다.";
        backwardState = 0;
    }
    else if (input.disableMoveBackward)
    {
        log = "청소기가 뒤로 이동을 정지합니다.";
    }
    fprintf(logFile, "%s\n", log);
    fclose(logFile);
}

void cleanerInterface(CleanerInterfaceInput input)
{
    FILE *logFile = fopen("log.txt", "a");
    char *log;

    if (input.On)
    {
        log = "청소기가 정상 출력입니다.";
    }
    else if (input.Off)
    {
        log = "청소기의 출력이 종료되었습니다.";
    }
    else if (input.Up)
    {
        log = "청소기가 강한 출력입니다.";
    }
    fprintf(logFile, "%s\n", log);
    fclose(logFile);
}