import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "data" / "progress.csv"
OUTPUT_PATH = BASE_DIR / "output" / "summary.txt"


def read_progress(path):
    records = []

    try:
        with path.open(
            "r",
            encoding="utf-8-sig",
            newline="",
        ) as file:
            reader = csv.DictReader(file)

            required_columns = {
                "date",
                "category",
                "task",
                "minutes",
                "status",
            }

            if reader.fieldnames is None:
                print("CSV 沒有欄位名稱。")
                return records

            missing_columns = (
                required_columns - set(reader.fieldnames)
            )

            if missing_columns:
                print(
                    "CSV 缺少欄位：",
                    ", ".join(missing_columns),
                )
                return records

            for line_number, row in enumerate(
                reader,
                start=2,
            ):
                try:
                    row["minutes"] = int(row["minutes"])
                    records.append(row)

                except (ValueError, TypeError):
                    print(
                        f"略過第 {line_number} 列："
                        "minutes 必須是數字"
                    )

    except FileNotFoundError:
        print(
            "找不到 progress.csv，"
            "請確認檔案位於 data 資料夾。"
        )

    except OSError as error:
        print("讀取 CSV 時發生錯誤：", error)

    return records


def summarize(records):
    category_totals = {}
    completed_count = 0

    for record in records:
        category = record["category"]
        minutes = record["minutes"]
        status = record["status"]

        category_totals[category] = (
            category_totals.get(category, 0)
            + minutes
        )

        if status == "完成":
            completed_count += 1

    return category_totals, completed_count


def create_summary_text(
    category_totals,
    completed_count,
):
    total_minutes = sum(category_totals.values())

    lines = [
        "學習進度摘要",
        "============",
        f"總學習分鐘：{total_minutes}",
        f"完成任務數：{completed_count}",
        "",
        "各類別分鐘：",
    ]

    for category, minutes in category_totals.items():
        lines.append(
            f"- {category}：{minutes} 分鐘"
        )

    return "\n".join(lines)


def write_summary(path, text):
    try:
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            text,
            encoding="utf-8",
        )

        print("\n摘要已輸出：", path)

    except OSError as error:
        print("無法寫入摘要檔案：", error)


def main():
    records = read_progress(CSV_PATH)

    if not records:
        print("沒有可用的學習紀錄，未產生摘要。")
        return

    category_totals, completed_count = summarize(
        records
    )

    summary_text = create_summary_text(
        category_totals,
        completed_count,
    )

    print(summary_text)

    write_summary(
        OUTPUT_PATH,
        summary_text,
    )


if __name__ == "__main__":
    main()