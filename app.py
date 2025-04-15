import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#read in the file
df = pd.read_csv("https://raw.githubusercontent.com/nv-thang/Data-Visualization-Course/main/Dataset%20for%20Practice/movies.csv")

df.info()

df.dropna()

# Title
st.title("🎬 Movie Score Explorer (Using Matplotlib)")

# Sidebar
st.sidebar.header("🎛️ Bộ lọc")

score_filter = st.sidebar.radio(
    "Chọn tiêu chí điểm số:",
    ("Lớn nhất", "Nhỏ nhất")
)

# Lọc theo năm
df = df[df['year'] < 2010]

# Lọc theo lựa chọn từ sidebar
if score_filter == "Lớn nhất":
    filtered = df[df['score'] > 7.5]
    filtered = filtered.sort_values(by='score', ascending=False).head(10)

else:
    filtered = df[df['score'] < 3 ]
    filtered = filtered.sort_values(by='score', ascending=False).tail(10)


# Sắp xếp và chọn top 10

# Hiển thị bảng
st.subheader(f"📋 Top 10 phim {'có điểm cao' if score_filter == 'Lớn nhất' else 'có điểm thấp'} trước năm 2010")
st.dataframe(filtered[['name', 'score', 'year', 'genre']])

# Vẽ biểu đồ
st.subheader("📊 Biểu đồ điểm số phim")

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(filtered['name'], filtered['score'], color='salmon')
ax.set_xlabel('Score')
ax.set_ylabel('Movie Name')
ax.set_title(f"Top 10 Phim theo tiêu chí: {score_filter}")
ax.invert_yaxis()

# Hiển thị biểu đồ
st.pyplot(fig)
