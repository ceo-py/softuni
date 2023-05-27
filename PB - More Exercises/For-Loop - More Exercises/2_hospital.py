days = int(input())
initial_doctors = 7
treated = 0
untreated = 0

for i in range(1, days + 1):
    patients_daily = int(input())
    if untreated > treated and i % 3 == 0:
        initial_doctors += 1
    if patients_daily <= initial_doctors:
        treated += patients_daily
    else:
        treated += initial_doctors
        untreated += patients_daily - initial_doctors

print(f'Treated patients: {treated}.')
print(f'Untreated patients: {untreated}.')






# period = int(input())
# doctors = 7
# treated_patients = 0
# untreated_patients = 0
# for days in range(1, period + 1):
#     patients_number = int(input())
#     if untreated_patients > treated_patients and days % 3 == 0:
#         doctors += 1
#     if patients_number <= doctors:
#         treated_patients += patients_number
#     else:
#         treated_patients += doctors
#         untreated_patients += patients_number - doctors
# print(f'Treated patients: {treated_patients}.')
# print(f'Untreated patients: {untreated_patients}.')




# days_for_reviewed_patients = int(input())
#
# total_treated_patients = 0
# total_untreated_patients = 0
# doctors = 7
# new_doctors = 0
#
# for day in range(1, days_for_reviewed_patients + 1):
#     patients_for_review = int(input())
#     if day % 3 == 0 and total_untreated_patients > total_treated_patients:
#         new_doctors += 1
#     if patients_for_review <= (doctors + new_doctors):
#         total_treated_patients += + patients_for_review
#
#     else:
#         total_treated_patients += + (doctors + new_doctors)
#         total_untreated_patients += +patients_for_review - (doctors + new_doctors)
#
# print(f"Treated patients: {total_treated_patients}.")
# print(f"Untreated patients: {total_untreated_patients}.")
