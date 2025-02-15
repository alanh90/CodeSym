# src/agents/function_agent_add.py
from . import Agent  # Import the base Agent class

class AddAgent(Agent):
    def __init__(self, agent_id, environment):
        super().__init__(agent_id, environment)
        # For now, we'll just store a simple value.
        self.value = 0

    def step(self, output_file):
        # VERY basic example: increment the value.
        self.value += 1
        output_file.write(f"Agent {self.agent_id}: Value = {self.value}\n")
        output_file.flush()  # Ensure the output is written immediately

    def evaluate(self):
        pass