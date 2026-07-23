import os
import pandas as pd
import plotly.express as px

from utils.database import get_documents

PDF_FOLDER = "pdfs"


def total_documents():

    return len(get_documents())


def total_pages():

    docs = get_documents()

    return sum(
        doc[1]
        for doc in docs
    )


def total_chunks():

    docs = get_documents()

    return sum(
        doc[2]
        for doc in docs
    )


def storage_size():

    total = 0

    if os.path.exists(PDF_FOLDER):

        for file in os.listdir(PDF_FOLDER):

            path = os.path.join(
                PDF_FOLDER,
                file
            )

            if os.path.isfile(path):

                total += os.path.getsize(path)

    return round(
        total / (1024 * 1024),
        2
    )

def document_dataframe():
    """
    Returns document information as a DataFrame.
    """

    docs = get_documents()

    return pd.DataFrame(
        docs,
        columns=[
            "Filename",
            "Pages",
            "Chunks",
            "Uploaded"
        ]
    )


def pages_chart():

    df = document_dataframe()

    if df.empty:
        return None

    fig = px.bar(
        df,
        x="Filename",
        y="Pages",
        title="Pages per PDF"
    )

    return fig


def chunks_chart():

    df = document_dataframe()

    if df.empty:
        return None

    fig = px.bar(
        df,
        x="Filename",
        y="Chunks",
        title="Chunks per PDF"
    )

    return fig


def upload_timeline():

    df = document_dataframe()

    if df.empty:
        return None

    df["Uploaded"] = pd.to_datetime(df["Uploaded"])

    fig = px.line(
        df,
        x="Uploaded",
        y="Pages",
        markers=True,
        title="Upload Timeline"
    )

    return fig


def storage_chart():

    files = []

    sizes = []

    folder = "pdfs"

    if not os.path.exists(folder):
        return None

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        files.append(file)

        sizes.append(
            round(
                os.path.getsize(path) / 1024,
                2
            )
        )

    df = pd.DataFrame(
        {
            "Filename": files,
            "Size": sizes
        }
    )

    fig = px.pie(
        df,
        names="Filename",
        values="Size",
        title="Storage Distribution (KB)"
    )

    return fig