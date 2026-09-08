import streamlit as st
import pandas as pd
from db import supabase
from styles import inject_css

inject_css()

st.title("📊 Dashboard")

response = supabase.table("tasks").select("*").execute()
df = pd.DataFrame(response.data)

if df.empty:
    st.markdown(
        '<div style="background:#fff3f3;color:#111;border:3px solid #111;border-radius:6px;'
        'box-shadow:5px 5px 0 #111;padding:16px 20px;font-weight:700;">&#9888; Belum ada task.</div>',
        unsafe_allow_html=True
    )
else:
    total_task  = len(df)
    selesai     = len(df[df["status"] == "Done"])
    in_progress = len(df[df["status"] == "In Progress"])
    progress    = selesai / total_task

    col1, col2, col3, col4 = st.columns(4)
    cards = [
        (col1, "#ffe600", "#111", "Total Task",   str(total_task)),
        (col2, "#4caf50", "#fff", "Task Selesai", str(selesai)),
        (col3, "#00bcd4", "#111", "In Progress",  str(in_progress)),
        (col4, "#f44336", "#fff", "Progress",     f"{progress*100:.0f}%"),
    ]
    for col, bg, fg, label, val in cards:
        with col:
            st.markdown(
                f'<div style="background:{bg};border:3px solid #111;border-radius:6px;'
                f'box-shadow:5px 5px 0 #111;padding:16px 20px;text-align:center;margin-bottom:8px;">'
                f'<div style="font-size:.78rem;font-weight:700;color:{fg};text-transform:uppercase;">{label}</div>'
                f'<div style="font-size:2.2rem;font-weight:900;color:{fg};">{val}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    bar_pct = int(progress * 100)
    st.markdown(
        '<p style="color:#111;font-weight:800;font-size:1rem;margin:16px 0 6px;">Overall Progress</p>'
        f'<div style="background:#e0e0e0;border:3px solid #111;border-radius:6px;height:30px;overflow:hidden;box-shadow:4px 4px 0 #111;">'
        f'<div style="width:{bar_pct}%;height:100%;background:#39ff14;border-right:3px solid #111;display:flex;align-items:center;padding-left:10px;">'
        f'<span style="font-weight:800;font-size:.85rem;color:#111;">{bar_pct}%</span>'
        f'</div></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p style="color:#111;font-weight:800;font-size:1.1rem;margin:20px 0 8px;">&#x1F4CB; Daftar Task</p>',
        unsafe_allow_html=True
    )
    st.dataframe(df, use_container_width=True)