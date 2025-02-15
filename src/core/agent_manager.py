# src/core/agent_manager.py
import importlib

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

    def run(self):
        print("Agent manager running...")
        while True: #Placeholder
            for agent_id, agent in list(self.agents.items()):
                agent.step()