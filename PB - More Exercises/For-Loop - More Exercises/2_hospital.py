days_for_reviewed_patients = int(input())

total_treated_patients = 0
total_untreated_patients = 0
doctors = 7
new_doctors = 0

for day in range(1, days_for_reviewed_patients + 1):
    patients_for_review = int(input())
    if day % 3 == 0 and total_untreated_patients > total_treated_patients:
        new_doctors += 1
    if patients_for_review <= (doctors + new_doctors):
        total_treated_patients += + patients_for_review

    else:
        total_treated_patients += + (doctors + new_doctors)
        total_untreated_patients += +patients_for_review - (doctors + new_doctors)

print(f"Treated patients: {total_treated_patients}.")
print(f"Untreated patients: {total_untreated_patients}.")