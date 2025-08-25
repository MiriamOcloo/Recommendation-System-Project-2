# Recommendation System

A comprehensive machine learning system that provides personalized product recommendations and detects abnormal user behavior for e-commerce platforms.

## Project Overview

This project solves two key business problems:
1. **Product Recommendations**: Predicts what items users will add to cart based on their viewing history using association rule mining
2. **Abnormal User Detection**: Identifies bots, scrapers, and suspicious activity using anomaly detection algorithms

## Machine Learning Architecture

### Recommendation System (Task 1)
**Primary Algorithm**: **Association Rule Learning (Apriori Algorithm)**
- **Technique**: Market Basket Analysis for pattern discovery
- **Implementation**: `mlxtend.frequent_patterns.apriori` + `association_rules`
- **Objective**: Discover "IF-THEN" patterns in user behavior

**Key Features:**
- Session-based sequence analysis (30-minute time windows)
- Temporal pattern matching using `pd.merge_asof()`
- Confidence-based rule filtering (>15% confidence, >1.5 lift)

### Abnormal User Detection (Task 2) 
**Primary Algorithm**: **Isolation Forest (Anomaly Detection)**
- **Technique**: Unsupervised anomaly detection using tree-based isolation
- **Implementation**: `sklearn.ensemble.IsolationForest`
- **Objective**: Identify statistical outliers in user behavior

**Feature Engineering:**
- `events_per_second`: User activity rate
- `unique_items`: Diversity of products viewed  
- `addtocart_ratio`: Conversion efficiency
- `purchase_ratio`: Purchase conversion rate
- `session_duration`: Engagement time span

## Model Performance

### Recommendation System Results
- **409 association rules** discovered with real predictive power
- **Average confidence**: 31.1% (above industry standard)
- **Maximum confidence**: 73.9% (exceptional accuracy)
- **Average lift**: 6.91x (7x better than random suggestions)
- **12.7% of rules** have >50% confidence

### Abnormal Detection Results
- **Contamination rate**: 1% (estimated abnormal users)
- **Statistical validation**: Clear separation between normal/abnormal patterns
- **Data quality improvement**: Significant noise reduction achieved

## Technical Stack

**Machine Learning Libraries Used**:
- `scikit-learn` (Isolation Forest)
- `mlxtend` (Apriori Algorithm) 
- `pandas` (Data manipulation)
- `numpy` (Numerical computing)

**Data Processing**:
- Temporal data alignment with Unix timestamp conversion
- Session-based user behavior analysis
- Feature scaling with `StandardScaler`

**Visualization**:
- `matplotlib` & `seaborn` for business insights
- Conversion funnel analysis
- Time-based pattern visualization

## Project Structure
Project-2-Recommendation-System/
│
├── Machine Learning Models/
│ ├── category_recommender.pkl # Trained Apriori-based recommender
│ └── association_rules_recommendations.csv # 409 discovered patterns
│
├── Data Files/
│ ├── abnormal_user_ids.csv # Users flagged by Isolation Forest
│ ├── abnormal_users_detected.csv # Statistical analysis of anomalies
│ └── events_cleaned.csv # Dataset after anomaly removal
│
├── Reports & Analysis/
│ ├── business_insights_report.txt # Comprehensive business analysis
│ ├── final_business_metrics.json # Key performance metrics
│ └── final_business_analysis.png # Visualizations and charts
│
└── Documentation/
└── README.md # This file


## Top Performing Rules

The Apriori algorithm discovered powerful patterns:

1. **IF** view categories `[317.0, 959.0]` **THEN** add to cart `1051.0`  
   - Confidence: **73.9%** 
   - Lift: 8.53x (8.5x better than random)

2. **IF** view categories `[57.0, 1483.0]` **THEN** add to cart `959.0`
   - Confidence: **73.1%** 
   - Lift: 9.65x

3. **IF** view categories `[1384.0, 1135.0]` **THEN** add to cart `589.0`
   - Confidence: **69.8%**
   - Lift: 17.01x  (17x better than random!)

## Methodology

### Data Preprocessing
- **Temporal alignment**: Property values matched to event timestamps
- **Session creation**: 30-minute inactivity timeouts for realistic user sessions
- **Feature engineering**: 10+ behavioral features for anomaly detection

### Model Training
- **Association Rules**: Minimum support 0.005, confidence threshold 0.1
- **Isolation Forest**: 100 estimators, 1% contamination, random state 42
- **Validation**: Time-based cross-validation approach

### Evaluation Metrics
- **Recommendation Quality**: Confidence + Lift scores
- **Anomaly Detection**: Statistical separation + business validation
- **Business Impact**: Conversion rate improvements

## Business Impact

- **74% accuracy** on top recommendations → increased conversions
- **17x lift** on best patterns → significantly better than random suggestions
- **Cleaned data** → more accurate analytics and split testing
- **Actionable insights** → optimized category placements and bundles

## Business Questions Answered
This project successfully addressed 7 key business questions:
- **What are the most viewed and purchased product categories?**
- **What does a typical user journey (view → addtocart → transaction) look like?**
- **Can we predict what item a user will add to their cart based on what they've viewed?**
- **What properties are most important when a user decides to add an item to the cart?**
- **What patterns separate a "normal" user from an "abnormal" one?**
- **How does the time of day or week affect user purchasing behavior?**
- **How accurate is our final recommendation model?**

**All Questions Successfully Answered**
Each question was thoroughly analyzed with quantitative results and actionable insights, providing a comprehensive understanding of user behavior and recommendation system performance.


