"""Run all quality checks on the Ghana WoSIS soil table and save the report.

Usage (from the csa_soil_project folder):
    python run_checks.py
Exit code 0 means success, 1 means a check failed.
"""
# 1. IMPORTS
import pandas as pd
from pathlib import Path
from agronomic_functions import build_flat, quality_flags, cleaning_report, dataset_alarm
from db_config import run_query

# 2. The main function


def main():
    """Build the table, run every check, print the results and save the report."""
    print("=== STARTING SOIL CHECKS ===")

    # Building flat
    flat = build_flat("orgc", ["ph", "clay", "sand"])
    print(f"flat table shape: {flat.shape}")

    # Run quality flags
    checked = quality_flags(flat)

    # Getting dataset_id and Merging
    meta = run_query(
        "SELECT dataset_id, layer_id FROM wosis_orgc WHERE country_name = 'Ghana'")
    traced = pd.merge(checked, meta, on="layer_id", how="left")

    # The self check Guard
    if len(traced) != len(checked):
        raise ValueError(
            f"Merge changed row count! Before: {len(checked)}, After: {len(traced)}")
    print(f"Merged rows: {len(traced)}")

    # 5. The Cleaning Report
    report = cleaning_report(traced, ["ph", "clay", "sand"], key="layer_id")
    print("\n--- CLEANING REPORT ---")
    print(report.to_string(index=False))

    # 6. The Dataset Alarm Loop
    print("\n--- DATASET ALARMS ---")
    for col in ["orgc", "ph", "clay", "sand"]:
        alarm = dataset_alarm(traced, col)
        if len(alarm) == 0:
            print(f"{col}: OK (No flags)")
        else:
            print(f"{col}: FLAGGED")
            for name, value in alarm.items():
                print(f"  {name} = {value:.1f}")

        # 7. Count Hard and Soft Flags
    hard_flags = traced[['flag_ph', 'flag_clay_sand',
                         'flag_clay', 'flag_sand', 'flag_oc_neg']].sum().sum()
    soft_flags = traced['flag_oc_high'].sum()
    print(f"\nHard flags: {hard_flags}")
    print(f"Soft flags: {soft_flags}")

    # 8. Save the report using the Path trick
    HERE = Path(__file__).parent
    out_path = HERE / "Reports" / "run_checks_report.csv"
    report.to_csv(out_path, index=False)
    print(f"\nReport saved to: {out_path}")

    # The Doorbell Guard and Safety Net
if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print("CHECK FAILED:", e)
        raise SystemExit(1)
