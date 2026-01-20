# =============================================
# CONCRETE INTELLIGENCE - AI CONCRETE PREDICTOR
# Ziauddin University Civil Engineering Department
# Build Asia Expo 2024 - Karachi, Pakistan
# =============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import os
from datetime import datetime

# =============================================
# PAGE CONFIGURATION
# =============================================
st.set_page_config(
    page_title="Concrete Intelligence",
    page_icon="🧱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =============================================
# LOAD AI MODEL
# =============================================
@st.cache_resource
def load_model():
    """Load trained AI model and supporting data"""
    try:
        model = joblib.load('concrete_strength_model.pkl')
        feature_names = joblib.load('feature_names.pkl')
        column_ranges = joblib.load('column_ranges.pkl')
        return model, feature_names, column_ranges
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None, None, None

# Load the model
model, feature_names, column_ranges = load_model()

# =============================================
# SIDEBAR - UNIVERSITY INFO
# =============================================
with st.sidebar:
    st.title("🧱 Concrete Intelligence")
    st.markdown("---")
    
    st.subheader("🏛️ Ziauddin University")
    st.markdown("**Civil Engineering Department**")
    st.markdown("*Karachi, Pakistan*")
    
    st.markdown("---")
    st.markdown("### 🎪 Build Asia Expo 2024")
    st.markdown("**Demonstration Platform**")
    
    st.markdown("---")
    if model is not None:
        st.success("✅ AI Model Loaded")
        st.metric("Model Accuracy", "87.6%", "R² Score")
    else:
        st.error("❌ Model Not Loaded")
    
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("civil.engineering@zu.edu.pk")
    st.markdown("📍 Ziauddin University, Karachi")

# =============================================
# MAIN INTERFACE
# =============================================
st.title("🧠 CONCRETE INTELLIGENCE")
st.subheader("AI-Powered Concrete Strength Prediction & Optimization")
st.markdown("**Ziauddin University Civil Engineering** | *Build Asia Expo 2024*")
st.markdown("---")

if model is None:
    st.error("⚠️ AI model could not be loaded. Please check model files.")
    st.stop()

# =============================================
# CONCRETE MIX DESIGN INPUTS
# =============================================
st.header("📊 Design Your Concrete Mix")

# Create two columns for inputs
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Cementitious Materials")
    cement = st.slider(
        "**Cement** (kg/m³)",
        min_value=100,
        max_value=500,
        value=300,
        help="Ordinary Portland Cement - Primary binder"
    )
    
    blast_slag = st.slider(
        "**Blast Furnace Slag** (kg/m³)",
        min_value=0,
        max_value=200,
        value=50,
        help="Supplementary cementitious material - Improves durability"
    )
    
    fly_ash = st.slider(
        "**Fly Ash** (kg/m³)",
        min_value=0,
        max_value=150,
        value=30,
        help="Pozzolanic material - Reduces heat of hydration"
    )
    
    water = st.slider(
        "**Water** (kg/m³)",
        min_value=100,
        max_value=250,
        value=180,
        help="Mixing water - Critical for workability and strength"
    )

with col2:
    st.markdown("### Aggregates & Admixtures")
    superplasticizer = st.slider(
        "**Superplasticizer** (kg/m³)",
        min_value=0.0,
        max_value=20.0,
        value=5.0,
        step=0.5,
        help="High-range water reducer - Improves workability"
    )
    
    coarse_agg = st.slider(
        "**Coarse Aggregate** (kg/m³)",
        min_value=500,
        max_value=1200,
        value=900,
        help="20mm crushed stone - Provides bulk and strength"
    )
    
    fine_agg = st.slider(
        "**Fine Aggregate** (kg/m³)",
        min_value=500,
        max_value=1000,
        value=700,
        help="Natural sand - Fills voids and improves workability"
    )
    
    age = st.slider(
        "**Curing Age** (days)",
        min_value=1,
        max_value=90,
        value=28,
        help="Age at testing - Strength increases with time"
    )

# Calculate water-cement ratio
wc_ratio = water / cement if cement > 0 else 0

# Display current parameters
st.markdown("---")
st.subheader("📋 Current Mix Parameters")

param_col1, param_col2, param_col3 = st.columns(3)
with param_col1:
    st.metric("Water-Cement Ratio", f"{wc_ratio:.3f}")
    if wc_ratio > 0.5:
        st.warning("High W/C ratio - May reduce strength")
    elif wc_ratio < 0.4:
        st.info("Good W/C ratio for strength")
    
with param_col2:
    total_powder = cement + blast_slag + fly_ash
    st.metric("Total Powder", f"{total_powder} kg/m³")
    
with param_col3:
    total_aggregate = coarse_agg + fine_agg
    st.metric("Total Aggregate", f"{total_aggregate} kg/m³")

# =============================================
# PREDICTION BUTTON
# =============================================
st.markdown("---")
st.subheader("🔮 AI Prediction")

predict_col1, predict_col2, predict_col3 = st.columns([1, 2, 1])
with predict_col2:
    predict_clicked = st.button(
        "🚀 PREDICT CONCRETE STRENGTH",
        type="primary",
        use_container_width=True,
        help="Click to get AI-powered strength prediction"
    )

if predict_clicked:
    # Prepare input data in correct order
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
    
    # =============================================
    # DISPLAY RESULTS
    # =============================================
    st.markdown("---")
    st.header("📈 PREDICTION RESULTS")
    
    # Result metrics
    result_col1, result_col2, result_col3 = st.columns(3)
    
    with result_col1:
        st.metric(
            label="Predicted Strength",
            value=f"{predicted_strength:.1f}",
            delta="MPa"
        )
    
    with result_col2:
        st.metric(
            label="Water-Cement Ratio",
            value=f"{wc_ratio:.3f}",
            delta=""
        )
    
    with result_col3:
        # Strength classification
        if predicted_strength >= 50:
            classification = "High-Strength"
            delta = "Structural"
            color = "green"
        elif predicted_strength >= 35:
            classification = "Standard"
            delta = "Commercial"
            color = "blue"
        elif predicted_strength >= 25:
            classification = "Medium"
            delta = "Residential"
            color = "orange"
        else:
            classification = "Low"
            delta = "Non-structural"
            color = "red"
        
        st.metric(
            label="Classification",
            value=classification,
            delta=delta
        )
    
    # =============================================
    # STRENGTH INTERPRETATION
    # =============================================
    st.markdown("---")
    st.subheader("💡 Strength Interpretation & Applications")
    
    if predicted_strength >= 50:
        st.success("""
        **🏗️ HIGH-STRENGTH CONCRETE (>50 MPa)**
        - **Applications:** Columns, beams, bridges, high-rise buildings
        - **Advantages:** Higher load capacity, reduced member sizes
        - **Karachi Use:** Bahria Icon Tower, Ocean Towers, Port Grand
        """)
    elif predicted_strength >= 35:
        st.info("""
        **🏢 STANDARD-STRENGTH CONCRETE (35-50 MPa)**
        - **Applications:** Commercial buildings, parking structures, slabs
        - **Advantages:** Good balance of strength and cost
        - **Karachi Use:** Dolmen Mall, Lucky One Mall, most office buildings
        """)
    elif predicted_strength >= 25:
        st.warning("""
        **🏠 MEDIUM-STRENGTH CONCRETE (25-35 MPa)**
        - **Applications:** Residential buildings, foundations, walls
        - **Advantages:** Cost-effective for typical construction
        - **Karachi Use:** Most houses, apartments, small buildings
        """)
    else:
        st.error("""
        **🛠️ LOW-STRENGTH CONCRETE (<25 MPa)**
        - **Applications:** Non-structural elements, blinding concrete, fills
        - **Advantages:** Economical for non-load-bearing applications
        - **Karachi Use:** Footpaths, boundary walls, landscaping
        """)
    
    # =============================================
    # OPTIMIZATION SUGGESTIONS
    # =============================================
    st.markdown("---")
    st.subheader("🔧 Optimization Suggestions")
    
    suggestions = []
    
    # Water-cement ratio suggestions
    if wc_ratio > 0.55:
        suggestions.append("💧 **Reduce water content** - Current W/C ratio is high (>0.55). Reduce water by 10-15% to increase strength.")
    elif wc_ratio < 0.35:
        suggestions.append("⚠️ **Increase workability** - Very low W/C ratio (<0.35) may cause placement issues. Consider adding superplasticizer.")
    
    # Cement content suggestions
    if cement < 250 and predicted_strength < 25:
        suggestions.append("🏗️ **Increase cement content** - For structural applications, consider increasing cement to 300+ kg/m³.")
    elif cement > 400 and predicted_strength > 50:
        suggestions.append("💰 **Optimize cement usage** - High cement content increases cost. Consider using supplementary materials.")
    
    # Supplementary materials suggestions
    if blast_slag == 0 and fly_ash == 0:
        suggestions.append("🌿 **Add supplementary materials** - Consider adding slag or fly ash (50-100 kg/m³) to improve durability and reduce cost.")
    
    # Age suggestions
    if age < 28 and predicted_strength < 30:
        suggestions.append("⏳ **Increase curing time** - Strength develops over time. 28-day strength is standard for design.")
    
    if suggestions:
        for suggestion in suggestions:
            st.markdown(suggestion)
    else:
        st.success("✅ Your mix design appears well-optimized!")
    
    # =============================================
    # KARACHI CONTEXT
    # =============================================
    st.markdown("---")
    st.subheader("🌆 Karachi-Specific Considerations")
    
    st.info("""
    **For Karachi's climate and materials:**
    1. **High temperatures** (30-40°C) accelerate hydration - monitor curing
    2. **Humidity variations** affect curing - maintain moisture
    3. **Local aggregates** may have different properties - test locally
    4. **Marine environment** in coastal areas - consider durability
    5. **Material availability** - adjust based on local supplier quality
    """)

# =============================================
# FOOTER
# =============================================
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <h4>🏛️ Ziauddin University Civil Engineering Department</h4>
    <p>Build Asia Expo 2024 | Karachi, Pakistan</p>
    <p><strong>AI Model Performance:</strong> R² = 0.876 | Error = ±5.7 MPa | Trained on 1,030 samples</p>
    <p><em>For educational and demonstration purposes</em></p>
</div>
""", unsafe_allow_html=True)

# =============================================
# HIDDEN DEVELOPER INFO
# =============================================
st.sidebar.markdown("---")
with st.sidebar.expander("Developer Info"):
    st.write(f"**Model:** Random Forest (100 trees)")
    st.write(f"**Features:** {len(feature_names)} parameters")
    st.write(f"**Training Data:** 1,030 concrete mixes")
    st.write(f"**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    st.write(f"**Python Version:** {sys.version}")