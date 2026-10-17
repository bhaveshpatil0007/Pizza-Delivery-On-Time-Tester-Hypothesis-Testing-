"""Pizza delivery average-time test. Default data are SYNTHETIC, not real deliveries."""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

def analyze_delivery_times(times, claimed_mean=30.0, alpha=0.05):
    times = np.asarray(times, dtype=float)
    if times.ndim != 1 or len(times) < 2:
        raise ValueError("Provide at least two delivery times in a one-dimensional array.")
    if not np.isfinite(times).all() or (times <= 0).any():
        raise ValueError("Delivery times must be finite and positive; inspect invalid data.")
    n = len(times)
    mean = times.mean()
    sd = times.std(ddof=1)
    if sd == 0:
        raise ValueError("Zero sample variability: this t-test is undefined.")
    se = sd / np.sqrt(n)
    test = stats.ttest_1samp(times, popmean=claimed_mean, alternative="greater")
    ci = stats.t.interval(1-alpha, df=n-1, loc=mean, scale=se)
    lower = mean - stats.t.ppf(1-alpha, df=n-1)*se
    return {"n": n, "mean": mean, "sample_sd": sd, "standard_error": se,
            "t_statistic": float(test.statistic), "degrees_of_freedom": n-1,
            "p_value": float(test.pvalue), "two_sided_ci": tuple(ci),
            "one_sided_lower_bound": float(lower),
            "on_time_count": int((times <= claimed_mean).sum()),
            "on_time_percent": float(100*(times <= claimed_mean).mean()),
            "reject_null": bool(test.pvalue < alpha)}

if __name__ == "__main__":
    data_path = Path(__file__).with_name("pizza_delivery_data.csv")
    data = pd.read_csv(data_path)
    results = analyze_delivery_times(data["delivery_minutes"])
    print("DEMONSTRATION ONLY: bundled data are synthetic. Replace with real observations.")
    for key, value in results.items():
        print(f"{key}: {value}")
    print("Evidence that the population mean exceeds 30 minutes." if results["reject_null"]
          else "Insufficient evidence that the population mean exceeds 30 minutes; this does not prove the claim.")
