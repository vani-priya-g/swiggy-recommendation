import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("cleaned_data.csv")
df['cuisine'] = df['cuisine'].astype(str).apply(lambda x: [i.strip() for i in x.split(',')])

# Page Setup
st.set_page_config("Swiggy Restaurant Recommender", page_icon="🍽️", layout="wide")

# Sidebar Filters
with st.sidebar:
    st.markdown("### 🌟 Customize Your Search")
    selected_city = st.selectbox("📍 City", sorted(df['city'].dropna().unique()))
    cuisines = sorted(set(c for sublist in df['cuisine'] for c in sublist))
    selected_cuisines = st.multiselect("🍽️ Cuisine", cuisines, default=["Biryani"])
    selected_rating = st.slider("⭐ Minimum Rating", 0.0, 5.0, 3.5, 0.1)
    selected_cost = st.slider("💰 Max Cost for Two", 100, 2000, 500, 50)
    dark_mode = st.checkbox("🌙 Dark Mode")

# Global Custom CSS with animation and sidebar color
st.markdown("""
    <style>
    @keyframes fadeSlide {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    section[data-testid="stSidebar"] {
        background-color: #f0f2f6;
        padding: 1rem;
        border-right: 2px solid #ddd;
        animation: fadeSlide 0.8s ease-in-out;
    }
    .restaurant-card {
        background-color: #e6f7ff;
        color: #000;
        padding: 1.5rem;
        border-radius: 1rem;
        margin-bottom: 2rem;
        animation: fadeSlide 0.8s ease-in-out;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align:center;'>🍴 Swiggy Restaurant Recommender</h1>", unsafe_allow_html=True)

# Filter Data
filtered_df = df[
    (df['city'].str.lower() == selected_city.lower()) &
    (df['rating'] >= selected_rating) &
    (df['cost'] <= selected_cost) &
    (df['cuisine'].apply(lambda x: any(c in x for c in selected_cuisines)))
]

# Show results
if not filtered_df.empty:
    st.success(f"🎯 {len(filtered_df)} restaurants found. Browse your recommendations below!")

    for _, row in filtered_df.iterrows():
        rating = row['rating']
        if rating >= 4.0:
            rating_color = "#28a745"  # Green
        elif rating >= 3.0:
            rating_color = "#fd7e14"  # Orange
        else:
            rating_color = "#dc3545"  # Red

        st.markdown(f"""
        <div class="restaurant-card">
            <h4 style="color:#007bff; margin-bottom:0.3rem;">{row['name']}</h4>
            <p>📍 <strong>City:</strong> {row['city']} &nbsp;&nbsp; 🍽️ {' , '.join(row['cuisine'])}</p>
            <p>⭐ <strong style="color:{rating_color};">Rating:</strong> <span style="color:{rating_color};">{rating} ({row['rating_count']} ratings)</span></p>
            <p>💸 <strong>Cost for two:</strong> ₹{row['cost']}</p>
            {f"<a href='{row['link']}' target='_blank' style='color:#6610f2; text-decoration:underline;'>🔗 View Menu</a>" if pd.notna(row['link']) else ""}
        </div>
        """, unsafe_allow_html=True)
else:
    st.warning("😕 No restaurants match your filters. Try adjusting your preferences.")
