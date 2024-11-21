import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def plot_win_percentage_by_weight_class(df, save=False):
    labels = ["bantam", "middle", "light", "welter", "fly", "light-heavy", "heavy"]

    plt.figure(figsize=(12, 6))

    # Define custom colors for the boxplot
    boxprops = dict(facecolor="#eb4034", color="#4a3abd")
    whiskerprops = dict(color="#4a3abd")
    capprops = dict(color="#4a3abd")
    medianprops = dict(color="#eb4034")
    flierprops = dict(marker="o", color="#eb4034", alpha=0.5)

    sns.boxplot(
        x="weight_class",
        y="win_percentage",
        data=df,
        order=labels,
        boxprops=boxprops,
        whiskerprops=whiskerprops,
        capprops=capprops,
        medianprops=medianprops,
        flierprops=flierprops,
    )

    plt.title("Win Percentage by Weight Class")
    plt.xlabel("Weight Class")
    plt.ylabel("Win Percentage")
    plt.xticks(rotation=45)
    plt.tight_layout()

    if save:
        plt.savefig("./plots/win_weightclass_boxplot.png")
    plt.show()
    st.pyplot(plt)
