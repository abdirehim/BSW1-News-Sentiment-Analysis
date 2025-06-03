
# BSW1-News-Sentiment-Analysis

## Project Overview
The **BSW1-News-Sentiment-Analysis** project, commissioned by Nova Financial Solutions, aims to advance predictive analytics by investigating the relationship between financial news sentiment and stock price movements. Utilizing the Financial News and Stock Price Integration Dataset (FNSPID), this project is structured into three key tasks:

- **Task 1: Exploratory Data Analysis (EDA)** - Conducted a comprehensive analysis of the FNSPID dataset, uncovering patterns in headline lengths, sentiment distributions, publication trends, and publisher biases.
- **Task 2: Quantitative Analysis** - Performed stock price analysis for multiple tickers (AAPL, GOOG, AMZN, MSFT, TSLA, NVDA, META) using technical indicators (MA20, RSI, MACD) and custom financial metrics (Sharpe Ratio, Volatility), with visualizations to highlight sector dynamics.
- **Task 3: Sentiment and Stock Returns Correlation** - Initiated correlation analysis between news sentiment and daily stock returns, starting with a subset of tickers (AAPL, AMZN, GOOG) over select days in June 2020.

This repository contains all code, scripts, and reports generated during Week 1, with an interim report . The project leverages Python 3.12, pandas, NumPy, NLTK, TextBlob, yfinance, TA-Lib, and matplotlib for data analysis, visualization, and modeling.

---

## Repository Structure
BSW1-News-Sentiment-Analysis/
├── .vscode/                  # VSCode settings for consistent development
├── github/workflows/         # GitHub Actions workflows for CI/CD
├── data/                     # Dataset and stock price data
│   ├── yfinance_data/        # Stock price CSVs (e.g., AAPL_historical_data.csv)
│   └── fnspid/               # FNSPID dataset (news sentiment data)
├── scripts/                  # Python scripts for analysis
│   ├── stock_data.py         # Loads stock price data from CSVs
│   ├── technical_indicators.py # Calculates TA-Lib indicators (MA20, RSI, MACD)
│   ├── financial_metrics_all.py # Computes financial metrics for all tickers
│   ├── visualization.py      # Generates MA20, RSI, and MACD plots
│   └── [task3_script].py     # Placeholder for Task 3 correlation script
├── output/                   # Visualization outputs
│   ├── AAPL_ma_plot.png      # MA20 plot for AAPL
│   ├── AAPL_rsi_plot.png     # RSI plot for AAPL
│   ├── AAPL_macd_plot.png    # MACD plot for AAPL
│   └── ...                   # Similar plots for other tickers
├── reports/                  # Project reports
│   └── interim_report.md     # Interim report (updated June 3, 2025)
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation (this file)



## Setup Instructions

### Prerequisites
- Python 3.12
- Git
- Virtual environment tool (e.g., `venv`)

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abidirehim/BSW1-News-Sentiment-Analysis.git
   cd BSW1-News-Sentiment-Analysis
Set Up a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies: Ensure requirements.txt includes the following:


pandas
numpy
nltk
textblob
yfinance
ta-lib
matplotlib
seaborn
Install them with:

pip install -r requirements.txt
Download NLTK Data:


import nltk
nltk.download('punkt')
Prepare Data:
Place the FNSPID dataset in data/fnspid/.
Generate stock price data using yfinance:


