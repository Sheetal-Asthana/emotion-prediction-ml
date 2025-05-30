import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='mental_health', data=df)
plt.title("Distribution of Mental Health vs Not")
plt.xlabel("Label (0 = Not MH, 1 = MH)")
plt.ylabel("Tweet Count")
plt.show()
