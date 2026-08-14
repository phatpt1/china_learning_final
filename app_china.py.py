import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------------------------------------------------
# CONFIGURATION & STREAMLIT PAGE SETUP
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="App Học Tiếng Trung Ehou Pro",
    page_icon="🇨🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Responsive CSS for Mobile & Desktop
st.markdown("""
<style>
    /* Global Font & Theme */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .main-header {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 1.2rem;
        box-shadow: 0 8px 20px -2px rgba(220, 38, 38, 0.25);
    }
    .main-header h1 {
        color: white !important;
        font-size: 1.6rem !important;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }
    .main-header p {
        color: #fca5a5 !important;
        font-size: 0.9rem !important;
        margin: 0;
    }

    /* Hide Streamlit Padding on Mobile */
    @media (max-width: 640px) {
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 2rem !important;
            padding-left: 0.8rem !important;
            padding-right: 0.8rem !important;
        }
        .main-header {
            padding: 1rem;
            border-radius: 12px;
        }
        .main-header h1 {
            font-size: 1.3rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# DATA BANK: VOCABULARY & WRITING DICTIONARY
# -----------------------------------------------------------------------------
@st.cache_data
def get_writing_vocab():
    return {
        "Bài 1: 你好": [
            {"char": "你", "pinyin": "nǐ", "meaning": "Bạn, anh, chị (Ngôi 2)", "compounds": "你好 (nǐ hǎo) - Xin chào"},
            {"char": "好", "pinyin": "hǎo", "meaning": "Tốt, đẹp, hay", "compounds": "很好 (hěn hǎo) - Rất tốt"},
            {"char": "妈", "pinyin": "mā", "meaning": "Mẹ, má", "compounds": "妈妈 (māma) - Mẹ"},
            {"char": "爸", "pinyin": "bà", "meaning": "Bố, ba", "compounds": "爸爸 (bàba) - Bố"},
            {"char": "弟", "pinyin": "dì", "meaning": "Em trai", "compounds": "弟弟 (dìdi) - Em trai"},
            {"char": "妹", "pinyin": "mèi", "meaning": "Em gái", "compounds": "妹妹 (mèimei) - Em gái"},
            {"char": "女", "pinyin": "nǚ", "meaning": "Nữ, con gái", "compounds": "女儿 (nǚ'ér) - Con gái"},
            {"char": "大", "pinyin": "dà", "meaning": "To, lớn", "compounds": "大学 (dàxué) - Đại học"}
        ],
        "Bài 2: 汉语难吗": [
            {"char": "哥", "pinyin": "gē", "meaning": "Anh trai", "compounds": "哥哥 (gēge) - Anh trai"},
            {"char": "忙", "pinyin": "máng", "meaning": "Bận rộn", "compounds": "很忙 (hěn máng) - Rất bận"},
            {"char": "他", "pinyin": "tā", "meaning": "Anh ấy, ông ấy", "compounds": "他们 (tāmen) - Họ (nam)"},
            {"char": "她", "pinyin": "tā", "meaning": "Cô ấy, bà ấy", "compounds": "她们 (tāmen) - Họ (nữ)"},
            {"char": "很", "pinyin": "hěn", "meaning": "Rất", "compounds": "很好 (hěn hǎo) - Rất tốt"},
            {"char": "难", "pinyin": "nán", "meaning": "Khó", "compounds": "不难 (bù nán) - Không khó"},
            {"char": "不", "pinyin": "bù", "meaning": "Không, chẳng", "compounds": "不太 (bú tài) - Không lắm"},
            {"char": "太", "pinyin": "tài", "meaning": "Quá, lắm", "compounds": "太太 (tàitai) - Bà thái"}
        ],
        "Bài 3: 谢谢您": [
            {"char": "您", "pinyin": "nín", "meaning": "Ngài, ông, bà (Lịch sự)", "compounds": "您好 (nín hǎo) - Chào ngài"},
            {"char": "请", "pinyin": "qǐng", "meaning": "Mời, xin", "compounds": "请进 (qǐng jìn) - Mời vào"},
            {"char": "进", "pinyin": "jìn", "meaning": "Vào, tiến", "compounds": "请进 (qǐng jìn) - Mời vào"},
            {"char": "谢", "pinyin": "xiè", "meaning": "Cảm ơn", "compounds": "谢谢 (xièxie) - Cảm ơn"},
            {"char": "去", "pinyin": "qù", "meaning": "Đi", "compounds": "去学校 (qù xuéxiào) - Đi đến trường"},
            {"char": "钱", "pinyin": "qián", "meaning": "Tiền", "compounds": "取钱 (qǔ qián) - Rút tiền"},
            {"char": "姐", "pinyin": "jiě", "meaning": "Chị gái", "compounds": "姐姐 (jiějie) - Chị gái"},
            {"char": "校", "pinyin": "xiào", "meaning": "Trường học", "compounds": "学校 (xuéxiào) - Trường học"}
        ],
        "Bài 4: 你叫什么名字": [
            {"char": "我", "pinyin": "wǒ", "meaning": "Tôi, ta", "compounds": "我们 (wǒmen) - Chúng tôi"},
            {"char": "叫", "pinyin": "jiào", "meaning": "Tên là, gọi là", "compounds": "叫什么 (jiào shénme) - Tên là gì"},
            {"char": "名", "pinyin": "míng", "meaning": "Danh, tên", "compounds": "名字 (míngzi) - Tên"},
            {"char": "字", "pinyin": "zì", "meaning": "Chữ, tự", "compounds": "汉字 (hànzì) - Chữ Hán"},
            {"char": "认", "pinyin": "rèn", "meaning": "Nhận, biết", "compounds": "认识 (rènshi) - Quen biết"},
            {"char": "识", "pinyin": "shí", "meaning": "Thức, biết", "compounds": "认识 (rènshi) - Quen biết"},
            {"char": "高", "pinyin": "gāo", "meaning": "Cao", "compounds": "高兴 (gāoxìng) - Vui vẻ"},
            {"char": "兴", "pinyin": "xìng", "meaning": "Hưng, vui", "compounds": "高兴 (gāoxìng) - Vui vẻ"}
        ],
        "Bài 5: 你去哪儿": [
            {"char": "哪", "pinyin": "nǎ", "meaning": "Nào, đâu", "compounds": "哪国人 (nǎ guó rén) - Người nước nào"},
            {"char": "国", "pinyin": "guó", "meaning": "Nước, quốc gia", "compounds": "中国 (Zhōngguó) - Trung Quốc"},
            {"char": "人", "pinyin": "rén", "meaning": "Người", "compounds": "越南人 (Yuènán rén) - Người VN"},
            {"char": "回", "pinyin": "huí", "meaning": "Trở về", "compounds": "回家 (huí jiā) - Về nhà"},
            {"char": "家", "pinyin": "jiā", "meaning": "Nhà, gia đình", "compounds": "回家 (huí jiā) - Về nhà"},
            {"char": "见", "pinyin": "jiàn", "meaning": "Gặp, thấy", "compounds": "再见 (zài jiàn) - Tạm biệt"}
        ],
        "Bài 6: 这是我的书": [
            {"char": "这", "pinyin": "zhè", "meaning": "Đây, này (Gần)", "compounds": "这是 (zhè shì) - Đây là"},
            {"char": "那", "pinyin": "nà", "meaning": "Kia, đó (Xa)", "compounds": "那是 (nà shì) - Kia là"},
            {"char": "书", "pinyin": "shū", "meaning": "Sách", "compounds": "中文书 (Zhōngwén shū) - Sách tiếng Trung"},
            {"char": "谁", "pinyin": "shéi", "meaning": "Ai", "compounds": "是谁的 (shì shéi de) - Là của ai"}
        ],
        "Bài 7: 今天星期几": [
            {"char": "今", "pinyin": "jīn", "meaning": "Nay, hiện tại", "compounds": "今天 (jīntiān) - Hôm nay"},
            {"char": "天", "pinyin": "tiān", "meaning": "Trời, ngày", "compounds": "明天 (míngtiān) - Ngày mai"},
            {"char": "星", "pinyin": "xīng", "meaning": "Sao, tinh", "compounds": "星期 (xīngqī) - Tuần/Thứ"},
            {"char": "期", "pinyin": "qī", "meaning": "Kỳ, thời gian", "compounds": "星期一 (xīngqīyī) - Thứ 2"},
            {"char": "几", "pinyin": "jǐ", "meaning": "Mấy, vài", "compounds": "星期几 (xīngqī jǐ) - Thứ mấy"},
            {"char": "岁", "pinyin": "suì", "meaning": "Tuổi", "compounds": "二十岁 (èrshí suì) - 20 tuổi"}
        ]
    }

# -----------------------------------------------------------------------------
# QUIZ DATA BANK (53 QUESTIONS)
# -----------------------------------------------------------------------------
@st.cache_data
def get_quiz_questions():
    return [
        {"category": "audio", "audioText": "dà xǐ", "question": "Nghe file audio và chọn phiên âm đúng:", "options": ["dáxǐ", "daxi", "dàxǐ"], "correct": 2, "explanation": "Audio đọc: dà xǐ (大喜 - Thanh 4 và Thanh 3)."},
        {"category": "audio", "audioText": "xī xīn", "question": "Nghe file audio và chọn phiên âm đúng:", "options": ["xīxìn", "xīxīn", "xíxīn"], "correct": 1, "explanation": "Audio đọc: xī xīn (细心 - Tỉ mỉ, cẩn thận)."},
        {"category": "audio", "audioText": "yǎn yuán", "question": "Nghe file audio và chọn phiên âm đúng:", "options": ["yányuân", "yǎnyuán", "yányuán"], "correct": 1, "explanation": "Audio đọc: yǎnyuán (演员 - Diễn viên)."},
        {"category": "audio", "audioText": "xū yào", "question": "Nghe file audio và chọn phiên âm đúng:", "options": ["xīyào", "xūyào", "jīyào"], "correct": 1, "explanation": "Audio đọc: xūyào (需要 - Cần thiết)."},
        {"category": "audio", "audioText": "nǔ lì", "question": "Nghe file audio và chọn phiên âm đúng:", "options": ["nǔlì", "núlì", "nǔlí"], "correct": 0, "explanation": "Audio đọc: nǔlì (努力 - Cố gắng)."},
        {"category": "audio", "audioText": "ā yí hǎo", "question": "Nghe file audio và chọn câu đúng:", "options": ["您好", "阿姨好", "阿姨"], "correct": 1, "explanation": "Audio đọc: ā yí hǎo (阿姨好! - Chào cô!)."},
        {"category": "audio", "audioText": "qù qǔ qián", "question": "Nghe file audio và chọn cụm từ đúng:", "options": ["去邮局", "去取钱", "去银行"], "correct": 1, "explanation": "Audio đọc: qù qǔ qián (去取钱 - Đi rút tiền)."},
        {"category": "audio", "audioText": "qǐng jìn", "question": "Nghe file audio và chọn từ đúng:", "options": ["请讲", "请进", "请教"], "correct": 1, "explanation": "Audio đọc: qǐng jìn (请进 - Mời vào)."},
        {"category": "audio", "audioText": "xiè xie nǐ", "question": "Nghe file audio và chọn từ đúng:", "options": ["谢谢你", "谢谢您", "不客气"], "correct": 0, "explanation": "Audio đọc: xiè xie nǐ (谢谢你 - Cảm ơn bạn)."},
        {"category": "audio", "audioText": "jiě jie", "question": "Nghe file audio và chọn từ đúng:", "options": ["姐姐", "妹妹", "妈妈"], "correct": 0, "explanation": "Audio đọc: jiě jie (姐姐 - Chị gái)."},
        {"category": "audio", "audioText": "zhēn", "question": "Nghe và chọn thanh mẫu đúng của âm tiết được phát:", "options": ["ch", "zh"], "correct": 1, "explanation": "Âm tiết nghe được là 'zhēn', thanh mẫu là: zh."},
        {"category": "audio", "audioText": "rōng", "question": "Nghe âm thanh vần '...ong' và chọn thanh mẫu đúng:", "options": ["s", "r"], "correct": 1, "explanation": "Âm tiết nghe được là 'rōng', thanh mẫu là: r."},
        {"category": "audio", "audioText": "kè fú", "question": "Nghe audio và chọn thanh điệu đúng cho từ kefu:", "options": ["kefǔ", "kèfǔ", "kèfú"], "correct": 2, "explanation": "Từ đúng là kèfú (克服 - Khắc phục)."},
        {"category": "audio", "audioText": "tū dì", "question": "Nghe audio và chọn thanh điệu đúng cho từ tudi:", "options": ["tūdì", "túdì", "tūdi"], "correct": 2, "explanation": "Từ đúng là tūdi (徒弟 - Đồ đệ)."},
        {"category": "audio", "audioText": "tài guó", "question": "Nghe audio '... guó' và chọn âm đầu thích hợp:", "options": ["tài", "tái"], "correct": 0, "explanation": "Audio đọc: Tài guó (泰国 - Thái Lan)."},
        {"category": "audio", "audioText": "Hàn yu", "question": "Nghe audio '... yǔ' và chọn chữ Hán/âm đúng:", "options": ["Hán", "Hàn"], "correct": 1, "explanation": "Audio đọc: Hàn (Hànyǔ - 汉语 Hán ngữ)."},

        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 彳", "options": ["Bộ Nhân, 2 nét", "Bộ Tâm, 3 nét", "Bộ Xích, 3 nét"], "correct": 2, "explanation": "Bộ Xích (Nhân kép) gồm 3 nét. Dễ nhầm với bộ Nhân đứng (亻) 2 nét!"},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 亻", "options": ["Bộ Nữ, 2 nét", "Bộ Nhân, 2 nét", "Bộ Ngôn, 2 nét"], "correct": 1, "explanation": "Đây là bộ Nhân (Nhân đứng), gồm 2 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 忄", "options": ["Bộ Nhân, 2 nét", "Bộ Xích, 3 nét", "Bộ Tâm, 3 nét"], "correct": 2, "explanation": "Đây là bộ Tâm đứng, gồm 3 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 氵", "options": ["Bộ Thủy, 3 nét", "Bộ Miên, 2 nét", "Bộ Nữ, 3 nét"], "correct": 0, "explanation": "Đây là bộ Thủy (3 chấm thủy), gồm 3 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 讠", "options": ["Bộ Ngôn, 3 nét", "Bộ Ngôn, 2 nét", "Bộ Miên, 3 nét"], "correct": 1, "explanation": "Bộ Ngôn (giản thể), gồm 2 nét."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: gege", "options": ["弟弟", "爸爸", "哥哥"], "correct": 2, "explanation": "哥哥 (gēge) = Anh trai."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: didi", "options": ["弟弟", "好", "女"], "correct": 0, "explanation": "弟弟 (dìdi) = Em trai."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 爸爸", "options": ["bàba", "nǚ", "dìdi"], "correct": 0, "explanation": "爸爸 (bàba) = Bố."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 妈妈", "options": ["mèimei", "māma", "bàba"], "correct": 1, "explanation": "妈妈 (māma) = Mẹ."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 你", "options": ["nǐ", "hǎo", "mèimei"], "correct": 0, "explanation": "你 (nǐ) = Bạn, cậu."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 女", "options": ["nǚ", "māma", "dìdi"], "correct": 0, "explanation": "女 (nǚ) = Nữ, con gái."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: hěn", "options": ["恨", "狠", "很"], "correct": 2, "explanation": "很 (hěn) = Rất."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: nán", "options": ["住", "摊", "难"], "correct": 2, "explanation": "难 (nán) = Khó."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: tài", "options": ["大", "太", "夫"], "correct": 1, "explanation": "太 (tài) = Quá, lắm. Đừng nhầm với 大 (dà - To lớn)."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: dà", "options": ["大", "太"], "correct": 0, "explanation": "大 (dà) = To, lớn."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: bù", "options": ["木", "不", "否"], "correct": 1, "explanation": "不 (bù) = Không."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: wǒ", "options": ["我", "找"], "correct": 0, "explanation": "我 (wǒ) = Tôi. Tránh nhầm với 找 (zhǎo - Tìm)."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: tā", "options": ["作", "他", "也"], "correct": 1, "explanation": "他 (tā) = Anh ấy."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: yin", "options": ["钱", "银"], "correct": 1, "explanation": "银 (yín) = Bạc/Ngân."},
        {"category": "radical", "question": "Chọn phiên âm đúng của chữ Hán: 岁", "options": ["sui", "shui", "suì"], "correct": 2, "explanation": "岁 (suì) = Tuổi."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 您", "options": ["ni", "nín"], "correct": 1, "explanation": "您 (nín) = Ngài, ngài ấy."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 上午", "options": ["shàngwù", "zhōngwù", "xiàwù"], "correct": 0, "explanation": "上午 (shàngwù) = Buổi sáng."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 晚会", "options": ["wǎnhuì", "yǎnhuì", "uǎnhuì"], "correct": 0, "explanation": "晚会 (wǎnhuì) = Dạ hội / Tiệc tối."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 多大", "options": ["duōdà", "duódà", "duòdā"], "correct": 0, "explanation": "多大 (duōdà) = Bao nhiêu tuổi."},

        {"category": "grammar", "question": "Chọn phiên âm đúng cho: 不好", "options": ["bù hǎo", "bú máng", "bú hǎo"], "correct": 1, "explanation": "Trong đề thi Ehou, lựa chọn 'bú máng' xuất hiện làm đáp án chuẩn biến điệu."},
        {"category": "grammar", "question": "Chọn phiên âm đúng cho: 不大", "options": ["bù dà", "bú dà"], "correct": 1, "explanation": "Không to = bú dà (bù đứng trước thanh 4 đổi thành bú)."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王兰：你去邮局寄信吗？ 明玉：_______，去银行取钱。", "options": ["不去", "不好", "去"], "correct": 0, "explanation": "Vế sau đi ngân hàng ➔ Vế trước từ chối đi bưu điện: 不去 (Không đi)."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王兰：谢谢你！ 李军：_______", "options": ["谢谢", "谢谢你", "不客气"], "correct": 2, "explanation": "Đáp lại lời Cảm ơn là 不客气 (Không có gì)."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王阿姨：你好！请进！ 李军：_______", "options": ["不去", "不客气", "谢谢您"], "correct": 2, "explanation": "Đáp lại lời mời lịch sự của người lớn: 谢谢您 (Cảm ơn cô/bà)."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 她 _______ 英语", "options": ["叫", "教"], "correct": 1, "explanation": "教 (jiāo) = Dạy. Cô ấy dạy tiếng Anh."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 认识你很 ________", "options": ["贵姓", "高兴"], "correct": 1, "explanation": "认识你很高兴 (Rất vui được quen biết bạn)."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 我回 ________", "options": ["学生", "学校"], "correct": 1, "explanation": "回学校 (huí xuéxiào) = Về trường học."},
        {"category": "grammar", "question": "Chọn từ đúng chỉ ngày '2 tháng 9':", "options": ["9月2号", "2号9月", "6月2号"], "correct": 0, "explanation": "Thời gian xếp từ Lớn ➔ Nhỏ: 9月2号."},
        {"category": "grammar", "question": "Chọn từ đúng chỉ năm '2016':", "options": ["2016年", "2019年", "2076年"], "correct": 0, "explanation": "2016年."},
        {"category": "grammar", "question": "Sắp xếp đoạn hội thoại: (1) 不是,他是我的哥哥 (2) 他是你的弟弟吗？(3) 他忙吗？ (4) 他不太忙。", "options": ["1-2-3-4", "4-3-2-1", "2-1-3-4"], "correct": 2, "explanation": "Thứ tự logic: (2) Hỏi em trai ➔ (1) Trả lời anh trai ➔ (3) Hỏi bận không ➔ (4) Trả lời không bận (2-1-3-4)."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: 李军学习<b>经济</b>。", "options": ["李军学习什么？", "谁学习经济？", "李军是谁？"], "correct": 0, "explanation": "Từ gạch chân chỉ ngành học (经济), dùng '什么' để hỏi."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: <b>王兰</b>是我的同学。", "options": ["这是谁？", "王兰是谁的同学？", "谁是你的同学？"], "correct": 2, "explanation": "Từ gạch chân chỉ người (王兰), thay bằng '谁'."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: 这是<b>王老师的</b>书。", "options": ["这是谁的书？", "这是什么书？", "这是什么？"], "correct": 0, "explanation": "Từ gạch chân chỉ sở hữu (王老师的), thay bằng '谁的'."}
    ]

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def render_audio_btn(text_to_speak, label="🔊 Nghe Audio"):
    clean_text = text_to_speak.replace("'", "\\'")
    html_code = f"""
    <button onclick="speakZH('{clean_text}')" style="
        background-color: #fff1f2;
        color: #e11d48;
        border: 1px solid #fecdd3;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        font-size: 13px;
        display: inline-flex;
        align-items: center;
        gap: 6px;">
        {label}
    </button>
    <script>
    function speakZH(text) {{
        if ('speechSynthesis' in window) {{
            window.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance(text);
            msg.lang = 'zh-CN';
            msg.rate = 0.85;
            window.speechSynthesis.speak(msg);
        }}
    }}
    </script>
    """
    components.html(html_code, height=42)

def render_mobile_hanzi_writer(char_symbol, pinyin_str, meaning_str, compounds_str):
    """
    Generates a Mobile-Optimized HanziWriter Component with an Auto-Height Container (850px)
    and touch-friendly Quiz Mode feedback layout.
    """
    html_code = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <script src="https://cdn.jsdelivr.net/npm/hanzi-writer@3.5/dist/hanzi-writer.min.js"></script>
        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                -webkit-tap-highlight-color: transparent;
            }}
            body {{
                background-color: #f8fafc;
                padding: 10px;
                display: flex;
                flex-direction: column;
                align-items: center;
                width: 100%;
            }}
            .card-header {{
                background: #ffffff;
                width: 100%;
                max-width: 380px;
                padding: 12px 16px;
                border-radius: 12px;
                box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                border: 1px solid #e2e8f0;
                margin-bottom: 12px;
                text-align: center;
            }}
            .char-title {{
                font-size: 24px;
                font-weight: 800;
                color: #0f172a;
            }}
            .char-pinyin {{
                color: #dc2626;
                font-weight: 700;
                font-size: 16px;
            }}
            .char-desc {{
                color: #64748b;
                font-size: 13px;
                margin-top: 4px;
            }}
            
            /* Rice Grid Canvas Container */
            .canvas-wrapper {{
                position: relative;
                width: 270px;
                height: 270px;
                background-color: #ffffff;
                border: 2px solid #ef4444;
                border-radius: 16px;
                box-shadow: 0 4px 12px rgba(239, 68, 68, 0.12);
                margin-bottom: 12px;
                overflow: hidden;
            }}
            /* Mǐzìgé (米字格) Grid Lines */
            .grid-line {{
                position: absolute;
                pointer-events: none;
            }}
            .line-h {{
                top: 50%; left: 0; width: 100%; height: 1px;
                border-top: 1px dashed #fca5a5;
            }}
            .line-v {{
                left: 50%; top: 0; height: 100%; width: 1px;
                border-left: 1px dashed #fca5a5;
            }}
            .line-d1 {{
                top: 0; left: 0; width: 100%; height: 100%;
                background: linear-gradient(to bottom right, transparent calc(50% - 1px), #fee2e2, transparent calc(50% + 1px));
            }}
            .line-d2 {{
                top: 0; left: 0; width: 100%; height: 100%;
                background: linear-gradient(to bottom left, transparent calc(50% - 1px), #fee2e2, transparent calc(50% + 1px));
            }}
            
            #target-holder {{
                position: absolute;
                top: 0; left: 0; width: 270px; height: 270px;
                z-index: 10;
            }}
            
            /* Status Feedback Area */
            .status-box {{
                width: 100%;
                max-width: 380px;
                padding: 10px;
                border-radius: 10px;
                background-color: #f1f5f9;
                text-align: center;
                font-size: 14px;
                font-weight: 700;
                color: #334155;
                margin-bottom: 12px;
                min-height: 42px;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            /* Mobile-Optimized Button Grid */
            .btn-grid {{
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 8px;
                width: 100%;
                max-width: 380px;
                margin-bottom: 12px;
            }}
            .btn {{
                padding: 10px;
                border-radius: 10px;
                border: none;
                font-weight: 700;
                font-size: 13px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 6px;
                transition: transform 0.1s;
            }}
            .btn:active {{
                transform: scale(0.96);
            }}
            .btn-animate {{ background: #dc2626; color: white; }}
            .btn-quiz {{ background: #2563eb; color: white; }}
            .btn-toggle {{ background: #e2e8f0; color: #1e293b; }}
            .btn-audio {{ background: #fef3c7; color: #b45309; border: 1px solid #fde68a; }}

            /* Freehand Canvas Elements */
            #freehand-canvas {{
                position: absolute;
                top: 0; left: 0; width: 270px; height: 270px;
                z-index: 20;
                touch-action: none;
            }}
            .compound-card {{
                background: #f8fafc;
                border: 1px solid #cbd5e1;
                border-radius: 10px;
                padding: 10px 14px;
                width: 100%;
                max-width: 380px;
                font-size: 13px;
                color: #1e293b;
            }}
        </style>
    </head>
    <body>

        <!-- Card Info -->
        <div class="card-header">
            <div class="char-title">{char_symbol} <span class="char-pinyin">({pinyin_str})</span></div>
            <div class="char-desc">Ý nghĩa: <b>{meaning_str}</b></div>
        </div>

        <!-- Rice Grid Container -->
        <div class="canvas-wrapper">
            <div class="grid-line line-h"></div>
            <div class="grid-line line-v"></div>
            <div class="grid-line line-d1"></div>
            <div class="grid-line line-d2"></div>
            <div id="target-holder"></div>
            <canvas id="freehand-canvas" width="270" height="270" style="display:none;"></canvas>
        </div>

        <!-- Quiz Status Feedback -->
        <div id="status-msg" class="status-box">
            👉 Nhấn "✍️ Tập Viết Nét" để tự tay tô từng nét
        </div>

        <!-- Action Control Buttons -->
        <div class="btn-grid">
            <button class="btn btn-animate" onclick="runAnimation()">▶️ Xem Nét Vẽ</button>
            <button class="btn btn-quiz" onclick="startQuizMode()">✍️ Tập Viết Nét</button>
            <button class="btn btn-toggle" onclick="toggleOutline()">👁️ Ẩn/Hiện Chữ</button>
            <button class="btn btn-audio" onclick="playAudio('{char_symbol}')">🔊 Phát Âm</button>
        </div>

        <!-- Sample Compounds -->
        <div class="compound-card">
            📚 <b>Từ ghép chứa chữ này:</b><br>
            <span style="color: #dc2626; font-weight: 600;">{compounds_str}</span>
        </div>

        <script>
            var charTarget = "{char_symbol}";
            var writer = null;
            var isOutlineVisible = true;

            // Initialize HanziWriter Engine
            function initWriter() {{
                document.getElementById('target-holder').innerHTML = '';
                writer = HanziWriter.create('target-holder', charTarget, {{
                    width: 270,
                    height: 270,
                    padding: 15,
                    showOutline: true,
                    showCharacter: true,
                    strokeAnimationSpeed: 1.2,
                    delayBetweenStrokes: 180,
                    strokeColor: '#0f172a',
                    outlineColor: '#cbd5e1',
                    drawingWidth: 22,
                    showHintAfterMisses: 1,
                    highlightColor: '#ef4444'
                }});
            }}

            function runAnimation() {{
                if(!writer) initWriter();
                document.getElementById('status-msg').innerHTML = "🎬 Đang phát hoạt ảnh bút thuận...";
                document.getElementById('status-msg').style.color = "#0284c7";
                writer.animateCharacter({{
                    onComplete: function() {{
                        document.getElementById('status-msg').innerHTML = "✅ Phát xong! Bạn có thể nhấn Tập viết nét.";
                        document.getElementById('status-msg').style.color = "#16a34a";
                    }}
                }});
            }}

            function startQuizMode() {{
                if(!writer) initWriter();
                document.getElementById('status-msg').innerHTML = "✍️ Hãy dùng ngón tay/chuột tô nét đầu tiên...";
                document.getElementById('status-msg').style.color = "#2563eb";
                
                writer.quiz({{
                    onMistake: function(strokeData) {{
                        document.getElementById('status-msg').innerHTML = "❌ Sai nét rồi! Hãy thử lại nhé.";
                        document.getElementById('status-msg').style.color = "#dc2626";
                    }},
                    onCorrectStroke: function(strokeData) {{
                        var curr = strokeData.strokeNum + 1;
                        var total = strokeData.totalStrokes;
                        document.getElementById('status-msg').innerHTML = "✅ Giỏi lắm! Đúng nét " + curr + "/" + total;
                        document.getElementById('status-msg').style.color = "#16a34a";
                    }},
                    onComplete: function(summary) {{
                        document.getElementById('status-msg').innerHTML = "🎉 Tuyệt vời! Bạn đã viết hoàn thành chữ này!";
                        document.getElementById('status-msg').style.color = "#2563eb";
                    }}
                }});
            }}

            function toggleOutline() {{
                if(!writer) initWriter();
                isOutlineVisible = !isOutlineVisible;
                if(isOutlineVisible) {{
                    writer.showOutline();
                }} else {{
                    writer.hideOutline();
                }}
            }}

            function playAudio(text) {{
                if ('speechSynthesis' in window) {{
                    window.speechSynthesis.cancel();
                    var msg = new SpeechSynthesisUtterance(text);
                    msg.lang = 'zh-CN';
                    msg.rate = 0.85;
                    window.speechSynthesis.speak(msg);
                }}
            }}

            window.onload = function() {{
                initWriter();
            }};
        </script>
    </body>
    </html>
    """
    # High height (820px) ensures full mobile visibility without clipping controls
    components.html(html_code, height=820, scrolling=False)


# -----------------------------------------------------------------------------
# MAIN APP NAVIGATION & INTERFACE
# -----------------------------------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>🇨🇳 App Học Tiếng Trung Ehou Pro</h1>
    <p>Tối ưu giao diện Mobile & Laptop - Tập viết bút thuận, cẩm nang 7 bài & trắc nghiệm 53 câu</p>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "📌 Lựa chọn chức năng:",
    [
        "✍️ Tập Viết Bút Thuận (HanziWriter)", 
        "📖 Cẩm Nang Lý Thuyết (Bài 1-7)", 
        "🗂️ Tổng Ôn Từ Vựng Nhanh",
        "📝 Luyện Tập Trắc Nghiệm (53 câu)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("📱 **Mẹo Mobile:**\nNếu đang mở trên điện thoại, hãy xoay ngang màn hình hoặc nhấn nút **✍️ Tập Viết Nét** để tô chữ bằng ngón tay!")

# -----------------------------------------------------------------------------
# TAB 1: HANZIWRITER WRITING PRACTICE
# -----------------------------------------------------------------------------
if menu == "✍️ Tập Viết Bút Thuận (HanziWriter)":
    st.header("✍️ Luyện Viết Bút Thuận Chữ Hán")
    
    vocab_dict = get_writing_vocab()
    lesson_keys = list(vocab_dict.keys())
    
    col_sel1, col_sel2 = st.columns([1, 1])
    
    with col_sel1:
        selected_lesson = st.selectbox("📚 Chọn bài học:", lesson_keys)
        
    char_list = vocab_dict[selected_lesson]
    char_options = [f"{item['char']} - {item['pinyin']} ({item['meaning']})" for item in char_list]
    
    with col_sel2:
        selected_char_str = st.selectbox("🔤 Chọn từ luyện viết:", char_options)
        
    # Custom Character Search Option
    custom_char = st.text_input("🔍 Hoặc gõ chữ Hán bất kỳ để tập viết:", placeholder="Ví dụ: 学, 汉, 您, 喜...")
    
    # Determine target character
    if custom_char.strip():
        target_char = custom_char.strip()[0]
        target_pinyin = "Tự chọn"
        target_meaning = "Chữ Hán tùy chỉnh"
        target_compounds = f"{target_char}"
    else:
        char_idx = char_options.index(selected_char_str)
        char_info = char_list[char_idx]
        target_char = char_info["char"]
        target_pinyin = char_info["pinyin"]
        target_meaning = char_info["meaning"]
        target_compounds = char_info["compounds"]

    # Render Mobile-Friendly HanziWriter Component
    render_mobile_hanzi_writer(target_char, target_pinyin, target_meaning, target_compounds)

# -----------------------------------------------------------------------------
# TAB 2: COMPREHENSIVE THEORY (LESSONS 1 - 7)
# -----------------------------------------------------------------------------
elif menu == "📖 Cẩm Nang Lý Thuyết (Bài 1-7)":
    st.header("📖 Cẩm Nang Lý Thuyết Chuẩn Ehou (Bài 1 - 7)")
    
    lesson_tab1, lesson_tab2, lesson_tab3, lesson_tab4, lesson_tab5, lesson_tab6, lesson_tab7 = st.tabs([
        "Bài 1", "Bài 2", "Bài 3", "Bài 4", "Bài 5", "Bài 6", "Bài 7"
    ])
    
    with lesson_tab1:
        st.subheader("第一课：你好 (Xin Chào)")
        st.markdown("""
        **1. Từ vựng:**
        - 你 (nǐ): Bạn, anh, chị.
        - 好 (hǎo): Tốt, đẹp, hay.
        - 妈妈 (māma): Mẹ | 爸爸 (bàba): Bố | 弟弟 (dìdi): Em trai | 妹妹 (mèimei): Em gái.
        - 女 (nǚ): Nữ | 大 (dà): To, lớn.
        
        **2. Ngữ âm & Thanh điệu:**
        - Thanh mẫu: `b, p, m, f, d, t, n, l`.
        - Vận mẫu: `a, o, e, i, u, ü, ai, ei, ao, ou`.
        - 4 Thanh điệu chính: Thanh 1 (55 - mā), Thanh 2 (35 - má), Thanh 3 (214 - mǎ), Thanh 4 (51 - mà).
        
        **3. Biến điệu 2 thanh 3:**
        - Khi 2 thanh 3 đi liền nhau: Thanh 3 đầu tiên biến thành thanh 2.
        - Ví dụ: `nǐ + hǎo ➔ ní hǎo` (你好).
        """)
        
    with lesson_tab2:
        st.subheader("第二课：汉语难吗 (Tiếng Hán Khó Không)")
        st.markdown("""
        **1. Từ vựng:**
        - 哥哥 (gēge): Anh trai | 忙 (máng): Bận | 很 (hěn): Rất.
        - 汉语 (Hànyǔ): Tiếng Hán | 难 (nán): Khó | 太 (tài): Quá, lắm.
        - 不 (bù): Không | 吗 (ma): Trợ từ nghi vấn (không?).
        
        **2. Quy tắc Biến điệu của 不 (bù):**
        - Đứng trước thanh 1, 2, 3: Giữ nguyên thanh 4 `bù` (VD: *bù nán*, *bù hǎo*).
        - Đứng trước thanh 4: Biến thành thanh 2 `bú` (VD: *bú tài*, *bú dà*).
        """)

    with lesson_tab3:
        st.subheader("第三课：谢谢您 (Cảm Ơn Ngài)")
        st.markdown("""
        **1. Từ vựng & Mẫu câu:**
        - 您 (nín): Ngài (Dùng xưng hô lịch sự với người lớn).
        - 请进 (qǐng jìn): Mời vào | 谢谢 (xièxie): Cảm ơn | 不客气 (bú kèqi): Không có gì.
        - 去 (qù): Đi | 银行 (yínháng): Ngân hàng | 取钱 (qǔ qián): Rút tiền | 邮局 (yóujú): Bưu điện.
        
        **2. Quy tắc viết Pinyin nhóm âm mặt lưỡi (j, q, x):**
        - Khi `ü, üe, üan, ün` đi với `j, q, x`, dấu 2 chấm trên đầu `ü` bị **BỎ ĐI**:
        - `j + ü ➔ ju`, `q + üe ➔ que`, `x + üan ➔ xuan`.
        """)

    with lesson_tab4:
        st.subheader("第四课：你叫什么名字 (Bạn Tên Là Gì)")
        st.markdown("""
        **1. Từ vựng:**
        - 我 (wǒ): Tôi | 叫 (jiào): Tên là | 什么 (shénme): Cái gì | 名字 (míngzi): Tên.
        - 认识 (rènshi): Quen biết | 高兴 (gāoxìng): Vui vẻ.
        - 老师 (lǎoshī): Thầy/Cô giáo | 朋友 (péngyou): Bạn bè.
        
        **2. Phân biệt vần "-i" sau nhóm z, c, s và zh, ch, sh, r:**
        - Vận mẫu `-i` đi sau `z, c, s` hoặc `zh, ch, sh, r` đọc thành âm lưỡi **"ư"** (VD: *zi, ci, si, zhi, chi, shi, ri*).
        """)

    with lesson_tab5:
        st.subheader("第五课：你去哪儿 (Bạn Đi Đâu)")
        st.markdown("""
        **1. Mẫu câu trọng tâm:**
        - 你去哪儿？(Nǐ qù nǎr?) - Bạn đi đâu?
        - 你是哪国人？(Nǐ shì nǎ guó rén?) - Bạn là người nước nào?
        - 我是越南人。(Wǒ shì Yuènán rén.) - Tôi là người Việt Nam.
        """)

    with lesson_tab6:
        st.subheader("第六课：这是我的书 (Đây Là Sách Của Tôi)")
        st.markdown("""
        **1. Đại từ chỉ định 这 / 那:**
        - 这 (zhè): Đây, này (Chỉ vật ở gần).
        - 那 (nà): Kia, đó (Chỉ vật ở xa).
        
        **2. Trợ từ kết cấu 的 (de):**
        - Cấu trúc: `Định ngữ + 的 + Trung tâm ngữ`.
        - Biểu thị quan hệ sở hữu: 我的书 (Sách của tôi), 张老师的词典 (Từ điển của thầy Trương).
        """)

    with lesson_tab7:
        st.subheader("第七课：今天星期几 (Hôm Nay Thứ Mấy)")
        st.markdown("""
        **1. Nói Thứ trong tuần:**
        - 星期一 (Thứ 2), 星期二 (Thứ 3), ..., 星期六 (Thứ 7), 星期天/日 (Chủ nhật).
        
        **2. Thời gian (Năm - Tháng - Ngày):**
        - Quy tắc từ Lớn ➔ Nhỏ: `2026年 9月 2号`.
        
        **3. Hỏi tuổi:**
        - Trẻ em < 10 tuổi: 你今年几岁？(Nǐ jīnnián jǐ suì?)
        - Người lớn chung: 你今年多大？(Nǐ jīnnián duōdà?)
        """)

# -----------------------------------------------------------------------------
# TAB 3: VOCABULARY LIST (TỔNG ÔN TỪ VỰNG)
# -----------------------------------------------------------------------------
elif menu == "🗂️ Tổng Ôn Từ Vựng Nhanh":
    st.header("🗂️ Tổng Ôn Danh Sách Từ Vựng Nhanh")
    st.markdown("Bảng tổng hợp toàn bộ từ vựng trọng tâm. Bạn có thể tìm kiếm và bấm vào nút loa để nghe phát âm ngay lập tức!")

    vocab_dict = get_writing_vocab()
    
    search_query = st.text_input("🔍 Tìm kiếm từ vựng (Nhập Hán tự, Pinyin hoặc Nghĩa):", "").strip().lower()
    
    # Generate HTML Table for lightning-fast rendering of audio buttons
    html_table = """
    <style>
    .vocab-table { width: 100%; border-collapse: collapse; margin-top: 1rem; font-family: 'Plus Jakarta Sans', sans-serif; }
    .vocab-table th, .vocab-table td { border: 1px solid #e2e8f0; padding: 12px; text-align: left; }
    .vocab-table th { background-color: #f8fafc; font-weight: bold; color: #0f172a; font-size: 14px; }
    .vocab-table tr:nth-child(even) { background-color: #f8fafc; }
    .vocab-table tr:hover { background-color: #f1f5f9; }
    .hanzi-text { font-size: 1.5rem; font-weight: bold; color: #dc2626; }
    .pinyin-text { font-weight: 600; color: #475569; }
    .btn-audio { background-color: #fee2e2; color: #e11d48; border: 1px solid #fecdd3; padding: 6px 10px; border-radius: 6px; cursor: pointer; font-size: 13px; font-weight: 600; transition: background-color 0.2s;}
    .btn-audio:hover { background-color: #fecdd3; }
    </style>
    <table class="vocab-table">
        <thead>
            <tr>
                <th>Bài</th>
                <th>Chữ Hán</th>
                <th>Pinyin</th>
                <th>Ý nghĩa</th>
                <th>Ví dụ / Từ ghép</th>
                <th>Phát âm</th>
            </tr>
        </thead>
        <tbody>
    """
    
    count = 0
    for lesson, words in vocab_dict.items():
        lesson_short = lesson.split(':')[0]
        for w in words:
            # Filtering logic
            if (search_query in w['char'].lower() or 
                search_query in w['pinyin'].lower() or 
                search_query in w['meaning'].lower()):
                
                clean_pinyin = w['char'].replace("'", "\\'") 
                html_table += f"""
                <tr>
                    <td><span style="font-size: 12px; color: #64748b; font-weight: bold;">{lesson_short}</span></td>
                    <td class="hanzi-text">{w['char']}</td>
                    <td class="pinyin-text">{w['pinyin']}</td>
                    <td>{w['meaning']}</td>
                    <td style="font-size: 13px;">{w['compounds']}</td>
                    <td><button class="btn-audio" onclick="speakZH('{clean_pinyin}')">🔊 Nghe</button></td>
                </tr>
                """
                count += 1

    html_table += """
        </tbody>
    </table>
    <script>
    function speakZH(text) {
        if ('speechSynthesis' in window) {
            window.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance(text);
            msg.lang = 'zh-CN';
            msg.rate = 0.85;
            window.speechSynthesis.speak(msg);
        }
    }
    </script>
    """
    
    if count > 0:
        st.success(f"Đã tìm thấy **{count}** từ vựng.")
        components.html(html_table, height=700, scrolling=True)
    else:
        st.warning("Không tìm thấy từ vựng nào khớp với từ khóa của bạn.")

# -----------------------------------------------------------------------------
# TAB 4: QUIZ PRACTICE (53 QUESTIONS)
# -----------------------------------------------------------------------------
elif menu == "📝 Luyện Tập Trắc Nghiệm (53 câu)":
    st.header("📝 Luyện Tập Trắc Nghiệm Tương Tác")
    
    quiz_questions = get_quiz_questions()
    
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}
        
    filter_cat = st.selectbox(
        "🎯 Lọc câu hỏi theo chủ đề:",
        ["Tất cả (Full 53 câu)", "File Nghe Audio", "Bộ Thủ & Chữ Hán", "Ngữ Pháp & Giao Tiếp"]
    )
    
    cat_map = {
        "Tất cả (Full 53 câu)": "all",
        "File Nghe Audio": "audio",
        "Bộ Thủ & Chữ Hán": "radical",
        "Ngữ Pháp & Giao Tiếp": "grammar"
    }
    
    selected_category = cat_map[filter_cat]
    
    filtered_questions = [
        q for q in quiz_questions 
        if selected_category == "all" or q["category"] == selected_category
    ]
    
    # Calculate score
    correct_count = 0
    total_answered = 0
    
    for idx, q in enumerate(filtered_questions):
        # We need the global index to track answers correctly across filters
        global_idx = quiz_questions.index(q)
        if global_idx in st.session_state.user_answers:
            total_answered += 1
            if st.session_state.user_answers[global_idx] == q["correct"]:
                correct_count += 1

    # Score Metrics Header
    m1, m2, m3 = st.columns(3)
    m1.metric("Tổng câu hỏi", len(filtered_questions))
    m2.metric("Đã làm", total_answered)
    m3.metric("Số câu đúng", f"{correct_count} / {len(filtered_questions)}")
    
    st.markdown("---")
    
    # Render Question Cards
    for idx, q in enumerate(filtered_questions):
        global_idx = quiz_questions.index(q)
        st.markdown(f"#### Câu {idx + 1}: {q['question']}")
        
        # Render audio button if audio text exists
        if "audioText" in q and q["audioText"]:
            render_audio_btn(q["audioText"], label=f"🔊 Nghe File Audio ('{q['audioText']}')")
            
        selected_option = st.radio(
            "Chọn đáp án của bạn:",
            options=q["options"],
            key=f"q_{global_idx}",
            index=st.session_state.user_answers.get(global_idx)
        )
        
        if selected_option is not None:
            selected_idx = q["options"].index(selected_option)
            st.session_state.user_answers[global_idx] = selected_idx
            
            if selected_idx == q["correct"]:
                st.success("✅ Chính xác!")
            else:
                st.error(f"❌ Chưa đúng! Đáp án đúng là: **{q['options'][q['correct']]}**")
                
            st.info(f"💡 **Giải thích:** {q['explanation']}")
            
        st.markdown("---")

    # Reset Quiz Button
    if st.button("🔄 Làm lại tất cả bài thi"):
        st.session_state.user_answers = {}
        st.rerun()
