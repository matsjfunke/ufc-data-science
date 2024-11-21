"""
matsjfunke
"""

import streamlit as st

from general_importance_plot import general_feature_importance
from height_reach_plot import height_reach_plot
from main import process_data
from win_weightclass_boxplot import plot_win_percentage_by_weight_class


def main():
    st.title("UFC Fighters Statistics Dashboard")

    df = process_data("./ufc-fighters-statistics.csv")

    st.write("## Data Overview")
    st.write(df.head())
    st.write(f"Dataframe has {df.shape[1]} columns and {df.shape[0]} rows")
    st.write(
        "The overall data quality is generally good, as it's fairly recent and up to date. \nHowever, there were a few rows with missing values that I needed to remove.\n I would have appreciated having a gender column in the dataset, but unfortunately, the underlying data is sourced from UFCStats.com, which does not provide gender information.Fortunately, this shouldn't be a significant issue, as I've categorized the fighters by their weight classes, which will help maintain the analysis's relevance."
    )

    st.write("## Plots")

    # Height and Reach Plot
    st.write("### Height and Reach Analysis")
    height_reach_plot(df, save=False)
    st.write(
        "Interestingly, for nearly all weight classes (6 out of 7), having a longer reach is a more reliable predictor of winning than simply being tall.\nEspecially in the bantamweight, flyweight, middleweight, and light-heavyweight divisions, a longer reach shows a strong correlation with the likelihood of winning.\nIn contrast, in the welterweight class, simply being taller is more advantageous for winning."
    )

    # Feature Importance Plot
    st.write("### Feature Importance")
    features = [
        "submissions_attempted_per_15_minutes",
        "takedowns_landed_per_15_minutes",
        "significant_strikes_landed_per_minute",
        "height_cm",
        "reach_in_cm",
        "takedown_defense",
        "takedown_accuracy",
        "significant_strike_defence",
        "significant_striking_accuracy",
    ]
    general_feature_importance(df, features, save=False)
    st.write(
        "The linear regression lines generally have shallow slopes, indicating weak correlations between the features and win percentage.\nAlthough features like takedowns landed per 15 minutes & significant strikes landed per minute display a slight positive trend, none serve as strong standalone predictors of win percentage.\nThe wide scatter of data points around the regression lines suggests significant variability not explained by these features alone.\nA more comprehensive model that includes multiple factors might be necessary for better prediction of success."
    )

    # Win Percentage by Weight Class
    st.write("### Win Percentage by Weight Class")
    plot_win_percentage_by_weight_class(df, save=False)
    st.write(
        "While the medians are similar, there are slight differences in range and outlier distribution, which could indicate **varying competitiveness** across classes.\nOverall, the boxplot suggests a generally consistent performance level across weight classes, with some individual outliers in each class."
    )


if __name__ == "__main__":
    main()
