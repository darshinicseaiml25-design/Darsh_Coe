import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np

# --- Page config ---
st.set_page_config(
    page_title="📄 Smart Image to PDF Scanner",
    page_icon="🖤",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for modern UI ---
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        font-family: 'Segoe UI', sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        height: 50px;
        width: 250px;
        border-radius: 12px;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    .css-1aumxhk {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("https://cdn-icons-png.flaticon.com/512/833/833314.png", width=80)
st.title("📄 Smart Image to PDF Scanner")
st.markdown("Upload images, convert them to **black & white**, and download as a **PDF** — just like Adobe Scan!")

# --- File uploader ---
uploaded_files = st.file_uploader(
    "Upload image(s)... (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

def convert_to_grayscale(img):
    """Convert image to grayscale."""
    return img.convert("L")

def create_pdf(images):
    """Convert list of PIL images to a single PDF in memory."""
    pdf_bytes = BytesIO()
    if len(images) == 1:
        images[0].save(pdf_bytes, format="PDF")
    else:
        images[0].save(pdf_bytes, save_all=True, append_images=images[1:], format="PDF")
    pdf_bytes.seek(0)
    return pdf_bytes

if uploaded_files:
    st.markdown("### Preview Uploaded Images:")
    grayscale_images = []

    for i, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file)
        st.image(img, caption=f"Original Image {i+1}", use_column_width=True)

    if st.button("🖤 Convert to Grayscale & Download PDF"):
        for uploaded_file in uploaded_files:
            img = Image.open(uploaded_file)
            gray_img = convert_to_grayscale(img)
            grayscale_images.append(gray_img)

        pdf_bytes = create_pdf(grayscale_images)

        # Show preview of first page
        st.markdown("### Grayscale Preview (First Page)")
        st.image(grayscale_images[0], use_column_width=True)

        # Download button
        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="scanned_document.pdf",
            mime="application/pdf",
        )
        st.success("✅ Your images have been converted to a grayscale PDF!")

# --- Footer with placeholder image ---
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
st.image("https://cdn-icons-png.flaticon.com/512/833/833314.png", width=50)
