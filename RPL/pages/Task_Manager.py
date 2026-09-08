import streamlit as st
import pandas as pd
from db import supabase
from styles import inject_css

inject_css()

st.title("📝 Task Manager")

st.markdown(
    '<p style="color:#111;font-weight:800;font-size:1.1rem;margin-bottom:4px;">&#x2795; Tambah Task Baru</p>',
    unsafe_allow_html=True
)

with st.form("task_form"):
    col_a, col_b = st.columns(2)
    with col_a:
        task_name   = st.text_input("Nama Task")
        assigned_to = st.text_input("Assigned To")
    with col_b:
        priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        deadline = st.date_input("Deadline")
    status = st.selectbox("Status", ["To Do", "In Progress", "Done"])
    submit = st.form_submit_button("Tambah Task")

if submit:
    if not task_name.strip():
        st.markdown(
            '<div style="background:#fff3f3;color:#111;border:3px solid #111;border-radius:6px;'
            'box-shadow:5px 5px 0 #111;padding:14px 20px;font-weight:700;margin-top:8px;">'
            '&#9888; Nama task tidak boleh kosong!</div>',
            unsafe_allow_html=True
        )
    else:
        supabase.table("tasks").insert({
            "task_name"  : task_name,
            "assigned_to": assigned_to,
            "priority"   : priority,
            "deadline"   : str(deadline),
            "status"     : status
        }).execute()
        st.markdown(
            '<div style="background:#e8f5e9;color:#111;border:3px solid #111;border-radius:6px;'
            'box-shadow:5px 5px 0 #111;padding:14px 20px;font-weight:800;margin-top:8px;">'
            '&#x2705; Task berhasil ditambahkan!</div>',
            unsafe_allow_html=True
        )

st.markdown(
    '<hr style="border:2px solid #111;margin:28px 0;">',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:#111;font-weight:800;font-size:1.1rem;margin-bottom:8px;">&#x1F4CB; Semua Task</p>',
    unsafe_allow_html=True
)

data = supabase.table("tasks").select("*").execute()
if data.data:
    df = pd.DataFrame(data.data)
    st.dataframe(df, use_container_width=True)
else:
    st.markdown(
        '<div style="background:#f5f5f5;color:#333;border:3px solid #111;border-radius:6px;'
        'box-shadow:4px 4px 0 #111;padding:16px 20px;font-weight:600;">'
        'Belum ada task. Tambahkan task pertamamu di atas!</div>',
        unsafe_allow_html=True
    )