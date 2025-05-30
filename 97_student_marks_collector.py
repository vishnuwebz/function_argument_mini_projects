# 1 student marks collector (using args)

def collect_marks(name, *marks):
    total = sum(marks)
    avg = total / len(marks)
    print(f"Student: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")

collect_marks("Vishnu", 86, 90, 95, 80)


"""
Student: Vishnu
Total Marks: 351
Average: 87.75
"""