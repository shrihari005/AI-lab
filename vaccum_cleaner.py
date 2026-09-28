class VacuumAgent:
    def __init__(self):
        self.rules = {
            "Dirty": "Suck",
            "Clean_A": "Right",
            "Clean_B": "Left"
        }

    def perceive_and_act(self, location, status):

        print(f"vaccum -> Location: {location}, Status: {status}")

        if status == "Dirty":
            action = self.rules["Dirty"]
        elif location == "A" and status == "Clean":
            action = self.rules["Clean_A"]
        elif location == "B" and status == "Clean":
            action = self.rules["Clean_B"]
        else:
            action = "NoOp"

        return action

environment = {"A": "Dirty", "B": "Dirty"}
agent = VacuumAgent()
current_location = "A"


for step in range(4):
    current_status = environment[current_location]
    action = agent.perceive_and_act(current_location, current_status)
    print(f"Action Taken: {action}\n")

    if action == "Suck":
        environment[current_location] = "Clean"
    elif action == "Right":
        current_location = "B"
    elif action == "Left":
        current_location = "A"


print("Shrihari Sudhakar Badiger: 1BM25CS522")