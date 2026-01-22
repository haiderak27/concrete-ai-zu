# =============================================
# CONCRETE INTELLIGENCE - EXPO 2026
# Ziauddin University Civil Engineer# =============================================
# CONCRETE INTELLIGENCE - P# =============================================
# CONCRETE INTELLIGENCE # =============================================
# CONCRETE INTELLIGENCE - EXPO EDITION
# Ziauddin University Civil Engineering
# Build Asia Expo 2026 - Karachi, Pakistan
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time

# =============================================
# PAGE CONFIG - EXPO MODE
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# =============================================
# CUSTOM CSS - EYE-CATCHING EFFECTS
# =============================================
st.markdown("""
<style>
    /* Vibrant gradient background */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Main container with glass effect */
    .main {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    /* Floating animation for buttons */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
    
    .float-btn {
        animation: float 3s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    
    .float-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(0,0,0,0.4);
    }
    
    /* Gradient buttons */
    .stButton>button {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 2rem;
        font-size: 1.2rem;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #FF8E53 0%, #FF6B6B 100%);
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(255,107,107,0.4);
    }
    
    /* Card styling */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: transform 0.3s;
    }
    
    .card:hover {
        transform: translateY(-5px);
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
    
    /* Animated title */
    @keyframes glow {
        0% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #667eea; }
        50% { text-shadow: 0 0 20px #fff, 0 0 30px #764ba2, 0 0 40px #764ba2; }
        100% { text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 30px #667eea; }
    }
    
    .glow-title {
        animation: glow 2s ease-in-out infinite;
        text-align: center;
        font-size: 3.5rem !important;
        background: linear-gradient(90deg, #FF6B6B, #FF8E53, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
    }
    
    /* Slider styling */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Progress bar for predictions */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #FF6B6B 0%, #FF8E53 100%);
    }
    
    /* Floating particles effect */
    .particles {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        pointer-events: none;
        z-index: -1;
    }
</style>

<div class="particles"></div>
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
        column_ranges = joblib.load('column_ranges.pkl')
        return model, feature_names, column_ranges
    except Exception as e:
        return None, None, None

# Load model
model, feature_names, column_ranges = load_model()

# =============================================
# SIDEBAR - EXPO MODE
# =============================================
with st.sidebar:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>🏗️ CONCRETE INTELLIGENCE</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("*Karachi, Pakistan*")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎪 Build Asia Expo 2026")
    st.markdown("**Live Demonstration**")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if model is not None:
        st.success("✅ **AI MODEL ACTIVE**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📱 Quick Access")
    st.markdown("**Scan QR code to try on your phone**")
    st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - EXPO DESIGN
# =============================================

# HEADER WITH ANIMATIONS
st.markdown("<h1 class='glow-title'>🧠 CONCRETE INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white; margin-bottom: 2rem;'>AI-Powered Concrete Strength Prediction & Optimization</h3>", unsafe_allow_html=True)

# STATS BADGES ROW
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='stats-badge'>🏗️ 87.6% Accurate</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='stats-badge'>⚡ Instant Predictions</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='stats-badge'>💰 Saves 15-20% Cost</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='stats-badge'>🏆 Expo 2026</div>", unsafe_allow_html=True)

# MAIN CONTENT CONTAINER
st.markdown("<div class='main'>", unsafe_allow_html=True)

# =============================================
# INPUT SECTION - FLOATING DESIGN
# =============================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📊 DESIGN YOUR CONCRETE MIX")

# Create tabs for different input modes
tab1, tab2, tab3 = st.tabs(["🎯 Standard Mix", "⚡ Quick Presets", "🔧 Advanced"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Cementitious Materials")
        cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                         help="Primary binding material - Most important factor")
        water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                         help="Critical for workability - Affects strength significantly")
        blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                              help="Improves durability - Reduces heat")
        fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                           help="Pozzolanic material - Enhances workability")
    
    with col2:
        st.markdown("### Aggregates & Admixtures")
        superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                    help="High-range water reducer - Improves flow")
        coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                              help="20mm crushed stone - Provides bulk")
        fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                            help="Natural sand - Fills voids")
        age = st.slider("**Curing Age** (days)", 1, 90, 28,
                       help="Testing age - Strength increases with time")

with tab2:
    st.markdown("### 🚀 Quick Preset Mixes")
    preset_col1, preset_col2, preset_col3 = st.columns(3)
    
    with preset_col1:
        if st.button("🏠 Grade 25 (Residential)", use_container_width=True):
            st.session_state.cement = 300
            st.session_state.water = 180
            st.session_state.age = 28
    
    with preset_col2:
        if st.button("🏢 Grade 35 (Commercial)", use_container_width=True):
            st.session_state.cement = 350
            st.session_state.water = 175
            st.session_state.age = 28
    
    with preset_col3:
        if st.button("🌉 Grade 50 (Structural)", use_container_width=True):
            st.session_state.cement = 400
            st.session_state.water = 160
            st.session_state.age = 28

with tab3:
    st.markdown("### 🔬 Advanced Parameters")
    st.info("For expert users - Fine-tune all parameters")
    # You can add more advanced controls here

st.markdown("</div>", unsafe_allow_html=True)

# REAL-TIME CALCULATIONS
wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

# METRICS DISPLAY
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📈 REAL-TIME ANALYSIS")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Ideal: 0.4-0.5" if 0.4 <= wc_ratio <= 0.5 else "Adjust")
with metric_col2:
    st.metric("Total Powder", f"{total_powder} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")
with metric_col4:
    st.metric("Aggregate Ratio", f"{coarse_agg/fine_agg:.2f}" if fine_agg > 0 else "0")

# Visual indicator for W/C ratio
if wc_ratio > 0.55:
    st.warning("⚠️ High water-cement ratio (>0.55) - May reduce strength")
elif wc_ratio < 0.35:
    st.info("✅ Low water-cement ratio - Good for strength, check workability")
else:
    st.success("✅ Optimal water-cement ratio (0.35-0.55)")

st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# FLOATING PREDICTION BUTTON
# =============================================
st.markdown("""
<div style='text-align: center; margin: 3rem 0;'>
    <div class='float-btn'>
""", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button(
        "🚀 **AI PREDICT STRENGTH NOW** 🚀",
        type="primary",
        use_container_width=True,
        help="Click to get instant AI prediction"
    )

st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# PREDICTION RESULTS - ANIMATED
# =============================================
if predict_clicked and model is not None:
    # Show loading animation
    with st.spinner('🤖 AI is analyzing your mix...'):
        time.sleep(1)  # Simulate processing
        
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
        
        # Ensure correct column order
        input_data = input_data[feature_names]
        
        # Make prediction
        predicted_strength = model.predict(input_data)[0]
    
    # SHOW RESULTS WITH FANFARE
    st.balloons()
    
    st.markdown("<div class='card' style='border-left: 5px solid #FF6B6B;'>", unsafe_allow_html=True)
    st.markdown("## 🎉 **PREDICTION RESULTS**")
    
    # Result metrics in columns
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            label="**Predicted Strength**",
            value=f"{predicted_strength:.1f}",
            delta="MPa",
            delta_color="normal"
        )
    
    with res_col2:
        st.metric(
            label="**Water-Cement Ratio**",
            value=f"{wc_ratio:.3f}",
            delta="Optimal" if 0.4 <= wc_ratio <= 0.5 else "Adjust"
        )
    
    with res_col3:
        # Strength classification with colors
        if predicted_strength >= 50:
            classification = "High-Strength"
            color = "green"
            icon = "🏗️"
            use = "Structural"
        elif predicted_strength >= 35:
            classification = "Standard"
            color = "blue"
            icon = "🏢"
            use = "Commercial"
        elif predicted_strength >= 25:
            classification = "Medium"
            color = "orange"
            icon = "🏠"
            use = "Residential"
        else:
            classification = "Low"
            color = "red"
            icon = "🛠️"
            use = "Non-structural"
        
        st.metric(
            label="**Classification**",
            value=f"{icon} {classification}",
            delta=use
        )
    
    # Progress bar visualization
    st.progress(min(predicted_strength/80, 1.0))
    st.caption(f"Strength Scale: 0-80 MPa | Your mix: {predicted_strength:.1f} MPa")
    
    # Strength interpretation
    st.markdown("### 💡 **Recommended Applications**")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (>50 MPa)**
        - **Best for:** Columns, beams, bridges, high-rise buildings
        - **Karachi Examples:** Bahria Icon Tower, Ocean Towers
        - **Advantages:** Higher load capacity, reduced member sizes
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        - **Best for:** Commercial buildings, parking structures, slabs
        - **Karachi Examples:** Dolmen Mall, Lucky One Mall
        - **Advantages:** Optimal balance of strength and cost
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        - **Best for:** Residential buildings, foundations, walls
        - **Karachi Examples:** Houses, apartments, small buildings
        - **Advantages:** Cost-effective for typical construction
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        - **Best for:** Non-structural elements, blinding concrete
        - **Karachi Examples:** Footpaths, boundary walls, landscaping
        - **Advantages:** Economical for non-load-bearing applications
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # OPTIMIZATION SUGGESTIONS
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 🔧 **AI Optimization Suggestions**")
    
    suggestions = []
    
    # Water-cement suggestions
    if wc_ratio > 0.55:
        suggestions.append("💧 **Reduce water by 10-15%** - Current W/C ratio is high (>0.55)")
    elif wc_ratio < 0.35:
        suggestions.append("⚗️ **Add superplasticizer** - Very low W/C may affect workability")
    
    # Cement optimization
    if cement < 250 and predicted_strength < 30:
        suggestions.append("🏗️ **Increase cement to 300+ kg/m³** for structural applications")
    elif cement > 400:
        suggestions.append("💰 **Consider slag/fly ash** - Reduce cement to save cost")
    
    # Supplementary materials
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("🌿 **Add 50-100 kg/m³ supplementary materials** for durability")
    
    # Age suggestion
    if age < 28:
        suggestions.append("⏳ **Wait for 28-day strength** - Current prediction is for early age")
    
    if suggestions:
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")
    else:
        st.success("✅ **Your mix design is well-optimized!**")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ **AI Model not loaded** - Please check model files")

# CLOSE MAIN CONTAINER
st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# FOOTER - EXPO INFO
# =============================================
st.markdown("""
<div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px; margin-top: 2rem;'>
    <h3 style='color: white;'>🏛️ Ziauddin University Civil Engineering Department</h3>
    <h4 style='color: white;'>🎪 Build Asia Expo 2026 | Karachi, Pakistan</h4>
    
    <div style='margin: 1rem 0;'>
        <span class='stats-badge'>AI Accuracy: 87.6%</span>
        <span class='stats-badge'>Error Margin: ±5.7 MPa</span>
        <span class='stats-badge'>Trained on: 1,030+ Samples</span>
        <span class='stats-badge'>Model: Random Forest</span>
    </div>
    
    <p style='color: white; opacity: 0.8;'>
        <strong>For Educational & Demonstration Purposes</strong><br>
        Live AI Tool - No Installation Required
    </p>
    
    <div style='margin-top: 1rem;'>
        <small style='color: white; opacity: 0.6;'>
            🔗 <strong>Live URL:</strong> https://concrete-ai-zu-haiderak27.streamlit.app<br>
            📱 <strong>Scan QR code to try on your phone</strong>
        </small>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# HIDDEN DEVELOPER SECTION
# =============================================
with st.sidebar.expander("🔧 Developer Info"):
    st.write("**Technology Stack:**")
    st.write("- Python + Streamlit")
    st.write("- Scikit-Learn (Random Forest)")
    st.write("- Plotly for visualizations")
    st.write("- Joblib for model serialization")
    
    if model is not None:
        st.write(f"**Model Info:**")
        st.write(f"- Features: {len(feature_names)}")
        st.write(f"- Trees: {len(model.estimators_)}")
        st.write(f"- Loaded: {datetime.now().strftime('%H:%M')}")- PROFESSIONAL EDITION
# Ziauddin University Civil Engineering
# Build Asia E# =============================================
# CONCRETE INTELLIGENCE - PROFESSIONAL EDITION
# Ziauddin University Civil Engineering
# Build Asia Expo 2026
# VERSION: 4.0 - UPDATED FOR EXPO
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import plotly.graph_objects as go

# FORCE STREAMLIT TO UPDATE CACHE
st.cache_data.clear()
st.cache_resource.clear()

# =============================================
# PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence AI Tool",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# CLEAN PROFESSIONAL CSS
# =============================================
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Professional header */
    .header-container {
        background: linear-gradient(90deg, #1a3a5f 0%, #2c5282 100%);
        color: white;
        padding: 2rem;
        border-radius: 0 0 15px 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Clean cards */
    .professional-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid #2c5282;
    }
    
    /* Subtle hover effects */
    .professional-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        transition: box-shadow 0.3s ease;
    }
    
    /* Professional buttons */
    .stButton > button {
        background-color: #2c5282;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #1a3a5f;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(44, 82, 130, 0.3);
    }
    
    /* Clean metrics */
    .stMetric {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* University colors */
    .zu-badge {
        background: #006838;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Subtle animation for predictions */
    @keyframes subtle-glow {
        0% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        50% { box-shadow: 0 4px 12px rgba(44, 82, 130, 0.15); }
        100% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    }
    
    .prediction-card {
        animation: subtle-glow 2s ease-in-out;
    }
    
    /* Clean sliders */
    .stSlider > div > div > div {
        background-color: #2c5282 !important;
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
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

model, feature_names = load_model()

# =============================================
# PROFESSIONAL HEADER
# =============================================
st.markdown("""
<div class="header-container">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <h1 style="margin: 0; font-size: 2.5rem;">🏗️ CONCRETE INTELLIGENCE</h1>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
                AI-Powered Concrete Strength Prediction System
            </p>
        </div>
        <div style="text-align: right;">
            <div class="zu-badge">ZIAUDDIN UNIVERSITY</div>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                Civil Engineering Department<br>
                Build Asia Expo 2026
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# SIDEBAR - CLEAN & PROFESSIONAL
# =============================================
with st.sidebar:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🔍 About This Tool")
    st.markdown("""
    **Concrete Intelligence** is an AI system developed at Ziauddin University to predict concrete compressive strength from mix proportions.
    
    **Key Features:**
    • 87.6% prediction accuracy (R²)
    • ±5.7 MPa average error
    • Trained on 1,030+ samples
    • Karachi-specific optimization
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Model Status")
    if model is not None:
        st.success("✅ **AI Model Active**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🎪 Expo Information")
    st.markdown("""
    **Build Asia Expo 2026**
    Karachi, Pakistan
    
    **Live Demonstration**
    Scan QR code to try on your device
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - CLEAN INTERFACE
# =============================================

# INPUT SECTION
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📐 Concrete Mix Design Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Cementitious Materials")
    cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                       help="Ordinary Portland Cement - Primary binder")
    water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                       help="Mixing water - Critical for workability")
    blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                            help="Supplementary cementitious material")
    fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                         help="Pozzolanic material")

with col2:
    st.markdown("#### Aggregates & Admixtures")
    superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                 help="High-range water reducer")
    coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                            help="20mm crushed stone")
    fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                          help="Natural sand")
    age = st.slider("**Curing Age** (days)", 1, 90, 28,
                     help="Testing age - Standard is 28 days")

st.markdown('</div>', unsafe_allow_html=True)

# QUICK PRESETS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## ⚡ Quick Preset Mixes")

preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("🏠 Residential (Grade 25)", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
        st.session_state.age = 28
        st.success("Residential mix loaded")
with preset_col2:
    if st.button("🏢 Commercial (Grade 35)", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
        st.session_state.age = 28
        st.success("Commercial mix loaded")
with preset_col3:
    if st.button("🌉 Structural (Grade 50)", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160
        st.session_state.age = 28
        st.success("Structural mix loaded")
st.markdown('</div>', unsafe_allow_html=True)

# REAL-TIME ANALYSIS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📈 Real-Time Analysis")

wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Optimal: 0.4-0.5" if 0.4 <= wc_ratio <= 0.5 else "Review")
with metric_col2:
    st.metric("Total Cementitious", f"{total_powder} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")

# Water-cement ratio indicator
if wc_ratio > 0.55:
    st.warning("⚠️ **High water-cement ratio** (>0.55) may reduce strength. Consider reducing water content.")
elif wc_ratio < 0.35:
    st.info("ℹ️ **Low water-cement ratio** (<0.35) is good for strength but may affect workability.")
else:
    st.success("✅ **Optimal water-cement ratio** (0.35-0.55) for typical applications.")
st.markdown('</div>', unsafe_allow_html=True)

# PREDICTION BUTTON
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3>Ready for AI Analysis</h3>
""", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button("🔬 **ANALYZE WITH AI**", 
                               type="primary", 
                               use_container_width=True,
                               help="Click to get AI-powered strength prediction")

st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    # Loading animation
    with st.spinner('🤖 **AI Model Analyzing Mix Design...**'):
        time.sleep(1)
        
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
    
    # RESULTS DISPLAY
    st.markdown('<div class="professional-card prediction-card">', unsafe_allow_html=True)
    st.markdown("## 📊 **AI Prediction Results**")
    
    # Result metrics
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            label="**Predicted Compressive Strength**",
            value=f"{predicted_strength:.1f}",
            delta="MPa",
            delta_color="normal"
        )
    
    with res_col2:
        st.metric(
            label="**Water-Cement Ratio**",
            value=f"{wc_ratio:.3f}",
            delta="Optimal" if 0.4 <= wc_ratio <= 0.5 else "Review"
        )
    
    with res_col3:
        if predicted_strength >= 50:
            classification = "High-Strength"
            icon = "🏗️"
            use = "Structural"
            color = "green"
        elif predicted_strength >= 35:
            classification = "Standard"
            icon = "🏢"
            use = "Commercial"
            color = "blue"
        elif predicted_strength >= 25:
            classification = "Medium"
            icon = "🏠"
            use = "Residential"
            color = "orange"
        else:
            classification = "Low"
            icon = "🛠️"
            use = "Non-structural"
            color = "red"
        
        st.metric(
            label="**Strength Classification**",
            value=f"{icon} {classification}",
            delta=use
        )
    
    # Strength visualization
    st.markdown("### 📈 Strength Visualization")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=predicted_strength,
        title={'text': "Compressive Strength (MPa)"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 80]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 25], 'color': "lightgray"},
                {'range': [25, 35], 'color': "lightblue"},
                {'range': [35, 50], 'color': "lightgreen"},
                {'range': [50, 80], 'color': "#90EE90"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': predicted_strength
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Application recommendations
    st.markdown("### 💡 **Recommended Applications**")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (≥50 MPa)**
        - **Primary Applications:** Columns, beams, bridges, high-rise buildings
        - **Karachi Examples:** High-rise structures, industrial facilities
        - **Design Considerations:** Reduced member sizes, higher load capacity
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        - **Primary Applications:** Commercial buildings, parking structures, slabs
        - **Karachi Examples:** Shopping malls, office buildings, hotels
        - **Design Considerations:** Balanced strength-cost ratio, typical construction
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        - **Primary Applications:** Residential buildings, foundations, walls
        - **Karachi Examples:** Houses, apartments, small commercial spaces
        - **Design Considerations:** Cost-effective, adequate for typical loads
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        - **Primary Applications:** Non-structural elements, blinding concrete, fills
        - **Karachi Examples:** Footpaths, boundary walls, landscaping
        - **Design Considerations:** Not for load-bearing structures
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # OPTIMIZATION SUGGESTIONS
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("## 🔧 **AI Optimization Suggestions**")
    
    suggestions = []
    
    if wc_ratio > 0.55:
        suggestions.append("**Reduce water content** - Current W/C ratio of {:.3f} is above recommended 0.55. Reduce water by 10-15% to increase strength.".format(wc_ratio))
    
    if wc_ratio < 0.35:
        suggestions.append("**Consider workability** - Very low W/C ratio ({:.3f}) may affect placement. Review mix design for adequate workability.".format(wc_ratio))
    
    if cement < 250 and predicted_strength < 30:
        suggestions.append("**Increase cement content** - For structural applications, consider increasing cement to 300+ kg/m³.")
    
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("**Consider supplementary materials** - Adding 50-100 kg/m³ of slag or fly ash can improve durability and reduce cost.")
    
    if age < 28:
        suggestions.append("**Note on curing age** - Prediction based on {} days. 28-day strength is standard for structural design.".format(age))
    
    if suggestions:
        st.markdown("### Suggested Improvements:")
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"{i}. {suggestion}")
    else:
        st.success("✅ **Mix design appears well-optimized** for the intended application.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ **AI Model Not Available** - Please check model files")

# =============================================
# FOOTER - PROFESSIONAL
# =============================================
st.markdown("""
<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e9ecef;">
    <div style="text-align: center;">
        <h4 style="color: #2c5282; margin-bottom: 1rem;">🏛️ Ziauddin University Civil Engineering Department</h4>
        <p style="color: #666; margin-bottom: 0.5rem;">
            <strong>Build Asia Expo 2026 | Karachi, Pakistan</strong>
        </p>
        
        <div style="display: flex; justify-content: center; gap: 1rem; margin: 1rem 0;">
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>AI Accuracy:</strong> 87.6% (R²)</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Error Margin:</strong> ±5.7 MPa</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Training Data:</strong> 1,030+ samples</small>
            </div>
        </div>
        
        <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">
            <strong>Educational & Research Tool</strong> | 
            <strong>Model:</strong> Random Forest (100 trees) | 
            <strong>Framework:</strong> Python/Scikit-Learn
        </p>
        
        <p style="color: #666; font-size: 0.85rem; margin-top: 0.5rem;">
            🔗 <strong>Live Access:</strong> https://concrete-ai-zu-fvgrjek6rsw85jct5gmiax.streamlit.app
        </p>
    </div>
</div>
""", unsafe_allow_html=True)xpo 2026
# VERSION: 4.0 - UPDATED FOR EXPO
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import plotly.graph_objects as go

# FORCE STREAMLIT TO UPDATE CACHE
st.cache_data.clear()
st.cache_resource.clear()

# =============================================
# PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence AI Tool",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# CLEAN PROFESSIONAL CSS
# =============================================
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Professional header */
    .header-container {
        background: linear-gradient(90deg, #1a3a5f 0%, #2c5282 100%);
        color: white;
        padding: 2rem;
        border-radius: 0 0 15px 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Clean cards */
    .professional-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid #2c5282;
    }
    
    /* Subtle hover effects */
    .professional-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        transition: box-shadow 0.3s ease;
    }
    
    /* Professional buttons */
    .stButton > button {
        background-color: #2c5282;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #1a3a5f;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(44, 82, 130, 0.3);
    }
    
    /* Clean metrics */
    .stMetric {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* University colors */
    .zu-badge {
        background: #006838;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Subtle animation for predictions */
    @keyframes subtle-glow {
        0% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        50% { box-shadow: 0 4px 12px rgba(44, 82, 130, 0.15); }
        100% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    }
    
    .prediction-card {
        animation: subtle-glow 2s ease-in-out;
    }
    
    /* Clean sliders */
    .stSlider > div > div > div {
        background-color: #2c5282 !important;
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
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

model, feature_names = load_model()

# =============================================
# PROFESSIONAL HEADER
# =============================================
st.markdown("""
<div class="header-container">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <h1 style="margin: 0; font-size: 2.5rem;">🏗️ CONCRETE INTELLIGENCE</h1>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
                AI-Powered Concrete Strength Prediction System
            </p>
        </div>
        <div style="text-align: right;">
            <div class="zu-badge">ZIAUDDIN UNIVERSITY</div>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                Civil Engineering Department<br>
                Build Asia Expo 2026
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# SIDEBAR - CLEAN & PROFESSIONAL
# =============================================
with st.sidebar:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🔍 About This Tool")
    st.markdown("""
    **Concrete Intelligence** is an AI system developed at Ziauddin University to predict concrete compressive strength from mix proportions.
    
    **Key Features:**
    • 87.6% prediction accuracy (R²)
    • ±5.7 MPa average error
    • Trained on 1,030+ samples
    • Karachi-specific optimization
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Model Status")
    if model is not None:
        st.success("✅ **AI Model Active**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🎪 Expo Information")
    st.markdown("""
    **Build Asia Expo 2026**
    Karachi, Pakistan
    
    **Live Demonstration**
    Scan QR code to try on your device
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - CLEAN INTERFACE
# =============================================

# INPUT SECTION
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📐 Concrete Mix Design Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Cementitious Materials")
    cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                       help="Ordinary Portland Cement - Primary binder")
    water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                       help="Mixing water - Critical for workability")
    blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                            help="Supplementary cementitious material")
    fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                         help="Pozzolanic material")

with col2:
    st.markdown("#### Aggregates & Admixtures")
    superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                 help="High-range water reducer")
    coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                            help="20mm crushed stone")
    fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                          help="Natural sand")
    age = st.slider("**Curing Age** (days)", 1, 90, 28,
                     help="Testing age - Standard is 28 days")

st.markdown('</div>', unsafe_allow_html=True)

# QUICK PRESETS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## ⚡ Quick Preset Mixes")

preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("🏠 Residential (Grade 25)", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
        st.session_state.age = 28
        st.success("Residential mix loaded")
with preset_col2:
    if st.button("🏢 Commercial (Grade 35)", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
        st.session_state.age = 28
        st.success("Commercial mix loaded")
with preset_col3:
    if st.button("🌉 Structural (Grade 50)", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160
        st.session_state.age = 28
        st.success("Structural mix loaded")
st.markdown('</div>', unsafe_allow_html=True)

# REAL-TIME ANALYSIS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📈 Real-Time Analysis")

wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Optimal: 0.4-0.5" if 0.4 <= wc_ratio <= 0.5 else "Review")
with metric_col2:
    st.metric("Total Cementitious", f"{total_powder} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")

# Water-cement ratio indicator
if wc_ratio > 0.55:
    st.warning("⚠️ **High water-cement ratio** (>0.55) may reduce strength. Consider reducing water content.")
elif wc_ratio < 0.35:
    st.info("ℹ️ **Low water-cement ratio** (<0.35) is good for strength but may affect workability.")
else:
    st.success("✅ **Optimal water-cement ratio** (0.35-0.55) for typical applications.")
st.markdown('</div>', unsafe_allow_html=True)

# PREDICTION BUTTON
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3>Ready for AI Analysis</h3>
""", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button("🔬 **ANALYZE WITH AI**", 
                               type="primary", 
                               use_container_width=True,
                               help="Click to get AI-powered strength prediction")

st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    # Loading animation
    with st.spinner('🤖 **AI Model Analyzing Mix Design...**'):
        time.sleep(1)
        
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
    
    # RESULTS DISPLAY
    st.markdown('<div class="professional-card prediction-card">', unsafe_allow_html=True)
    st.markdown("## 📊 **AI Prediction Results**")
    
    # Result metrics
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            label="**Predicted Compressive Strength**",
            value=f"{predicted_strength:.1f}",
            delta="MPa",
            delta_color="normal"
        )
    
    with res_col2:
        st.metric(
            label="**Water-Cement Ratio**",
            value=f"{wc_ratio:.3f}",
            delta="Optimal" if 0.4 <= wc_ratio <= 0.5 else "Review"
        )
    
    with res_col3:
        if predicted_strength >= 50:
            classification = "High-Strength"
            icon = "🏗️"
            use = "Structural"
            color = "green"
        elif predicted_strength >= 35:
            classification = "Standard"
            icon = "🏢"
            use = "Commercial"
            color = "blue"
        elif predicted_strength >= 25:
            classification = "Medium"
            icon = "🏠"
            use = "Residential"
            color = "orange"
        else:
            classification = "Low"
            icon = "🛠️"
            use = "Non-structural"
            color = "red"
        
        st.metric(
            label="**Strength Classification**",
            value=f"{icon} {classification}",
            delta=use
        )
    
    # Strength visualization
    st.markdown("### 📈 Strength Visualization")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=predicted_strength,
        title={'text': "Compressive Strength (MPa)"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 80]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 25], 'color': "lightgray"},
                {'range': [25, 35], 'color': "lightblue"},
                {'range': [35, 50], 'color': "lightgreen"},
                {'range': [50, 80], 'color': "#90EE90"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': predicted_strength
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Application recommendations
    st.markdown("### 💡 **Recommended Applications**")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (≥50 MPa)**
        - **Primary Applications:** Columns, beams, bridges, high-rise buildings
        - **Karachi Examples:** High-rise structures, industrial facilities
        - **Design Considerations:** Reduced member sizes, higher load capacity
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        - **Primary Applications:** Commercial buildings, parking structures, slabs
        - **Karachi Examples:** Shopping malls, office buildings, hotels
        - **Design Considerations:** Balanced strength-cost ratio, typical construction
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        - **Primary Applications:** Residential buildings, foundations, walls
        - **Karachi Examples:** Houses, apartments, small commercial spaces
        - **Design Considerations:** Cost-effective, adequate for typical loads
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        - **Primary Applications:** Non-structural elements, blinding concrete, fills
        - **Karachi Examples:** Footpaths, boundary walls, landscaping
        - **Design Considerations:** Not for load-bearing structures
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # OPTIMIZATION SUGGESTIONS
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("## 🔧 **AI Optimization Suggestions**")
    
    suggestions = []
    
    if wc_ratio > 0.55:
        suggestions.append("**Reduce water content** - Current W/C ratio of {:.3f} is above recommended 0.55. Reduce water by 10-15% to increase strength.".format(wc_ratio))
    
    if wc_ratio < 0.35:
        suggestions.append("**Consider workability** - Very low W/C ratio ({:.3f}) may affect placement. Review mix design for adequate workability.".format(wc_ratio))
    
    if cement < 250 and predicted_strength < 30:
        suggestions.append("**Increase cement content** - For structural applications, consider increasing cement to 300+ kg/m³.")
    
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("**Consider supplementary materials** - Adding 50-100 kg/m³ of slag or fly ash can improve durability and reduce cost.")
    
    if age < 28:
        suggestions.append("**Note on curing age** - Prediction based on {} days. 28-day strength is standard for structural design.".format(age))
    
    if suggestions:
        st.markdown("### Suggested Improvements:")
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"{i}. {suggestion}")
    else:
        st.success("✅ **Mix design appears well-optimized** for the intended application.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ **AI Model Not Available** - Please check model files")

# =============================================
# FOOTER - PROFESSIONAL
# =============================================
st.markdown("""
<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e9ecef;">
    <div style="text-align: center;">
        <h4 style="color: #2c5282; margin-bottom: 1rem;">🏛️ Ziauddin University Civil Engineering Department</h4>
        <p style="color: #666; margin-bottom: 0.5rem;">
            <strong>Build Asia Expo 2026 | Karachi, Pakistan</strong>
        </p>
        
        <div style="display: flex; justify-content: center; gap: 1rem; margin: 1rem 0;">
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>AI Accuracy:</strong> 87.6% (R²)</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Error Margin:</strong> ±5.7 MPa</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Training Data:</strong> 1,030+ samples</small>
            </div>
        </div>
        
        <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">
            <strong>Educational & Research Tool</strong> | 
            <strong>Model:</strong> Random Forest (100 trees) | 
            <strong>Framework:</strong> Python/Scikit-Learn
        </p>
        
        <p style="color: #666; font-size: 0.85rem; margin-top: 0.5rem;">
            🔗 <strong>Live Access:</strong> https://concrete-ai-zu-fvgrjek6rsw85jct5gmiax.streamlit.app
        </p>
    </div>
</div>
""", unsafe_allow_html=True)ROFESSIONAL EDITION
# Ziauddin University Civil Engineering
# Build Asia Expo 2026
# VERSION: 4.0 - UPDATED FOR EXPO
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import time
import plotly.graph_objects as go

# FORCE STREAMLIT TO UPDATE CACHE
st.cache_data.clear()
st.cache_resource.clear()

# =============================================
# PAGE CONFIG
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence AI Tool",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# CLEAN PROFESSIONAL CSS
# =============================================
st.markdown("""
<style>
    /* Clean white background */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Professional header */
    .header-container {
        background: linear-gradient(90deg, #1a3a5f 0%, #2c5282 100%);
        color: white;
        padding: 2rem;
        border-radius: 0 0 15px 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Clean cards */
    .professional-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 4px solid #2c5282;
    }
    
    /* Subtle hover effects */
    .professional-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        transition: box-shadow 0.3s ease;
    }
    
    /* Professional buttons */
    .stButton > button {
        background-color: #2c5282;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #1a3a5f;
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(44, 82, 130, 0.3);
    }
    
    /* Clean metrics */
    .stMetric {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #e9ecef;
    }
    
    /* University colors */
    .zu-badge {
        background: #006838;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    /* Subtle animation for predictions */
    @keyframes subtle-glow {
        0% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        50% { box-shadow: 0 4px 12px rgba(44, 82, 130, 0.15); }
        100% { box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    }
    
    .prediction-card {
        animation: subtle-glow 2s ease-in-out;
    }
    
    /* Clean sliders */
    .stSlider > div > div > div {
        background-color: #2c5282 !important;
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
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None

model, feature_names = load_model()

# =============================================
# PROFESSIONAL HEADER
# =============================================
st.markdown("""
<div class="header-container">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <h1 style="margin: 0; font-size: 2.5rem;">🏗️ CONCRETE INTELLIGENCE</h1>
            <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
                AI-Powered Concrete Strength Prediction System
            </p>
        </div>
        <div style="text-align: right;">
            <div class="zu-badge">ZIAUDDIN UNIVERSITY</div>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                Civil Engineering Department<br>
                Build Asia Expo 2026
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# SIDEBAR - CLEAN & PROFESSIONAL
# =============================================
with st.sidebar:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🔍 About This Tool")
    st.markdown("""
    **Concrete Intelligence** is an AI system developed at Ziauddin University to predict concrete compressive strength from mix proportions.
    
    **Key Features:**
    • 87.6% prediction accuracy (R²)
    • ±5.7 MPa average error
    • Trained on 1,030+ samples
    • Karachi-specific optimization
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 📊 Model Status")
    if model is not None:
        st.success("✅ **AI Model Active**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("### 🎪 Expo Information")
    st.markdown("""
    **Build Asia Expo 2026**
    Karachi, Pakistan
    
    **Live Demonstration**
    Scan QR code to try on your device
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - CLEAN INTERFACE
# =============================================

# INPUT SECTION
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📐 Concrete Mix Design Parameters")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Cementitious Materials")
    cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                       help="Ordinary Portland Cement - Primary binder")
    water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                       help="Mixing water - Critical for workability")
    blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                            help="Supplementary cementitious material")
    fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                         help="Pozzolanic material")

with col2:
    st.markdown("#### Aggregates & Admixtures")
    superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                 help="High-range water reducer")
    coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                            help="20mm crushed stone")
    fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                          help="Natural sand")
    age = st.slider("**Curing Age** (days)", 1, 90, 28,
                     help="Testing age - Standard is 28 days")

st.markdown('</div>', unsafe_allow_html=True)

# QUICK PRESETS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## ⚡ Quick Preset Mixes")

preset_col1, preset_col2, preset_col3 = st.columns(3)
with preset_col1:
    if st.button("🏠 Residential (Grade 25)", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
        st.session_state.age = 28
        st.success("Residential mix loaded")
with preset_col2:
    if st.button("🏢 Commercial (Grade 35)", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
        st.session_state.age = 28
        st.success("Commercial mix loaded")
with preset_col3:
    if st.button("🌉 Structural (Grade 50)", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160
        st.session_state.age = 28
        st.success("Structural mix loaded")
st.markdown('</div>', unsafe_allow_html=True)

# REAL-TIME ANALYSIS
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown("## 📈 Real-Time Analysis")

wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

metric_col1, metric_col2, metric_col3 = st.columns(3)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Optimal: 0.4-0.5" if 0.4 <= wc_ratio <= 0.5 else "Review")
with metric_col2:
    st.metric("Total Cementitious", f"{total_powder} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")

# Water-cement ratio indicator
if wc_ratio > 0.55:
    st.warning("⚠️ **High water-cement ratio** (>0.55) may reduce strength. Consider reducing water content.")
elif wc_ratio < 0.35:
    st.info("ℹ️ **Low water-cement ratio** (<0.35) is good for strength but may affect workability.")
else:
    st.success("✅ **Optimal water-cement ratio** (0.35-0.55) for typical applications.")
st.markdown('</div>', unsafe_allow_html=True)

# PREDICTION BUTTON
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <h3>Ready for AI Analysis</h3>
""", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button("🔬 **ANALYZE WITH AI**", 
                               type="primary", 
                               use_container_width=True,
                               help="Click to get AI-powered strength prediction")

st.markdown('</div>', unsafe_allow_html=True)

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    # Loading animation
    with st.spinner('🤖 **AI Model Analyzing Mix Design...**'):
        time.sleep(1)
        
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
    
    # RESULTS DISPLAY
    st.markdown('<div class="professional-card prediction-card">', unsafe_allow_html=True)
    st.markdown("## 📊 **AI Prediction Results**")
    
    # Result metrics
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            label="**Predicted Compressive Strength**",
            value=f"{predicted_strength:.1f}",
            delta="MPa",
            delta_color="normal"
        )
    
    with res_col2:
        st.metric(
            label="**Water-Cement Ratio**",
            value=f"{wc_ratio:.3f}",
            delta="Optimal" if 0.4 <= wc_ratio <= 0.5 else "Review"
        )
    
    with res_col3:
        if predicted_strength >= 50:
            classification = "High-Strength"
            icon = "🏗️"
            use = "Structural"
            color = "green"
        elif predicted_strength >= 35:
            classification = "Standard"
            icon = "🏢"
            use = "Commercial"
            color = "blue"
        elif predicted_strength >= 25:
            classification = "Medium"
            icon = "🏠"
            use = "Residential"
            color = "orange"
        else:
            classification = "Low"
            icon = "🛠️"
            use = "Non-structural"
            color = "red"
        
        st.metric(
            label="**Strength Classification**",
            value=f"{icon} {classification}",
            delta=use
        )
    
    # Strength visualization
    st.markdown("### 📈 Strength Visualization")
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=predicted_strength,
        title={'text': "Compressive Strength (MPa)"},
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [None, 80]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 25], 'color': "lightgray"},
                {'range': [25, 35], 'color': "lightblue"},
                {'range': [35, 50], 'color': "lightgreen"},
                {'range': [50, 80], 'color': "#90EE90"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': predicted_strength
            }
        }
    ))
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)
    
    # Application recommendations
    st.markdown("### 💡 **Recommended Applications**")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (≥50 MPa)**
        - **Primary Applications:** Columns, beams, bridges, high-rise buildings
        - **Karachi Examples:** High-rise structures, industrial facilities
        - **Design Considerations:** Reduced member sizes, higher load capacity
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        - **Primary Applications:** Commercial buildings, parking structures, slabs
        - **Karachi Examples:** Shopping malls, office buildings, hotels
        - **Design Considerations:** Balanced strength-cost ratio, typical construction
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        - **Primary Applications:** Residential buildings, foundations, walls
        - **Karachi Examples:** Houses, apartments, small commercial spaces
        - **Design Considerations:** Cost-effective, adequate for typical loads
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        - **Primary Applications:** Non-structural elements, blinding concrete, fills
        - **Karachi Examples:** Footpaths, boundary walls, landscaping
        - **Design Considerations:** Not for load-bearing structures
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # OPTIMIZATION SUGGESTIONS
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown("## 🔧 **AI Optimization Suggestions**")
    
    suggestions = []
    
    if wc_ratio > 0.55:
        suggestions.append("**Reduce water content** - Current W/C ratio of {:.3f} is above recommended 0.55. Reduce water by 10-15% to increase strength.".format(wc_ratio))
    
    if wc_ratio < 0.35:
        suggestions.append("**Consider workability** - Very low W/C ratio ({:.3f}) may affect placement. Review mix design for adequate workability.".format(wc_ratio))
    
    if cement < 250 and predicted_strength < 30:
        suggestions.append("**Increase cement content** - For structural applications, consider increasing cement to 300+ kg/m³.")
    
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("**Consider supplementary materials** - Adding 50-100 kg/m³ of slag or fly ash can improve durability and reduce cost.")
    
    if age < 28:
        suggestions.append("**Note on curing age** - Prediction based on {} days. 28-day strength is standard for structural design.".format(age))
    
    if suggestions:
        st.markdown("### Suggested Improvements:")
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"{i}. {suggestion}")
    else:
        st.success("✅ **Mix design appears well-optimized** for the intended application.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ **AI Model Not Available** - Please check model files")

# =============================================
# FOOTER - PROFESSIONAL
# =============================================
st.markdown("""
<div style="margin-top: 3rem; padding-top: 2rem; border-top: 1px solid #e9ecef;">
    <div style="text-align: center;">
        <h4 style="color: #2c5282; margin-bottom: 1rem;">🏛️ Ziauddin University Civil Engineering Department</h4>
        <p style="color: #666; margin-bottom: 0.5rem;">
            <strong>Build Asia Expo 2026 | Karachi, Pakistan</strong>
        </p>
        
        <div style="display: flex; justify-content: center; gap: 1rem; margin: 1rem 0;">
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>AI Accuracy:</strong> 87.6% (R²)</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Error Margin:</strong> ±5.7 MPa</small>
            </div>
            <div style="background: #f8f9fa; padding: 0.5rem 1rem; border-radius: 6px; border: 1px solid #e9ecef;">
                <small><strong>Training Data:</strong> 1,030+ samples</small>
            </div>
        </div>
        
        <p style="color: #888; font-size: 0.9rem; margin-top: 1rem;">
            <strong>Educational & Research Tool</strong> | 
            <strong>Model:</strong> Random Forest (100 trees) | 
            <strong>Framework:</strong> Python/Scikit-Learn
        </p>
        
        <p style="color: #666; font-size: 0.85rem; margin-top: 0.5rem;">
            🔗 <strong>Live Access:</strong> https://concrete-ai-zu-fvgrjek6rsw85jct5gmiax.streamlit.app
        </p>
    </div>
</div>
""", unsafe_allow_html=True)ing
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




