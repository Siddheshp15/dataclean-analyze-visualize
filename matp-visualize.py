import pandas as pd
import matplotlib.pyplot as plt

# Load raw CSV
df = pd.read_csv("flipkart_com-ecommerce_sample.csv")

# 🧼 Clean category for avg price analysis
df['category'] = df['product_category_tree'].str.extract(r"'([^']+)'")

# Clean and convert retail_price
df = df[df['retail_price'].notnull()]
df['retail_price'] = pd.to_numeric(df['retail_price'], errors='coerce')
df = df.dropna(subset=['retail_price'])

# 💰 Average Retail Price per Category
avg_price = df.groupby('category')['retail_price'].mean().reset_index()
avg_price = avg_price.sort_values(by='retail_price', ascending=False).head(10)

# 📊 Plot Avg Price
plt.figure(figsize=(14, 6))
bars = plt.bar(avg_price['category'], avg_price['retail_price'], color='skyblue', edgecolor='black')
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 100, f"₹{int(bar.get_height())}", 
             ha='center', va='bottom', fontsize=9)
plt.title("Top 10 Product Categories by Average Retail Price", fontsize=14, fontweight='bold')
plt.xlabel("Product Category")
plt.ylabel("Average Retail Price (INR)")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# 🌟 Best Rated Products
df = df[df['overall_rating'].notnull()]
df['overall_rating'] = pd.to_numeric(df['overall_rating'], errors='coerce')
df = df.dropna(subset=['overall_rating'])

# Get top 10 best rated products
top_rated = df.sort_values(by='overall_rating', ascending=False).head(10)

# 📊 Plot Best Rated Products
plt.figure(figsize=(14, 6))
bars = plt.barh(top_rated['product_name'], top_rated['overall_rating'], color='lightgreen', edgecolor='black')
for index, bar in enumerate(bars):
    plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2, f"{bar.get_width():.1f}", 
             va='center', fontsize=9)
plt.title("Top 10 Best Rated Products", fontsize=14, fontweight='bold')
plt.xlabel("Overall Rating")
plt.ylabel("Product Name")
plt.tight_layout()
plt.gca().invert_yaxis()  # Highest rating on top
plt.show()