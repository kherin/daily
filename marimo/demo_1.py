import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""# Demonstrating the reactive nature of Marimo""")
    return


@app.cell
def _(mo):
    mo.md(r"""## Average monthly potable water production from treatment plants and boreholes to distribution systems""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ### Dataset description:
    Dataset shows the average monthly potable water production from treatment plants and boreholes to distribution systems, 2015 - 2022, Island of Mauritius
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(pd):
    df = pd.read_csv('./datasets/average-monthly-potable-water-production-treatment-plants-and-boreholes.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df, mo):
    year_slider = mo.ui.slider(
        start=df['Year'].min(),
        stop=df['Year'].max(),
        step=1,
        value=2022,
        label="Select a year to inspect:"
    )

    year_slider
    return (year_slider,)


@app.cell
def _(df, year_slider):
    selected_year = year_slider.value
    filtered_df = df[df['Year'] == selected_year]
    return filtered_df, selected_year


@app.cell
def _(filtered_df, mo, selected_year):
    total_surface = filtered_df['Surface'].sum()
    total_borehole = filtered_df['Borehole'].sum()

    mo.md(
        f"""
        ## 📊 Production Summary for {selected_year}

        - **Total from Surface:** `{total_surface:,.0f} Mm³`
        - **Total from Boreholes:** `{total_borehole:,.0f} Mm³`
        - **Combined Total:** `{(total_surface + total_borehole):,.0f} Mm³`
        """
    )
    return


@app.cell
def _(filtered_df, mo, selected_year):
    mo.md(f"### Data for {selected_year}")
    filtered_df
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
