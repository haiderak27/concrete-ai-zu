# =============================================
# CONCRETE INTELLIGENCE - EXPO 2026
# Ziauddin University Civil Engineering
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time

# =============================================
# PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# CUSTOM CSS - WORKING VERSION
# =============================================
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main content area */
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Cards */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #FF8E53 0%, #FF6B6B 100%);
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(255,107,107,0.4);
    }
    
    /* Title */
    .main-title {
        text-align: center;
        font-size: 3.5rem !important;
        background: linear-gradient(90deg, #FF6B6B, #FF8E53, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
    }
    
    /* Stats badges */
    .stats-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        display: inline-block;
        margin: 0.2rem;
        font-weight: bold;
    }
    
    /* Floating effect */
    .float-animation {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    /* Slider color */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# LOAD AI MODEL
# =============================================
@st.cache_resource
def load_model():
    try:
        model = joblib.load('concrete_strength_model.pkl')
        feature_names = joblib.load('feature_names.pkl')
        return model, feature_names
    except:
        return None, None

model, feature_names = load_model()

# =============================================
# SIDEBAR
# =============================================
with st.sidebar:
    st.markdown("## 🏗️ CONCRETE INTELLIGENCE")
    st.markdown("---")
    
    st.markdown("### 🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("*Karachi, Pakistan*")
    
    st.markdown("---")
    st.markdown("### 🎪 Build Asia Expo 2026")
    st.markdown("**Live AI Demonstration**")
    
    st.markdown("---")
    if model is not None:
        st.success("✅ **AI MODEL ACTIVE**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")

# =============================================
# MAIN CONTENT
# =============================================

# HEADER
st.markdown('<h1 class="main-title">🧠 CONCRETE INTELLIGENCE</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: white;">AI-Powered Concrete Strength Prediction</h3>', unsafe_allow_html=True)

# STATS BADGES
st.markdown('<div style="text-align: center; margin: 1rem 0;">', unsafe_allow_html=True)
st.markdown('<span class="stats-badge">🏗️ 87.6% Accurate</span>', unsafe_allow_html=True)
st.markdown('<span class="stats-badge">⚡ Instant Predictions</span>', unsafe_allow_html=True)
st.markdown('<span class="stats-badge">💰 Saves 15-20% Cost</span>', unsafe_allow_html=True)
st.markdown('<span class="stats-badge">🏆 Expo 2026</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# MAIN CONTAINER
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# INPUT SECTION
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.markdown("## 📊 DESIGN YOUR CONCRETE MIX")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Cementitious Materials")
    cement = st.slider("**Cement** (kg/m³)", 100, 500, 300)
    water = st.slider("**Water** (kg/m³)", 100, 250, 180)
    blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50)
    fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30)

with col2:
    st.markdown("### Aggregates & Admixtures")
    superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5)
    coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900)
    fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700)
    age = st.slider("**Curing Age** (days)", 1, 90, 28)

st.markdown('</div>', unsafe_allow_html=True)

# QUICK PRESETS
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
st.markdown("## 🚀 QUICK PRESETS")

preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("🏠 Grade 25 (Residential)", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
with preset_col2:
    if st.button("🏢 Grade 35 (Commercial)", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
with preset_col3:
    if st.button("🌉 Grade 50 (Structural)", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160
st.markdown('</div>', unsafe_allow_html=True)

# REAL-TIME METRICS
st.markdown('<div class="custom-card">', unsafe_allow_html=True)
wc_ratio = water / cement if cement > 0 else 0
st.markdown("## 📈 REAL-TIME ANALYSIS")

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}")
with metric_col2:
    st.metric("Total Cementitious", f"{cement + blast_slag + fly_ash} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{coarse_agg + fine_agg} kg/m³")

# W/C Ratio Indicator
if wc_ratio > 0.55:
    st.warning("⚠️ High water-cement ratio (>0.55) - May reduce strength")
elif wc_ratio < 0.35:
    st.info("✅ Low W/C ratio - Good for strength")
else:
    st.success("✅ Optimal water-cement ratio (0.35-0.55)")

st.markdown('</div>', unsafe_allow_html=True)

# PREDICTION BUTTON
st.markdown('<div style="text-align: center; margin: 2rem 0;">', unsafe_allow_html=True)
st.markdown('<div class="float-animation">', unsafe_allow_html=True)
predict_clicked = st.button("🚀 **AI PREDICT STRENGTH NOW** 🚀", 
                           type="primary", 
                           use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# PREDICTION RESULTS
if predict_clicked and model is not None:
    with st.spinner('🤖 AI is analyzing your mix...'):
        time.sleep(1)
        input_data = pd.DataFrame([{
            'cement': cement,
            'blast_furnace_slag': blast_slag,
            'fly_ash': fly_ash,
            'water': water,
            'superplasticizer': superplasticizer,
            'coarse_aggregate': coarse_agg,
            'fine_aggregate': fine_agg,
            'age': age
        }])
        input_data = input_data[feature_names]
        predicted_strength = model.predict(input_data)[0]
    
    st.balloons()
    
    st.markdown('<div class="custom-card" style="border-left: 5px solid #FF6B6B;">', unsafe_allow_html=True)
    st.markdown("## 🎉 **PREDICTION RESULTS**")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Predicted Strength", f"{predicted_strength:.1f} MPa")
    with col2:
        st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}")
    with col3:
        if predicted_strength >= 50:
            st.metric("Classification", "High-Strength", "Structural")
        elif predicted_strength >= 35:
            st.metric("Classification", "Standard", "Commercial")
        elif predicted_strength >= 25:
            st.metric("Classification", "Medium", "Residential")
        else:
            st.metric("Classification", "Low", "Non-structural")
    
    # Strength bar
    progress = min(predicted_strength/80, 1.0)
    st.progress(progress)
    st.caption(f"Strength Scale: 0-80 MPa | Your mix: {predicted_strength:.1f} MPa")
    
    # Applications
    if predicted_strength >= 50:
        st.success("**🏗️ HIGH-STRENGTH:** Columns, beams, bridges, high-rise buildings")
    elif predicted_strength >= 35:
        st.info("**🏢 STANDARD:** Commercial buildings, parking structures, slabs")
    elif predicted_strength >= 25:
        st.warning("**🏠 MEDIUM:** Residential buildings, foundations, walls")
    else:
        st.error("**🛠️ LOW:** Non-structural elements, blinding concrete")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # OPTIMIZATION
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("## 🔧 **OPTIMIZATION SUGGESTIONS**")
    
    if wc_ratio > 0.55:
        st.markdown("- 💧 **Reduce water by 10-15%** to increase strength")
    if cement < 250 and predicted_strength < 30:
        st.markdown("- 🏗️ **Increase cement to 300+ kg/m³** for structural use")
    if blast_slag == 0 and fly_ash == 0:
        st.markdown("- 🌿 **Add slag/fly ash (50-100 kg/m³)** for durability")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ AI Model not loaded")

st.markdown('</div>', unsafe_allow_html=True)  # Close main container

# FOOTER
st.markdown("""
<div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px; margin-top: 2rem;'>
    <h3 style='color: white;'>🏛️ Ziauddin University Civil Engineering</h3>
    <h4 style='color: white;'>🎪 Build Asia Expo 2026 | Karachi, Pakistan</h4>
    
    <div style='margin: 1rem 0;'>
        <span style='background: #667eea; color: white; padding: 0.5rem 1rem; border-radius: 25px; margin: 0.2rem; display: inline-block;'>AI Accuracy: 87.6%</span>
        <span style='background: #764ba2; color: white; padding: 0.5rem 1rem; border-radius: 25px; margin: 0.2rem; display: inline-block;'>Error: ±5.7 MPa</span>
        <span style='background: #FF6B6B; color: white; padding: 0.5rem 1rem; border-radius: 25px; margin: 0.2rem; display: inline-block;'>Trained on 1,030+ samples</span>
    </div>
    
    <p style='color: white;'>
        <strong>Live AI Tool - No Installation Required</strong><br>
        🔗 <strong>URL:</strong> https://concrete-ai-zu-haiderak27.streamlit.app
    </p>
</div>
""", unsafe_allow_html=True)
