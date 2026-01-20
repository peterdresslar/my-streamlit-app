import streamlit as st

def render_sidebar() -> None:
    with st.sidebar:
        st.markdown("""Navigation in progress""")
    
def render_intro() -> None:
  with st.container():
    st.header("Kantian Wholes in complexity science")
    st.subheader("Peter Dresslar")
    st.markdown(
        r"""Text here.
        
        
        
        
        
        
        """
    )
    
def render_note() -> None:
    st.caption(
        "Notes: No notes yet."
    )


def render_footer() -> None:
    st.divider()
    st.markdown("Quick Navigation")
    # st.page_link("pages/somepage.py", label="Next: Some Page", icon="➡️")
    # st.page_link("pages/home.py", label="Home", icon="🏠")


def main() -> None:
    render_sidebar()
    render_intro()
    render_note()
    render_footer()
    
main()