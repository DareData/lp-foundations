"""Module providing function clean_data"""
import pathlib
import argparse
import pandas

PROJECT_DIR = pathlib.Path(__file__).parent
DATA_DIR = PROJECT_DIR / 'data'

def clean_data(region_filter :str) -> None:
    """Cleans data referent to life expectancy in 
    Europe grouped by Country, Age, Sex and Time."""
    df_separated = pandas.read_csv(DATA_DIR / 'eu_life_expectancy_raw.tsv',
                         sep= r'[\t,]', engine = 'python', index_col=False)

    df_unpivot = df_separated.melt(id_vars = df_separated.columns[:4], var_name = 'year'
                                   , value_name = 'value')

    df_unpivot.rename(columns = {'geo\\time':'region'}, inplace = True)

    df_unpivot['year'] = df_unpivot['year'].apply(pandas.to_numeric, errors='coerce')

    df_unpivot['value'] = df_unpivot['value'].str.extract(r'(\d*\.?\d*)', expand=False)
    df_unpivot['value'] = df_unpivot['value'].apply(pandas.to_numeric, errors='coerce')

    df_unpivot = df_unpivot.dropna()

    df_unpivot = df_unpivot.astype({'year':'int'})
    df_unpivot = df_unpivot.astype({'value':'float'})

    df_unpivot = df_unpivot[df_unpivot['region'] == region_filter]


    df_unpivot.to_csv(DATA_DIR / 'pt_life_expectancy.csv', index=False)

def main():
    """Main Function"""
    parser = argparse.ArgumentParser()

    parser.add_argument('--region_filter', type=str, required=False,
                        default='PT', help='Enter region filter, default \'PT\'')

    args = parser.parse_args()

    clean_data(args.region_filter)

if __name__ == "__main__": #pragma: no cover
    main()
