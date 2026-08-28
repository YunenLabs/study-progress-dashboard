student_name = "Yunen"
excel_minutes = 85
python_minutes = 50
github_minutes = 25
goal_minutes = 180

print("姓名：", student_name)
print("Excel 分鐘：", excel_minutes)
print("Python 分鐘：", python_minutes)
print("GitHub 分鐘：", github_minutes)

print(type(student_name))
print(type(excel_minutes))

total_minutes = excel_minutes + python_minutes + github_minutes
print("累計學習分鐘：", total_minutes)

if total_minutes >= goal_minutes:
    print("本週目標已完成")
else:
    print("本週目標尚未完成")

completion_rate = total_minutes / goal_minutes

if completion_rate >= 1:
    status = "完成"
elif completion_rate >= 0.6:
    status = "進行中"
else:
    status = "落後"

print("完成率：", round(completion_rate * 100, 1), "%")
print("目前狀態：", status)

categories = ["Excel", "Python", "GitHub"]

print("今天追蹤的類別：")

for category in categories:
    print("-", category)

study_minutes = {
    "Excel": excel_minutes,
    "Python": python_minutes,
    "GitHub": github_minutes,
}

print("各類別學習分鐘：")

for category, minutes in study_minutes.items():
    print(category, "：", minutes, "分鐘")

# --------------------
# 8/28 資料結構與函式
# --------------------

subjects = ["Excel", "Python", "GitHub"]

print("學習類別清單：", subjects)
print("第一個類別：", subjects[0])
print("類別數量：", len(subjects))

subject_goals = {
    "Excel": 90,
    "Python": 60,
    "GitHub": 30,
}

print("Excel 目標：", subject_goals["Excel"], "分鐘")
print("Python 目標：", subject_goals["Python"], "分鐘")

study_records = [
    {"date": "8/19", "category": "GitHub", "minutes": 10},
    {"date": "8/19", "category": "Python", "minutes": 20},
    {"date": "8/20", "category": "Excel", "minutes": 60},
    {"date": "8/20", "category": "Python", "minutes": 30},
    {"date": "8/21", "category": "Excel", "minutes": 20},
    {"date": "8/21", "category": "GitHub", "minutes": 15},
    {"date": "8/22", "category": "Excel", "minutes": 5},
]

def calculate_subject_totals(records):
    totals = {}

    for record in records:
        category = record["category"]
        minutes = record["minutes"]

        totals[category] = totals.get(category, 0) + minutes

    return totals

subject_totals = calculate_subject_totals(study_records)

print("各類別累計分鐘：")

for category, minutes in subject_totals.items():
    print(category, "：", minutes, "分鐘")

subjects_over_30 = [
    category
    for category, minutes in subject_totals.items()
    if minutes >= 30
]

print("累計達到30分鐘的類別：", subjects_over_30)