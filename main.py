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