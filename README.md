# My Streamlit App Template

A quick start on Streamlit apps with a tilt toward pages.

Peter Dresslar, @peterdresslar

## To develop

Clone or create a repo from this template.

Adding a page:
```bash
touch app/pages/somepage.py
```

## To clean

```bash
uv run ruff check --fix
```

## To run with uv

```bash
uv venv
uv sync
uv run streamlit run app/app.py

# or, if you use just:
# just start
```

## To deploy

There is a button, but I prefer to just find my repo from the streamlit app site. YOLO and/or YMMV
