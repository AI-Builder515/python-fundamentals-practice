"""STUDENT PERFORMANCE REPORT"""
english	 = 78
mathematics =	92
computer_science =	85
physics	 = 74
chemistry =	81

total_marks = 500

marks_obtained = (
    english
    + mathematics
    + computer_science
    + physics
    + chemistry
)
average = marks_obtained / 5
percentage = marks_obtained / total_marks * 100

print("=" * 42) 
print("       STUDENT PERFORMANCE REPORT")
print("=" * 42)
print(f"English:   {english:>6.2f}")
print(f"Mathematics: {mathematics:>6.2f}")
print(f"Computer Science: {computer_science:>6.2f}")
print(f"Physics: {physics:>6.2f}")
print(f"Chemistry:{chemistry:>6.2f}")

print("-" * 42)
print(f"Marks Obtained: {marks_obtained}/{total_marks}")
print(f"Average Marks {average:.2f}")
print(f"percentage: {percentage:.2f} %")

