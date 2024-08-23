import streamlit as st
from page_topics import home, model_explain, eda, predict, top_clients, ticket_simulation, about

st.set_page_config(page_title="Previsão de Churn da Top Bank",
                   page_icon=":bank:",
                   layout="wide")

# Lists for page names and corresponding functions
PAGE_NAMES = [
    "Home",
    "Explicação do Modelo",
    "Análise Exploratória de Dados",
    "Top Clients",
    "Previsão de Churn",
    "Simulação de Ticket",
    "Sobre"
]

PAGE_FUNCTIONS = [
    home.run,
    model_explain.run,
    eda.run,
    top_clients.run,
    predict.run,
    ticket_simulation.run,
    about.run
]

def main():
    # Add lateral bar
    st.sidebar.title("Navegação")
    selection = st.sidebar.selectbox("Ir para", PAGE_NAMES)

    # Find the index of the selected page
    page_index = PAGE_NAMES.index(selection)

    # Get the corresponding function from the PAGE_FUNCTIONS list
    page_function = PAGE_FUNCTIONS[page_index]
    page_function()

if __name__ == "__main__":
    main()

