import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr(profile_url, logo_file=None):
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=40,  
        border=4,
    )
    qr.add_data(profile_url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')

    if logo_file is not None:
        logo = Image.open(logo_file).convert("RGBA")
        basewidth = int(float(qr_img.size[0]) * 0.2)
        wpercent = (basewidth / float(logo.size[0]))
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS)
        pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)
        qr_img.paste(logo, pos, mask=logo)
    
    return qr_img

st.set_page_config(page_title="QR Code Generator", page_icon="📱")

def reset_app():
    st.session_state.url_input = ""
    if "logo_input" in st.session_state:
        del st.session_state["logo_input"]
    st.session_state.show_qr = False

if "show_qr" not in st.session_state:
    st.session_state.show_qr = False

st.title("Professional QR Code Generator")

profile_url = st.text_input("Enter the URL:", key="url_input")
logo_file = st.file_uploader("Upload an Optional Logo (PNG)", type=["png", "jpg", "jpeg"], key="logo_input")

col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Generate QR Code"):
        if profile_url:
            st.session_state.show_qr = True
        else:
            st.warning("Please provide a URL to generate the code.")

with col2:
    st.button("Reset / Start Over", on_click=reset_app)


if st.session_state.show_qr and profile_url:
    st.markdown("---")
    with st.spinner("Generating high-res QR code..."):
        final_img = generate_qr(profile_url, logo_file)
        
        st.image(final_img, caption="Your Custom QR Code", width=400)
        
        buf = io.BytesIO()
        final_img.save(buf, format="PNG")
        byte_im = buf.getvalue()
        
        st.download_button(
            label="Download High-Res QR Code",
            data=byte_im,
            file_name="custom_qr_code.png",
            mime="image/png"
        )