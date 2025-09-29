# made by gao le
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    print(f"📊 BMI: {bmi:.1f} - {category}")
