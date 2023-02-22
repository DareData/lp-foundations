import pandas
import pathlib

path = pathlib.Path.cwd()
    
def clean_data():
    df = pandas.read_csv(path.joinpath('./life_expectancy/data/eu_life_expectancy_raw.tsv'), sep= r'[\t,]', engine = 'python', index_col=False)

    df = df.melt(id_vars = df.columns[:4], value_vars=df.columns[4:], var_name = 'year', value_name = 'value')

    df.rename(columns = {'geo\\time':'region'}, inplace = True)
    
    df['year'] = df['year'].apply(pandas.to_numeric, errors='coerce')

    df['value'] = df['value'].str.extract('(\d*\.?\d*)', expand=False)
    df['value'] = df['value'].apply(pandas.to_numeric, errors='coerce')

    df = df.dropna()

    df = df.astype({'year':'int'})
    df = df.astype({'value':'float'})

    df = df[df['region'] == 'PT'] 
    
    
    df.to_csv(path.joinpath('./life_expectancy/data/pt_life_expectancy.csv'), index=False)


clean_data()