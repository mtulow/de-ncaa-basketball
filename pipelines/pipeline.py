import io
import os
import rdata
import requests
import datetime as dt
import pandas as pd


class Converter:
    def __init__(self) -> None:
        pass


# %%
# Helper Functions
# ================

def validate_season(season: str = None):
    """
    Return a valid season formatted as `YYYY-YYYY`
    """
    current_date = dt.datetime.today()
    # default case
    if season is None:
        return f"{current_date.year}-{current_date.year+1}" if (5 <= current_date.month <= 12) else f"{current_date.year-1}-{current_date.year}"
    # if season isn't a string object
    if not isinstance(season, str):
        raise TypeError(f'season must be season not `{type(season)}`')
    # if season == 'YYYY'
    season_obj = season.split('-')
    if len(season_obj) == 1:
        start_year, end_year = int(season_obj[0]), int(season_obj[0])+1
        if start_year < 2002 or end_year > current_date.year:
            raise ValueError(f'ncaam basketball data available from 2002-{current_date.year}, season: `{season}`, is unavailable.')
        return f'{start_year}-{end_year}'
    # if season is formatted as: 'YYYY-YYYY', 'MM-YYYY'
    if len(season_obj) == 2:
        # 'YYYY-YYYY' case
        start_year, end_year = map(int, season_obj)
        # between earliest date and latest date available
        if start_year < 2002 or end_year > current_date.year:
            raise ValueError(f'ncaam basketball data available from 2002-{current_date.year}, season: `{season}`, is unavailable.')
        # single season
        if end_year - start_year > 1:
            raise ValueError(f'season: `{season}`, must be a single season.')
        return season
    else:
        raise ValueError(f'season: `{season}`, unrecognized, unable to parse.')

    


    # dates available
    start_year, end_year = map(int, season.split('-'))
    if start_year < 2002 or end_year > current_date.year:
        raise ValueError(f'ncaam basketball data available from 2002-{current_date.year}, season {season} is unavailable.')
    # return as is
    else:
        return season


def fetch_dictionary():
    url = 'datasets/dict.rda'
    # r = requests.get(url)
    converted = rdata.conversion.convert(
        rdata.parser.parse_file(url)
    )
    if len(converted) == 1:
        v, = converted.values()
        return v
    else:
        return converted


def fetch_team_id(team: str):
    dictionary = fetch_dictionary()
    # url = 'https://github.com/lbenz730/ncaahoopR/blob/master/data/dict.rda'
    
    
    
    
# %%
# Funtions
# ========


def get_roster_data(team: str, season: str = None):
    """
    Get a particular team's roster. season defaults to current season, but can be specified in "2019-20" form.
    """
    # season is available
    season = validate_season(season)
    team_id = fetch_team_id(team)

def save_roster_data(df: pd.DataFrame):
    pass


# %%
# Tests
# =====


def test_validate_season():
    season = validate_season()
    assert season == '2022-2023', f'season: {season} is invalid or unavailable'

    season = validate_season('2022-2023')
    assert season == '2022-2023', f'season: {season} is invalid or unavailable'


# %%
# Run Pipeline
# ============


def main():
    dictionary = fetch_dictionary()
    print(dictionary)
    
    
if __name__ == '__main__':
    print()
    main()
    print()