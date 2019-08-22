from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import yaml

from vivarium_public_health.dataset_manager import Artifact

sns.set(style='darkgrid')

disease_model_spec = str(Path(__file__).parent.resolve() / 'disease_model.yaml')
artifact_path = str(Path('.').parent.resolve() / 'artifact.hdf')

def get_pop_data(delta):
    a = Artifact(artifact_path)
    population = a.load('population.structure')
    population = population.reset_index().drop(columns=['age_group_end', 'year_end', 'location'])
    p = population[(population.year_start == 2010 + delta) 
                   & (population.age_group_start >= 40 + delta) 
                   & (population.age_group_start < 100 + delta)]
    
    return p


def plot_pop_data(delta=0):
    p = get_pop_data(delta)
    g = sns.catplot(x='age_group_start', y='value', hue='sex', kind='bar', height=6, aspect=2, data=p)
    g.set_xticklabels(rotation=45)
    plt.show()

def plot_pop_sim(s):
    pop = s.get_population()
    pop = pop[pop.alive == 'alive']
    p = get_pop_data(0)
    pop['age_start'] = pd.cut(pop.age, p.age_group_start.unique(), right=False) 
    q = pop.groupby(['age_start', 'sex']).apply(len).reset_index().rename(columns={0: 'value'})
    g = sns.catplot(x='age_start', y='value', hue='sex', kind='bar', height=6, aspect=2, data=q)
    g.set_xticklabels(rotation=45)
    plt.show()
