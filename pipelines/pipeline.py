import os
import requests
import datetime as dt
import pandas as pd


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
    # dates available
    start_year, end_year = map(int, season.split('-'))
    if start_year < 2002 or end_year > current_date.year:
        raise ValueError(f'ncaam basketball data available from 2002-{current_date.year}, season {season} is unavailable.')
    # return as is
    else:
        return season






def get_roster(team: str, season: str = None):
    """
    Get a particular team's roster. season defaults to current season, but can be specified in "2019-20" form.
    """
    season = validate_season(season)


def main():
    season = validate_season()
    print(season)

    season = validate_season()
    print(season)

if __name__ == '__main__':
    print()
    main()
    print()