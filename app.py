import streamlit as st
import difflib
import re

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hệ thống chấm điểm gõ tiếng Hàn", layout="wide")

# --- CÁC HÀM XỬ LÝ ---
def normalize_text(text, mode):
    """
    Xử lý văn bản dựa trên luật chấm điểm được chọn
    """
    if not text: return ""
    
    if mode == "Nới lỏng (Bỏ qua lỗi dư Khoảng trắng / Enter)":
        # Gom nhiều khoảng trắng/tab/enter thành 1 dấu cách duy nhất
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    else:
        # Khắt khe: Giữ nguyên định dạng, chỉ xóa khoảng trống thừa ở 2 đầu văn bản
        return text.strip()

def generate_visual_diff(original, student):
    """
    Tạo mã HTML để hiển thị gạch đỏ (lỗi sai) trực quan
    """
    matcher = difflib.SequenceMatcher(None, original, student)
    
    orig_html = []
    stud_html = []
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        # Lấy các đoạn text tương ứng
        o_chunk = original[i1:i2]
        s_chunk = student[j1:j2]
        
        # Chuyển đổi ký tự đặc biệt sang HTML để hiển thị đúng
        o_chunk = o_chunk.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        s_chunk = s_chunk.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        
        if tag == 'equal':
            # Phần giống nhau: Hiển thị chữ màu đen bình thường
            orig_html.append(f"<span>{o_chunk}</span>")
            stud_html.append(f"<span>{s_chunk}</span>")
        elif tag == 'delete':
            # Chữ có trong bản gốc nhưng SV gõ thiếu: Gạch ngang màu đỏ (Bản gốc)
            orig_html.append(f"<span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>{o_chunk}</span>")
        elif tag == 'insert':
            # Chữ SV gõ thừa/dư ra: Gạch dưới màu xanh (Bản SV)
            stud_html.append(f"<span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>{s_chunk}</span>")
        elif tag == 'replace':
            # SV gõ sai chữ gốc thành chữ khác: Gạch đỏ chữ gốc, Gạch xanh chữ SV gõ sai
            orig_html.append(f"<span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>{o_chunk}</span>")
            stud_html.append(f"<span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>{s_chunk}</span>")
            
    # Bọc mã HTML vào khung (box) có thanh cuộn và font chữ rõ ràng
    box_template = """
    <div style="border: 1px solid #ccc; border-radius: 5px; padding: 15px; height: 400px; overflow-y: auto; background-color: white; color: black; font-size: 16px; font-family: 'Malgun Gothic', sans-serif; line-height: 1.6;">
        {content}
    </div>
    """
    
    return box_template.format(content="".join(orig_html)), box_template.format(content="".join(stud_html))

# --- GIAO DIỆN NGƯỜI DÙNG ---
st.title("🖥️ Hệ thống chấm điểm gõ văn bản Copy & Paste")
st.markdown("Hệ thống tự động loại bỏ các định dạng (in đậm, in nghiêng) để chấm điểm công bằng dựa trên nội dung thuần.")

# 1. Tùy chọn luật chấm điểm
st.subheader("⚙️ Cài đặt Luật chấm điểm")
scoring_mode = st.radio(
    "Vui lòng chọn cách hệ thống xử lý Khoảng trắng (Space) và Dấu xuống dòng (Enter):",
    (
        "Nới lỏng (Bỏ qua lỗi dư Khoảng trắng / Enter)", 
        "Khắt khe (Tính chính xác tuyệt đối từng Dấu cách / Enter)"
    ),
    help="Thầy có thể thử thay đổi tùy chọn này sau khi chấm điểm để so sánh sự khác biệt của kết quả."
)

st.divider()

# 2. Vùng nhập liệu Copy - Paste
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📁 Văn bản GỐC")
    raw_original = st.text_area("Dán nội dung văn bản gốc vào đây:", height=250, key="orig_text")

with col2:
    st.markdown("### 🎓 Bài làm của SINH VIÊN")
    raw_student = st.text_area("Dán bài làm của sinh viên vào đây:", height=250, key="stud_text")

# 3. Xử lý và Chấm điểm
if st.button("🚀 BẮT ĐẦU CHẤM ĐIỂM", use_container_width=True, type="primary"):
    if not raw_original or not raw_student:
        st.warning("Vui lòng dán đầy đủ nội dung vào cả 2 ô trước khi chấm điểm.")
    else:
        with st.spinner("Đang tính toán và vẽ sơ đồ lỗi..."):
            # Chuẩn hóa văn bản theo luật đã chọn
            norm_original = normalize_text(raw_original, scoring_mode)
            norm_student = normalize_text(raw_student, scoring_mode)
            
            # Tính điểm
            matcher = difflib.SequenceMatcher(None, norm_original, norm_student)
            score = matcher.ratio() * 100
            
            # Hiển thị điểm số
            st.success("✅ Đã chấm điểm xong!")
            st.metric("Điểm số tương đồng", f"{score:.2f}%", f"Chế độ: {scoring_mode.split(' ')[0]}")
            
            # Tạo và hiển thị Visual Diff
            st.markdown("### 🔍 Phân tích chi tiết lỗi sai")
            
            # Ghi chú bảng màu
            st.markdown("""
            **Chú giải màu sắc:** 
            * <span style='color: red; text-decoration: line-through; background-color: #ffe6e6;'>Gạch đỏ:</span> Phần văn bản gốc mà sinh viên gõ thiếu hoặc gõ sai.
            * <span style='color: blue; text-decoration: underline; background-color: #e6f0ff;'>Gạch xanh dương:</span> Phần văn bản sinh viên gõ thừa ra hoặc gõ sai thay thế cho bản gốc.
            """, unsafe_allow_html=True)
            
            diff_orig_html, diff_stud_html = generate_visual_diff(norm_original, norm_student)
            
            diff_col1, diff_col2 = st.columns(2)
            with diff_col1:
                st.markdown("**Văn bản Gốc (Hiển thị phần SV gõ thiếu):**")
                st.markdown(diff_orig_html, unsafe_allow_html=True)
            with diff_col2:
                st.markdown("**Văn bản SV gõ (Hiển thị phần SV gõ sai/thừa):**")
                st.markdown(diff_stud_html, unsafe_allow_html=True)