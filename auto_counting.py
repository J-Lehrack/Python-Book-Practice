# A program to count between a chosen range

start_range = int(input("Starting number: "))

end_range = int(input("Ending Number: "))

count_by = int(input("Amount to count by: "))

for i in range(start_range, end_range, count_by):
    print(i, end=" ")
