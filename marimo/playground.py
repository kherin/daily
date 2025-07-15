import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(pd):
    df = pd.read_csv('./datasets/cane_production.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    df.groupby('Year')['Owner_planters'].sum()
    return


@app.cell
def _(df, mo):
    transformed_df = mo.ui.dataframe(df)
    transformed_df
    return


@app.cell
def _(mo):
    region_filter = mo.ui.dropdown(options=['North', 'South', 'East', 'West'], value='North')
    region_filter
    return (region_filter,)


@app.cell
def _(df, mo, region_filter):
    filtered_by_region_df = df[df['Region'] == region_filter.selected_key]
    mo.ui.table(filtered_by_region_df)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
