def students_credits(*args):
    output, courses_score = [], {}
    for item in args:
        course_name, credits, max_points, diyans_points = [int(x) if x.isdigit() else x for x in item.split("-")]
        courses_score[course_name] = credits * (diyans_points / max_points)

    total_credits = sum(courses_score.values())
    if total_credits >= 240:
        output.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        output.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")

    for k, v in sorted(courses_score.items(), key=lambda x: -x[1]):
        output.append(f"{k} - {v:.1f}")

    return '\n'.join(output)

