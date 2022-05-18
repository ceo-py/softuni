from datetime import datetime


exam_date = input()
compere_date = "2018-08-26"
date_format = "%Y-%m-%d"

exam_date_ = datetime.strptime(exam_date, date_format)
compere_date_ = datetime.strptime(compere_date, date_format)
date_diff = exam_date_ - compere_date_
result = ""
if exam_date_ < compere_date_:
    result = "Passed"
elif date_diff.days == 0:
    result = "Today date"
else:
    result = f"{date_diff.days+1} days left"

print(result)