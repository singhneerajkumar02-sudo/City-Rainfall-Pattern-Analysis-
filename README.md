# City Rainfall Pattern Analysis – Durg District

## Project Overview
This project analyzes rainfall patterns for Indian districts using historical rainfall data.  
The focus of this analysis is **Durg district in Chhattisgarh**, carried out as part of **Minor 1 – Statistics**.

The project studies:
- Monthly rainfall distribution
- Seasonal rainfall variation
- Rainfall trends using line plots
- Variability of rainfall using variance analysis

A Gradio-based user interface is developed so that users can upload the dataset and automatically view important insights.

## Gradio UI
- Intractive Dashboard = [click here for the Dashboard Ui](https://huggingface.co/spaces/Niraj078/City-Rainfall-Pattern-Analysis)

---

## Dataset Description
- Dataset name: District-wise Rainfall Normal
- Format: CSV
- Total records: 641 districts
- Total columns: 19

### Important Columns
- `STATE_UT_NAME` – State or Union Territory name  
- `DISTRICT` – District name  
- `JAN` to `DEC` – Monthly rainfall values in millimeters  
- `Jan-Feb`, `Mar-May`, `Jun-Sep`, `Oct-Dec` – Seasonal rainfall values  
- `ANNUAL` – Total annual rainfall  

The dataset contains no missing values and no duplicate records.

---

## Objective of the Project
1. To analyze monthly rainfall patterns of Durg district  
2. To study seasonal variation in rainfall  
3. To visualize rainfall using bar charts and line plots  
4. To calculate variance and understand rainfall fluctuation  
5. To build an interactive UI for easy analysis using a CSV file  

---

## Tools and Technologies Used
- Python  
- NumPy  
- Pandas  
- Matplotlib  
- Seaborn  
- Gradio  

---

## Methodology
1. Load the rainfall dataset using Pandas  
2. Filter the dataset for Durg district  
3. Extract monthly and seasonal rainfall values  
4. Compute variance of monthly rainfall  
5. Generate visualizations:
   - Monthly rainfall bar plot  
   - Seasonal rainfall bar plot  
   - Monthly rainfall line plot  
   - Seasonal rainfall line plot  
6. Display results using a Gradio-based interface  
 

---

## Results and Insights
- Rainfall in Durg district is highly concentrated during the monsoon season (June to September)  
- Monthly rainfall shows high variation, confirmed by the variance value  
- Winter and summer months receive significantly less rainfall compared to monsoon months  
- Seasonal analysis clearly highlights monsoon dominance  

---