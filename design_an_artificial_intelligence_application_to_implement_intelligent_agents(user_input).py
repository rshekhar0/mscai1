import random

class Agent:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, direction):
        x, y = self.position
        if direction == 'up':
            self.position = (x, y + 1)
        elif direction == 'down':
            self.position = (x, y - 1)
        elif direction == 'left':
            self.position = (x - 1, y)
        elif direction == 'right':
            self.position = (x + 1, y)

class Environment:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def display(self):
        matrix = [['.' for _ in range(self.width)] for _ in range(self.height)]
        for agent in self.agents:
            x, y = agent.position
            matrix[y][x] = 'A'  # A for Agent

        for row in matrix:
            print(' '.join(row))
        print()

def main():
    width = int(input("Enter the width of the environment: "))
    height = int(input("Enter the height of the environment: "))
    env = Environment(width=width, height=height)

    num_agents = int(input("Enter the number of agents: "))
    for i in range(1, num_agents + 1):
        agent_name = f"Agent{i}"
        initial_x = int(input(f"Enter the initial x-coordinate for {agent_name}: "))
        initial_y = int(input(f"Enter the initial y-coordinate for {agent_name}: "))
        agent = Agent(name=agent_name, position=(initial_x, initial_y))
        env.add_agent(agent)

    num_iterations = int(input("Enter the number of iterations: "))
    for _ in range(num_iterations):
        env.display()
        print("Agents' positions:")
        for agent in env.agents:
            print(f"{agent.name}: {agent.position}")
        print()

        for agent in env.agents:
            direction = random.choice(['up', 'down', 'left', 'right'])
            agent.move(direction)

if __name__ == "__main__":
    main()