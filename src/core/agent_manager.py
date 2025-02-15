# src/core/agent_manager.py
import importlib
import time

class AgentManager:
    def __init__(self, environment):
        self.agents = {}
        self.environment = environment
        self.next_agent_id = 1

    def create_agent(self, agent_type, agent_module):
        try:
            module = importlib.import_module(agent_module)
            agent_class = getattr(module, agent_type.capitalize() + "Agent")
            agent_id = f"{agent_type}_{self.next_agent_id}"
            agent = agent_class(agent_id, self.environment)
            self.agents[agent_id] = agent
            self.next_agent_id += 1
            print(f"Created agent: {agent_id} of type {agent_type}")
            return agent_id
        except (ImportError, AttributeError) as e:
            print(f"Error creating agent: {e}")
            return None

    def delete_agent(self, agent_id):
        if agent_id in self.agents:
            del self.agents[agent_id]
            print(f"Deleted agent: {agent_id}")
        else:
            print(f"Agent not found: {agent_id}")

    def run(self, output_file): #Added output file
        print("Agent manager running...")
        running = True # added a running variable
        while running:
            for agent_id, agent in list(self.agents.items()):
                agent.step(output_file) # Pass output file
                time.sleep(0.5) #slow down for viewing purposes.

            # For demonstration purposes, stop after a few iterations.
            # In a real application, you'd have a different mechanism
            # to control when the system stops (e.g., a command from the GUI).
            if self.next_agent_id > 5:
                running = False
                print("Stopping agent manager (for demo purposes).")