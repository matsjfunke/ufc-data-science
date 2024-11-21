import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def height_reach_plot(df, save=False, show=True):
    # Calculate the correlation
    correlation = df["height_cm"].corr(df["reach_in_cm"])

    # Define a consistent colors
    height_color = "#eb4034"
    reach_color = "#4a3abd"

    # Create a figure with subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Plot the distribution of height
    sns.histplot(df["height_cm"], kde=True, color=height_color, ax=axs[0, 0])
    axs[0, 0].set_title("Height Distribution")
    axs[0, 0].set_xlabel("Height (cm)")
    axs[0, 0].set_ylabel("Frequency")

    # Plot the distribution of reach
    sns.histplot(df["reach_in_cm"], kde=True, color=reach_color, ax=axs[0, 1])
    axs[0, 1].set_title("Reach Distribution")
    axs[0, 1].set_xlabel("Reach (cm)")
    axs[0, 1].set_ylabel("Frequency")

    # Scatter plot with regression line
    sns.regplot(x="height_cm", y="reach_in_cm", data=df, scatter_kws={"alpha": 0.5}, ax=axs[1, 0], color=height_color)
    axs[1, 0].set_title("Height vs. Reach")
    axs[1, 0].set_xlabel("Height (cm)")
    axs[1, 0].set_ylabel("Reach (cm)")
    axs[1, 0].annotate(f"Correlation: {correlation:.2f}", xy=(0.05, 0.95), xycoords="axes fraction", fontsize=16, color=reach_color)

    # Group by weight class and determine the better predictor
    grouped = df.groupby("weight_class")
    correlation_results = {}
    for name, group in grouped:
        height_corr = group["height_cm"].corr(group["win_percentage"])
        reach_corr = group["reach_in_cm"].corr(group["win_percentage"])
        better_predictor = "height" if abs(height_corr) > abs(reach_corr) else "reach"
        correlation_results[name] = {"height_correlation": height_corr, "reach_correlation": reach_corr, "better_predictor": better_predictor}

    height_reach_df = pd.DataFrame.from_dict(correlation_results, orient="index")
    height_reach_df.reset_index(inplace=True)
    height_reach_df.rename(columns={"index": "weight_class"}, inplace=True)

    # Melt the DataFrame for plotting
    melted_df = height_reach_df.melt(
        id_vars="weight_class", value_vars=["height_correlation", "reach_correlation"], var_name="Predictor", value_name="Correlation"
    )

    sns.barplot(data=melted_df, x="weight_class", y="Correlation", hue="Predictor", palette=[height_color, reach_color], ax=axs[1, 1])
    axs[1, 1].set_title("Height vs Reach Correlation with Win Percentage by Weight Class")
    axs[1, 1].set_xlabel("Weight Class")
    axs[1, 1].set_ylabel("Correlation Coefficient")
    axs[1, 1].set_xticklabels(axs[1, 1].get_xticklabels(), rotation=45)
    axs[1, 1].legend(title="Predictor")

    # Adjust layout
    plt.tight_layout()

    if save:
        plt.savefig("plots/height_reach_plot.png")

    if show:
        plt.show()
