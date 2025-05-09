import streamlit as st
from PIL import Image
st.set_page_config(
    page_title="Khoa học màu sắc", layout="wide"
)
# Chia làm 2 cột
col1, col2 = st.columns([1, 5])

with col1:
    st.image("Logo_FGAM.png", 
             caption="Khoa In và Truyền Thông")
width = 100
with col2:
    st.image("Logo_Trường_Đại_Học_Sư_Phạm_Kỹ_Thuật_TP_Hồ_Chí_Minh.JPG", 
             caption="Trường Sư phạm Kỹ thuật TPHCM")
width = 100
# Tiêu đề & giới thiệu
st.write("## Chào mừng bạn đến với project Khoa học màu sắc của mình!")
st.write("# Mình tên là Đinh Nguyễn Hoài Nhi, MSSV 21158050")
st.markdown("---")

# === Phần giới thiệu ===
st.markdown("## 🔎 Giới thiệu")
st.write("""
Khoa học màu sắc đóng vai trò then chốt trong ngành in ấn, giúp đảm bảo chất lượng hình ảnh, độ chính xác của màu sắc và sự đồng nhất giữa các thiết bị.
Trong in ấn hiện đại, việc quản lý màu sắc (color management) trở thành yêu cầu bắt buộc để đáp ứng các tiêu chuẩn quốc tế như ISO 12647.
""")
st.write("""
Trang web này nhằm hỗ trợ việc tìm hiểu và thực hành các kiến thức về Khoa học màu sắc trong in ấn, 
đặc biệt liên quan đến quy trình đo, chuyển đổi và mô phỏng không gian màu của các thiết bị in.
""")
# === Các chủ đề chính ===
st.markdown("## 📚 Nội dung chính")

col4, col5 = st.columns(2)

with col4:
    st.markdown("### 1️⃣ Chuyển đổi không gian màu sRGB ↔ XYZ")
    st.write("- Chuyển đổi qua lại giữa hệ màu sRGB và không gian XYZ.")

    st.markdown("### 2️⃣ Tính giá trị X, Y, Z từ file phổ đo")
    st.write("- Xử lý file phổ đo trên máy đo màu của Khoa để tính 3 thành phần X, Y, Z.")

    st.markdown("### 3️⃣ Vẽ biểu đồ CIE hình móng ngựa")
    st.write("- Vẽ biểu đồ CIE xy, còn gọi là biểu đồ hình móng ngựa, hiển thị các màu khả dụng của mắt người.")

with col5:
    st.markdown("### 4️⃣ Vẽ gamut màu của thiết bị RGB")
    st.write("- Minh hoạ dải màu (gamut) của một thiết bị hiển thị RGB trên biểu đồ CIE.")

    st.markdown("### 5️⃣ Vẽ gamut màu của máy in Khoa")
    st.write("- Dựa vào file gamut đo được từ máy in, vẽ dải màu in được trên không gian CIE.")

    st.markdown("### 6️⃣ Đặc tính hoá của máy in nửa tone")
    st.write("- Nghiên cứu và mô phỏng quá trình đặc tính hoá (characterization) máy in nửa tone tại Khoa.")
# === Thêm hàng mới ===
st.markdown("## 🔥 Ngoài ra")
st.write("Ngoài ra còn có các nội dung liên quan đến chủ đề Khoa học màu sắc khác rất hấp dẫn. Hãy trải nghiệm nhé!")
st.image("CIE-XYZ-colour-matching-functions-and-CIE-xy-chromacity-diagram-768x292-1.png", 
             caption="Các hàm phối màu chuẩn CIE 1931 và biểu đồ sắc độ CIE 1931 xy ")
# Hiệu ứng
st.success("✅ Cùng trải nghiệm với chúng tôi nào!")
st.balloons()
# === Footer ===
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 Đinh Nguyễn Hoài Nhi | Project Khoa học màu sắc</p>", unsafe_allow_html=True)
