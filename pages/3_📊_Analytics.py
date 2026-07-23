import streamlit as st

from utils.analytics import (
    total_documents,
    total_pages,
    total_chunks,
    storage_size,
    pages_chart,
    chunks_chart,
    upload_timeline,
    storage_chart
)

st.title("📊 Analytics Dashboard")

st.caption(
    "Overview of your AI PDF Research Assistant."
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📄 Documents",
        total_documents()
    )

    st.metric(
        "📃 Pages",
        total_pages()
    )

with col2:

    st.metric(
        "🧩 Chunks",
        total_chunks()
    )

    st.metric(
        "💾 Storage (MB)",
        storage_size()
    )

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = pages_chart()

    if fig:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    fig = chunks_chart()

    if fig:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

st.divider()

col1, col2 = st.columns(2)

with col1:

    fig = upload_timeline()

    if fig:
        st.plotly_chart(
            fig,
            use_container_width=True
        )

with col2:

    fig = storage_chart()

    if fig:
        st.plotly_chart(
            fig,
            use_container_width=True
        )