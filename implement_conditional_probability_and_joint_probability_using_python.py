import enum
import random

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

def probability_example(iterations):
    both_girls = 0
    older_girl = 0
    either_girl = 0

    random.seed(0)

    for _ in range(iterations):
        younger = random_kid()
        older = random_kid()

        if older == Kid.GIRL:
            older_girl += 1
        if older == Kid.GIRL and younger == Kid.GIRL:
            both_girls += 1
        if older == Kid.GIRL or younger == Kid.GIRL:
            either_girl += 1

    # Conditional Probability: P(both | older)
    conditional_prob_both_given_older = both_girls / older_girl

    # Conditional Probability: P(both | either)
    conditional_prob_both_given_either = both_girls / either_girl

    # Joint Probability: P(either_girls)
    joint_prob_either_girls = (either_girl / iterations) * 100

    # Joint Probability: P(both_girls)
    joint_prob_both_girls = (both_girls / iterations) * 100

    # Joint Probability: P(older_girl)
    joint_prob_older_girl = (older_girl / iterations) * 100

    print("Conditional Probability - P(both | older):", conditional_prob_both_given_older)
    print("Conditional Probability - P(both | either):", conditional_prob_both_given_either)
    print("Joint Probability - P(either_girls):", joint_prob_either_girls)
    print("Joint Probability - P(both_girls):", joint_prob_both_girls)
    print("Joint Probability - P(older_girl):", joint_prob_older_girl)

if __name__ == "__main__":
    # Get user input for the number of iterations
    iterations = int(input("Enter the number of iterations: "))

    # Run the probability example with user-specified iterations
    probability_example(iterations)