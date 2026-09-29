import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re
from nltk.stem import SnowballStemmer

# ─────────────────────────────────────
# CONFIGURACIÓN
# ─────────────────────────────────────

st.set_page_config(
    page_title="TextDetective",
    page_icon="🕵️",
    layout="wide"
)

# ─────────────────────────────────────
# ESTILOS
# ─────────────────────────────────────

st.markdown("""
<style>

.stApp {
    background-color: #F5F0E6;
}

h1 {
    color: #29251F;
    font-weight: 800;
}

h2, h3 {
    color: #493F32;
}

p, label {
    color: #3D372F;
}

/* Tarjetas */
.card {
    background-color: #FFFDF8;
    border: 1px solid #D8CDBB;
    border-radius: 16px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 4px 12px rgba(60, 48, 30, 0.08);
}

/* Botones */
.stButton > button {
    background-color: #3D372F;
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #635442;
}

/* Botón principal */
button[kind="primary"] {
    background-color: #B8872F !important;
    color: white !important;
}

/* Métricas */
[data-testid="stMetric"] {
    background-color: #FFFDF8;
    border: 1px solid #D8CDBB;
    border-radius: 12px;
    padding: 12px;
}

/* Inputs */
textarea, input {
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────
# ENCABEZADO
# ─────────────────────────────────────

st.markdown("""
<div class="card">

<h1>🕵️ TextDetective</h1>

<p>
Analiza documentos, encuentra coincidencias y descubre
qué expediente está más relacionado con tu pregunta.
</p>

</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────
# DOCUMENTOS
# ─────────────────────────────────────

default_docs = """El perro ladra fuerte en el parque.
El gato maúlla suavemente durante la noche.
El perro y el gato juegan juntos en el jardín.
Los niños corren y se divierten en el parque.
La música suena muy alta en la fiesta.
Los pájaros cantan hermosas melodías al amanecer."""


# Stemmer español
stemmer = SnowballStemmer("spanish")


def tokenize_and_stem(text):

    text = text.lower()

    text = re.sub(
        r'[^a-záéíóúüñ\s]',
        ' ',
        text
    )

    tokens = [
        t for t in text.split()
        if len(t) > 1
    ]

    stems = [
        stemmer.stem(t)
        for t in tokens
    ]

    return stems


# ─────────────────────────────────────
# ENTRADAS
# ─────────────────────────────────────

col1, col2 = st.columns([2, 1])


with col1:

    st.markdown("""
    <div class="card">
    <h3>📁 Expedientes</h3>
    <p>
    Introduce los documentos que quieres investigar,
    uno por línea.
    </p>
    </div>
    """, unsafe_allow_html=True)

    text_input = st.text_area(
        "Documentos:",
        default_docs,
        height=170
    )

    question = st.text_input(
        "🔎 Pregunta de investigación:",
        "¿Dónde juegan el perro y el gato?"
    )


with col2:

    st.markdown("""
    <div class="card">
    <h3>💡 Pistas sugeridas</h3>
    <p>
    Selecciona una pregunta para comenzar la investigación.
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(
        "🐶 ¿Dónde juegan el perro y el gato?",
        use_container_width=True
    ):
        st.session_state.question = (
            "¿Dónde juegan el perro y el gato?"
        )
        st.rerun()

    if st.button(
        "👦 ¿Qué hacen los niños en el parque?",
        use_container_width=True
    ):
        st.session_state.question = (
            "¿Qué hacen los niños en el parque?"
        )
        st.rerun()

    if st.button(
        "🐦 ¿Cuándo cantan los pájaros?",
        use_container_width=True
    ):
        st.session_state.question = (
            "¿Cuándo cantan los pájaros?"
        )
        st.rerun()

    if st.button(
        "🎵 ¿Dónde suena la música alta?",
        use_container_width=True
    ):
        st.session_state.question = (
            "¿Dónde suena la música alta?"
        )
        st.rerun()

    if st.button(
        "🐱 ¿Qué animal maúlla durante la noche?",
        use_container_width=True
    ):
        st.session_state.question = (
            "¿Qué animal maúlla durante la noche?"
        )
        st.rerun()


# ─────────────────────────────────────
# ACTUALIZAR PREGUNTA
# ─────────────────────────────────────

if "question" in st.session_state:
    question = st.session_state.question


# ─────────────────────────────────────
# ANALIZAR
# ─────────────────────────────────────

if st.button(
    "🕵️ Investigar expediente",
    type="primary"
):

    documents = [
        d.strip()
        for d in text_input.split("\n")
        if d.strip()
    ]

    if len(documents) < 1:

        st.error(
            "⚠️ No hay expedientes para investigar."
        )

    elif not question.strip():

        st.error(
            "⚠️ Escribe una pregunta de investigación."
        )

    else:

        # ─────────────────────────────
        # TF-IDF
        # ─────────────────────────────

        vectorizer = TfidfVectorizer(
            tokenizer=tokenize_and_stem,
            min_df=1
        )

        X = vectorizer.fit_transform(documents)


        # ─────────────────────────────
        # MATRIZ
        # ─────────────────────────────

        st.markdown("""
        <div class="card">
        <h3>📋 Evidencia encontrada</h3>
        <p>
        Esta matriz muestra la importancia de cada término
        dentro de los expedientes.
        </p>
        </div>
        """, unsafe_allow_html=True)

        df_tfidf = pd.DataFrame(
            X.toarray(),
            columns=vectorizer.get_feature_names_out(),
            index=[
                f"Expediente {i + 1}"
                for i in range(len(documents))
            ]
        )

        st.dataframe(
            df_tfidf.round(3),
            use_container_width=True
        )


        # ─────────────────────────────
        # SIMILITUD
        # ─────────────────────────────

        question_vec = vectorizer.transform(
            [question]
        )

        similarities = cosine_similarity(
            question_vec,
            X
        ).flatten()


        best_idx = similarities.argmax()

        best_doc = documents[best_idx]

        best_score = similarities[best_idx]


        # ─────────────────────────────
        # RESULTADO
        # ─────────────────────────────

        st.markdown("""
        <div class="card">
        <h3>🎯 Pista principal</h3>
        </div>
        """, unsafe_allow_html=True)

        st.write(
            f"**Pregunta:** {question}"
        )

        if best_score > 0.01:

            st.success(
                f"📁 **Expediente relacionado:** "
                f"{best_idx + 1}"
            )

            st.write(
                f"**Evidencia:** {best_doc}"
            )

            st.metric(
                "Nivel de coincidencia",
                f"{best_score:.3f}"
            )

        else:

            st.warning(
                f"📁 **Coincidencia débil:** "
                f"Expediente {best_idx + 1}"
            )

            st.write(
                f"**Evidencia encontrada:** {best_doc}"
            )

            st.metric(
                "Nivel de coincidencia",
                f"{best_score:.3f}"
            )


        # ─────────────────────────────
        # TODAS LAS COINCIDENCIAS
        # ─────────────────────────────

        st.markdown("""
        <div class="card">
        <h3>📊 Comparación de expedientes</h3>
        </div>
        """, unsafe_allow_html=True)

        sim_df = pd.DataFrame({
            "Expediente": [
                f"Expediente {i + 1}"
                for i in range(len(documents))
            ],
            "Evidencia": documents,
            "Coincidencia": similarities
        })

        sim_df = sim_df.sort_values(
            "Coincidencia",
            ascending=False
        )

        st.dataframe(
            sim_df,
            use_container_width=True,
            hide_index=True
        )


        # ─────────────────────────────
        # GRÁFICO
        # ─────────────────────────────

        st.markdown("### 📈 Nivel de coincidencia")

        chart = sim_df.set_index(
            "Expediente"
        )[["Coincidencia"]]

        st.bar_chart(chart)


# ─────────────────────────────────────
# PIE
# ─────────────────────────────────────

st.markdown("---")

st.caption(
    "🕵️ TextDetective · Análisis de texto "
    "con TF-IDF y similitud coseno"
)
