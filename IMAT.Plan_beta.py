"""
Created on Fri May 23 13:41:27 2025

@author: Scott
"""
# EDITTING for STREAMSLIT
import streamlit as st
import numpy as np
import math
from math import pi, ceil
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
import base64

# Total cross-section data in barns
cross_sections = {
'H': 82.3526, '1H': 82.3626, '2H': 7.640518999999999, '3H': 3.03, 'He': 1.3474700000000002, '3He': 5339.0, '4He': 1.34, 'Li': 71.87, '6Li': 940.97, '7Li': 1.4454, 'Be': 7.6376, 'B': 772.24, '10B': 3838.1, '11B': 5.775499999999999, 'C': 5.5545, '12C': 5.56253, '13C': 4.8413699999999995, 'N': 13.41, '14N': 13.44, '15N': 5.210024, 'O': 4.23219, '16O': 4.2321, '17O': 4.436, '18O': 4.29016, 'F': 4.0276, 'Ne': 2.6670000000000003, '20Ne': 2.731, '21Ne': 6.37, '22Ne': 1.926, 'Na': 3.8099999999999996, 'Mg': 3.773, '24Mg': 4.08, '25Mg': 2.12, '26Mg': 3.0382, 'Al': 1.734, 'Si': 2.3379999999999996, '28Si': 2.297, '29Si': 2.881, '30Si': 2.7470000000000003, 'P': 3.484, 'S': 1.556, '32S': 1.528, '33S': 3.64, '34S': 1.747, '36S': 1.25, 'Cl': 50.3, '35Cl': 65.9, '37Cl': 1.623, 'Ar': 1.358, '36Ar': 83.10000000000001, '38Ar': 2.3, '40Ar': 1.081, 'K': 4.0600000000000005, '39K': 4.109999999999999, '40K': 36.6, '41K': 2.66, 'Ca': 3.2600000000000002, '40Ca': 3.31, '42Ca': 2.1, '43Ca': 7.0, '44Ca': 1.13, '46Ca': 2.34, '48Ca': 1.109, 'Sc': 51.0, 'Ti': 10.44, '46Ti': 3.6399999999999997, '47Ti': 4.9, '48Ti': 12.49, '49Ti': 5.6, '50Ti': 4.979, 'V': 10.18, '50V': 67.8, '51V': 9.99, 'Cr': 6.54, '50Cr': 18.34, '52Cr': 3.8019999999999996, '53Cr': 26.25, '54Cr': 2.96, 'Mn': 15.450000000000001, 'Fe': 14.18, '54Fe': 4.45, '56Fe': 15.01, '57Fe': 3.48, '58Fe': 29.28, 'Co': 42.78, 'Ni': 22.990000000000002, '58Ni': 30.700000000000003, '60Ni': 3.8899999999999997, '61Ni': 11.7, '62Ni': 24.0, '64Ni': 1.537, 'Cu': 11.809999999999999, '63Cu': 9.7, '65Cu': 16.67, 'Zn': 5.2410000000000005, '64Zn': 4.35, '66Zn': 5.1000000000000005, '67Zn': 14.26, '68Zn': 5.67, '70Zn': 4.592, 'Ga': 9.58, '69Ga': 10.07, '71Ga': 8.84, 'Ge': 10.8, '70Ge': 15.6, '72Ge': 9.9, '73Ge': 19.8, '74Ge': 7.6000000000000005, '76Ge': 8.16, 'As': 10.0, 'Se': 20.0, '74Se': 51.9, '76Se': 103.7, '77Se': 50.65, '78Se': 8.93, '80Se': 7.640000000000001, '82Se': 5.093999999999999, 'Br': 12.8, '79Br': 16.96, '81Br': 8.54, 'Kr': 32.68, '78Kr': 6.4, '80Kr': 11.8, '82Kr': 29.0, '83Kr': 185.0, '84Kr': 6.713, '86Kr': 8.203, 'Rb': 7.18, '85Rb': 7.18, '87Rb': 7.22, 'Sr': 7.53, '84Sr': 6.87, '86Sr': 5.08, '87Sr': 23.4, '88Sr': 6.478, 'Y': 8.98, 'Zr': 6.645, '90Zr': 5.111, '91Zr': 10.87, '92Zr': 7.12, '94Zr': 8.4499, '96Zr': 3.8228999999999997, 'Nb': 7.404999999999999, 'Mo': 8.19, '92Mo': 6.019, '94Mo': 5.824999999999999, '95Mo': 19.6, '96Mo': 5.33, '97Mo': 9.6, '98Mo': 5.567, '100Mo': 6.090000000000001, 'Tc': 26.3, 'Ru': 9.16, '96Ru': 0.28, '98Ru': 8.0, '99Ru': 6.9, '100Ru': 4.8, '101Ru': 3.3, '102Ru': 145.97, '104Ru': 4.792999999999999, 'Rh': 149.4, 'Pd': 11.38, '102Pd': 10.9, '104Pd': 8.1, '105Pd': 24.6, '106Pd': 5.404, '108Pd': 10.65, '110Pd': 7.726, 'Ag': 68.28999999999999, '107Ag': 44.9, '109Ag': 93.5, 'Cd': 2526.5, '106Cd': 4.1, '108Cd': 4.800000000000001, '110Cd': 15.4, '111Cd': 29.6, '112Cd': 7.3, '113Cd': 20612.4, '114Cd': 7.4399999999999995, '116Cd': 5.075, 'In': 196.42000000000002, '113In': 15.65, '115In': 204.57, 'Sn': 5.518000000000001, '112Sn': 5.5, '114Sn': 4.914, '115Sn': 34.8, '116Sn': 4.56, '117Sn': 7.8999999999999995, '118Sn': 4.85, '119Sn': 7.2, '120Sn': 5.43, '122Sn': 4.319999999999999, '124Sn': 4.613, 'Sb': 8.81, '121Sb': 9.85, '123Sb': 7.4399999999999995, 'Te': 9.02, '120Te': 5.8, '122Te': 5.2, '123Te': 418.52, '124Te': 14.8, '125Te': 4.73, '126Te': 4.92, '128Te': 4.575, '130Te': 4.84, 'I': 9.96, 'Xe': 23.9, '124Xe': 165.0, '126Xe': 3.5, '128Xe': 8.0, '129Xe': 21.0, '130Xe': 26.0, '131Xe': 85.0, '132Xe': 0.45, '134Xe': 0.265, '136Xe': 0.26, 'Cs': 32.9, 'Ba': 4.48, '130Ba': 31.6, '132Ba': 14.6, '134Ba': 6.08, '135Ba': 9.0, '136Ba': 3.71, '137Ba': 10.0, '138Ba': 3.21, 'La': 18.630000000000003, '138La': 65.5, '139La': 18.59, 'Ce': 3.57, '136Ce': 11.530000000000001, '138Ce': 6.74, '140Ce': 3.51, '142Ce': 3.79, 'Pr': 14.16, 'Nd': 67.1, '142Nd': 26.2, '143Nd': 417.0, '144Nd': 4.6, '145Nd': 72.0, '146Nd': 10.9, '148Nd': 6.6, '150Nd': 4.7, 'Pm': 189.70000000000002, 'Sm': 5961.0, '144Sm': 1.7, '147Sm': 96.0, '148Sm': 3.4, '149Sm': 42280.0, '150Sm': 129.0, '152Sm': 209.1, '154Sm': 19.4, 'Eu': 4539.2, '151Eu': 9108.6, '153Eu': 321.8, 'Gd': 49880.0, '152Gd': 748.0, '154Gd': 98.0, '155Gd': 61166.0, '156Gd': 6.5, '157Gd': 260044.0, '158Gd': 12.2, '160Gd': 11.29, 'Tb': 30.24, 'Dy': 1084.3, '156Dy': 37.7, '158Dy': 48.0, '160Dy': 61.6, '161Dy': 616.0, '162Dy': 194.25, '163Dy': 127.3, '164Dy': 3147.0, 'Ho': 73.12, 'Er': 167.7, '162Er': 28.7, '164Er': 21.4, '166Er': 33.7, '167Er': 660.2, '168Er': 9.64, '170Er': 17.4, 'Tm': 106.38, 'Yb': 58.199999999999996, '168Yb': 2232.13, '170Yb': 17.2, '171Yb': 64.2, '172Yb': 12.0, '173Yb': 32.1, '174Yb': 116.2, '176Yb': 12.45, 'Lu': 81.2, '175Lu': 28.2, '176Lu': 2070.9, 'Hf': 114.3, '174Hf': 576.0, '176Hf': 29.0, '177Hf': 373.2, '178Hf': 88.4, '179Hf': 48.1, '180Hf': 34.94, 'Ta': 26.61, '180Ta': 570.0, '181Ta': 26.509999999999998, 'W': 22.9, '180W': 33.0, '182W': 26.799999999999997, '183W': 15.8, '184W': 8.73, '186W': 37.964999999999996, 'Re': 101.2, '185Re': 122.7, '187Re': 88.30000000000001, 'Os': 30.7, '184Os': 3013.0, '186Os': 97.0, '187Os': 333.0, '188Os': 12.0, '189Os': 39.9, '190Os': 28.299999999999997, '192Os': 18.6, 'Ir': 439.0, '191Ir': 954.0, '193Ir': 111.0, 'Pt': 22.01, '190Pt': 162.0, '192Pt': 22.3, '194Pt': 15.44, '195Pt': 37.4, '196Pt': 13.020000000000001, '198Pt': 11.26, 'Au': 106.4, 'Hg': 399.1, '196Hg': 3195.0, '198Hg': 2.0, '199Hg': 2216.0, '200Hg': 60.0, '201Hg': 7.8, '202Hg': 14.718, '204Hg': 0.43, 'Tl': 13.32, '203Tl': 17.68, '205Tl': 11.504, 'Pb': 11.289, '204Pb': 12.950000000000001, '206Pb': 10.709999999999999, '207Pb': 11.519, '208Pb': 11.34048, 'Bi': 9.1898, 'Ra': 12.8, 'Th': 7.37, 'Pa': 213.2, 'U': 7.57, '233U': 587.7, '234U': 100.1, '235U': 694.26, '238U': 13.18, 'Np': 184.808, '238Pu': 570.9, '239Pu': 1036.6, '240Pu': 303.6, '242Pu': 27.371000000000002, 'Am': 89.8, '244Cm': 16.2, '246Cm': 26.36, '248Cm': 10.7
}

# Molar masses for base elements (g/mol)
molar_masses = {
'H': 1.008, 'He': 4.002, 'Li': 6.94, 'Be': 9.012, 'B': 10.81, 'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.085, 'P': 30.974, 'S': 32.06, 'Cl': 35.45, 'Ar': 39.95, 'K': 39.098, 'Ca': 40.078, 'Sc': 44.956, 'Ti': 47.867, 'V': 50.942, 'Cr': 51.996, 'Mn': 54.938, 'Fe': 55.845, 'Co': 58.933, 'Ni': 58.693, 'Cu': 63.546, 'Zn': 65.38, 'Ga': 69.723, 'Ge': 72.63, 'As': 74.922, 'Se': 78.971, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.468, 'Sr': 87.62, 'Y': 88.906, 'Zr': 91.224, 'Nb': 92.906, 'Mo': 95.95, 'Tc': 98.0, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71, 'Sb': 121.76, 'Te': 127.6, 'I': 126.9, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145.0, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.5, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05, 'Lu': 174.97, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 75.0, 'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 107.87, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 'Bi': 208.98, 'Po': 209.0, 'At': 210.0, 'Rn': 222.0, 'Fr': 223.0, 'Ra': 226.0, 'Ac': 227.0, 'Th': 232.04, 'Pa': 231.04, 'U': 238.03, 'Np': 237.0, 'Pu': 244.0, 'Am': 243.0, 'Cm': 247.0, 'Bk': 247.0, 'Cf': 251.0, 'Es': 252.0, 'Fm': 257.0, 'Md': 258.0, 'No': 259.0, 'Lr': 266.0, 'Rf': 267.0, 'Db': 268.0, 'Sg': 269.0, 'Bh': 270.0, 'Hs': 277.0, 'Mt': 278.0, 'Ds': 281.0, 'Rg': 282.0, 'Cn': 285.0, 'Nh': 286.0, 'Fl': 289.0, 'Mc': 290.0, 'Lv': 293.0, 'Ts': 294.0, 'Og': 294.0
}

# Pinhole sizes and corresponding neutron flux (neutrons/sec)
flux_by_pinhole = {
    20.0: 70581968.97, 30.0: 75222807.0, 40.0: 81194515.79,
    60.0: 84445614.0, 80.0: 92143968.85, 100.0: 95849937.58
}

# Camera options
camera_options = {
    "CCD": {
        "48 µm (98.3 mm FOV)": 48.0,
        "31.4 µm (64.3 mm FOV)": 31.4,
    },
    "CMOS": {
        "103 µm (211.5 mm FOV)": 103.0,
        "55 µm (112.7 mm FOV)": 55.0,
        "42 µm (85.5 mm FOV)": 42.0,
        "29 µm (59.5 mm FOV)": 29.0,
    }
}

# Helper function to extract element from isotope string
def get_element(isotope):
    return ''.join(filter(str.isalpha, isotope))

# App title
st.title("IMAT.Plan")

# Session state to track added isotopes
if 'sample_list' not in st.session_state:
    st.session_state.sample_list = []

if 'results_text_lines' not in st.session_state:
    st.session_state.results_text_lines = []

if 'isotope_transmission_log' not in st.session_state:
    st.session_state.isotope_transmission_log = []

if 'effective_transmission_log' not in st.session_state:
    st.session_state.effective_transmission_log = []

if 'sample_details_log' not in st.session_state:
    st.session_state.sample_details_log = []

# Sidebar inputs
st.sidebar.header("Just Add Isotopes!")
isotope = st.sidebar.selectbox("Isotope", list(cross_sections.keys()))
density = st.sidebar.number_input("Density (g/cm³)", value=1.0)
thickness = st.sidebar.number_input("Thickness (cm)", value=1.0)
if st.sidebar.button("Add Isotope"):
    st.session_state.sample_list.append({
        'isotope': isotope,
        'density': density,
        'thickness': thickness
    })

# Delete isotope
if st.sidebar.button("Delete Last Isotope"):
    if st.session_state.sample_list:
        st.session_state.sample_list.pop()

# Show current sample list
if st.session_state.sample_list:
    st.subheader("Sample List")
    for idx, item in enumerate(st.session_state.sample_list):
        st.markdown(f"{idx+1}. **{item['isotope']}**, ρ={item['density']} g/cm³, thickness={item['thickness']} cm")

# Inputs for calculations
pinhole = st.selectbox("Pinhole (mm)", list(flux_by_pinhole.keys()))
target_T = st.number_input("Target Transmission", value=0.2)

# Inputs for scan time calculation
sample_size = st.number_input("Sample size (mm)", value=10.0)
scint_dist = st.number_input("Scintillator distance (mm)", value=10.0)
camera = st.selectbox("Camera", list(camera_options.keys()))
pixel_label = st.selectbox("Pixel size", list(camera_options[camera].keys()))
pixel_size = camera_options[camera][pixel_label]
scan_range = st.selectbox("Scan range (°)", [180, 360], index=1)
exposure_time = st.number_input("Exposure time per projection (s)", value=60.0)

# Transmission calculation
def calculate_transmission():
    st.session_state.isotope_transmission_log.clear()
    st.session_state.sample_details_log.clear()

    if not st.session_state.sample_list:
        st.warning("Just Add isotopes")
        return

    T_eff = 1.0
    st.session_state.sample_details_log.append("Sample Composition Details:")
    for item in st.session_state.sample_list:
        isotope = item['isotope']
        sigma_barns = cross_sections[isotope]
        sigma_cm2 = sigma_barns * 1e-24
        element = get_element(isotope)
        molar_mass = molar_masses[element]
        n = (6.022e23 * item['density']) / molar_mass
        mu = n * sigma_cm2
        T = np.exp(-mu * item['thickness'])
        T_eff *= T
        st.session_state.sample_details_log.append(f"   Isotope: {isotope}, Density: {item['density']} g/cm³, Thickness: {item['thickness']} cm")
        st.session_state.isotope_transmission_log.append(f"**{isotope}** → Transmission: {T*100:.2f}%, Attenuation: {(1-T)*100:.2f}%")

    flux = flux_by_pinhole[pinhole]
    open_beam_counts = 100000000 * 40
    required_time = open_beam_counts / (flux * T_eff)
    required_time = math.ceil(required_time / 5) * 5

    st.session_state.effective_transmission_log.clear()
    st.session_state.effective_transmission_log.append(f"Effective Transmission: **{T_eff*100:.2f}%**")
    st.session_state.effective_transmission_log.append(f"Estimated Exposure Time: **{required_time:.1f} seconds**")

    st.markdown("---")
    st.markdown(f"### Effective Transmission: **{T_eff*100:.2f}%**")
    st.markdown(f"- Desired Target Transmission: **{target_T*100:.1f}%**")
    st.markdown(f"- Estimated Exposure Time: **{required_time:.1f} seconds**")

# Scan time calculation
def calculate_scan_time():
    st.session_state.results_text_lines.clear()
    try:
        overhead = 2
        half_sample = sample_size / 2
        beam_length = 10.4 * 1000
        ld_ratio = beam_length / pinhole
        actual_resolution = (scint_dist / ld_ratio) * 1000
        best_spatial_res = pixel_size * 2
        pixels_across_sample = (sample_size * 1000) / pixel_size
        projections_nyquist = pixels_across_sample * (pi / 2)
        projections_actual = ceil(projections_nyquist)
        angular_increment = scan_range / projections_actual
        angular_increment_rounded = round(angular_increment, 2)
        angle_step_below_180 = angular_increment_rounded * (projections_actual - 1) / 2
        angle_step_above_180 = angle_step_below_180 + angular_increment_rounded
        total_time_sec = (exposure_time + overhead) * projections_actual
        total_time_hr = total_time_sec / 3600

        def log(label, value):
            st.session_state.results_text_lines.append(f"{label}: {value}")
            st.markdown(f"**{label}:** {value}")

        log("Camera", camera)
        log("Pixel size", f"{pixel_size} µm")
        log("Half sample", f"{round(half_sample, 2)} mm")
        log("L/D Ratio", f"{round(ld_ratio, 1)}")
        log("Actual resolution (blurring)", f"{round(actual_resolution, 2)} µm")
        log("Best spatial resolution", f"{round(best_spatial_res, 2)} µm")
        log("Pixels across full sample", f"{round(pixels_across_sample, 2)} px")
        log("Projections (Nyquist)", f"{round(projections_nyquist, 2)}")
        log("Projections (Actual)", projections_actual)
        log("Angular increment", f"{angular_increment:.5f}°")
        log("Angular increment (rounded)", f"{angular_increment_rounded:.2f}°")
        log("Angle step below 180°", f"{round(angle_step_below_180, 2)}°")
        log("Angle step above 180°", f"{round(angle_step_above_180, 2)}°")
        log("Exposure time", f"{exposure_time} s")
        log("Total scan time", f"{round(total_time_hr, 2)} hours")

    except Exception as e:
        st.error(f"Error: {e}")

# PDF generation
def generate_pdf():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M")
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("Neutron Imaging Plan", styles['Title']))
    content.append(Spacer(1, 12))
    content.append(Paragraph(f"Generated on IMAT.plan : {now.strftime('%Y-%m-%d %H:%M:%S')}. Please consult results with a beamline scientist.", styles['Normal']))
    content.append(Spacer(1, 24))

    content.append(Paragraph("Sample Details", styles['Heading2']))
    for line in st.session_state.sample_details_log:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 6))
    for line in st.session_state.isotope_transmission_log:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 6))
    for line in st.session_state.effective_transmission_log:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 6))

    content.append(Paragraph("Scan Conditions", styles['Heading2']))
    for line in st.session_state.results_text_lines:
        content.append(Paragraph(line, styles['Normal']))
        content.append(Spacer(1, 6))

    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    doc.build(content)
    pdf_buffer.seek(0)

    st.success("✅ PDF created successfully!")
    b64 = base64.b64encode(pdf_buffer.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="Plan_{timestamp}.pdf"> 💾 Download PDF</a>'
    st.markdown(href, unsafe_allow_html=True)

# Buttons
if st.button("Calculate Effective Transmission"):
    calculate_transmission()

if st.button("Calculate Scan Time"):
    calculate_scan_time()

if st.button("Export to PDF"):
    generate_pdf()
