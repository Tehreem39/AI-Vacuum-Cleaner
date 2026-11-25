class VacuumEnvironment:
    # 1. The Setup Box: Where is the vacuum, and which rooms are dirty?
    def __init__(self, start_location="A", status_A="Dirty", status_B="Dirty"):
        self.location = start_location  # Can be 'A' or 'B'
        self.room_A = status_A  # Can be 'Clean' or 'Dirty'
        self.room_B = status_B  # Can be 'Clean' or 'Dirty'

    # 2. Method: Show the current status of the world
    def display_status(self):
        print(f"🤖 Vacuum Location: {self.location} | Room A: {self.room_A} | Room B: {self.room_B}")

    # 3. Method: The "Suck" action function
    def suck_dirt(self):
        if self.location == "A":
            self.room_A = "Clean"
        elif self.location == "B":
            self.room_B = "Clean"
        print(f"🧹 Sucked dirt at Location {self.location}!")

    # 4. Method: Move actions functions
    def move_right(self):
        self.location = "B"
        print("➡️ Moving Right to Room B.")

    def move_left(self):
        self.location = "A"
        print("⬅️ Moving Left to Room A.")


# A standalone function representing a Reflex AI Agent
def reflex_vacuum_agent(env_object):
  # Step 1: Check if the room the vacuum is currently in is dirty
  current_room_status = env_object.room_A if env_object.location == "A" else env_object.room_B

  if current_room_status == "Dirty":
    return env_object.suck_dirt()  # If dirty, clean it!

  # Step 2: If the current room is already clean, move to the other room
  if env_object.location == "A":
    return env_object.move_right()
  else:
    return env_object.move_left()


# --- RUNNING THE SIMULATION ---

# Create our initial dirty world environment object from our class blueprint
simulated_world = VacuumEnvironment(start_location="A", status_A="Dirty", status_B="Dirty")

print("--- Start Simulation ---")
simulated_world.display_status()

# Step 1 of AI Agent choice loop
reflex_vacuum_agent(simulated_world)
simulated_world.display_status()

# Step 2 of AI Agent choice loop
reflex_vacuum_agent(simulated_world)
simulated_world.display_status()

# Step 3 of AI Agent choice loop
reflex_vacuum_agent(simulated_world)
simulated_world.display_status()

