# =============================================
# CONCRETE INTELLIGENCE - EXPO PROFESSIONAL
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
    page_title="Concrete Intelligence | Ziauddin University",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# MINIMAL PROFESSIONAL CSS
# =============================================
st.markdown("""
<style>
    /* Clean professional background */
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Main content area */
    .main-content {
        background: white;
        border-radius: 12px;
        padding: 2.5rem;
        margin: 1.5rem auto;
        max-width: 1400px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
    }
    
    /* Professional headers */
    .main-header {
        text-align: center;
        color: #1e293b;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    .sub-header {
        text-align: center;
        color: #64748b;
        font-size: 1.4rem;
        font-weight: 500;
        margin-bottom: 2.5rem;
        line-height: 1.5;
    }
    
    .section-header {
        color: #1e293b;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 2rem 0 1.5rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #3b82f6;
    }
    
    /* Clean sliders */
    .stSlider {
        margin: 1.2rem 0;
    }
    
    /* Professional buttons */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 1rem 2.5rem;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
    }
    
    /* Clean metrics */
    .stMetric {
        background: #f8fafc;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
    }
    
    /* University badge */
    .uni-badge {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.95rem;
    }
    
    /* Expo badge */
    .expo-badge {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        padding: 0.6rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.3rem;
        font-size: 0.95rem;
    }
    
    /* Clean divider */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    
    /* Info boxes */
    .info-box {
        background: #f0f9ff;
        border-left: 4px solid #3b82f6;
        padding: 1.2rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    
    /* High contrast for readability */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        font-size: 1.1rem;
        font-weight: 500;
    }
    
    /* Remove streamlit default spacing issues */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
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
        st.error(f"Model loading error: {str(e)}")
        return None, None

model, feature_names = load_model()

# =============================================
# SIDEBAR - CLEAN & INFORMATIVE
# =============================================
with st.sidebar:
    # University Logo Area
    st.markdown("<div style='text-align: center; margin-bottom: 2rem;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #1d4ed8;'>🏗️</h2>", unsafe_allow_html=True)
    st.markdown("<h3 style='color: #1e293b; margin: 0;'>Concrete Intelligence</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # University Info
    st.markdown("### 🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("<small style='color: #64748b;'>Karachi, Pakistan</small>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Expo Info
    st.markdown("### 🎪 Build Asia Expo 2026")
    st.markdown("<small style='color: #059669; font-weight: 600;'>Live Demonstration</small>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Model Status
    if model is not None:
        st.success("**✅ AI Model Active**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%", delta="R²")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("**❌ Model Not Loaded**")
    
    st.markdown("---")
    
    # Quick Links
    st.markdown("### 📱 Quick Access")
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    st.markdown("**Scan QR Code**")
    st.markdown("<small style='color: #64748b;'>concrete-ai-zu.streamlit.app</small>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - PROFESSIONAL LAYOUT
# =============================================

# HEADER SECTION
st.markdown("<h1 class='main-header'>CONCRETE INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>AI-Powered Concrete Strength Prediction & Optimization Platform</p>", unsafe_allow_html=True)

# BADGES FOR QUICK INFO
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='uni-badge'>🏛️ Ziauddin University</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='expo-badge'>🎪 Expo 2026</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='uni-badge'>🤖 AI Model: 87.6%</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='expo-badge'>📊 1,030+ Samples</div>", unsafe_allow_html=True)

# MAIN CONTENT AREA
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# =============================================
# CONCRETE MIX DESIGN SECTION
# =============================================
st.markdown("<h2 class='section-header'>Design Your Concrete Mix</h2>", unsafe_allow_html=True)

# Two column layout for inputs
col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Cementitious Materials")
    cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                      help="Primary binding material - Most important for strength")
    water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                     help="Critical for workability - Affects water-cement ratio")
    blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                          help="Supplementary material - Improves durability")
    fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                       help="Pozzolanic material - Enhances workability")

with col_right:
    st.markdown("#### Aggregates & Admixtures")
    superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                help="High-range water reducer - Improves flow")
    coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                          help="20mm crushed stone - Provides bulk and strength")
    fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                        help="Natural sand - Fills voids and improves workability")
    age = st.slider("**Curing Age** (days)", 1, 90, 28,
                   help="Testing age - Standard is 28 days")

# Quick Preset Buttons
st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
st.markdown("#### ⚡ Quick Preset Mixes")

preset_col1, preset_col2, preset_col3 = st.columns(3)

with preset_col1:
    if st.button("**🏠 Residential Mix**\nGrade 25 MPa", use_container_width=True):
        st.session_state.cement = 300
        st.session_state.water = 180
        st.session_state.age = 28

with preset_col2:
    if st.button("**🏢 Commercial Mix**\nGrade 35 MPa", use_container_width=True):
        st.session_state.cement = 350
        st.session_state.water = 175
        st.session_state.age = 28

with preset_col3:
    if st.button("**🌉 Structural Mix**\nGrade 50 MPa", use_container_width=True):
        st.session_state.cement = 400
        st.session_state.water = 160
        st.session_state.age = 28

# =============================================
# REAL-TIME ANALYSIS SECTION
# =============================================
st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>Real-Time Analysis</h2>", unsafe_allow_html=True)

# Calculate key metrics
wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

# Display metrics in clean cards
metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Optimal" if 0.4 <= wc_ratio <= 0.5 else "Review")

with metric_col2:
    st.metric("Total Powder", f"{total_powder:,} kg/m³")

with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate:,} kg/m³")

with metric_col4:
    agg_ratio = coarse_agg / fine_agg if fine_agg > 0 else 0
    st.metric("Aggregate Ratio", f"{agg_ratio:.2f}")

# Instant feedback on water-cement ratio
st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)

if wc_ratio > 0.55:
    st.warning("""
    **⚠️ High Water-Cement Ratio Detected**
    - Current ratio: **{:.3f}** (above 0.55)
    - **Recommendation:** Reduce water content to improve strength
    """.format(wc_ratio))
elif wc_ratio < 0.35:
    st.info("""
    **✅ Low Water-Cement Ratio**
    - Current ratio: **{:.3f}** (below 0.35)
    - **Good for strength**, check workability
    """.format(wc_ratio))
else:
    st.success("""
    **✅ Optimal Water-Cement Ratio**
    - Current ratio: **{:.3f}** (0.35-0.55 range)
    - **Ideal for balanced strength and workability**
    """.format(wc_ratio))

# =============================================
# PREDICTION SECTION
# =============================================
st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
st.markdown("<h2 class='section-header'>AI Strength Prediction</h2>", unsafe_allow_html=True)

# Centered prediction button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_clicked = st.button(
        "**🚀 PREDICT CONCRETE STRENGTH**",
        type="primary",
        use_container_width=True,
        help="Click to get AI-powered strength prediction"
    )

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    # Show loading state
    with st.spinner('🤖 AI analyzing your concrete mix design...'):
        time.sleep(0.8)
        
        # Prepare input data
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
    
    # Success animation
    st.balloons()
    
    st.markdown("<div class='custom-divider'></div>", unsafe_allow_html=True)
    st.markdown("## 🎉 **Prediction Results**")
    
    # Display results in clean metrics
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
            value=f"{wc_ratio:.3f}"
        )
    
    with res_col3:
        # Strength classification
        if predicted_strength >= 50:
            classification = "High-Strength"
            use = "Structural"
            color = "green"
        elif predicted_strength >= 35:
            classification = "Standard"
            use = "Commercial"
            color = "blue"
        elif predicted_strength >= 25:
            classification = "Medium"
            use = "Residential"
            color = "orange"
        else:
            classification = "Low"
            use = "Non-structural"
            color = "red"
        
        st.metric(
            label="**Classification**",
            value=classification,
            delta=use
        )
    
    # Strength visualization
    st.progress(min(predicted_strength/80, 1.0))
    st.caption(f"**Strength Scale:** 0-80 MPa | **Your Mix:** {predicted_strength:.1f} MPa")
    
    # Application recommendations
    st.markdown("### 💡 **Recommended Applications**")
    
    app_col1, app_col2 = st.columns(2)
    
    with app_col1:
        if predicted_strength >= 50:
            st.success("""
            **🏗️ HIGH-STRENGTH CONCRETE**
            - Columns & beams
            - Bridges & flyovers
            - High-rise buildings
            - Industrial floors
            """)
        elif predicted_strength >= 35:
            st.info("""
            **🏢 STANDARD CONCRETE**
            - Commercial buildings
            - Parking structures
            - Office slabs
            - Shopping malls
            """)
    
    with app_col2:
        if predicted_strength >= 25:
            st.warning("""
            **🏠 MEDIUM CONCRETE**
            - Residential buildings
            - House foundations
            - Boundary walls
            - Small structures
            """)
        else:
            st.error("""
            **🛠️ LOW STRENGTH**
            - Non-structural elements
            - Blinding concrete
            - Landscaping
            - Footpaths
            """)
    
    # Optimization suggestions
    st.markdown("### 🔧 **Optimization Suggestions**")
    st.markdown("<div class='info-box'>", unsafe_allow_html=True)
    
    suggestions = []
    if wc_ratio > 0.55:
        suggestions.append("**Reduce water by 10-15%** to improve strength")
    if cement < 250 and predicted_strength < 30:
        suggestions.append("**Increase cement to 300+ kg/m³** for structural use")
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("**Add supplementary materials** to improve durability")
    if age < 28:
        suggestions.append("**28-day strength** is standard for design purposes")
    
    if suggestions:
        st.markdown("**AI Recommendations:**")
        for suggestion in suggestions:
            st.markdown(f"• {suggestion}")
    else:
        st.markdown("**✅ Your mix design appears well-optimized!**")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif predict_clicked:
    st.error("**❌ AI Model not loaded** - Please check model files")

# =============================================
# FOOTER
# =============================================
st.markdown("</div>", unsafe_allow_html=True)  # Close main-content

st.markdown("""
<div style='text-align: center; padding: 2.5rem; background: white; border-radius: 12px; margin-top: 2rem; box-shadow: 0 5px 20px rgba(0,0,0,0.05);'>
    <h3 style='color: #1e293b; margin-bottom: 1rem;'>🏛️ Ziauddin University Civil Engineering</h3>
    <h4 style='color: #059669; margin-bottom: 1.5rem;'>🎪 Build Asia Expo 2026 | Karachi, Pakistan</h4>
    
    <div style='margin: 1.5rem 0;'>
        <span class='uni-badge'>AI Accuracy: 87.6%</span>
        <span class='expo-badge'>Error Margin: ±5.7 MPa</span>
        <span class='uni-badge'>Trained on 1,030+ Samples</span>
        <span class='expo-badge'>Random Forest Model</span>
    </div>
    
    <hr style='margin: 2rem auto; width: 80%; opacity: 0.2;'>
    
    <p style='color: #64748b; font-size: 0.95rem; line-height: 1.6;'>
        <strong>For Educational & Demonstration Purposes</strong><br>
        Live AI Tool - No Installation Required | Works on Any Device
    </p>
    
    <p style='color: #3b82f6; font-weight: 600; margin-top: 1rem;'>
        🔗 <strong>Live URL:</strong> 
        <a href='https://concrete-ai-zu-haiderak27.streamlit.app' style='color: #3b82f6; text-decoration: none;'>
            concrete-ai-zu-haiderak27.streamlit.app
        </a>
    </p>
    
    <p style='color: #059669; font-weight: 600;'>
        📱 <strong>Scan QR code to try on your phone</strong>
    </p>
</div>
""", unsafe_allow_html=True)
