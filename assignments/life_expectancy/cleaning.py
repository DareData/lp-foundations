import pandas
import pathlib

PROJECT_DIR = pathlib.Path(__file__).parent
DATA_DIR = PROJECT_DIR / data
  
def clean_data():
    df = pandas.read_csv(DATA_DIR / 'eu_life_expectancy_raw.tsv'), sep= r'[\t,]', engine = 'python', index_col=False)

    df = df.melt(id_vars = df.columns['unit', 'sex', 'age', ], var_name = 'year', value_name = 'value')

    df.rename(columns = {'geo\\time':'region'}, inplace = True)
    
    df['year'] = df['year'].apply(pandas.to_numeric, errors='coerce')

    df['value'] = df['value'].str.extract(r'(\d*\.?\d*)', expand=False)
    df['value'] = df['value'].apply(pandas.to_numeric, errors='coerce')

    df = df.dropna()

    df = df.astype({'year':'int'})
    df = df.astype({'value':'float'})

    df = df[df['region'] == 'PT'] 
    
    
    df.to_csv(DATA_DIR / 'pt_life_expectancy.csv', index=False)


clean_data()