import streamlit as st
import pandas as pd
import altair as alt

# -----------------------------------
# Load Data
# -----------------------------------
@st.cache_data
def load_data():
    return pd.read_excel("data-gol-premier-league-25-26.xlsx")

df = load_data()
df.index = df.index + 1  # Start index from 1

# -----------------------------------
# Page Config
# -----------------------------------
st.set_page_config(
    page_title="Premier League Top Scorers",
    layout="wide",
    page_icon="⚽"
)

# -----------------------------------
# Custom CSS
# -----------------------------------
st.markdown("""
<style>
.header-title {
    font-size: 40px;
    font-weight: bold;
    color: #1E90FF;
    text-align: center;
    padding-bottom: 10px;
}
.subtitle {
    font-size: 18px;
    text-align: center;
    color: #6c757d;
    margin-bottom: 30px;
}
.dataframe table {
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Header
# -----------------------------------
st.markdown("<div class='header-title'>Premier League Goal Leaderboard</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Data per pemain: nama & jumlah gol</div>", unsafe_allow_html=True)

# -----------------------------------
# Search Player
# -----------------------------------
st.markdown("### 🔍 Cari Pemain")
search = st.text_input("Masukkan nama pemain:")

filtered_df = df[df["Name"].str.contains(search, case=False)] if search else df

# -----------------------------------
# Show Table
# -----------------------------------
st.markdown("### 📋 Tabel Data Pemain")
st.dataframe(
    filtered_df,
    use_container_width=True
)

# -----------------------------------
# Top Goals Chart
# -----------------------------------
st.markdown("### 📊 Grafik Top Skor")

chart = (
    alt.Chart(filtered_df.sort_values("Gol", ascending=False).head(10))
    .mark_bar(color="#1E90FF")
    .encode(
        x=alt.X("Gol:Q", title="Jumlah Gol"),
        y=alt.Y("Name:N", sort="-x", title="Pemain"),
        tooltip=["Name", "Gol"]
    )
    .properties(height=400)
)

st.altair_chart(chart, use_container_width=True)

# -----------------------------------
# Footer
# -----------------------------------
st.markdown("---")
st.markdown("⚽ Dibuat dengan **Streamlit** - by Fikri Alfian.")
