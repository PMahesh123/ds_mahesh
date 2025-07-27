Web3 Trading Data Analysis
Project Structure
ds_candidate_name/ ├── notebook_1.ipynb # Main analysis notebook ├── README.md # This file ├── ds_report.pdf # Final analysis report ├── csv_files/ # Data storage │ ├── historical_trades.csv │ └── fear_greed.csv └── outputs/ # Visualizations ├── sentiment_trend.png ├── pnl_vs_sentiment.png └── leverage_distribution.png

Setup Instructions
Data Download:

mkdir -p ds_candidate_name/csv_files cd ds_candidate_name/csv_files

Download datasets from:
Trader Data: Hyperliquid Historical Data
Sentiment Data: Fear & Greed Index
Run Analysis:

Upload notebook_1.ipynb to Google Colab

Update file paths if needed

Run all cells sequentially

Dependencies: pip install pandas numpy matplotlib seaborn scipy
