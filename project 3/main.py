import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Devid Hidayat\Documents\Pelatihan Data Analyst\Project\project 3\medical_examination.csv')

df = pd.read_csv('medical_examination.csv')
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 'good' if x == 0 else 'normal' if x == 1 else 'bad')
df['gluc'] = df['gluc'].apply(lambda x: 'good' if x == 0 else 'normal' if x == 1 else 'bad')

df_cat = pd.melt(df, 
                id_vars=['cardio'],  # Kolom yang tetap
                value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
fig = sns.catplot(
    x="variable", y=None, hue="value", col="cardio", 
    data=df_cat, kind="count", height=5, aspect=1
)
def draw_heat_map():
    df_filtered = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))) &
        (df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975)))
    ]

    df_filtered = df_filtered.select_dtypes(include=[np.number])
    
    corr = df_filtered.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, cmap="coolwarm", square=True, linewidths=0.5, ax=ax)

    return

fig = draw_heat_map()
plt.show()