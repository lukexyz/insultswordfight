import streamlit as st
from collections import namedtuple, defaultdict

STAGE_COLORS = {
    "Needs triage": "rgba(206, 205, 202, 0.5)",
    "Backlog": "rgba(206, 205, 202, 0.5)",
    "Prioritized": "rgba(206, 205, 202, 0.5)",
    "👟 Scoping / speccing": "rgba(221, 0, 129, 0.2)",
    "👷 Ready for tech design": "rgba(255, 0, 26, 0.2)",
    "👷 In tech design": "rgba(245, 93, 0, 0.2)",
    "👷 Ready for dev": "rgba(233, 168, 0, 0.2)",
    "👷 In development": "rgba(0, 135, 107, 0.2)",
    "👟 👷 In testing + polishing": "rgba(0, 120, 223, 0.2)",
    "🏁 Ready for launch": "rgba(103, 36, 222, 0.2)",
    "✅ Done / Launched": "rgba(140, 46, 0, 0.2)",
    "❌ Won't fix": "rgba(155, 154, 151, 0.4)",
}

class project():
    def __init__(self, icon, title, stage):
        self.icon = icon
        self.title = title
        self.stage = stage
        
p = project("🗃️", "Project", "👷 In development")


def get_stage_div(stage):
    color = STAGE_COLORS.get(stage, "rgba(206, 205, 202, 0.5)")
    return (
        f'<div style="background-color: {color}; padding: 1px 6px; '
        "margin: 0 5px; display: inline; vertical-align: middle; "
        f'border-radius: 3px; font-size: 0.75rem; font-weight: 400;">{stage}'
        "</div>"
    )

stage = get_stage_div(p.stage)
notion_link_str = f" &nbsp; [link](notion_url)"

st.markdown(
    f"#### {p.icon} {p.title} {stage} <small>{notion_link_str}</small>",
    unsafe_allow_html=True,
)