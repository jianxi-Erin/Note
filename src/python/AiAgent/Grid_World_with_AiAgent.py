import tkinter as tk
import heapq
import time

# 可自定义参数
GRID_WIDTH = 5  # 网格宽度
GRID_HEIGHT = 5  # 网格高度
AGENT_START = (0, 0)  # 智能体初始位置
TARGET_POSITION = (4, 4)  # 目标位置
OBSTACLES = [(1, 1), (1, 2), (1, 3), (1, 4), (3, 2), (4, 2), (3, 4)]  # 障碍物位置
UPDATE_TIME = 1000  # 智能体移动时间间隔（毫秒）

class GridWorld:
    """ 网格世界类 """
    def __init__(self, width, height, agent_start, target, obstacles):
        self.width = width
        self.height = height
        self.agent_position = agent_start  # 记录智能体当前位置
        self.target_position = target  # 目标位置
        self.obstacles = set(obstacles)  # 障碍物集合，方便快速查找
        
    def move_agent(self, new_position):
        """ 移动智能体到新位置（如果不是障碍物）"""
        if new_position not in self.obstacles:
            self.agent_position = new_position

    def get_agent_position(self):
        """ 获取当前智能体位置 """
        return self.agent_position

    def is_agent_at_target(self):
        """ 判断智能体是否到达目标 """
        return self.agent_position == self.target_position

class AStarAgent:
    """ A*（A-Star）路径规划智能体 """
    def __init__(self, environment):
        self.env = environment
        self.path = self.a_star_path()
    
    def heuristic(self, a, b):
        """ 计算曼哈顿距离（启发式函数） """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    
    def a_star_path(self):
        """ 使用 A* 算法计算最优路径 """
        start, goal = self.env.agent_position, self.env.target_position
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}  # 记录路径
        g_score = {start: 0}  # 从起点到当前节点的代价
        f_score = {start: self.heuristic(start, goal)}  # 估算总代价
        
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                return self.reconstruct_path(came_from, current)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if (0 <= neighbor[0] < self.env.width and 0 <= neighbor[1] < self.env.height 
                        and neighbor not in self.env.obstacles):
                    temp_g_score = g_score[current] + 1
                    if neighbor not in g_score or temp_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = temp_g_score
                        f_score[neighbor] = temp_g_score + self.heuristic(neighbor, goal)
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
        return []
    
    def reconstruct_path(self, came_from, current):
        """ 生成最终路径 """
        path = []
        while current in came_from:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path
    
    def act(self):
        """ 按路径移动智能体 """
        if self.path:
            self.env.move_agent(self.path.pop(0))

class GridWorldApp:
    """ 可视化 GUI 界面 """
    def __init__(self, root, world, agent):
        self.root = root
        self.world = world
        self.agent = agent
        self.cell_size = 50
        self.canvas = tk.Canvas(root, width=world.width * self.cell_size, height=world.height * self.cell_size)
        self.canvas.pack()
        self.draw_grid()
        self.draw_obstacles()
        self.draw_target()
        self.draw_agent()
        self.root.after(UPDATE_TIME, self.update)
    
    def draw_grid(self):
        for y in range(self.world.height):
            for x in range(self.world.width):
                x0, y0 = x * self.cell_size, y * self.cell_size
                x1, y1 = x0 + self.cell_size, y0 + self.cell_size
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black")
    
    def draw_obstacles(self):
        for x, y in self.world.obstacles:
            x0, y0 = x * self.cell_size, y * self.cell_size
            x1, y1 = x0 + self.cell_size, y0 + self.cell_size
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")
    
    def draw_target(self):
        x, y = self.world.target_position
        x0, y0 = x * self.cell_size + 15, y * self.cell_size + 15
        x1, y1 = x0 + 20, y0 + 20
        self.canvas.create_oval(x0, y0, x1, y1, fill="green")
    
    def draw_agent(self):
        x, y = self.world.get_agent_position()
        x0, y0 = x * self.cell_size + 15, y * self.cell_size + 15
        x1, y1 = x0 + 20, y0 + 20
        self.agent_rect = self.canvas.create_oval(x0, y0, x1, y1, fill="blue")
    
    def update(self):
        if not self.world.is_agent_at_target():
            self.agent.act()
            self.canvas.delete(self.agent_rect)
            self.draw_agent()
            self.root.after(UPDATE_TIME, self.update)
        else:
            self.canvas.create_text(self.world.width * self.cell_size // 2, self.world.height * self.cell_size // 2,
                                    text="目标达成!", font=("Arial", 20), fill="red")

if __name__ == "__main__":
    world = GridWorld(GRID_WIDTH, GRID_HEIGHT, AGENT_START, TARGET_POSITION, OBSTACLES)
    agent = AStarAgent(world)
    root = tk.Tk()
    root.title("Grid_World_with_AiAgent")
    app = GridWorldApp(root, world, agent)
    root.mainloop()
