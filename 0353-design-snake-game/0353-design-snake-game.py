class SnakeGame:
    
    
    food = []
    width, height = 0,0
    
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = food
        self.width = width
        self.height = height
        self.snake = [(0,0)]
        self.curr = 0

    def move(self, direction: str) -> int:
        
        x, y = self.snake[-1]
        if direction == 'R':
            y += 1
        elif direction == 'D':
            x += 1
        elif direction == 'L':
            y -= 1
        elif direction == 'U':
            x -= 1
            
        
        if y < self.width and x < self.height and x >= 0 and y >= 0:
            
            if self.curr < len(self.food):
                if self.food[self.curr] == [x,y]:
                    self.curr += 1
                
                else:
                    self.snake.pop(0)
            else:
                self.snake.pop(0)
                
            if (x,y) in self.snake:
                return -1
            self.snake.append((x,y))
        else:
            return -1
        return len(self.snake)-1
        