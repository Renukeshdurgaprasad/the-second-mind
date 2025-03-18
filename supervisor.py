import queue
from memory_db import MemoryDB

class Supervisor:
    def __init__(self):
        self.task_queue = queue.PriorityQueue()
        self.memory = MemoryDB()

    def assign_task(self, priority, agent, data):
        self.task_queue.put((priority, agent, data))

    def execute_tasks(self):
        while not self.task_queue.empty():
            _, agent, data = self.task_queue.get()
            result = agent.process(data, self.memory)
            self.memory.store(data, result)
            return result  # Pass to next agent
