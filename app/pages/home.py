import streamlit as st

def render_sidebar() -> None:
    with st.sidebar:
        # note that nav can build automatically
        st.link_button("About Me", "#")
    
def render_intro() -> None:
  with st.container():
    st.header("This is a Streamlit App")
    st.subheader("By a person named: ")
    st.markdown(
        r"""Some text can go here
        
        
        
        
        
        
        """
    )
    
def render_note() -> None:
    st.write(
        "Notes: No notes yet."
    )


def render_footer() -> None:
    st.divider()
    st.subheader("Quick Navigation")
    # st.page_link("pages/somepage.py", label="Next: Some Page", icon="➡️")
    # st.page_link("pages/home.py", label="Home", icon="🏠")


def main() -> None:
    render_sidebar()
    render_intro()
    render_note()
    render_footer()
    
main()