import streamlit as st

st.set_page_config(
    initial_sidebar_state= 'collapsed'
)

# --- Painel Principal ---
st.header(f'Olá, {st.user.name}!', divider='rainbow')
st.write('Selecione uma das opções abaixo para começar a gerenciar a saúde do seu pet.')

# --- Bloco de Estilo CSS ---
# Este CSS será aplicado aos 3 cartões. Ele foi projetado para funcionar dentro dos containers.
# Usamos uma altura fixa e flexbox para garantir que todos os cartões tenham o mesmo tamanho
# e que o botão (que é um elemento do Streamlit) fique bem posicionado visualmente.
st.markdown("""
<style>
    /* Importa a fonte do Google Fonts e ícones do Font Awesome */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');

    /* O st.container com border=True já cria a "caixa" externa.
       Este CSS estiliza o nosso div.card DENTRO dessa caixa. */
    div[data-testid="stContainer"] > div.card {
        background-color: white;
        border-radius: 10px;
        padding: 25px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease;
        font-family: 'Poppins', sans-serif;
        
        /* Flexbox para alinhar o conteúdo verticalmente */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        height: 320px; /* Altura fixa para o conteúdo do cartão */
    }
    
    div[data-testid="stContainer"] > div.card:hover {
        transform: scale(1.02); /* Efeito de zoom sutil no hover */
    }

    .card-icon {
        font-size: 3rem;
        color: #6EBBA5; /* Cor primária do seu tema */
        margin-bottom: 15px;
    }

    .card h3 {
        font-weight: 600;
        color: #31333F; /* Cor do texto do seu tema */
        margin-bottom: 10px;
    }

    .card p {
        color: #555;
        font-size: 0.9rem;
        line-height: 1.5;
        flex-grow: 1; /* Faz com que este elemento ocupe o espaço, empurrando o botão para baixo */
    }
</style>
""", unsafe_allow_html=True)


# --- Criação das Colunas e dos Cartões ---
col1, col2, col3 = st.columns(3)

# Coluna 1: Exames e Relatórios
with col1:
    with st.container(border=True):
        st.markdown("""
        <div class="card">
            <div>
                <div class="card-icon"><i class="fa-solid fa-file-medical"></i></div>
                <h3>Exames e Relatórios</h3>
                <p>Visualize, envie e gerencie os exames e relatórios de saúde do seu pet.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Ver Exames", key="exames", use_container_width=True):
            st.switch_page('paginas/exames.py') 

# Coluna 2: Registros do Pet
with col2:
    with st.container(border=True):
        st.markdown("""
        <div class="card">
            <div>
                <div class="card-icon"><i class="fa-solid fa-paw"></i></div>
                <h3>Registros do Pet</h3>
                <p>Acesse o perfil completo, incluindo informações de contato, vacinas e histórico de saúde.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Ver Registros", key="registros", use_container_width=True):
            st.switch_page('paginas/registros.py')

# Coluna 3: Chatbot Caramelo
with col3:
    with st.container(border=True):
        st.markdown("""
        <div class="card">
            <div>
                <div class="card-icon"><i class="fa-solid fa-comments"></i></div>
                <h3>Fale com o Dr. Caramelo</h3>
                <p>Tire dúvidas sobre a saúde e o bem-estar do seu pet com nosso assistente virtual com IA.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Conversar Agora", key="chatbot", use_container_width=True):
            st.switch_page('paginas/chatbot.py')
