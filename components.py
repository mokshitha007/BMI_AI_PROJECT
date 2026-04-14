def calculate_bmi(height, weight):
    return weight / ((height / 100) ** 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_health_score(bmi, activity):
    score = 100

    if bmi < 18.5 or bmi > 30:
        score -= 30
    elif bmi >= 25:
        score -= 15

    if activity == "Low":
        score -= 20
    elif activity == "Moderate":
        score -= 10

    return max(score, 0)