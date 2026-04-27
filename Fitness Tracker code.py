print("===================================")
print("   Welcome to Fitness Tracker 💪")
print("===================================")

name = input("What is your name? ")

goal = input("Do you want to gain weight or lose weight? Type 'gain' or 'lose': ").lower()

days = int(input("How many days per week can you work out? "))
minutes = int(input("How many minutes do you have per workout? "))

current_lift = input("What is one exercise you currently do? ")
current_weight = input("How much weight do you currently use? ")

print("\n===================================")
print(" Fitness Plan for", name)
print("===================================")

# ---------------- GOAL SETTINGS ----------------
if goal == "gain":
    reps = "6-10 reps"
    sets = "4-5 sets"
    style = "Heavy weight, slow controlled movement"
elif goal == "lose":
    reps = "12-15 reps"
    sets = "3-4 sets"
    style = "Lighter weight, fast pace, short rest"
else:
    reps = "10-12 reps"
    sets = "3 sets"
    style = "Balanced training"

print("\nYour Training Style:")
print("Reps:", reps)
print("Sets:", sets)
print("Style:", style)

# ---------------- WORKOUT LIBRARY ----------------
gain_workouts = [
    "Bench Press", "Squats", "Deadlifts", "Shoulder Press",
    "Pull-Ups", "Barbell Rows", "Leg Press", "Incline Dumbbell Press",
    "Lat Pulldown", "Bicep Curls", "Tricep Dips", "Lunges"
]

lose_workouts = [
    "Jump Rope", "Burpees", "Mountain Climbers", "High Knees",
    "Push-Ups", "Bodyweight Squats", "Lunges", "Plank",
    "Jump Squats", "Battle Ropes", "Sprints", "Bicycle Crunches"
]

# ---------------- WORKOUT PLAN ----------------
print("\nYour Weekly Workout Plan:\n")

if goal == "gain":
    if days <= 2:
        print("Full Body Strength (2 Days):")
        for w in gain_workouts[:6]:
            print("-", w, "|", sets, "|", reps)

    elif days <= 4:
        print("Upper / Lower Split:")
        print("\nDay 1 (Upper Body):")
        for w in ["Bench Press", "Shoulder Press", "Pull-Ups", "Bicep Curls"]:
            print("-", w, "|", sets, "|", reps)

        print("\nDay 2 (Lower Body):")
        for w in ["Squats", "Deadlifts", "Leg Press", "Lunges"]:
            print("-", w, "|", sets, "|", reps)

    else:
        print("Body Part Split (Advanced):")
        print("\nChest & Triceps:")
        for w in ["Bench Press", "Incline Press", "Tricep Dips"]:
            print("-", w, "|", sets, "|", reps)

        print("\nBack & Biceps:")
        for w in ["Deadlifts", "Rows", "Curls"]:
            print("-", w, "|", sets, "|", reps)

        print("\nLegs:")
        for w in ["Squats", "Leg Press", "Lunges"]:
            print("-", w, "|", sets, "|", reps)

elif goal == "lose":
    if days <= 2:
        print("Fat Burn Full Body Circuit:")
        for w in lose_workouts[:6]:
            print("-", w, "| 30 sec each | repeat 3 rounds")

    elif days <= 4:
        print("Cardio + Strength Mix:")
        print("\nDay 1:")
        for w in ["Jump Rope", "Push-Ups", "Squats", "Plank"]:
            print("-", w, "| 30-45 sec")

        print("\nDay 2:")
        for w in ["Burpees", "Lunges", "Mountain Climbers", "Crunches"]:
            print("-", w, "| 30-45 sec")

    else:
        print("High Intensity Weekly Plan:")
        for w in lose_workouts:
            print("-", w, "| 30 sec | minimal rest")

else:
    print("General Fitness Plan:")
    for w in ["Push-Ups", "Squats", "Plank", "Lunges"]:
        print("-", w, "|", sets, "|", reps)

# ---------------- PROGRESS ----------------
print("\nCurrent Exercise:", current_lift)
print("Current Weight:", current_weight)

print("\nOne-Month Goal:")
if goal == "gain":
    print("- Increase weight by 5-10 lbs on main lifts")
    print("- Focus on eating more protein")
elif goal == "lose":
    print("- Improve endurance and burn more calories")
    print("- Stay consistent and track progress")
else:
    print("- Stay consistent and improve weekly")

# ---------------- MISSED DAY ----------------
missed_day = input("\nDid you miss a workout this week? (yes/no): ").lower()

if missed_day == "yes":
    print("\nMake-Up Workout (Quick 20 min):")
    for w in ["Jumping Jacks", "Push-Ups", "Squats", "Plank"]:
        print("-", w, "| 30 sec x 3 rounds")
else:
    print("Great job staying consistent!")

# ---------------- MOTIVATION ----------------
print("\nMotivation:")
print("Consistency beats motivation. Keep going 💪")

print("\nThank you for using Fitness Tracker!")