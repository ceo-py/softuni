number_of_snowballs = int(input())

best_snowball = 0
best_weight_sb = 0
best_time_needed = 0
best_quality = 0
for _ in range(number_of_snowballs):

    weight_sb = int(input())
    time_needed = int(input())
    quality = int(input())
    current_snowball = (weight_sb / time_needed) ** quality
    if _ == 0:
        best_snowball = current_snowball
        best_weight_sb = weight_sb
        best_time_needed = time_needed
        best_quality = quality
    else:
        if current_snowball > best_snowball:
            best_snowball = current_snowball
            best_weight_sb = weight_sb
            best_time_needed = time_needed
            best_quality = quality

print(f"{best_weight_sb} : {best_time_needed} = {int(best_snowball)} ({best_quality})")
