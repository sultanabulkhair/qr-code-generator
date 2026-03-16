# High-Resolution QR Code Generator

A lightweight, interactive web application built with Python and Streamlit that generates permanent, high-resolution, static QR codes. Users can optionally embed a custom logo in the center of the QR code without sacrificing scannability.

## 🌟 Features
* **100% Static & Permanent:** Generates raw QR codes that never expire and do not route through third-party tracking links.
* **Custom Logo Integration:** Upload any PNG or JPG to perfectly center it within the QR code.
* **High Error Correction:** Utilizes Level H (30%) error correction to ensure the QR code remains perfectly readable even with a logo obscuring the center.
* **High-Resolution Output:** Generates crisp, large-scale images (approx. 1800x1800 pixels) suitable for both print and digital use.
* **Instant Download:** Renders the image in memory and provides a direct, secure `.png` download right from the browser.
* **One-Click Reset:** Quickly clear the session state to generate multiple codes in a row.

## 🛠️ Technology Stack
* **[Streamlit](https://streamlit.io/):** For the interactive web interface.
* **[qrcode](https://pypi.org/project/qrcode/):** For generating the mathematical matrix of the QR code.
* **[Pillow (PIL)](https://pillow.readthedocs.io/):** For high-quality image manipulation, anti-aliasing, and alpha-compositing (transparency) of the logo.
