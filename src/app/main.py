import streamlit as st
from page_topics import home, model_explain, eda, predict, top_clients, ticket_simulation, about

st.set_page_config(page_title="Previsão de Churn da Top Bank",
                   page_icon=":bank:",
                   layout="wide")

def main():
    # Add lateral bar
    st.sidebar.title("Navegação")
    selection = st.sidebar.selectbox("Ir para", [
        "Home",
        "Explicação do Modelo",
        "Análise Exploratória de Dados",
        "Top Clients",
        "Previsão de Churn",
        "Simulação de Ticket",
        "Sobre"
    ])

    if selection == "Home":
        home.run()
    elif selection == "Explicação do Modelo":
        model_explain.run()
    elif selection == "Análise Exploratória de Dados":
        eda.run()
    elif selection == "Top Clients":
        top_clients.run()
    elif selection == "Previsão de Churn":
        predict.run()
    elif selection == "Simulação de Ticket":
        ticket_simulation.run()
    elif selection == "Sobre":
        about.run()
    else:
        st.error("Página não encontrada!")

if __name__ == "__main__":
    main()

