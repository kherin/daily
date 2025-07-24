# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Combining multiple datasets to find correlations and insights""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    - Dataset A: Number of casualty accidents by severity of accident and weather condition
    - Dataset B: Number of drivers and riders involved in casualty accidents by age group and gender
    - Dataset C: Vehicles registered by type as at end of year - Island of Mauritius
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    return alt, mo, pd


@app.cell
def _():
    # years = [2013, 2014, 2015, 2016, 2017, 2018]
    years = [2015, 2016]
    return (years,)


@app.cell
def _(mo):
    mo.md(r"""## **Dataset A:** Number of casualty accidents by severity of accident and weather condition""")
    return


@app.cell
def _(pd):
    casualty_by_year_df = pd.read_csv('./datasets/number-of-casualty-by-severity-of-accident-and-weather-condition_0.csv')
    casualty_by_year_df.head()
    return (casualty_by_year_df,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## **Dataset B:** Number of drivers and riders involved in casualty accidents by age group and gender

    """
    )
    return


@app.cell
def _(pd):
    drivers_involved_in_accident_by_year_df = pd.read_csv('./datasets/number-of-drivers-and-riders-involved-in-accidents.csv')
    drivers_involved_in_accident_by_year_df.head()
    return (drivers_involved_in_accident_by_year_df,)


@app.cell
def _(mo):
    mo.md(
        r"""
    ## **Dataset C:** Vehicles registered by type as at end of year - Island of Mauritius

    """
    )
    return


@app.cell
def _(pd):
    vehicles_registered_by_year_df = pd.read_csv('./datasets/vehicleregisteredbyyearandtypemauritius_0.csv')
    vehicles_registered_by_year_df.head()
    return (vehicles_registered_by_year_df,)


@app.cell
def _(mo):
    mo.md(r"""## Pre-processing Dataset A""")
    return


@app.cell
def _(casualty_by_year_df):
    casualty_by_year_filtered_df = casualty_by_year_df[casualty_by_year_df['SeverityOfAccident'] == 'Fatal']
    fatal_accidents_summary = casualty_by_year_filtered_df.groupby('Year').sum(['Number']).reset_index()
    fatal_accidents_summary = fatal_accidents_summary[['Year', 'Number']]
    fatal_accidents_summary.rename(columns={'Number': 'total_fatal_accidents', 'year':'Year'}, inplace=True)
    fatal_accidents_summary
    return (fatal_accidents_summary,)


@app.cell
def _(mo):
    mo.md(r"""## Pre-processing Dataset B""")
    return


@app.cell
def _(drivers_involved_in_accident_by_year_df, years):
    drivers_involved_in_accident_by_year_filtered_df = drivers_involved_in_accident_by_year_df[drivers_involved_in_accident_by_year_df['year'].isin(years)]

    drivers_involved_in_accident_by_year_filtered_df['Total'] = drivers_involved_in_accident_by_year_filtered_df[['less_than_15', '15_to_18', '19_to_24', '25_to_34', '35_to_44', '45_to_54', '55_to_60', 'over_60']].sum(axis=1)
    drivers_involved_summary = drivers_involved_in_accident_by_year_filtered_df.groupby('year').sum(['Total']).reset_index()

    drivers_involved_summary = drivers_involved_summary[['year', 'Total']]
    drivers_involved_summary.rename(columns={'Total': 'total_drivers_involved', 'year': 'Year'}, inplace=True)
    drivers_involved_summary
    return (drivers_involved_summary,)


@app.cell
def _(mo):
    mo.md(r"""## Pre-processing Dataset C""")
    return


@app.cell
def _(vehicles_registered_by_year_df, years):
    vehicles_registered_by_year_filtered_df = vehicles_registered_by_year_df[vehicles_registered_by_year_df['Year'].isin(years)]

    vehicles_registered_summary = vehicles_registered_by_year_filtered_df.groupby('Year').sum(['Amount']).reset_index()
    vehicles_registered_summary.rename(columns={'Amount': 'total_vehicles_registered'}, inplace=True)
    vehicles_registered_summary
    return (vehicles_registered_summary,)


@app.cell
def _(
    drivers_involved_summary,
    fatal_accidents_summary,
    pd,
    vehicles_registered_summary,
):
    merged_df = pd.merge(fatal_accidents_summary, drivers_involved_summary, on='Year')
    final_df = pd.merge(merged_df, vehicles_registered_summary, on='Year')
    final_df
    return (final_df,)


@app.cell
def _(mo):
    mo.md(
        """
        ### Insight: Vehicles vs. Accidents
        """
    )
    return


@app.cell
def _(alt, final_df):
    # Scatter plot with regression line
    scatter_plot = alt.Chart(final_df).mark_circle(size=100).encode(
        x=alt.X('total_vehicles_registered', title='Total Registered Vehicles', scale=alt.Scale(zero=False)),
        y=alt.Y('total_fatal_accidents', title='Total Casualty Accidents', scale=alt.Scale(zero=False)),
        tooltip=['Year', 'total_vehicles_registered', 'total_fatal_accidents']
    ).properties(
        title='More Vehicles vs. More Accidents'
    )

    # Add a regression line to show the trend
    scatter_plot + scatter_plot.transform_regression('total_vehicles_registered', 'total_fatal_accidents').mark_line(color='red')

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
