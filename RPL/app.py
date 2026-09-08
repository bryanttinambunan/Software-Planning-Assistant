import streamlit as st
from styles import inject_css

st.set_page_config(
    page_title="Software Planning Assistant",
    page_icon="📋",
    layout="wide"
)

inject_css()

# ══════════════════════════════════════════════════════════════════════════════
# DECORATIVE ELEMENTS
# KEY: no blank lines inside the HTML block — Python-Markdown treats blank lines
# as block separators and will show raw HTML as code.
# ══════════════════════════════════════════════════════════════════════════════
st.markdown(
    '<div style="position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:9998;overflow:hidden;">'
    # Pink arrow ↙ top-area
    '<div style="position:absolute;top:72px;left:310px;font-size:3.5rem;color:#ff00aa;font-weight:900;transform:rotate(15deg);user-select:none;">&#x2199;</div>'
    # Stacked squares (yellow + purple) top-right
    '<div style="position:absolute;top:118px;right:52px;">'
    '<div style="width:28px;height:28px;background:#ffe600;border:2.5px solid #111;position:absolute;top:0;left:0;"></div>'
    '<div style="width:28px;height:28px;background:#9b59b6;border:2.5px solid #111;position:absolute;top:14px;left:14px;"></div>'
    '</div>'
    # Orange-red arrow ↗ bottom-left
    '<div style="position:absolute;bottom:88px;left:148px;font-size:3rem;color:#f44336;font-weight:900;transform:rotate(-10deg);user-select:none;">&#x2197;</div>'
    # Pink triangle bottom-center
    '<div style="position:absolute;bottom:60px;left:calc(240px + 38%);width:0;height:0;border-left:22px solid transparent;border-right:22px solid transparent;border-bottom:38px solid #ff00aa;"></div>'
    # Pink sparkle ✦ bottom-right
    '<div style="position:absolute;bottom:55px;right:44px;font-size:2.5rem;color:#ff00aa;font-weight:900;user-select:none;">&#x2726;</div>'
    # Pink arrow ↖ right-center
    '<div style="position:absolute;top:238px;right:30px;font-size:2.8rem;color:#ff00aa;font-weight:900;transform:rotate(5deg);user-select:none;">&#x2196;</div>'
    '</div>',
    unsafe_allow_html=True
)

# ══════════════════════════════════════════════════════════════════════════════
# PAGE TITLE
# ══════════════════════════════════════════════════════════════════════════════
st.title("📋 Software Planning Assistant")

# ══════════════════════════════════════════════════════════════════════════════
# WELCOME CARD
# KEY: every element on its own line, NO blank lines between elements.
# Python-Markdown stops treating content as an HTML block on blank lines.
# ══════════════════════════════════════════════════════════════════════════════
welcome_html = "\n".join([
    '<div style="background:#e4e4e4;border:4px solid #111;border-radius:6px;box-shadow:7px 7px 0 #111;padding:24px 28px;max-width:680px;">',
    '<h2 style="font-weight:900;color:#111;margin:0 0 6px;font-size:1.35rem;">Selamat Datang</h2>',
    '<p style="color:#333;font-weight:600;font-size:.95rem;margin:0 0 18px;">Software Planning Assistant membantu tim dalam:</p>',
    '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:18px;">',
    '<div style="display:flex;align-items:stretch;"><div style="background:#555;border:3px solid #111;border-right:none;padding:10px 12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;min-width:52px;">🏗️</div><div style="background:#fff;border:3px solid #111;padding:10px 16px;font-weight:700;font-size:.95rem;color:#111;display:flex;align-items:center;flex:1;">Perencanaan proyek</div></div>',
    '<div style="display:flex;align-items:stretch;"><div style="background:#7b1e1e;border:3px solid #111;border-right:none;padding:10px 12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;min-width:52px;">➗</div><div style="background:#fff;border:3px solid #111;padding:10px 16px;font-weight:700;font-size:.95rem;color:#111;display:flex;align-items:center;flex:1;">Pembagian tugas</div></div>',
    '<div style="display:flex;align-items:stretch;"><div style="background:#2e7d32;border:3px solid #111;border-right:none;padding:10px 12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;min-width:52px;">📈</div><div style="background:#fff;border:3px solid #111;padding:10px 16px;font-weight:700;font-size:.95rem;color:#111;display:flex;align-items:center;flex:1;">Monitoring progress</div></div>',
    '<div style="display:flex;align-items:stretch;"><div style="background:#1565c0;border:3px solid #111;border-right:none;padding:10px 12px;display:flex;align-items:center;justify-content:center;font-size:1.4rem;min-width:52px;">📋</div><div style="background:#fff;border:3px solid #111;padding:10px 16px;font-weight:700;font-size:.95rem;color:#111;display:flex;align-items:center;flex:1;">Dokumentasi pekerjaan</div></div>',
    '</div>',
    '<p style="color:#111;font-weight:700;font-size:.95rem;margin:0;">Silakan pilih menu di sidebar.</p>',
    '</div>',
])

st.markdown(welcome_html, unsafe_allow_html=True)