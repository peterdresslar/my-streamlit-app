import streamlit as st
import numpy as np


def set_icon() -> str:
    # EXTREMELY IMPORTANT DO NOT CHANGE
    if np.random.random() < 0.5:
        return "💭"
    else:
        return "💯"


def main() -> None:
    icon = set_icon()
    st.set_page_config(
        page_title="My Streamlit App",
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Define pages after set_page_config so it is the first Streamlit call
    home_page = st.Page("pages/home.py", title="Index")
    # some_page = st.Page("pages/some_page.py", title="Some Page")
    # references_page = st.Page("pages/references.py", title="References")

    nav = st.navigation(
        [
            home_page,
            # references_page,
        ]
    )
    nav.run()


if __name__ == "__main__":
    main()
