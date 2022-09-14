import streamlit as st

st.title("Olá Mundo StreamLit 🤖🎶")
st.write("Obrigado Ubiratan!")
st.markdown("## Subtítulo de **Seção**:")
st.code(
    """
    def somar(a,b):
        return a + b
    val1 = 10
    val2 = 12
    print(somar(val1,val2))
    """,
    language='python'
)
st.code(
    """
    python -m streamlit run arquivo.py
    """,
    language='powershell'
)
st.metric(
    label='Total da Compra (R$)',
    value=105.92
)

def fui_apertado():
    print("Ola Mundo!")

def somar_dois(v1, v2):
    resultado = v1 + v2
    print(resultado)

numero1 = st.number_input(
    label = "Valor 1:",
    min_value = 5,
    max_value = 100
)

numero2 = st.number_input(
    label = "Valor 2:",
    min_value = 5,
    max_value = 100
)
st.button(
    label = "Clicar aqui 💀",
    help = "Clique para ver comida!",
    on_click = somar_dois,
    kwargs = {"v1": numero1, "v2": numero2}
)