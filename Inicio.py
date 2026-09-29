import streamlit as st
from PIL import Image

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="AI Lab",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(139,79,203,0.10), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(242,201,76,0.12), transparent 25%),
        #FAF9FF;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #35145C 0%, #5B2A86 55%, #7139A5 100%);
}

[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: white;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #35145C, #7139A5);
    padding: 42px 35px;
    border-radius: 28px;
    text-align: center;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 35px rgba(72, 35, 110, 0.22);
    border: 1px solid rgba(255,255,255,0.15);
}

.hero h1 {
    font-size: 43px;
    margin: 0 0 10px 0;
    font-weight: 800;
}

.hero p {
    font-size: 17px;
    margin: 0;
    opacity: 0.92;
}

/* Intro */
.info-box {
    background: linear-gradient(135deg, #FFF7C7, #FFF1A8);
    border: 1px solid #F2D46B;
    border-left: 7px solid #F2C94C;
    padding: 20px 24px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 5px 15px rgba(120, 90, 20, 0.08);
}

.info-box h3 {
    color: #4A206B;
    margin: 0 0 5px 0;
}

.info-box p {
    color: #5B4B20;
    margin: 0;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.92);
    border: 1px solid #E6DDF0;
    border-radius: 22px;
    padding: 20px;
    margin-bottom: 22px;
    min-height: 345px;
    box-shadow: 0 8px 25px rgba(70,40,100,0.08);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 14px 32px rgba(91,42,134,0.16);
    border-color: #CDB4E5;
}

.card h3 {
    color: #4D2072;
    font-size: 20px;
    margin: 8px 0 10px 0;
    line-height: 1.25;
}

.card p {
    color: #5E5964;
    font-size: 14px;
    line-height: 1.55;
}

/* Tags */
.tag {
    display: inline-block;
    padding: 5px 11px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 0.5px;
}

.purple {
    background: #EDE0F8;
    color: #5B2A86;
}

.yellow {
    background: #FFF1A8;
    color: #735900;
}

/* Links */
.boton {
    display: inline-block;
    background: #5B2A86;
    color: white !important;
    text-decoration: none;
    padding: 9px 17px;
    border-radius: 11px;
    font-weight: 700;
    font-size: 13px;
    margin-top: 7px;
    transition: 0.2s;
}

.boton:hover {
    background: #F2C94C;
    color: #43205F !important;
}

/* Separador */
.sparkles {
    text-align: center;
    color: #D1A92F;
    font-size: 22px;
    letter-spacing: 12px;
    margin: 10px 0 25px 0;
}

/* Footer */
.footer {
    text-align: center;
    color: #76529A;
    padding: 30px 10px;
    margin-top: 25px;
}

.footer strong {
    color: #5B2A86;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------

with st.sidebar:

    st.markdown("## 🤖 AI LAB")

    st.markdown("---")

    st.markdown("### Laboratorio de IA")

    st.write(
        "Un espacio para explorar aplicaciones prácticas "
        "de Inteligencia Artificial mediante diferentes "
        "herramientas y experimentos."
    )

    st.markdown("---")

    st.markdown("### ✦ Explora")

    st.write("🎙️ Voz y audio")
    st.write("👁️ Visión artificial")
    st.write("📊 Datos y texto")
    st.write("📄 Documentos")
    st.write("🧠 Modelos de IA")
    st.write("⚙️ Sistemas interactivos")


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <h1>🤖 AI Lab</h1>
    <p>
        Explorando aplicaciones creativas y prácticas de Inteligencia Artificial
    </p>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENLACE PRINCIPAL
# --------------------------------------------------

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown("""
<div class="info-box">
    <h3>✨ Explora el laboratorio completo</h3>
    <p>
        Encuentra más páginas, ejercicios y experimentos relacionados
        con Inteligencia Artificial.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a class="boton" href="{url_ia}" target="_blank">'
    '🔗 Ver páginas y ejercicios →'
    '</a>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sparkles">✦ · ✧ · ✦</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# COLUMNAS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)


# ==================================================
# COLUMNA 1
# ==================================================

with col1:

    # 1
    st.markdown("""
    <div class="card">
        <span class="tag yellow">🎙️ AUDIO</span>
        <h3>Conversión de texto a voz</h3>
    """, unsafe_allow_html=True)

    image = Image.open("txt_to_audio2.png")
    st.image(image, width=190)

    st.write(
        "Convierte texto escrito en voz utilizando una aplicación "
        "basada en Inteligencia Artificial."
    )

    st.markdown(
        '<a class="boton" href="https://interfazmultimodal1-paula.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 2
    st.markdown("""
    <div class="card">
        <span class="tag purple">💗 INTERACTIVO</span>
        <h3>Mi Mood de Hoy</h3>
    """, unsafe_allow_html=True)

    image = Image.open("txt_to_audio.png")
    st.image(image, width=200)

    st.write(
        "Un espacio interactivo para compartir mi estado de ánimo, "
        "explorar emociones y descubrir qué tan relatable es mi mood del día."
    )

    st.markdown(
        '<a class="boton" href="https://introstrelit.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 3
    st.markdown("""
    <div class="card">
        <span class="tag yellow">🔎 VISIÓN</span>
        <h3>Reconocimiento Óptico de Caracteres</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG5.jpg")
    st.image(image, width=200)

    st.write(
        "Convierte imágenes en texto de forma rápida y sencilla "
        "mediante reconocimiento automático de caracteres."
    )

    st.markdown(
        '<a class="boton" href="https://4di4tgzegjkvtdx98nnspw.streamlit.app/" target="_blank">'
        'Probar modelo →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# COLUMNA 2
# ==================================================

with col2:

    # 4
    st.markdown("""
    <div class="card">
        <span class="tag purple">🗣️ VOZ</span>
        <h3>Traductor</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG8.jpg")
    st.image(image, width=200)

    st.write(
        "Traduce lo que dices de forma interactiva. "
        "Habla, selecciona el idioma y deja que la herramienta haga el resto."
    )

    st.markdown(
        '<a class="boton" href="https://traductorr5d9v9t32kchhniyxnsdos.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 5
    st.markdown("""
    <div class="card">
        <span class="tag yellow">📷 TRADUCCIÓN</span>
        <h3>LumiTranslate</h3>
    """, unsafe_allow_html=True)

    image = Image.open("data_analisis.png")
    st.image(image, width=190)

    st.write(
        "Convierte imágenes en texto y traduce su contenido "
        "a diferentes idiomas con ayuda de la Inteligencia Artificial."
    )

    st.markdown(
        '<a class="boton" href="https://ocr-audio-wvhaldww4dn4zze8kltksm.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 6
    st.markdown("""
    <div class="card">
        <span class="tag purple">☁️ TEXTO</span>
        <h3>WordCloud: Laboratorio de Palabras</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG3.jpg")
    st.image(image, width=200)

    st.write(
        "Analiza un texto, identifica las palabras más frecuentes "
        "y conviértelas en una nube visual personalizable."
    )

    st.markdown(
        '<a class="boton" href="https://wordcloud-8xcyhnovzzx3urhzjdvxcf.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ==================================================
# COLUMNA 3
# ==================================================

with col3:

    # 7
    st.markdown("""
    <div class="card">
        <span class="tag yellow">👁️ VISIÓN</span>
        <h3>VisionScan</h3>
    """, unsafe_allow_html=True)

    image = Image.open("Chat_pdf.png")
    st.image(image, width=190)

    st.write(
        "Utiliza visión artificial para identificar objetos "
        "en imágenes capturadas con la cámara."
    )

    st.markdown(
        '<a class="boton" href="https://yolov5-bhfvwptkqgplobjtsjr8xj.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 8
    st.markdown("""
    <div class="card">
        <span class="tag purple">🕵️ TEXTO</span>
        <h3>TextDetective</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG4.jpg")
    st.image(image, width=200)

    st.write(
        "Analiza documentos y encuentra la pista más relacionada "
        "con tu pregunta mediante TF-IDF y similitud de textos."
    )

    st.markdown(
        '<a class="boton" href="https://questanswer-qnpwbc5jnzurzcdjfnrzzp.streamlit.app/" target="_blank">'
        'Probar aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


    # 9
    st.markdown("""
    <div class="card">
        <span class="tag yellow">⚙️ INTERACCIÓN</span>
        <h3>Sistema Ciberfísico</h3>
    """, unsafe_allow_html=True)

    image = Image.open("OIG6.jpg")
    st.image(image, width=200)

    st.write(
        "Explora la interacción entre la Inteligencia Artificial "
        "y el mundo físico mediante un sistema interactivo."
    )

    st.markdown(
        '<a class="boton" href="https://vision2-gpt4o.streamlit.app/" target="_blank">'
        'Ver aplicación →</a>',
        unsafe_allow_html=True
    )

    st.markdown("</div>", unsafe_allow_html=True)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">
    <div class="sparkles">✦ · ✧ · ✦</div>
    <strong>🤖 AI Lab</strong>
    <br>
    Explorando las posibilidades de la Inteligencia Artificial
    <br>
    <small>Aplicaciones · Experimentación · Creatividad</small>
</div>
""", unsafe_allow_html=True)
