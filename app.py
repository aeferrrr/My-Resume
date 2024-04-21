from pathlib import Path

import streamlit as st
from PIL import Image

# path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV-Arief Fadhillah R.pdf"
profile_pic = current_dir / "assets" / "mypic.png"

# --- GENERAL SETTING --- #
PAGE_TITLE = "Digital CV | Arief Fadhillah Rochmala"
PAGE_ICON = ":wave:"
NAME = "Arief Fadhillah Rochmala"
DESCRIPTION = """
A student with experience in creating a web-based system 
Using the framework codeigniter four that successfully met the project's needs. With that,
My passion for understanding the technology and the trend of web development led me to
Pursuing increased skill and knowledge in this area.
"""
EMAIL = "arief.fadhillah.r@gmail.com"
SOCIAL_MEDIA = {
    "Instagram" : "https://www.instagram.com/aefer_/",
    "Linkedin" : "https://www.linkedin.com/in/arief-fadhillah-rochmala-017354284/",
    "GitHub" : "https://github.com/aeferrrr"
}
PROJECT = {
    "✨ Sistem Parkir RFID" : "https://github.com/MrcSatrio/ParkingManagementSystem-EBIU",
    "✨ Kasir Koperasi RFID" : "https://github.com/MrcSatrio/Sistem-Kasir-AL_IDRUS"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- Load Css, PDF and PICTURE ---
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write("📫", EMAIL)

#Social Links 
st.write("#", align="center")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Experience and Qualification ---

st.write("#")
st.subheader("Work Experience")
st.write("###### HR & Mill Services DEPT | PT Pindo Deli Pulp and Paper Mills (Aug 2019 – Okt 2019)")
st.write(
    """
- Mengkoordinasikan dokumen dari mitra persahaan untuk mendukung kegiatan operasional perusahaan.
- Mengelola dan melaksanakan pengiriman ekspor impor barang perusahaan yang dibutuhkan oleh mitra perusahaan.
- Berkontribusi dalam menjaga barang serta dokumen datang, memberikan barang / dokumen kepada karyawan
"""
)
st.write("###### Warehouse Staff | Disdukcapil Karawang (Nov 2019 – Feb 2020)")
st.write(
    """
- Mengelola data kependudukan, termasuk menjaga integritas dan keamanan informasi.
-  Menjaga dan memperbaharui data kependudukan, membina data kependudukan terorganisir dan efisien.
"""
)
st.write("----")
st.write("#")
st.subheader("Project Experience")
st.write("###### Sistem Parkir RFID | Universitas Bina Insani (Feb 2023 – Juni 2023)")
st.write(
 """
-  Menjadi bagian integral dalam proyek pembuatan halaman admin website, dengan fokus mengelola
   kebutuhan dan fungsionalitas situs.
-  Mengemban tanggung jawab sebagai bagian dari tim manajerial dalam proyek, bekerja sama dengan 
   manajer proyek untuk mengoordinasikan dan mengelola tim, serta berperan aktif dalam 
   pengambilan keputusan untuk mencapai target proyek.
- Source code berhasil dijadikan sumber penulisan buku berjudul “CodeIgniter 4 untuk Pemula: 
  Panduan Langkah demi Langkah dalam Membangun Sistem Parkir”. [Lihat Sertifikat](https://drive.google.com/file/d/1pTUKDrQgl0CCJdHUQ7UkVO9uy7Q5KWFQ/view)
"""
)
st.write("###### Kasir Koperasi RFID | Yayasan Ponpes Al-Idrus (Agu 2023 – Sep 2023)")
st.write(
 """
-  Bertanggung jawab dalam pengembangan halaman website dengan fokus utama pada pembuatan 
   bagian login dan CRUD pada produk, pegawai, dan pelanggan untuk fungsionalitas situs.
-  Berhasil mengimplementasikan kebutuhan klien, yang secara signifikan meningkatkan kecepatan
   dan ketepatan dalam proses transaksi.
"""
)

# --- SKills ----
st.write("----")
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
- Programming : PHP, CodeIgniter4, SQL, Python
- Database : MySql
"""
)
st.write("----")
# (11.32)