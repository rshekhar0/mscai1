import aiml
import os

# Create a Kernel instance
kernel = aiml.Kernel()

# Load AIML files
aiml_files = [
    "basic.aiml",
    # Add more AIML files as needed
]

for aiml_file in aiml_files:
    file_path = os.path.join(os.path.dirname(__file__), aiml_file)
    kernel.learn(file_path)

# Load the brain file (if exists)
brain_file = "bot_brain.brn"
if os.path.exists(brain_file):
    kernel.bootstrap(brainFile=brain_file)

# Main loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        # Save the brain file before exiting
        kernel.saveBrain(brain_file)
        break

    response = kernel.respond(user_input)
    print(f"Bot: {response}")
