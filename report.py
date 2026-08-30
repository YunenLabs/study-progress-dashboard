from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "data" / "progress.csv"
OUTPUT_PATH = BASE_DIR / "output" / "summary.csv"


def load_progress(path):
    try:
        data = pd.read_csv(
            path,
            encoding="utf-8-sig",
        )
    except FileNotFoundError:
        print("找不到 data/progress.csv。")
        return None
    except pd.errors.EmptyDataError:
        print("progress.csv 沒有資料。")
        return None
    except pd.errors.ParserError as error:
        print("CSV 格式錯誤：", error)
        return None

    required_columns = {
        "date",
        "category",
        "task",
        "minutes",
        "status",
    }

    missing_columns = required_columns - set(data.columns)

    if missing_columns:
        print(
            "CSV 缺少欄位：",
            ", ".join(sorted(missing_columns)),
        )
        return None

    data["minutes"] = pd.to_numeric(
        data["minutes"],
        errors="coerce",
    )

    invalid_count = data["minutes"].isna().sum()

    if invalid_count:
        print(f"略過 {invalid_count} 筆分鐘格式錯誤的資料。")
        data = data.dropna(subset=["minutes"])

    data["minutes"] = data["minutes"].astype(int)

    return data


def create_summary(data):
    summary = (
        data.groupby(
            "category",
            as_index=False,
        )
        .agg(
            total_minutes=("minutes", "sum"),
            task_count=("task", "count"),
            completed_tasks=(
                "status",
                lambda values: (values == "完成").sum(),
            ),
        )
    )

    summary["completion_rate_percent"] = (
        summary["completed_tasks"]
        / summary["task_count"]
        * 100
    ).round(1)

    return summary


def save_summary(summary, path):
    try:
        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        summary.to_csv(
            path,
            index=False,
            encoding="utf-8-sig",
        )

        print("\n摘要已輸出：", path)

    except OSError as error:
        print("無法輸出 summary.csv：", error)


def main():
    data = load_progress(INPUT_PATH)

    if data is None or data.empty:
        print("沒有可用資料，程式結束。")
        return

    print("原始資料：")
    print(data)

    summary = create_summary(data)

    print("\n分組統計：")
    print(summary)

    save_summary(
        summary,
        OUTPUT_PATH,
    )


if __name__ == "__main__":
    main()