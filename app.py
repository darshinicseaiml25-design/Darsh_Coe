import streamlit as st
from PIL import Image
from io import BytesIO

# Set page config for a modern look
st.set_page_config(
    page_title="Image to PDF Scanner",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS for a modern UI
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        height: 50px;
        width: 200px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📄 Modern Image to PDF Scanner")
st.subheader("Upload an image, convert it to black & white, and download as PDF!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display original image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    if st.button("Convert to Grayscale PDF"):
        # Convert to grayscale
        grayscale_image = image.convert("L")

        # Save to PDF in memory
        pdf_bytes = BytesIO()
        grayscale_image.save(pdf_bytes, format="PDF")
        pdf_bytes.seek(0)

        # Display grayscale image
        st.image(grayscale_image, caption="Grayscale Preview", use_column_width=True)

        # Provide download button
        st.download_button(
            label="📥 Download PDF",
            data=pdf_bytes,
            file_name="scanned_document.pdf",
            mime="application/pdf",
        )

        st.success("Your image has been converted to a grayscale PDF!")
