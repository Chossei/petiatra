import streamlit as st

st.set_page_config(
    page_title='PetIAtra',
    initial_sidebar_state = 'collapsed',
    layout = 'wide'
)

_, col, _ = st.columns([1,2,1])

if not st.user.is_logged_in:
    # HTML e CSS para criar um "card" de login elegante.
    # Este card servirá como um contêiner visual para o botão st.login().
    with col:
        login_card_html = """
            <style>
                /* Importa uma fonte e ícones para um visual mais refinado */
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
                @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

                /* Estilo do nosso card de login */
                .login-card {
                    font-family: 'Poppins', sans-serif;
                    background-color: #F0F8F0; /* Cor de fundo secundária do seu tema */
                    padding: 40px;
                    border-radius: 15px;
                    text-align: center;
                    border: 1px solid #E6E6E6; /* Borda sutil */
                    box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Sombra para dar profundidade */
                }
                .login-icon {
                    font-size: 4rem; /* Tamanho do ícone */
                    color: #6EBBA5; /* Cor primária do seu tema */
                    margin-bottom: 20px;
                }
                .login-card h2 {
                    color: #31333F; /* Cor do texto do seu tema */
                    font-weight: 600;
                    font-size: 2.2rem;
                    margin-bottom: 10px;
                }
                .login-card p {
                    color: #555;
                    font-size: 1rem;
                    margin-bottom: 30px;
                }
            </style>

            <div class="login-card">
                <div class="login-icon"><i class="fa-solid fa-paw"></i></div>
                <h2>PetIAtra</h2>
                <p>Sua plataforma inteligente para o cuidado pet. Faça login para continuar.</p>
            </div>
            """
        # Renderiza o card que criamos acima
        st.markdown(login_card_html, unsafe_allow_html=True)
        

        if st.button('Log in com o Google', use_container_width=True):
            st.login()

else:
    # --- SEU CÓDIGO ORIGINAL (INTOCADO, COMO SOLICITADO) ---
    paginas = {
    'Início': [st.Page(page='paginas/inicio.py', title = 'Homepage',
                    default = True, )],
    'Seu pet': [st.Page(page = 'paginas/exames.py', title= 'Exames'),
                st.Page(page = 'paginas/registros.py', title = 'Registros'),
                st.Page(page = "paginas/chatbot.py", title = 'PetIA')]
    }
    pg = st.navigation(paginas)
    pg.run()
    if st.sidebar.button("Log out"):
        st.logout()



