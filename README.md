# Pizza Delivery "On-Time" Tester 🍕

A beginner-friendly data analysis and hypothesis-testing workflow designed to evaluate whether a pizza shop's average delivery time exceeds its 30-minute threshold promise.

This project implements a right-tailed one-sample t-test to assess the population mean delivery time while independently calculating the observed sample on-time rates.

## 📅 Development Timeline
* **June 2024 – July 2024**

## 📊 Demonstration Results (Synthetic Dataset)
When executed against the provided baseline data file (50 observations), the project yields the following statistical insights:

* **Sample Count (n):** 50 deliveries
* **Sample Mean:** 32.45 minutes
* **Sample Standard Deviation (s):** 3.84 minutes
* **Standard Error (SE):** 0.54 minutes
* **Observed On-Time Rate:** 28.0% (14 out of 50 deliveries met the ≤ 30-minute window)
* **Late Deliveries:** 72.0% (36 out of 50 deliveries)

### Hypothesis Test Metrics:
* **t-Statistic:** 4.5137
* **Degrees of Freedom:** 49
* **One-Sided p-value:** 0.000020
* **Confidence Interval (Two-Sided 95%):** [31.36, 33.55] minutes
* **Statistical Decision:** **Reject H₀**. There is statistically significant evidence at α = 0.05 that the population mean delivery time exceeds 30 minutes.

*Note: These baseline metrics are derived from a simulated control dataset for demonstration purposes.*

## 🎯 Learning Outcomes
* Implement a **one-sample t-test** using `scipy.stats`.
* Generate and validate representative synthetic control datasets using NumPy.
* Evaluate critical statistical assumptions (normality, independence, scale) via **Q–Q plots** and the **Shapiro–Wilk test**.
* Formulate clear, non-overclaiming statistical conclusions along with business-centric recommendations.

## 🛠️ Project Structure & Tech Stack
The repository includes:
* **Python Scripts & Notebooks:** Modular codebases (`pizza_analyzer.py` and a comprehensive interactive Jupyter Notebook) containing data loading, visualization, validation, and testing logic.
* **Data Layer:** A clean dataset schema containing tracked `delivery_id` and `delivery_minutes`.

### Tech Stack
* **Language:** Python 3
* **Libraries:** `numpy`, `pandas`, `scipy`, `matplotlib`, `jupyter`

## 📊 Methodology & Statistical Framework

### Hypotheses
Let μ represent the true population mean delivery time:
* **Null Hypothesis (H₀):** μ ≤ 30 minutes *(The true average delivery time is 30 minutes or less)*
* **Alternative Hypothesis (H₁):** μ > 30 minutes *(The true average delivery time exceeds 30 minutes)*
* **Significance Level (α):** 0.05

### Visualizations & Diagnostics
The workflow automatically produces descriptive and diagnostic assets to evaluate distribution behaviors:
1. **Histogram distribution overlay** mapped against the 30-minute benchmark threshold.
2. **Normal Quantile-Quantile (Q–Q) Plot** paired with the Shapiro–Wilk normality diagnostic.

## 🚀 Getting Started

### Prerequisites
Install the required analytical dependencies:
```bash
pip install numpy pandas scipy matplotlib jupyter
```

### Running the Analysis
To execute the interactive walkthrough notebook:
```bash
jupyter notebook pizza_delivery_tester.ipynb
```

Alternatively, run the standalone automation script:
```bash
python pizza_analyzer.py
```

## 🔄 Adapting for Real-World Data
The default verification data provided in the template is strictly **synthetic** (generated via normal distribution distributions with seed tracking). To execute this project on real business data:
1. Ensure your order tracking mechanism correctly isolates order acceptance timestamps from delivery receipt timestamps.
2. Export your values into a tabular CSV file following the `delivery_minutes` column format.
3. Replace `pizza_delivery_data.csv` with your true empirical observations and re-run the pipeline.
