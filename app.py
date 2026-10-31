import streamlit as st
from pathlib import Path
from io import BytesIO
from xml.sax.saxutils import escape
from base64 import b64encode

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="E-CV Resti Jamilah",
    page_icon="🌸",
    layout="centered"
)

# =========================
# DATA CV
# =========================
data = {
    "nama": "Resti Jamilah",
    "posisi": "Information System Analyst",
    "email": "restijamilah81@gmail.com",
    "telepon": "085624908600",
    "alamat": "Sukabumi, Jawa Barat",

    "tentang": (
        "Mahasiswi Sistem Informasi Universitas Bina Sarana Informatika "
        "yang memiliki ketertarikan pada bidang Information System Analyst. "
        "Memiliki kemampuan berpikir analitis, teliti, dan bertanggung jawab, "
        "serta tertarik mempelajari analisis kebutuhan dan pengembangan sistem informasi."
    ),

    "pendidikan": (
        "Universitas Bina Sarana Informatika\n"
        "Sistem Informasi, Fakultas Teknik dan Informatika | 2023–Sekarang\n"
        "IPK: 3,92"
    ),

    "pengalaman": (
        "PENGALAMAN ORGANISASI\n"
        "Himpunan Mahasiswa Sistem Informasi (HIMASI)\n"
        "Anggota Pengurus Divisi Sumber Daya Mahasiswa\n"
        "Januari 2024 – Desember 2024\n\n"
        "Anggota Pengurus Departemen Pendidikan, Divisi Penelitian dan Pengembangan\n"
        "Januari 2025 – Desember 2025\n\n"

        "KEPANITIAAN\n"
        "• Ketua Pelaksana Kegiatan Bedah Skripsi dan TA 2024.\n"
        "• Ketua Pelaksana Pemilihan Ketua Umum HIMASI Tahun 2025.\n"
        "• Moderator Study Club Bulanan “Program Dasar Python”.\n"
        "• Berpartisipasi aktif dalam kepanitiaan dan kegiatan himpunan.\n\n"

        "PROYEK PERGURUAN TINGGI\n"
        "• Proyek Statistika dan Probabilitas: Analisis Pengguna Nyata "
        "Aplikasi X terhadap Mahasiswa/i Sistem Informasi Semester 1 dan 3 "
        "Tahun 2024 Universitas Bina Sarana Informatika.\n"
        "• Publikasi artikel ilmiah: Illegal Deepfake-Based Artificial "
        "Intelligence Content and Efforts to Combat It in Indonesia, "
        "Jurnal Ilmiah Sistem Informasi (JUSI), Vol. 5 No. 1, 2026."
    ),

    "keterampilan": (
        "HARD SKILLS\n"
        "• Microsoft Office (Word, Excel, PowerPoint)\n"
        "• Google Workspace\n"
        "• SQL dan Database Management\n"
        "• Analisis Kebutuhan Sistem\n"
        "• Pengolahan dan Analisis Data\n\n"

        "SOFT SKILLS\n"
        "• Kerja sama tim\n"
        "• Komunikasi yang baik\n"
        "• Manajemen waktu"
    ),

    "sertifikat": (
        "PELATIHAN BERSERTIFIKASI\n"
        "• Database Design & Database Programming with SQL – "
        "Talent Scouting Academy, Digital Talent Scholarship 2024 "
        "bersama KOMINFO dan Oracle Academy.\n"
        "• Workshop & Mini Proyek Sistem Basis Data bersama "
        "PT. Zahir Internasional."
    )
}

# =========================
# LOKASI FOTO
# =========================
FOLDER_APP = Path(__file__).resolve().parent
FOTO_PATH = FOLDER_APP / "foto_resti.jpeg"

# =========================
# WARNA
# =========================
PINK = "#BD5C91"
BIRU = "#35518A"
TEKS = "#34415C"

# =========================
# CSS TAMPILAN
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg, #fff0f6 0%, #f0f5ff 55%, #fceef5 100%
    );
    color: #26334d;
}

.block-container {
    max-width: 850px;
    padding-top: 2rem;
    padding-bottom: 2.5rem;
}

.cv-title {
    text-align: center;
    color: #35518a;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: 2px;
    margin-bottom: 4px;
}

.cv-subtitle {
    text-align: center;
    color: #bd5c91;
    font-size: 15px;
    margin-bottom: 24px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.97);
    border: 1px solid #f0cfe0;
    border-radius: 20px;
    padding: 24px;
    box-shadow: 0 8px 28px rgba(74,86,130,0.10);
}

.stApp h1, .stApp h2, .stApp h3 {
    color: #35518a !important;
}

.stApp p, .stApp li,
.stApp [data-testid="stCaptionContainer"] {
    color: #34415c;
}

.stDownloadButton button {
    background: linear-gradient(90deg, #d96ca5, #6888d8);
    color: white !important;
    border: none;
    border-radius: 12px;
    min-height: 48px;
    font-weight: 700;
    width: 100%;
}

.stDownloadButton button:hover {
    background: linear-gradient(90deg, #c65391, #4f70c4);
    color: white !important;
    border: none;
}

hr {
    border-color: #f0cfe0 !important;
}

.footer {
    text-align: center;
    color: #8a7190;
    font-size: 12px;
    margin-top: 22px;
}

@media (max-width: 600px) {
    .block-container {
        padding: 1rem 0.7rem 2rem;
    }

    .cv-title {
        font-size: 26px;
    }
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown(
    '<div class="cv-title">CURRICULUM VITAE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="cv-subtitle">'
    '🌸 E-CV · Information System Analyst · 2026'
    '</div>',
    unsafe_allow_html=True
)

# =========================
# FOTO PROFIL
# =========================
if FOTO_PATH.is_file():
    foto_base64 = b64encode(
        FOTO_PATH.read_bytes()
    ).decode("utf-8")

    st.markdown(
        f"""
        <div style="
            width: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px auto 25px auto;
        ">
            <img
                src="data:image/jpeg;base64,{foto_base64}"
                style="
                    display: block;
                    width: 155px;
                    height: 155px;
                    object-fit: cover;
                    object-position: center;
                    border-radius: 50%;
                    border: 5px solid #f3b6d2;
                    box-shadow: 0 0 0 4px #b9d9f8;
                "
            >
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.error("Foto profil belum ditemukan. Periksa nama file foto.")

# =========================
# MENAMPILKAN DATA CV
# =========================
with st.container(border=True):

    st.markdown(
        f"<h1 style='text-align:center;color:{PINK};"
        f"font-size:30px;font-weight:800;margin-bottom:0;'>"
        f"{escape(data['nama'])}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='text-align:center;color:{PINK};font-size:18px;"
        f"font-weight:700;margin-top:4px;'>"
        f"{escape(data['posisi'])}</p>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<p style='text-align:center;color:{TEKS};line-height:1.9;'>"
        f"📧 {escape(data['email'])}<br>"
        f"📱 {escape(data['telepon'])}<br>"
        f"📍 {escape(data['alamat'])}</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 👤 Tentang Saya")
    st.write(data["tentang"])

    st.markdown("### 🎓 Pendidikan")
    st.text(data["pendidikan"])

    st.markdown("### 💼 Pengalaman")
    st.text(data["pengalaman"])

    st.markdown("### 💻 Keterampilan")
    st.text(data["keterampilan"])

    st.markdown("### 📜 Sertifikat dan Pelatihan")
    st.text(data["sertifikat"])

# =========================
# MEMBUAT PDF
# =========================
pdf_buffer = BytesIO()

doc = SimpleDocTemplate(
    pdf_buffer,
    pagesize=A4,
    rightMargin=45,
    leftMargin=45,
    topMargin=35,
    bottomMargin=35
)

styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name="NamaCV",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=21,
    leading=26,
    textColor=colors.HexColor(BIRU),
    alignment=1,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name="PosisiCV",
    parent=styles["Normal"],
    fontSize=12,
    leading=16,
    textColor=colors.HexColor(PINK),
    alignment=1,
    spaceAfter=7
))

styles.add(ParagraphStyle(
    name="KontakCV",
    parent=styles["Normal"],
    fontSize=8.5,
    leading=13,
    textColor=colors.HexColor(TEKS),
    alignment=1,
    spaceAfter=8
))

styles.add(ParagraphStyle(
    name="BagianCV",
    parent=styles["Heading2"],
    fontSize=11.5,
    leading=15,
    textColor=colors.HexColor(BIRU),
    spaceBefore=9,
    spaceAfter=5
))

styles.add(ParagraphStyle(
    name="IsiCV",
    parent=styles["BodyText"],
    fontSize=8.5,
    leading=12,
    textColor=colors.HexColor("#26334D"),
    spaceAfter=3
))

story = []

# Foto profil PDF
if FOTO_PATH.is_file():
    try:
        foto_pdf = Image(str(FOTO_PATH), width=78, height=78)
        foto_pdf.hAlign = "CENTER"
        story.extend([foto_pdf, Spacer(1, 8)])
    except Exception:
        pass

story.extend([
    Paragraph(escape(data["nama"]), styles["NamaCV"]),
    Paragraph(escape(data["posisi"]), styles["PosisiCV"]),
    Paragraph(
        escape(" | ".join([
            data["email"],
            data["telepon"],
            data["alamat"]
        ])),
        styles["KontakCV"]
    ),
    HRFlowable(
        width="100%",
        thickness=1,
        color=colors.HexColor("#E9A8CC"),
        spaceBefore=3,
        spaceAfter=5
    )
])

bagian = [
    ("Tentang Saya", "tentang"),
    ("Pendidikan", "pendidikan"),
    ("Pengalaman", "pengalaman"),
    ("Keterampilan", "keterampilan"),
    ("Sertifikat dan Pelatihan", "sertifikat")
]

for judul, kunci in bagian:
    story.append(
        Paragraph(escape(judul), styles["BagianCV"])
    )

    paragraf = []

    for baris in data[kunci].splitlines():
        teks = escape(baris)

        if teks.startswith("• "):
            paragraf.append("&bull; " + teks[2:])
        elif teks:
            paragraf.append(teks)
        else:
            paragraf.append("&#160;")

    story.append(
        Paragraph("<br/>".join(paragraf), styles["IsiCV"])
    )

doc.build(story)
pdf_buffer.seek(0)

# =========================
# TOMBOL UNDUH PDF
# =========================
st.download_button(
    label="📥 Unduh CV dalam PDF",
    data=pdf_buffer.getvalue(),
    file_name="CV_Resti_Jamilah.pdf",
    mime="application/pdf",
    use_container_width=True
)

st.markdown(
    '<div class="footer">E-CV Resti Jamilah · '
    'Sistem Informasi</div>',
    unsafe_allow_html=True
)
