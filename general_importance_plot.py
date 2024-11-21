import matplotlib.pyplot as plt
import streamlit as st
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def general_feature_importance(df, features, save=False):
    # Create subplots in a 2x5 grid (with one empty plot)
    fig, axes = plt.subplots(2, 5, figsize=(20, 10), sharey=True)

    # Flatten the axes array for easy iteration
    axes = axes.flatten()

    # Plot each feature against win_percentage
    for i, feature in enumerate(features):
        # Scatter plot
        axes[i].scatter(df[feature], df["win_percentage"], alpha=0.5, color="#eb4034")

        # Fit linear regression for each feature
        X_feature = df[[feature]].values
        y = df["win_percentage"].values
        model = LinearRegression()
        model.fit(X_feature, y)

        # Predict values for the regression line using the same X_feature
        y_fit = model.predict(X_feature)

        # Plot regression line
        axes[i].plot(X_feature, y_fit, color="#4a3abd", linewidth=2)

        # Calculate R^2
        r2 = r2_score(y, y_fit)
        print(f"{feature}: R^2 = {r2:.2f}")

        # Set labels and title
        axes[i].set_title(feature)
        axes[i].grid(True)

    # Hide the last unused subplot
    axes[-1].set_visible(False)

    # Set a common y-label for the first plot in each row
    axes[0].set_ylabel("Win Percentage")
    axes[5].set_ylabel("Win Percentage")

    # Adjust layout
    plt.tight_layout()

    if save:
        plt.savefig("./plots/features_linear_regression.png")

    plt.show()
    st.pyplot(plt)
