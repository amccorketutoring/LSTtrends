# lsttrends/cli.py

import argparse
import pandas as pd
from pathlib import Path
from .summer_trend import compute_summer_lst_trend


def main():
    parser = argparse.ArgumentParser(description="Analyze LST summer trends.")
    parser.add_argument(
        "csv_path", nargs="?", help="Path to CSV file with 'year' and 'lst' columns."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Run a sample sanity check using built-in data.",
    )

    args = parser.parse_args()

    # Sanity check mode
    if args.check:
        try:
            # Load bundled sample data
            data_dir = Path(__file__).parent.parent / "data"
            df = pd.read_csv(data_dir / "sample_data.csv")
            print("[Check] Sample data preview:")
            print(df.head())

            trend = compute_summer_lst_trend(df)
            print(f"[Check] Computed trend: {trend:.2f} °C/decade")
        except Exception as e:
            print(f"❌ Failed to run check: {e}")
        return

    # Run with user-provided CSV
    if not args.csv_path:
        print("❌ Please provide a CSV file path or use --check for sample data.")
        return

    try:
        df = pd.read_csv(args.csv_path)
        trend = compute_summer_lst_trend(df)
        print(f"📈 LST Summer Trend: {trend:.2f} °C per decade")
    except Exception as e:
        print(f"❌ Error processing file: {e}")


# ✅ Ensure main() runs when using: python -m lsttrends.cli
if __name__ == "__main__":
    main()
