import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    from bs4 import BeautifulSoup
    import requests
    from lxml import html
    import matplotlib.pyplot as plt 
    return html, mo, pd, requests


@app.cell
def _():
    raw_data = []
    return (raw_data,)


@app.cell
def _(html, mo, raw_data, requests):
    # 1. Fetch the page
    for pageNumber in mo.status.progress_bar(range(1, 27)):
    
        resp = requests.get(f"https://results.finishtime.co.za/results.aspx?CId=35&RId=5248&EId=2&dt=0&PageNo={pageNumber}")
        resp.raise_for_status()

        # 2. Parse into an lxml element tree
        tree = html.fromstring(resp.content)

        # 3. Locate your table
        table_xpath = '//*[@id="ctl00_Content_Main_divGrid"]/table'
        table = tree.xpath(table_xpath)[0]

        # 4. Iterate over rows
        for idx, row in enumerate(table.xpath(".//tr")):
            # skip header
            if idx == 0:
                continue
            
            values = []
            for cell in row.xpath(".//td"):
                # try to pull anchor text
                anchor_texts = cell.xpath(".//a/text()")
                if anchor_texts:
                    values.append(anchor_texts[0].strip())
                else:
                    # string(.) collapses all text descendants
                    values.append(cell.xpath("string(.)").strip())
        
            raw_data.append([values[1], values[2], values[5], values[7], values[8], values[9], values[11], values[12], values[13], values[14], values[15], values[17]])
    return


@app.cell
def _(raw_data):
    raw_data[0]
    return


@app.cell
def _():
    columns = ['Race No', 'Pos', 'Name', 'Time', 'Pace', 'Overall Pos', 'Category', 'Cat Pos', 'Gender', 'Gen Pos', 'Country', 'Finish']
    return (columns,)


@app.cell
def _(columns, pd, raw_data):
    df = pd.DataFrame(raw_data, columns=columns)
    df
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""## Converting Race Times to Minutes""")
    return


@app.cell
def _(df, pd):
    # converting to time_delta
    td = pd.to_timedelta(df['Finish'])
    td
    return (td,)


@app.cell
def _(df, td):
    # converting to minutes
    df['Finish in minutes'] = td.dt.total_seconds() / 60
    df['Finish in minutes'] = df['Finish in minutes'].round(2)
    df.head(1)
    return


@app.cell
def _(mo):
    mo.md(r"""## Bucketing the Finish Times""")
    return


@app.cell
def _(df):
    min_finish_time = int(df['Finish in minutes'].min())
    max_finish_time = int(df['Finish in minutes'].max())

    bin_edges = range(min_finish_time, max_finish_time + 5, 5)
    return (bin_edges,)


@app.cell
def _(bin_edges, df, pd):
    df['time_bucket'] = pd.cut(df['Finish in minutes'], bins=bin_edges)
    df.head(2)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
