def calculate_cgpa():
    # Get the number of courses
    num_courses = int(input("Enter the number of courses: "))

    # Initialize variables to store the total weighted grade points and total credit hours
    total_weighted_grade_points = 0
    total_credit_hours = 0

    for i in range(num_courses):
        # Get grade point and credit hours for each course
        grade_point = float(input(f"Enter grade point for course {i + 1}: "))
        credit_hours = float(input(f"Enter credit hours for course {i + 1}: "))
        
        # Update the totals
        total_weighted_grade_points += grade_point * credit_hours
        total_credit_hours += credit_hours

    # Calculate CGPA
    if total_credit_hours == 0:
        print("Error: Total credit hours cannot be zero.")
        return
    
    cgpa = total_weighted_grade_points / total_credit_hours

    # Print the result
    print(f"Your CGPA is: {cgpa:.2f}")

# Run the CGPA calculator
calculate_cgpa()
