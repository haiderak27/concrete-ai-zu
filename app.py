# =============================================
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
# CUSTOM CSS - PROFESSIONAL & EASY ON EYES
# =============================================
st.markdown("""
<style>
    /* Soft gradient background - Professional */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Main container with subtle shadow */
    .main {
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.5);
    }
    
    /* Floating animation for buttons */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    
    .float-btn {
        animation: float 3s ease-in-out infinite;
        transition: all 0.3s ease;
    }
    
    .float-btn:hover {
        transform: scale(1.03);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    
    /* Professional buttons - Civil Engineering theme */
    .stButton>button {
        background: linear-gradient(90deg, #2c3e50 0%, #3498db 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.8rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    }
    
    .stButton>button:hover {
        background: linear-gradient(90deg, #3498db 0%, #2c3e50 100%);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(52, 152, 219, 0.4);
    }
    
    /* Card styling - Clean & professional */
    .card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        border-left: 4px solid #3498db;
        transition: all 0.3s;
        border: 1px solid #eaeaea;
    }
    
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    
    /* Stats badges - Subtle */
    .stats-badge {
        background: linear-gradient(135deg, #3498db 0%, #2c3e50 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.2rem;
        font-weight: 600;
        font-size: 0.9rem;
        box-shadow: 0 3px 10px rgba(52, 152, 219, 0.2);
    }
    
    /* Title with subtle gradient */
    .main-title {
        text-align: center;
        font-size: 3rem !important;
        background: linear-gradient(90deg, #2c3e50, #3498db);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem !important;
        font-weight: 700;
    }
    
    /* Subtitle */
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 2rem !important;
    }
    
    /* Slider styling - Professional */
    .stSlider > div > div > div {
        background: linear-gradient(90deg, #3498db 0%, #2c3e50 100%);
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #2c3e50 0%, #3498db 100%);
    }
    
    /* Metric cards */
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 3px 10px rgba(0,0,0,0.08);
        border-top: 3px solid #3498db;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9fa;
        border-radius: 5px 5px 0px 0px;
        padding: 0.5rem 1rem;
    }
    
    /* Watermark effect */
    .watermark {
        position: fixed;
        opacity: 0.03;
        font-size: 15rem;
        color: #2c3e50;
        z-index: -1;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-weight: 900;
        pointer-events: none;
    }
</style>

<div class="watermark">ZU</div>
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
        st.error(f"Error loading model: {str(e)}")
        return None, None, None

# Load model
model, feature_names, column_ranges = load_model()

# =============================================
# SIDEBAR - PROFESSIONAL DESIGN
# =============================================
with st.sidebar:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>🏗️ CONCRETE INTELLIGENCE</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("*Karachi, Pakistan*")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🎪 Build Asia Expo 2026")
    st.markdown("**Live AI Demonstration**")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if model is not None:
        st.success("✅ **AI MODEL ACTIVE**")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Accuracy", "87.6%", delta="R² Score")
        with col2:
            st.metric("Error", "±5.7 MPa")
    else:
        st.error("❌ Model Loading Failed")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📱 Quick Access")
    st.markdown("**Scan QR code**")
    st.markdown("")
    st.markdown("<div style='background: #f8f9fa; padding: 1rem; border-radius: 10px; text-align: center;'>", unsafe_allow_html=True)
    st.markdown("🔗 [concrete-ai-zu.streamlit.app](https://concrete-ai-zu-haiderak27.streamlit.app)")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# MAIN CONTENT - PROFESSIONAL DESIGN
# =============================================

# HEADER
st.markdown("<h1 class='main-title'>🧠 CONCRETE INTELLIGENCE</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subtitle'>AI-Powered Concrete Strength Prediction & Optimization System</h3>", unsafe_allow_html=True)

# STATS BADGES ROW
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("<div class='stats-badge'>📊 87.6% Accurate</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='stats-badge'>⚡ Instant Predictions</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='stats-badge'>💰 Cost Optimizer</div>", unsafe_allow_html=True)
with col4:
    st.markdown("<div class='stats-badge'>🏛️ Ziauddin University</div>", unsafe_allow_html=True)

# MAIN CONTENT CONTAINER
st.markdown("<div class='main'>", unsafe_allow_html=True)

# =============================================
# INPUT SECTION - CLEAN DESIGN
# =============================================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📊 Design Your Concrete Mix")

# Create tabs for different input modes
tab1, tab2, tab3 = st.tabs(["🎯 Standard Mix", "⚡ Quick Presets", "🔧 Advanced"])

with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Cementitious Materials")
        cement = st.slider("**Cement** (kg/m³)", 100, 500, 300, 
                         help="Ordinary Portland Cement - Primary binding material")
        water = st.slider("**Water** (kg/m³)", 100, 250, 180,
                         help="Mixing water - Critical for workability")
        blast_slag = st.slider("**Blast Furnace Slag** (kg/m³)", 0, 200, 50,
                              help="Supplementary cementitious material")
    
    with col2:
        st.markdown("#### Aggregates & Admixtures")
        fly_ash = st.slider("**Fly Ash** (kg/m³)", 0, 150, 30,
                           help="Pozzolanic material")
        superplasticizer = st.slider("**Superplasticizer** (kg/m³)", 0.0, 20.0, 5.0, 0.5,
                                    help="High-range water reducer")
        coarse_agg = st.slider("**Coarse Aggregate** (kg/m³)", 500, 1200, 900,
                              help="20mm crushed stone")
        fine_agg = st.slider("**Fine Aggregate** (kg/m³)", 500, 1000, 700,
                            help="Natural sand")
        age = st.slider("**Curing Age** (days)", 1, 90, 28,
                       help="Testing age - 28 days standard")

with tab2:
    st.markdown("#### 🚀 Quick Preset Mixes")
    st.info("Click any preset to auto-fill values")
    
    preset_col1, preset_col2, preset_col3 = st.columns(3)
    
    with preset_col1:
        if st.button("🏠 **Grade 25**\nResidential", use_container_width=True):
            st.session_state.cement = 300
            st.session_state.water = 180
            st.session_state.age = 28
            st.success("Residential mix loaded!")
    
    with preset_col2:
        if st.button("🏢 **Grade 35**\nCommercial", use_container_width=True):
            st.session_state.cement = 350
            st.session_state.water = 175
            st.session_state.age = 28
            st.success("Commercial mix loaded!")
    
    with preset_col3:
        if st.button("🌉 **Grade 50**\nStructural", use_container_width=True):
            st.session_state.cement = 400
            st.session_state.water = 160
            st.session_state.age = 28
            st.success("Structural mix loaded!")

with tab3:
    st.markdown("#### 🔬 Advanced Parameters")
    st.info("For expert users and researchers")
    # Add any advanced controls here

st.markdown("</div>", unsafe_allow_html=True)

# REAL-TIME ANALYSIS
wc_ratio = water / cement if cement > 0 else 0
total_powder = cement + blast_slag + fly_ash
total_aggregate = coarse_agg + fine_agg

# METRICS DISPLAY
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("## 📈 Real-Time Analysis")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
with metric_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}", 
              "Ideal: 0.4-0.5" if 0.4 <= wc_ratio <= 0.5 else "Monitor")
with metric_col2:
    st.metric("Total Powder", f"{total_powder} kg/m³")
with metric_col3:
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")
with metric_col4:
    agg_ratio = coarse_agg/fine_agg if fine_agg > 0 else 0
    st.metric("Aggregate Ratio", f"{agg_ratio:.2f}")

# Water-cement ratio indicator
if wc_ratio > 0.55:
    st.warning("⚠️ High water-cement ratio (>0.55) - Consider reducing water")
elif wc_ratio < 0.35:
    st.info("✅ Low water-cement ratio - Good for strength")
else:
    st.success("✅ Optimal water-cement ratio (0.35-0.55)")

st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# PREDICTION BUTTON - PROFESSIONAL
# =============================================
st.markdown("""
<div style='text-align: center; margin: 2.5rem 0;'>
    <div class='float-btn'>
""", unsafe_allow_html=True)

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button(
        "🚀 **PREDICT CONCRETE STRENGTH**",
        type="primary",
        use_container_width=True,
        help="Click for AI-powered strength prediction"
    )

st.markdown("""
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# PREDICTION RESULTS
# =============================================
if predict_clicked and model is not None:
    # Show loading animation
    with st.spinner('🤖 AI is analyzing your concrete mix...'):
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
        
        # Ensure correct column order
        input_data = input_data[feature_names]
        
        # Make prediction
        predicted_strength = model.predict(input_data)[0]
    
    # Show success animation
    st.balloons()
    
    st.markdown("<div class='card' style='border-left: 4px solid #27ae60;'>", unsafe_allow_html=True)
    st.markdown("## 🎉 Prediction Results")
    
    # Result metrics
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(
            label="Predicted Strength",
            value=f"{predicted_strength:.1f}",
            delta="MPa",
            delta_color="normal"
        )
    
    with res_col2:
        st.metric(
            label="Water-Cement Ratio",
            value=f"{wc_ratio:.3f}",
            delta="Optimal" if 0.4 <= wc_ratio <= 0.5 else "Review"
        )
    
    with res_col3:
        # Strength classification
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
            label="Classification",
            value=f"{icon} {classification}",
            delta=use
        )
    
    # Strength visualization
    st.progress(min(predicted_strength/80, 1.0))
    st.caption(f"Strength Scale: 0-80 MPa | Your mix: {predicted_strength:.1f} MPa")
    
    # Application recommendations
    st.markdown("### 💡 Recommended Applications")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (>50 MPa)**
        • **Applications:** Columns, beams, bridges, high-rise buildings
        • **Karachi Examples:** Bahria Icon Tower, Ocean Towers
        • **Advantages:** Higher load capacity, reduced member sizes
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        • **Applications:** Commercial buildings, parking structures, slabs
        • **Karachi Examples:** Dolmen Mall, Lucky One Mall
        • **Advantages:** Optimal balance of strength and cost
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        • **Applications:** Residential buildings, foundations, walls
        • **Karachi Examples:** Houses, apartments, small buildings
        • **Advantages:** Cost-effective for typical construction
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        • **Applications:** Non-structural elements, blinding concrete
        • **Karachi Examples:** Footpaths, boundary walls, landscaping
        • **Advantages:** Economical for non-load-bearing applications
        """)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # OPTIMIZATION SUGGESTIONS
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("## 🔧 Optimization Suggestions")
    
    suggestions = []
    
    # Water-cement suggestions
    if wc_ratio > 0.55:
        suggestions.append("💧 **Reduce water** - High W/C ratio (>0.55) reduces strength")
    elif wc_ratio < 0.35:
        suggestions.append("⚗️ **Add superplasticizer** - Low W/C may affect workability")
    
    # Cement optimization
    if cement < 250 and predicted_strength < 30:
        suggestions.append("🏗️ **Increase cement** - For structural applications, aim for 300+ kg/m³")
    
    # Supplementary materials
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("🌿 **Add supplementary materials** - Improve durability and reduce cost")
    
    # Age suggestion
    if age < 28:
        suggestions.append("⏳ **Consider 28-day strength** - Standard testing age for design")
    
    if suggestions:
        st.markdown("**AI Recommendations:**")
        for suggestion in suggestions:
            st.markdown(f"• {suggestion}")
    else:
        st.success("✅ Your mix design appears well-optimized!")
    
    st.markdown("</div>", unsafe_allow_html=True)

elif predict_clicked:
    st.error("❌ AI Model not loaded - Please check model files")

# CLOSE MAIN CONTAINER
st.markdown("</div>", unsafe_allow_html=True)

# =============================================
# FOOTER - PROFESSIONAL
# =============================================
st.markdown("""
<div style='text-align: center; padding: 2rem; background: white; border-radius: 12px; margin-top: 2rem; box-shadow: 0 5px 15px rgba(0,0,0,0.05);'>
    <h4 style='color: #2c3e50;'>🏛️ Ziauddin University Civil Engineering Department</h4>
    <p style='color: #7f8c8d; font-size: 1.1rem;'>🎪 Build Asia Expo 2026 | Karachi, Pakistan</p>
    
    <div style='margin: 1rem 0;'>
        <span class='stats-badge'>AI Model: Random Forest</span>
        <span class='stats-badge'>Accuracy: 87.6%</span>
        <span class='stats-badge'>Training Data: 1,030+ samples</span>
        <span class='stats-badge'>Error Margin: ±5.7 MPa</span>
    </div>
    
    <hr style='margin: 1.5rem 0; opacity: 0.2;'>
    
    <div style='color: #7f8c8d; font-size: 0.9rem;'>
        <p><strong>For Educational & Demonstration Purposes</strong></p>
        <p>Live AI Tool - No Installation Required</p>
        <p style='margin-top: 0.5rem;'>
            🔗 <strong>Live URL:</strong> 
            <a href='https://concrete-ai-zu-haiderak27.streamlit.app' style='color: #3498db; text-decoration: none;'>
                concrete-ai-zu-haiderak27.streamlit.app
            </a>
        </p>
        <p>📱 <strong>Scan QR code to try on your phone</strong></p>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================================
# DEVELOPER INFO
# =============================================
with st.sidebar.expander("🔧 Technical Details"):
    st.write("**Technology Stack:**")
    st.write("• Python + Streamlit")
    st.write("• Scikit-Learn (Random Forest)")
    st.write("• Pandas + NumPy")
    st.write("• Joblib for model serialization")
    
    if model is not None:
        st.write(f"**Model Information:**")
        st.write(f"• Features: {len(feature_names)} parameters")
        st.write(f"• Decision Trees: {len(model.estimators_)}")
        st.write(f"• Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
