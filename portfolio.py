import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Page settings
st.set_page_config(page_title="Preethiviraj Murugesan | Solar Design Engineer", page_icon="🌍", layout="wide")

# Add simple CSS for smooth transition effect
st.markdown("""
    <style>
    .fade-in {
        animation: fadeInAnimation ease 2s;
        animation-iteration-count: 1;
        animation-fill-mode: forwards;
    }

    @keyframes fadeInAnimation {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="fade-in">Preethiviraj Murugesan</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="fade-in">Solar Design Engineer | BESS Specialist | Renewable Energy Professional</h3>', unsafe_allow_html=True)

# About Me
st.header("About Me")
st.write("""
I'm a dynamic Solar Design Engineer with 3 years of proven success delivering high-performance PV systems, BESS solutions, and commercial rooftop installations across the UK. I bring a strong mechanical engineering foundation, combined with expertise in PVCase, PVsyst, AutoCAD, and Excel-based energy tools. Passionate about clean energy innovation, project optimization, and creating efficient, impactful renewable energy solutions.
""")

# Portfolio Section
st.header("Portfolio")

# Load Images
ground_mount = Image.open("GM.png")
commercial_rooftop = Image.open("RT.png")
hybrid_system = Image.open("Hybrid.png")
mechanical_site = Image.open("Tank.png")
autocad_design = Image.open("Autocad.png")
piping_design = Image.open("Pipe.png")
solar_curve = Image.open("Solar.png")
solar_data_analytics = Image.open("Data.png")

# Display projects with smooth layout
with st.container():
    st.subheader("🌌 Ground-Mount Solar Systems")
    st.write("Designed 10+ utility-scale ground-mount PV systems ranging from 500 kW to 50 MW, optimizing layout development using PVCase and performance simulations with PVsyst to maximize energy yield.")
    st.image(ground_mount, use_container_width=True)

with st.container():
    st.subheader("🏢 Commercial Rooftop Solar Projects")
    st.write("Delivered 20+ commercial rooftop PV installations for major clients like Tesco and David Lloyd, achieving Performance Ratios consistently above 85% and driving significant client savings.")
    st.image(commercial_rooftop, use_container_width=True)

with st.container():
    st.subheader("💡 Hybrid Systems (PV + Storage)")
    st.write("Modeled hybrid energy systems using HOMER Pro, integrating PV with battery storage solutions to enhance energy resilience and maximize ROI for both on-grid and off-grid applications.")
    st.image(hybrid_system, use_container_width=True)

with st.container():
    st.subheader("🚷 Mechanical Site Engineering")
    st.write("Supervised fabrication and erection of large storage tanks in industrial projects, ensuring compliance with safety standards, quality assurance, and efficient project delivery timelines.")
    st.image(mechanical_site, use_container_width=True)

with st.container():
    st.subheader("🗚️ AutoCAD Design Projects")
    st.write("Created detailed mechanical and piping layouts using AutoCAD and PDMS, supporting thermal power plant and industrial projects with high-precision technical drawings.")
    st.image(autocad_design, use_container_width=True)

with st.container():
    st.subheader("🔧 Piping Design Projects")
    st.write("Performed piping stress analysis using CAESAR II and coordinated piping system fabrication for large industrial facilities, ensuring system integrity and operational efficiency.")
    st.image(piping_design, use_container_width=True)

with st.container():
    st.subheader("📈 Solar Curve Visualization")
    st.write("Typical photovoltaic production curve highlighting peak generation periods and informing better load-matching strategies for PV system designs.")
    st.image(solar_curve, use_container_width=True)

with st.container():
    st.subheader("📊 Solar Data Analytics")
    st.write("Performed in-depth solar data analytics using Excel and Power BI to optimize system performance, simulate financial scenarios, and maximize energy self-consumption opportunities.")
    st.image(solar_data_analytics, use_container_width=True)

# CV Download Section
st.header("Download My CV")
with open("CV - Preethiviraj Murugesan.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="🔗 Download My CV", data=PDFbyte, file_name="Preethiviraj_Murugesan_CV.pdf", mime='application/octet-stream')

# Skills Section
st.header("Skills")
st.write("""
- **Solar Design Tools**: PVCase, PVsyst, PVSol
- **Simulation & Analysis**: Excel tools, HH data analysis, HOMER Pro
- **Programming**: Python (data automation, PV data visualization)
- **Mechanical Design**: AutoCAD, SolidWorks, PDMS
- **Energy Storage Solutions**: BESS feasibility and modelling
- **Project Management Tools**: Primavera Scheduling, Tender Documentation
""")

# Contact Section
st.header("Contact")
st.write("""
- 📧 Email: preethivirajmurugesan@gmail.com
- 👤 LinkedIn: [linkedin.com/in/preethiviraj-murugesan-161058164](https://linkedin.com/in/preethiviraj-murugesan-161058164)
""")

# Footer
st.markdown("---")
st.caption("Built with Streamlit | Designed by Preethiviraj Murugesan")
