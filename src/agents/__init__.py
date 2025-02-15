# src/agents/__init__.py

class Agent:
    def __init__(self, agent_id, environment):
        self.agent_id = agent_id
        self.environment = environment

    def step(self):
        """
        This method represents a single step of the agent's execution.
        Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement the step() method.")

    def evaluate(self):
        """
        Evaluates if the agent should be deleted
        It should be overriden by subclasses
        """
        raise NotImplementedError("Subclasses must implement the evaluate() method.")