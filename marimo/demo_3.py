import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import altair as alt
    import io
    return alt, mo, pd


@app.cell
def _(mo):
    mo.md("# 📊 Distribution of offenders Adults placed on probation")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Dataset shows the Distribution of offenders Adults placed on probation by age group and sex, 1990 - 2021

    """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv('./datasets/Distribution-of-offenders-Adults-placed-on-probation.csv')
    return (df,)


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    age_cols = df.columns[2:]
    df_long = df.melt(
        id_vars=["Year", "Sex"],
        value_vars=age_cols,
        var_name="Age Group",
        value_name="Count"
    )
    return age_cols, df_long


@app.cell
def _(age_cols, mo):
    year_slider = mo.ui.slider(1999, 2021, step=1, value=2021, label="Year")
    sex_radio = mo.ui.radio(["Men", "Women"], value="Men", label="Sex")
    age_select = mo.ui.multiselect(
        options=list(age_cols),
        value=["28-32", "33-37", "38-42"],
        label="Select Age Groups"
    )

    # Display the widgets in a horizontal layout
    mo.hstack([year_slider, sex_radio, age_select], justify='space-around')
    return age_select, sex_radio, year_slider


@app.cell
def _(age_select, df_long, sex_radio, year_slider):
    filtered_data = df_long[
        (df_long["Year"] == year_slider.value) &
        (df_long["Sex"] == sex_radio.value) &
        (df_long["Age Group"].isin(age_select.value))
    ]
    return (filtered_data,)


@app.cell
def _(filtered_data, mo, sex_radio, year_slider):
    total_count = filtered_data["Count"].sum()

    mo.md(f"""
    ### Results for **{sex_radio.value}s** in **{year_slider.value}**
    Total count for selected age groups: **{total_count:,}**
    """)
    return


@app.cell
def _(alt, filtered_data, sex_radio, year_slider):
    # Create a bar chart that updates reactively
    chart = alt.Chart(filtered_data).mark_bar().encode(
        x=alt.X('Age Group', sort=None, title='Age Group'),
        y=alt.Y('Count', title='Population Count'),
        color=alt.Color('Age Group', legend=None),
        tooltip=['Age Group', 'Count']
    ).properties(
        title=f"Distribution for {sex_radio.value}s in {year_slider.value}"
    )

    chart
    return


if __name__ == "__main__":
    app.run()
