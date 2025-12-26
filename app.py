import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def analyze_rainfall(csv_file):
    # Load dataset
    df = pd.read_csv(csv_file.name)

    # Filter DURG district
    durg_data = df[df["DISTRICT"] == "DURG"]

    if durg_data.empty:
        return "DURG district not found in dataset", None, None, None, None, None

    # Columns
    month_cols = ["JAN","FEB","MAR","APR","MAY","JUN",
                  "JUL","AUG","SEP","OCT","NOV","DEC"]
    
    season_cols = ["Jan-Feb","Mar-May","Jun-Sep","Oct-Dec"]

    monthly_avg = durg_data[month_cols].mean()
    seasonal_avg = durg_data[season_cols].mean()

    # Variance
    variance = monthly_avg.var()

    
    plt.figure(figsize=(7,4))
    sns.barplot(x=monthly_avg.index, y=monthly_avg.values)
    plt.xticks(rotation=45)
    plt.title("Average Monthly Rainfall in DURG")
    plt.ylabel("Rainfall (mm)")
    monthly_bar = "monthly_bar.png"
    plt.tight_layout()
    plt.savefig(monthly_bar)
    plt.close()

    
    plt.figure(figsize=(6,4))
    sns.barplot(x=seasonal_avg.index, y=seasonal_avg.values)
    plt.title("Average Seasonal Rainfall in DURG")
    plt.ylabel("Rainfall (mm)")
    seasonal_bar = "seasonal_bar.png"
    plt.tight_layout()
    plt.savefig(seasonal_bar)
    plt.close()

    
    plt.figure(figsize=(7,4))
    sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker="o")
    plt.grid(True)
    plt.title("Monthly Rainfall Trend - DURG")
    plt.ylabel("Rainfall (mm)")
    monthly_line = "monthly_line.png"
    plt.tight_layout()
    plt.savefig(monthly_line)
    plt.close()

    
    plt.figure(figsize=(6,4))
    sns.lineplot(x=seasonal_avg.index, y=seasonal_avg.values, marker="o")
    plt.grid(True)
    plt.title("Seasonal Rainfall Trend – DURG")
    plt.ylabel("Rainfall (mm)")
    seasonal_line = "seasonal_line.png"
    plt.tight_layout()
    plt.savefig(seasonal_line)
    plt.close()

    # Convert results to tables
    monthly_table = pd.DataFrame({
        "Month": monthly_avg.index,
        "Average Rainfall (mm)": monthly_avg.values
    })

    seasonal_table = pd.DataFrame({
        "Season": seasonal_avg.index,
        "Average Rainfall (mm)": seasonal_avg.values
    })

    variance_text = f" Variance of Monthly Rainfall in DURG: {variance:.2f}"

    return (
        variance_text,
        monthly_table,
        seasonal_table,
        monthly_bar,
        seasonal_bar,
        monthly_line,
        seasonal_line
    )


with gr.Blocks(title="City Rainfall Pattern Analysis") as app:
    gr.Markdown("""
    #  City Rainfall Pattern Analysis – DURG  
    **Minor Project – Statistics**  

    **Features:**
    - Monthly Rainfall Analysis  
    - Seasonal Variation  
    - Variance Analysis  
    - Line & Bar Plots  
    """)

    file_input = gr.File(label=" Upload District-wise Rainfall CSV")

    analyze_btn = gr.Button(" Analyze Rainfall")

    variance_output = gr.Textbox(label="Variance Result")

    monthly_df = gr.Dataframe(label=" Monthly Rainfall Data")
    seasonal_df = gr.Dataframe(label=" Seasonal Rainfall Data")

    monthly_bar_img = gr.Image(label="Monthly Rainfall (Bar Plot)")
    seasonal_bar_img = gr.Image(label="Seasonal Rainfall (Bar Plot)")
    monthly_line_img = gr.Image(label="Monthly Rainfall (Line Plot)")
    seasonal_line_img = gr.Image(label="Seasonal Rainfall (Line Plot)")

    analyze_btn.click(
        analyze_rainfall,
        inputs=file_input,
        outputs=[
            variance_output,
            monthly_df,
            seasonal_df,
            monthly_bar_img,
            seasonal_bar_img,
            monthly_line_img,
            seasonal_line_img
        ]
    )

app.launch()