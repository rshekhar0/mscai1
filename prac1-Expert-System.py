import aiml

def initialize_aiml_kernel():
    kernel = aiml.Kernel()
    try:
        kernel.learn("animal_expert.aiml")
    except Exception as e:
        print("Error loading AIML file:", e)
        return None
    return kernel

def expert_system():
    print("Welcome to the Animal Expert System")
    print("You can ask questions about animals. Type 'EXIT' to quit.")
    kernel = initialize_aiml_kernel()
    if kernel is None:
        print("Exiting due to AIML initialization error.")
        return
    while True:
        user_input = input("You: ").strip().upper()
        if user_input == 'EXIT':
            print("Goodbye!")
            break
        try:
            response = kernel.respond(user_input)
            print("Expert System: " + response)
        except Exception as e:
            print("Error processing input:", e)

if __name__ == "__main__":
    expert_system()
