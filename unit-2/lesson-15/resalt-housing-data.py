#!/usr/bin/env python3

from pathlib import Path
import argparse
import random

import numpy as np
import pandas as pd
from scipy import stats


REQUIRED_COLUMNS = [
    'MedInc',
    'HouseAge',
    'AveRooms',
    'AveBedrms',
    'Population',
    'AveOccup',
    'Latitude',
    'Longitude',
    'MedHouseVal',
]


def load_source_data(data_dir: Path) -> tuple[pd.DataFrame, str]:
    '''Load source data for lesson 15 salting.

    It prefers housing_data.csv if the required columns are present;
    otherwise it falls back to california_housing.csv.
    '''
    primary_path = data_dir / 'housing_data.csv'
    fallback_path = data_dir / 'california_housing.csv'

    primary_df = pd.read_csv(primary_path)
    if all(column in primary_df.columns for column in REQUIRED_COLUMNS):
        return primary_df[REQUIRED_COLUMNS].copy(), primary_path.name

    fallback_df = pd.read_csv(fallback_path)
    return fallback_df[REQUIRED_COLUMNS].copy(), fallback_path.name


def build_quartiles(population: pd.Series) -> pd.Series:
    '''Create stable population quartiles even with duplicate values.'''
    labels = ['Q1_lowest', 'Q2', 'Q3', 'Q4_highest']
    return pd.qcut(population.rank(method='first'), q=4, labels=labels)

def salt_features(df: pd.DataFrame, features: list[str], prob_range: tuple[float] = (0.01, 0.1)) -> pd.DataFrame:
    '''Salts each feature in features with np.nan using a randomly selected
    probability in prob_range.'''

    for feature in features:
        prob = random.uniform(prob_range[0], prob_range[1])

        mask = np.random.rand(len(df)) < prob
        df.loc[mask, feature] = np.nan

    return df

def salt_house_age(
    df: pd.DataFrame,
    seed: int,
    q1_missing_prob: float,
    q2_missing_prob: float,
    q3_missing_prob: float,
    q4_missing_prob: float,
) -> pd.DataFrame:
    '''Add mild feature noise and quartile-dependent HouseAge missingness.'''
    rng = np.random.default_rng(seed)
    salted = df.copy()

    quartiles = build_quartiles(salted['Population'])
    probabilities = {
        'Q1_lowest': q1_missing_prob,
        'Q2': q2_missing_prob,
        'Q3': q3_missing_prob,
        'Q4_highest': q4_missing_prob,
    }

    draw = rng.random(len(salted))
    missing_mask = np.zeros(len(salted), dtype=bool)
    for quartile, probability in probabilities.items():
        quartile_mask = quartiles == quartile
        missing_mask[quartile_mask] = draw[quartile_mask] < probability

    salted.loc[missing_mask, 'HouseAge'] = np.nan
    return salted


def summarize_missingness(df: pd.DataFrame) -> None:
    '''Print missingness summary and chi-square test by population quartile.'''
    quartiles = build_quartiles(df['Population'])
    is_missing = df['HouseAge'].isna()

    contingency_table = pd.crosstab(quartiles, is_missing)
    _, p_value, _, _ = stats.chi2_contingency(contingency_table)
    rates = is_missing.groupby(quartiles).mean()

    print('Missing HouseAge by population quartile:')
    for quartile, rate in rates.items():
        print(f'  {quartile}: {rate:.2%}')
    print(f'Overall missing HouseAge: {is_missing.mean():.2%} ({int(is_missing.sum())} rows)')
    print(f'Chi-square p-value: {p_value:.3e}')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Regenerate salted_housing_data.csv for lesson 15.',
    )
    parser.add_argument('--seed', type=int, default=2605, help='Random seed.')
    parser.add_argument(
        '--output',
        type=Path,
        default=None,
        help='Output CSV path. Defaults to data/salted_housing_data.csv.',
    )
    parser.add_argument('--q1', type=float, default=0.053)
    parser.add_argument('--q2', type=float, default=0.041)
    parser.add_argument('--q3', type=float, default=0.037)
    parser.add_argument('--q4', type=float, default=0.040)
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    data_dir = repo_root / 'data'
    output_path = args.output or (data_dir / 'salted_housing_data.csv')

    for probability in [
        args.q1,
        args.q2,
        args.q3,
        args.q4,
    ]:
        if probability < 0 or probability > 1:
            raise ValueError('All missing probabilities must be between 0 and 1.')

    source_df, source_name = load_source_data(data_dir)
    salted_df = salt_house_age(
        source_df,
        seed=args.seed,
        q1_missing_prob=args.q1,
        q2_missing_prob=args.q2,
        q3_missing_prob=args.q3,
        q4_missing_prob=args.q4,
    )

    features = ["MedInc", "AveRooms", "AveBedrms", "AveOccup", "Latitude", "Longitude", "MedHouseVal", "Population"]
    salted_df = salt_features(salted_df, features)
    salted_df.to_csv(output_path, index=False)

    print(f'Source used: {source_name}')
    print(f'Wrote file: {output_path}')
    print(f'Rows: {len(salted_df)}')
    summarize_missingness(salted_df)


if __name__ == '__main__':
    main()
