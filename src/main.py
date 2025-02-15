# src/main.py
from core.agent_manager import AgentManager
from core.environment import Environment
import config


def main():
    environment = Environment()
    agent_manager = AgentManager(environment)

    # Example: Create an agent (we'll define this agent later)
    agent_manager.create_agent("add_agent", "agents.function_agent_add")

    agent_manager.run()


if __name__ == "__main__":
    main()
