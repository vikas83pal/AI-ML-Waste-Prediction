# 3R ZeroWaste -- Waste Level Prediction (Option A)

## Problem Statement

Predict whether a waste bin will be Full (1) or Not Full (0) at the time
of pickup.

## Business Objective

-   Reduce overflow penalties
-   Avoid unnecessary pickup trips
-   Optimize fuel and manpower usage
-   Improve route planning efficiency

We prioritize Recall for Full bins to minimize overflow risk.

## Feature Engineering

### 1. Estimated Waste

estimated_waste = avg_daily_waste_kg × days_since_last_pickup

### 2. Utilization Ratio

utilization_ratio = estimated_waste / bin_capacity_kg

### 3. Encoded Features

-   location_type (One-hot encoding)
-   weather (Binary encoding)

These features help model real operational waste accumulation patterns.

## Model Selection

Baseline: Logistic Regression\
Final Model: Random Forest Classifier

Reason: - Handles nonlinear relationships - Works well with mixed data
types - Provides feature importance

## Evaluation Metrics

-   Accuracy
-   Precision
-   Recall (Priority for Full bins)
-   F1-score
-   Confusion Matrix

## Business Impact

-   Reduce emergency dispatch costs
-   Prevent overflow incidents
-   Optimize truck routes
-   Improve fleet utilization

## Deployment Plan

Model can be integrated into: - Route optimization systems - Daily
pickup scheduling dashboards - Smart waste management platforms

## Author

Vikas Pal\
AI/ML Internship Assessment -- 3R ZeroWaste
