# src/main.py
from core.agent_manager import AgentManager
from core.environment import Environment
import config
import time  # Import the time module

def main():
    environment = Environment()
    agent_manager = AgentManager(environment)
    agent_manager.create_agent("add_agent", "agents.function_agent_add")

    # Open a file for output
    with open("output.txt", "w") as output_file:
        agent_manager.run(output_file)  # Pass the file to the run method


if __name__ == "__main__":
    main()