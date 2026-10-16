
import pandas as pd


def analyze_business_data(df):
    df = df.copy()

    required_columns = [
        "Product",
        "Total_Sales",
        "Total_Cost",
    ]

    missing = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing:
        raise ValueError(
            f"Missing required columns: {missing}"
        )

    df["Total_Sales"] = pd.to_numeric(
        df["Total_Sales"], errors="coerce"
    )
    df["Total_Cost"] = pd.to_numeric(
        df["Total_Cost"], errors="coerce"
    )

    df["Total_Profit"] = (
        df["Total_Sales"] - df["Total_Cost"]
    )

    valid_sales = df["Total_Sales"].where(
        df["Total_Sales"] != 0
    )

    df["Profit_Margin_%"] = (
        df["Total_Profit"] / valid_sales * 100
    ).round(2)

    def classify_margin(margin):
        if pd.isna(margin):
            return "Needs Review"
        elif margin >= 40:
            return "High Margin"
        elif margin >= 25:
            return "Medium Margin"
        return "Low Margin"

    df["Margin_Category"] = (
        df["Profit_Margin_%"].apply(classify_margin)
    )

    return df
