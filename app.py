# =============================================
# CONCRETE INTELLIGENCE - CLEAN EXPO VERSION
# Ziauddin University Civil Engineering
# Build Asia Expo 2026 - Karachi, Pakistan
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
from datetime import datetime

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
# MINIMAL CSS - CLEAN & PROFESSIONAL
# =============================================
st.markdown("""
<style>
    /* Clean background */
    .stApp {
        background: #f8f9fa;
    }
    
    /* Only ONE main container */
    .main-container {
        background: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem auto;
        max-width: 1400px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }
    
    /* Professional title */
    .main-title {
        text-align: center;
        color: #2c3e50;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    /* Clean subtitle */
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Subtle section divider */
    .section {
        margin: 2rem 0;
        padding: 1.5rem;
        background: #f8f9fa;
        border-radius: 8px;
        border-left: 4px solid #3498db;
    }
    
    /* Clean button */
    .stButton>button {
        background: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
    }
    
    .stButton>button:hover {
        background: #2980b9;
    }
    
    /* Clean metric display */
    .metric-box {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #eaeaea;
    }
    
    /* Remove excessive white boxes from streamlit */
    div[data-testid="stVerticalBlock"] > div {
        background: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# =============================================
# LOAD AI MODEL
# =============================================
@st.cache_resource
def load_model():
    """Load trained AI model"""
    try:
        model = joblib.load('concrete_strength_model.pkl')
        feature_names = joblib.load('feature_names.pkl')
        return model, feature_names
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

model, feature_names = load_model()

# =============================================
# SIDEBAR - CLEAN & SIMPLE
# =============================================
with st.sidebar:
    st.markdown("## 🏗️ Concrete Intelligence")
    st.markdown("---")
    
    st.markdown("### 🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("*Karachi, Pakistan*")
    
    st.markdown("---")
    
    st.markdown("### 🎪 Build Asia Expo 2026")
    st.markdown("**Live AI Demonstration**")
    
    st.markdown("---")
    
    if model is not None:
        st.success("✅ **AI Model Active**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Not Loaded")
    
    st.markdown("---")
    st.markdown("📱 **Scan QR Code**")
    st.caption("concrete-ai-zu.streamlit.app")

# =============================================
# MAIN CONTENT - CLEAN LAYOUT
# =============================================

# HEADER
st.markdown("<h1 class='main-title'>🧠 CONCRETE INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>AI-Powered Concrete Strength Prediction System</p>", unsafe_allow_html=True)

# STATS BADGES (Simple row)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Accuracy", "87.6%", "R² Score")
with col2:
    st.metric("Error", "±5.7 MPa")
with col3:
    st.metric("Samples", "1,030+")
with col4:
    st.metric("University", "Ziauddin")

# MAIN CONTAINER (ONE box only)
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# =============================================
# INPUT SECTION - CLEAN & ORGANIZED
# =============================================
st.markdown("## 📊 Design Your Concrete Mix")

# Two columns for inputs
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

# Quick Presets
st.markdown("### ⚡ Quick Presets")
preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("🏠 Residential (Grade 25)", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
with preset_col2:
    if st.button("🏢 Commercial (Grade 35)", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
with preset_col3:
    if st.button("🌉 Structural (Grade 50)", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160

# Real-time Analysis
st.markdown("---")
st.markdown("## 📈 Real-Time Analysis")

wc_ratio = water / cement if cement > 0 else 0

analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
with analysis_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}")
with analysis_col2:
    st.metric("Total Powder", f"{cement + blast_slag + fly_ash} kg/m³")
with analysis_col3:
    st.metric("Total Aggregate", f"{coarse_agg + fine_agg} kg/m³")

# Water-cement feedback
if wc_ratio > 0.55:
    st.warning("⚠️ High water-cement ratio (>0.55) - May reduce strength")
elif wc_ratio < 0.35:
    st.info("✅ Low water-cement ratio - Good for strength")
else:
    st.success("✅ Optimal water-cement ratio (0.35-0.55)")

# =============================================
# PREDICTION BUTTON - CENTERED
# =============================================
st.markdown("---")
predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button(
        "🚀 **PREDICT CONCRETE STRENGTH**",
        type="primary",
        use_container_width=True,
        help="Click for AI-powered prediction"
    )

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    with st.spinner('🤖 AI analyzing your mix...'):
        time.sleep(0.5)
        
        # Prepare input
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
    
    # Show results
    st.balloons()
    
    st.markdown("---")
    st.markdown("## 🎉 Prediction Results")
    
    # Results in columns
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        st.metric("Predicted Strength", f"{predicted_strength:.1f} MPa")
    
    with result_col2:
        st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}")
    
    with result_col3:
        if predicted_strength >= 50:
            st.metric("Classification", "High-Strength", "Structural")
        elif predicted_strength >= 35:
            st.metric("Classification", "Standard", "Commercial")
        elif predicted_strength >= 25:
            st.metric("Classification", "Medium", "Residential")
        else:
            st.metric("Classification", "Low", "Non-structural")
    
    # Strength visualization
    st.progress(min(predicted_strength/80, 1.0))
    st.caption(f"Strength Scale: 0-80 MPa | Your mix: {predicted_strength:.1f} MPa")
    
    # Applications
    st.markdown("### 💡 Recommended Applications")
    
    if predicted_strength >= 50:
        st.success("**🏗️ High-Strength Concrete** - Columns, beams, bridges, high-rise buildings")
    elif predicted_strength >= 35:
        st.info("**🏢 Standard-Strength Concrete** - Commercial buildings, slabs, parking structures")
    elif predicted_strength >= 25:
        st.warning("**🏠 Medium-Strength Concrete** - Residential buildings, foundations, walls")
    else:
        st.error("**🛠️ Low-Strength Concrete** - Non-structural elements, blinding concrete")
    
    # Optimization suggestions
    st.markdown("### 🔧 Optimization Suggestions")
    
    suggestions = []
    if wc_ratio > 0.55:
        suggestions.append("Reduce water content to improve strength")
    if cement < 250 and predicted_strength < 30:
        suggestions.append("Increase cement content for structural applications")
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("Consider adding supplementary materials for durability")
    
    if suggestions:
        for suggestion in suggestions:
            st.markdown(f"• {suggestion}")
    else:
        st.success("✅ Your mix design is well-optimized!")

elif predict_clicked:
    st.error("❌ AI Model not loaded")

# CLOSE MAIN CONTAINER
st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# FOOTER - SIMPLE
# =============================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1.5rem; color: #7f8c8d;'>
    <h4>🏛️ Ziauddin University Civil Engineering Department</h4>
    <p>🎪 Build Asia Expo 2026 | Karachi, Pakistan</p>
    <p><strong>Live AI Tool - No Installation Required</strong></p>
    <p>🔗 <a href='https://concrete-ai-zu-haiderak27.streamlit.app' style='color: #3498db;'>
        concrete-ai-zu-haiderak27.streamlit.app
    </a></p>
</div>
""", unsafe_allow_html=True)
