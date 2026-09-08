import streamlit as st
from styles import inject_css

inject_css()

st.title(" Team Manager")

st.markdown(
    '<p style="color:#111;font-weight:800;font-size:1.1rem;margin-bottom:16px;">Anggota Tim</p>',
    unsafe_allow_html=True
)

members = [
    {"name": "Bryant Tinambunan", "bg": "#ffe600", "fg": "#111"},
    {"name": "Alya Namira",       "bg": "#f44336", "fg": "#fff"},
    {"name": "Adinda Soleha",     "bg": "#4caf50", "fg": "#111"},
    {"name": "Zulfahmi Indra",    "bg": "#00bcd4", "fg": "#111"},
]

cols = st.columns(2)
for i, m in enumerate(members):
    with cols[i % 2]:
        st.markdown(
            f'<div style="background:{m["bg"]};border:3px solid #111;border-radius:6px;'
            f'box-shadow:6px 6px 0 #111;padding:24px;margin-bottom:14px;">'
            f'<div style="font-size:1.1rem;font-weight:900;color:{m["fg"]};">{m["name"]}</div>'
            f'</div>',
            unsafe_allow_html=True
        )

st.markdown(
    '<hr style="border:2px solid #111;margin:20px 0;">',
    unsafe_allow_html=True
)

st.markdown(
    '<div style="background:#f9f9f9;border:3px solid #111;border-radius:6px;box-shadow:6px 6px 0 #111;padding:20px 24px;">'
    '<p style="color:#111;font-weight:900;font-size:1rem;margin:0 0 8px;">Kelompok RPL &#x2014; Software Planning Assistant</p>'
    '<p style="color:#444;font-weight:600;font-size:.9rem;margin:0;">Tim ini berkolaborasi untuk merancang, mengembangkan, dan mendokumentasikan sistem perencanaan perangkat lunak yang efektif dan terstruktur.</p>'
    '</div>',
    unsafe_allow_html=True
)