def check_eligibility(age, income):
    rules = {
        "Rule1": age >= 18 and income > 30000,
        "Rule2": age >= 25 and income > 20000,
        "Rule3": age >= 30 and income > 15000
    }

    # Applying rules
    if rules["Rule1"]:
        return "Eligible for 10% discount"
    elif rules["Rule2"]:
        return "Eligible for 15% discount"
    elif rules["Rule3"]:
        return "Eligible for 20% discount"
    else:
        return "Not eligible for any discount"

# Test the rule-based system
person_age = 28
person_income = 25000
result = check_eligibility(person_age, person_income)
print(result)
