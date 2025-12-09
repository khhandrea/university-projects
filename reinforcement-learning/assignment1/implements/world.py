class GridWorld:
    def __init__(
            self, 
            size:int=4, 
            start:int=0,
            goal:int=-1
            ) -> None:
        self.__size = size
        self.__state = 0
        self.__start = start
        self.__goal = goal
        if goal == -1:
            self.__goal = size * size - 1

    def step(self, action):
        if action == 0:
            self.__move_left()
        elif action == 1:
            self.__move_up()
        elif action == 2:
            self.__move_right()
        elif action == 3:
            self.__move_down()

        reward = -1
        done = self.__is_done()
        return self.__state, reward, done

    def reset(self) -> None:
        self.__state = self.__start
        return self.__state
    
    def __move_left(self): 
        if self.__state % self.__size != 0:
            self.__state -= 1

    def __move_right(self):
        if self.__state % self.__size != self.__size - 1:
            self.__state += 1
    
    def __move_up(self): 
        if self.__state >= self.__size:
            self.__state -= self.__size

    def __move_down(self): 
        if self.__state < self.__size * (self.__size - 1):
            self.__state += self.__size

    def __is_done(self):
        return self.__state == self.__goal