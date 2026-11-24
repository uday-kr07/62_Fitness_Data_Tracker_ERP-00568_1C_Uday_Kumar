import matplotlib.pyplot as plt

steps_list = []
calories_list = []

GOAL = 10000


# Function to add daily fitness record
def add_record():
    try:
        steps = int(input("Enter steps: "))
        calories = int(input("Enter calories burned: "))

        if steps < 0:
            print("Invalid steps. Enter a non-negative whole number.")
            print("Record not saved.")
            return

        if calories < 0:
            print("Invalid calories. Enter a non-negative whole number.")
            print("Record not saved.")
            return

        steps_list.append(steps)
        calories_list.append(calories)

        day = len(steps_list) #len() counts the number of elements in a list.

        goal_status = "Yes" if steps >= GOAL else "No" #ternary conditional expression
        percentage = (steps / GOAL) * 100

        print(
            f"Record saved for Day {day}. " #f before a string makes it an f-string.
            f"Goal achieved: {goal_status} "
            f"({percentage:.2f}% of goal)" #displays the percentage with two decimal places.
        )

#except handles an error that occurs in the try block
    except ValueError:
        print("Invalid input. Enter a non-negative whole number.")
        print("Record not saved.")


# Function to calculate average steps
def calculate_average():
    if len(steps_list) == 0: 
        return 0
    return sum(steps_list) / len(steps_list)


# Function to calculate total calories
def calculate_total_calories():
    return sum(calories_list)


# Function to find best day
def find_best_day():
    if len(steps_list) == 0:
        return None

    best_steps = max(steps_list)
    best_day = steps_list.index(best_steps) + 1 # index starts from 0 so + 1 converts the position into the actual day number.

    return best_day, best_steps


# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Enter valid numbers.")


# Function to show weekly summary
def show_summary():
    if len(steps_list) == 0:
        print("No fitness records available.")
        return

    average = calculate_average()
    total_calories = calculate_total_calories()
    best_day, best_steps = find_best_day()

    goals_achieved = sum(
        1 for steps in steps_list if steps >= GOAL #generator expression
    )

    print("\n----- WEEKLY FITNESS SUMMARY -----")
    print(f"Average steps: {average:.2f}")
    print(f"Total calories: {total_calories}")
    print(f"Best day: Day {best_day} ({best_steps} steps)")
    print(f"Goal days: {goals_achieved}/{len(steps_list)}")
    print("----------------------------------")


# chart function
def show_chart():
    if len(steps_list) == 0:
        print("No records available to display.")
        return

    days = [f"Day {i + 1}" for i in range(len(steps_list))] #Creates labels

    plt.bar(days, steps_list, label="Daily Steps")

    plt.axhline(
        y=GOAL, #Goal 10,000
        color="red",
        linestyle="--",
        label="10000 Step Goal"
    )

    plt.title("Daily Steps")
    plt.xlabel("Days")
    plt.ylabel("Number of Steps")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()


#main ;
def main():
    while True:
        print("\n===== FITNESS DATA TRACKER =====")
        print("1. Add Record")
        print("2. Weekly Summary")
        print("3. Calculate BMI")
        print("4. Show Chart")
        print("5. Exit")

        choice = input("Enter your choice: ")
 
        if choice == "1":
            add_record()

        elif choice == "2":
            show_summary()

        elif choice == "3":
            calculate_bmi()

        elif choice == "4":
            show_chart()

        elif choice == "5":
            print("Thank you for using Fitness Data Tracker!")
            break

        else:
            print("Invalid menu option. Please try again.")


if __name__ == "__main__": #Checks file executed directly
    main()
