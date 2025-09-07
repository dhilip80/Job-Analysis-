# 📌 Job Market & Skills Demand Analysis Project
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("job_market.csv")   # Make sure your CSV is in the same folder
print("Dataset Preview:")
print(df.head(), "\n")

# -------------------------------
# STEP 2: Data Cleaning
# -------------------------------
# Drop missing values (if any)
df.dropna(inplace=True)

# Convert Salary (remove 'LPA' and convert to float)
df['Salary'] = df['Salary'].str.replace(" LPA", "").str.replace("LPA", "").astype(float)

# -------------------------------
# STEP 3: Top Skills Analysis
# -------------------------------
# Split skills column into individual skills
all_skills = df['Skills'].str.split(',').sum()
skill_counts = pd.Series(all_skills).str.strip().value_counts()

print("Top 5 Skills in Demand:")
print(skill_counts.head(5), "\n")

# -------------------------------
# STEP 4: Average Salary by Skill
# -------------------------------
# Expand skills into separate rows
skills_df = df.assign(Skill=df['Skills'].str.split(',')).explode('Skill')
skills_df['Skill'] = skills_df['Skill'].str.strip()

# Group by Skill to find average salary
avg_salary = skills_df.groupby('Skill')['Salary'].mean().sort_values(ascending=False)

print("Top 5 Skills by Average Salary:")
print(avg_salary.head(5), "\n")

# -------------------------------
# STEP 5: Jobs by City
# -------------------------------
jobs_by_city = df['Location'].value_counts()
print("Jobs by City:")
print(jobs_by_city, "\n")

# -------------------------------
# STEP 6: Visualizations
# -------------------------------

# Bar Chart: Top 5 Skills in Demand
plt.figure(figsize=(6,4))
skill_counts.head(5).plot(kind='bar', color="skyblue")
plt.title("Top 5 In-Demand Skills")
plt.xlabel("Skill")
plt.ylabel("Count")
plt.show()

# Bar Chart: Top 5 Skills by Average Salary
plt.figure(figsize=(6,4))
sns.barplot(x=avg_salary.head(5).index, y=avg_salary.head(5).values, palette="viridis")
plt.title("Top 5 Skills by Average Salary (LPA)")
plt.ylabel("Salary (LPA)")
plt.show()

# Pie Chart: Jobs by City
plt.figure(figsize=(6,6))
jobs_by_city.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title("Jobs Distribution by City")
plt.ylabel("")
plt.show()
