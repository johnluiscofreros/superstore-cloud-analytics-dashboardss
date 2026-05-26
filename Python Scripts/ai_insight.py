import requests
import pandas as pd

# Paste your OpenRouter API key here
API_KEY = "YOUR_OPENROUTER_API_KEY"

# Load cleaned dataset
df = pd.read_csv("cleaned_superstore.csv")

# Create real dataset summary
total_sales = round(df["Sales"].sum(), 2)
average_sales = round(df["Sales"].mean(), 2)
top_category = df.groupby("Category")["Sales"].sum().idxmax()
top_region = df.groupby("Region")["Sales"].sum().idxmax()

# AI prompt
prompt = f"""
You are a business data analyst.

Analyze this retail dataset:

Total Sales: {total_sales}
Average Sales: {average_sales}
Top Category: {top_category}
Top Region: {top_region}

Write a short business insight and one recommendation.
"""

# Send request to OpenRouter AI
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "openrouter/free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
)

# Convert response to JSON
result = response.json()

print("\nFULL API RESPONSE:\n")
print(result)

# Check if AI response exists
if "choices" in result:
    print("\nAI GENERATED INSIGHT:\n")
    print(result["choices"][0]["message"]["content"])
else:
    print("\nERROR FROM API:")
    print(result)