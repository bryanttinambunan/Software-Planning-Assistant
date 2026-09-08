"""
Shared Neubrutalism CSS — light theme.
"""
import streamlit as st

NEUBRUTALISM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700;800;900&display=swap');
@import url('https://fonts.googleapis.com/icon?family=Material+Icons+Rounded');

*, *::before, *::after { box-sizing: border-box; }

/* Only hide footer */
footer { visibility: hidden; }

html, body {
    font-family: 'Space Grotesk', sans-serif !important;
}

/* ── PAGE BG ── */
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    background-color: #d9c8f0 !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

/* ── MAIN CONTENT ── */
[data-testid="stMain"] { background-color: #ffffff !important; }
[data-testid="stMain"] .block-container,
.main .block-container {
    background-color: #ffffff !important;
    padding-top: 1.5rem !important;
}

/* ── HEADER ── */
[data-testid="stHeader"],
header[data-testid="stHeader"] {
    background-color: #ffffff !important;
    border-bottom: 3px solid #111 !important;
}

/* ── SIDEBAR COLLAPSE BUTTON — hide icon text, use CSS arrow ── */
[data-testid="stSidebarCollapseButton"] button span,
[data-testid="stSidebarCollapsedControl"] button span {
    font-size: 0 !important;
    width: 0 !important;
    overflow: hidden !important;
    display: inline-block !important;
}
[data-testid="stSidebarCollapseButton"] button,
[data-testid="stSidebarCollapsedControl"] button {
    background: #00e5ff !important;
    border: 2px solid #111 !important;
    border-radius: 4px !important;
    box-shadow: 3px 3px 0 #111 !important;
    color: #111 !important;
    font-weight: 900 !important;
    font-size: 1rem !important;
}
[data-testid="stSidebarCollapseButton"] button::after {
    content: "◀" !important;
    font-size: 1rem !important;
    color: #111 !important;
}
[data-testid="stSidebarCollapsedControl"] button::after {
    content: "▶" !important;
    font-size: 1rem !important;
    color: #111 !important;
}

/* ── DEPLOY BUTTON ── */
[data-testid="stDeployButton"] button,
[data-testid="stDeployButton"] > button {
    background: #ffffff !important;
    border: 3px solid #111 !important;
    border-radius: 4px !important;
    box-shadow: 4px 4px 0 #111 !important;
    color: #111 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 900 !important;
    font-size: .95rem !important;
    padding: 4px 16px !important;
    transition: transform .1s, box-shadow .1s !important;
}
[data-testid="stDeployButton"] button:hover {
    transform: translate(2px,2px) !important;
    box-shadow: 2px 2px 0 #111 !important;
}

/* ── THREE-DOTS (⋮): orange circle ── */
[data-testid="stMainMenuButton"] button,
button[data-testid="stMainMenuButton"] {
    background: #ff6200 !important;
    border-radius: 50% !important;
    border: 3px solid #111 !important;
    color: #fff !important;
    box-shadow: 3px 3px 0 #111 !important;
    transition: transform .1s, box-shadow .1s !important;
}
[data-testid="stMainMenuButton"] button:hover {
    transform: translate(2px,2px) !important;
    box-shadow: 1px 1px 0 #111 !important;
}

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background-color: #8c5fa8 !important;
    border-right: 4px solid #111 !important;
    padding: 0 !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

/* ── NAV LINKS ── */
[data-testid="stSidebarNav"] ul { padding: 0 !important; margin: 0 !important; }
[data-testid="stSidebarNav"] li { list-style: none !important; }
[data-testid="stSidebarNav"] a {
    display: block !important;
    margin: 0 14px 12px !important;
    padding: 12px 18px !important;
    border: 3px solid #111 !important;
    border-radius: 4px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 800 !important;
    font-size: 1.05rem !important;
    text-decoration: none !important;
    box-shadow: 5px 5px 0 #111 !important;
    transition: transform .1s, box-shadow .1s !important;
    color: #000 !important;
    background: #ffe600;
}
[data-testid="stSidebarNav"] a:hover {
    transform: translate(3px,3px) !important;
    box-shadow: 2px 2px 0 #111 !important;
}
/* 1=app(cyan large), 2=Dashboard(yellow), 3=Task Manager(red), 4=Team Manager(green) */
[data-testid="stSidebarNav"] li:nth-child(1) a {
    background-color: #00e5ff !important;
    font-size: 1.45rem !important;
    font-weight: 900 !important;
    letter-spacing: -.5px !important;
    margin-bottom: 18px !important;
    margin-top: 14px !important;
}
[data-testid="stSidebarNav"] li:nth-child(2) a { background-color: #ffe600 !important; }
[data-testid="stSidebarNav"] li:nth-child(3) a { background-color: #f44336 !important; }
[data-testid="stSidebarNav"] li:nth-child(4) a { background-color: #4caf50 !important; }

/* ── HEADINGS ── */
h1, h2, h3, h4 {
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 900 !important;
    color: #111 !important;
}
h1 {
    background: #ffffff !important;
    border: 4px solid #00bcd4 !important;
    border-radius: 6px !important;
    padding: 10px 20px !important;
    box-shadow: 6px 6px 0 #00bcd4 !important;
    display: inline-block !important;
    margin-bottom: 20px !important;
}

/* ── FORM BUTTONS ── */
.stButton > button,
[data-testid="baseButton-secondaryFormSubmit"],
[data-testid="baseButton-secondary"] {
    background-color: #ff00aa !important;
    color: #fff !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 900 !important;
    font-size: 1rem !important;
    border: 3px solid #111 !important;
    border-radius: 4px !important;
    box-shadow: 5px 5px 0 #111 !important;
    transition: transform .1s, box-shadow .1s !important;
    padding: 8px 24px !important;
}
.stButton > button:hover,
[data-testid="baseButton-secondaryFormSubmit"]:hover {
    transform: translate(3px,3px) !important;
    box-shadow: 2px 2px 0 #111 !important;
}

/* ── FORM ── */
[data-testid="stForm"] {
    background: #f5f5f5 !important;
    border: 4px solid #111 !important;
    border-radius: 8px !important;
    box-shadow: 8px 8px 0 #111 !important;
    padding: 20px !important;
}

/* ── INPUTS ── */
.stTextInput > div > input,
.stDateInput > div > input {
    background: #fff !important;
    color: #111 !important;
    border: 3px solid #111 !important;
    border-radius: 4px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    box-shadow: 3px 3px 0 #111 !important;
}

/* ── SELECTBOX ── */
[data-baseweb="select"] > div {
    background: #fff !important;
    border: 3px solid #111 !important;
    border-radius: 4px !important;
    box-shadow: 3px 3px 0 #111 !important;
    color: #111 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
}

/* ── LABELS ── */
label {
    color: #222 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
}

/* ── METRICS ── */
[data-testid="stMetric"] {
    border: 3px solid #111 !important;
    border-radius: 6px !important;
    box-shadow: 5px 5px 0 #111 !important;
    padding: 12px 16px !important;
}
[data-testid="stMetric"] label { font-weight: 700 !important; color: #111 !important; }
[data-testid="stMetric"] [data-testid="stMetricValue"] { font-weight: 900 !important; color: #111 !important; }

/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border: 3px solid #111 !important;
    border-radius: 6px !important;
    box-shadow: 6px 6px 0 #111 !important;
    overflow: hidden !important;
}

/* ── PROGRESS ── */
.stProgress > div > div { background-color: #39ff14 !important; border-radius: 4px !important; }
.stProgress > div { background-color: #e0e0e0 !important; border: 2px solid #111 !important; border-radius: 4px !important; }

/* ── ALERTS ── */
.stAlert {
    border: 3px solid #111 !important;
    border-radius: 6px !important;
    box-shadow: 5px 5px 0 #111 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 700 !important;
}

hr { border-color: #111 !important; border-width: 2px !important; }
[data-testid="column"] { padding: 6px !important; }
</style>
"""

_SIDEBAR_BTN_FIX = """
<script>
(function(){
    function fix(){
        try{
            var doc = window.parent.document;
            doc.querySelectorAll('span,button').forEach(function(el){
                var t = (el.innerText||el.textContent||'').trim();
                if(t === 'keyboard_double_arrow_left' || t === 'keyboard_double_arrow_right'){
                    el.style.setProperty('font-size','0','important');
                    el.style.setProperty('line-height','0','important');
                    el.style.setProperty('overflow','hidden','important');
                    el.style.setProperty('color','transparent','important');
                    el.style.setProperty('width','0','important');
                    el.style.setProperty('height','0','important');
                    el.style.setProperty('display','inline-block','important');
                }
            });
        }catch(e){}
    }
    fix();
    [100,300,600,1200,2500].forEach(function(d){ setTimeout(fix,d); });
    try{
        var obs = new MutationObserver(fix);
        obs.observe(window.parent.document.body,{subtree:true,childList:true});
    }catch(e){}
})();
</script>
"""

def inject_css():
    import streamlit.components.v1 as components
    st.markdown(NEUBRUTALISM_CSS, unsafe_allow_html=True)
    # JS fix: hide the Material Icons text that shows as plain text when font fails to load
    components.html(_SIDEBAR_BTN_FIX, height=0, scrolling=False)
