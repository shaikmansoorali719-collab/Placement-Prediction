import os
import pandas as pd
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

# Loading the Dataset
df = pd.read_csv("E:/2026-2027/ML/Placement_Prediction/Data/placement_predict_50k Dataset (2).csv")


print(df.head(),"\n")
print(df.tail(),"\n")
print(df.shape,"\n")
print(df.columns,"\n")
print(df.info(),"\n")
print(df.duplicated(),"\n")
print(df.isnull().sum(),"\n")
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "Data")
PLOT_DIR = os.path.join(BASE_DIR,"Output", "Plot")
REPORT_DIR = os.path.join(BASE_DIR, "Output", "Report")
print(BASE_DIR)
print(DATA_PATH)
print(PLOT_DIR)
print(REPORT_DIR)
os.makedirs(PLOT_DIR,exist_ok=True)
os.makedirs(REPORT_DIR,exist_ok=True)
"""""
#BarGraph
plt.figure(figsize=(6,4))
sns.countplot(data=df,x="PlacementStatus")
plt.xlabel("Placement Status")
plt.ylabel("Number of Placements")
plt.savefig(os.path.join(PLOT_DIR,"Placement.png"))
plt.show()
plt.close()


#histogram
plt.figure(figsize=(10,10))
plt.hist(df["CGPA"], bins=10, edgecolor="black")
plt.title("distribution of CGPA")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
plt.savefig(os.path.join(PLOT_DIR,"CGPA.png"))
plt.show()
plt.close()

#pie Chat
df["Gender"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
)
plt.title("Distribution of Gender")
plt.ylabel("")
plt.savefig(os.path.join(PLOT_DIR,"Gender.png"))
plt.show()
plt.close()

#Scatter Plot
plt.figure(figsize=(6,4))
sns.scatterplot(x="CGPA", y="AttendancePercent", data=df,color="blue")
plt.title("CGPA vs AttendancePercent")
plt.savefig(os.path.join(PLOT_DIR,"CGPA vs attendence.png"))
plt.show()
plt.close()

#Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x="PlacementStatus", y="CGPA", data=df)
plt.title("CGPA vs Placement Status")
plt.savefig(os.path.join(PLOT_DIR,"CGPA vs placement.png"))
plt.show()
plt.close()

#Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x="Gender", hue="PlacementStatus", data=df)
plt.title("Gender vs Placement Status")
plt.savefig(os.path.join(PLOT_DIR,"Gender vs placement.png"))
plt.show()
plt.close()
"""

