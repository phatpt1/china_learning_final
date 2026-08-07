import streamlit as st
import streamlit.components.v1 as components
import json

# Page Configuration
st.set_page_config(
    page_title="App Tiếng Trung 1 Ehou Pro - Tập Viết & Ôn Thi",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #dc2626 0%, #991b1b 100%);
        padding: 1.8rem 2rem;
        border-radius: 20px;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px -3px rgba(220, 38, 38, 0.3);
    }
    
    .main-header h1 {
        color: #ffffff !important;
        font-weight: 800;
        margin-bottom: 0.3rem;
        font-size: 2rem;
    }
    
    .main-header p {
        color: #fca5a5 !important;
        font-size: 0.95rem;
        margin-bottom: 0;
    }
    
    .stButton>button {
        border-radius: 12px;
        font-weight: 700;
        transition: all 0.2s ease-in-out;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Database of Ehou Chinese 1 Characters categorized by lessons
EHOU_CHAR_DATABASE = {
    1: [
        {"char": "你", "pinyin": "nǐ", "meaning": "Bạn, anh, chị (Ngôi 2)", "compounds": ["你好 (nǐ hǎo)", "你们 (nǐ men)"]},
        {"char": "好", "pinyin": "hǎo", "meaning": "Tốt, khỏe, hay", "compounds": ["你好 (nǐ hǎo)", "好人 (hǎo rén)", "很好 (hěn hǎo)"]},
        {"char": "妈", "pinyin": "mā", "meaning": "Mẹ", "compounds": ["妈妈 (mā ma)"]},
        {"char": "爸", "pinyin": "bà", "meaning": "Bố, ba", "compounds": ["爸爸 (bà ba)"]},
        {"char": "哥", "pinyin": "gē", "meaning": "Anh trai", "compounds": ["哥哥 (gē ge)"]},
        {"char": "弟", "pinyin": "dì", "meaning": "Em trai", "compounds": ["弟弟 (dì di)"]},
        {"char": "妹", "pinyin": "mèi", "meaning": "Em gái", "compounds": ["妹妹 (mèi mei)"]},
        {"char": "女", "pinyin": "nǚ", "meaning": "Nữ, con gái", "compounds": ["女儿 (nǚ ér)", "女人 (nǚ rén)"]},
        {"char": "大", "pinyin": "dà", "meaning": "To, lớn", "compounds": ["大学 (dà xué)", "大人 (dà rén)"]}
    ],
    2: [
        {"char": "忙", "pinyin": "máng", "meaning": "Bận rộn", "compounds": ["很忙 (hěn máng)", "不忙 (bù máng)"]},
        {"char": "很", "pinyin": "hěn", "meaning": "Rất", "compounds": ["很好 (hěn hǎo)", "很忙 (hěn máng)", "很难 (hěn nán)"]},
        {"char": "他", "pinyin": "tā", "meaning": "Anh ấy, ông ấy", "compounds": ["他们 (tā men)"]},
        {"char": "她", "pinyin": "tā", "meaning": "Cô ấy, bà ấy", "compounds": ["她们 (tā men)"]},
        {"char": "汉", "pinyin": "hàn", "meaning": "Hán (Dân tộc, ngôn ngữ)", "compounds": ["汉语 (hàn yǔ)", "汉字 (hàn zì)"]},
        {"char": "语", "pinyin": "yǔ", "meaning": "Ngôn ngữ", "compounds": ["汉语 (hàn yǔ)", "英语 (yīng yǔ)", "越南语 (yuè nán yǔ)"]},
        {"char": "难", "pinyin": "nán", "meaning": "Khó", "compounds": ["很难 (hěn nán)", "不难 (bù nán)"]},
        {"char": "不", "pinyin": "bù", "meaning": "Không, chẳng", "compounds": ["不好 (bù hǎo)", "不大 (bú dà)", "不去 (bú qù)"]},
        {"char": "太", "pinyin": "tài", "meaning": "Quá, lắm", "compounds": ["不太 (bú tài)", "太太 (tài tai)"]}
    ],
    3: [
        {"char": "您", "pinyin": "nín", "meaning": "Ngài, ông/bà (Kính ngữ)", "compounds": ["您好 (nín hǎo)", "谢谢您 (xiè xie nín)"]},
        {"char": "请", "pinyin": "qǐng", "meaning": "Mời, xin", "compounds": ["请进 (qǐng jìn)", "请问 (qǐng wèn)"]},
        {"char": "进", "pinyin": "jìn", "meaning": "Vào, tiến", "compounds": ["请进 (qǐng jìn)"]},
        {"char": "谢", "pinyin": "xiè", "meaning": "Cảm ơn", "compounds": ["谢谢 (xiè xie)"]},
        {"char": "去", "pinyin": "qù", "meaning": "Đi", "compounds": ["去银行 (qù yín háng)", "去邮局 (qù yóu jú)"]},
        {"char": "银", "pinyin": "yín", "meaning": "Ngân, bạc", "compounds": ["银行 (yín háng)"]},
        {"char": "行", "pinyin": "háng", "meaning": "Hàng, tiệm / xíng (được)", "compounds": ["银行 (yín háng)"]},
        {"char": "取", "pinyin": "qǔ", "meaning": "Rút, lấy", "compounds": ["取钱 (qǔ qián)"]},
        {"char": "钱", "pinyin": "qián", "meaning": "Tiền", "compounds": ["取钱 (qǔ qián)", "多少钱 (duō shǎo qián)"]},
        {"char": "邮", "pinyin": "yóu", "meaning": "Bưu điện, thư", "compounds": ["邮局 (yóu jú)"]},
        {"char": "局", "pinyin": "jú", "meaning": "Cục, cơ quan", "compounds": ["邮局 (yóu jú)"]},
        {"char": "信", "pinyin": "xìn", "meaning": "Thư, tin tưởng", "compounds": ["寄信 (jì xìn)"]},
        {"char": "姐", "pinyin": "jiě", "meaning": "Chị gái", "compounds": ["姐姐 (jiě jie)"]},
        {"char": "明", "pinyin": "míng", "meaning": "Sáng, minh bạch", "compounds": ["明天 (míng tiān)", "明白 (míng bai)"]},
        {"char": "学", "pinyin": "xué", "meaning": "Học", "compounds": ["学习 (xué xí)", "学校 (xué xiào)", "学生 (xué sheng)"]},
        {"char": "校", "pinyin": "xiào", "meaning": "Trường học", "compounds": ["学校 (xué xiào)"]},
        {"char": "见", "pinyin": "jiàn", "meaning": "Gặp, thấy", "compounds": ["再见 (zài jiàn)", "明天见 (míng tiān jiàn)"]}
    ],
    4: [
        {"char": "我", "pinyin": "wǒ", "meaning": "Tôi, ta (Ngôi 1)", "compounds": ["我们 (wǒ men)", "我家 (wǒ jiā)"]},
        {"char": "叫", "pinyin": "jiào", "meaning": "Gọi, tên là", "compounds": ["叫什么 (jiào shén me)"]},
        {"char": "什", "pinyin": "shén", "meaning": "Cái gì", "compounds": ["什么 (shén me)"]},
        {"char": "么", "pinyin": "me", "meaning": "Trợ từ nghi vấn", "compounds": ["什么 (shén me)"]},
        {"char": "名", "pinyin": "míng", "meaning": "Tên, danh", "compounds": ["名字 (míng zi)", "有名 (yǒu míng)"]},
        {"char": "字", "pinyin": "zì", "meaning": "Chữ", "compounds": ["名字 (míng zi)", "汉字 (hàn zì)"]},
        {"char": "认", "pinyin": "rèn", "meaning": "Nhận, quen", "compounds": ["认识 (rèn shi)"]},
        {"char": "识", "pinyin": "shi", "meaning": "Biết, thức", "compounds": ["认识 (rèn shi)"]},
        {"char": "高", "pinyin": "gāo", "meaning": "Cao", "compounds": ["高兴 (gāo xìng)"]},
        {"char": "兴", "pinyin": "xìng", "meaning": "Hưng phấn, vui", "compounds": ["高兴 (gāo xìng)"]},
        {"char": "也", "pinyin": "yě", "meaning": "Cũng", "compounds": ["也是 (yě shì)"]},
        {"char": "是", "pinyin": "shì", "meaning": "Là, đúng", "compounds": ["是不是 (shì bú shì)"]},
        {"char": "朋", "pinyin": "péng", "meaning": "Bạn", "compounds": ["朋友 (péng you)"]},
        {"char": "友", "pinyin": "yǒu", "meaning": "Hữu, bạn", "compounds": ["朋友 (péng you)"]},
        {"char": "老", "pinyin": "lǎo", "meaning": "Lão, già, cũ", "compounds": ["老师 (lǎo shī)"]},
        {"char": "师", "pinyin": "shī", "meaning": "Thầy, sư", "compounds": ["老师 (lǎo shī)"]},
        {"char": "教", "pinyin": "jiāo", "meaning": "Dạy học", "compounds": ["教英语 (jiāo yīng yǔ)"]}
    ],
    5: [
        {"char": "哪", "pinyin": "nǎ / nǎr", "meaning": "Nào, ở đâu", "compounds": ["哪儿 (nǎr)", "哪国人 (nǎ guó rén)"]},
        {"char": "看", "pinyin": "kàn", "meaning": "Xem, nhìn, thăm", "compounds": ["看书 (kàn shū)", "看朋友 (kàn péng you)"]},
        {"char": "回", "pinyin": "huí", "meaning": "Về, trở lại", "compounds": ["回家 (huí jiā)", "回学校 (huí xué xiào)"]},
        {"char": "家", "pinyin": "jiā", "meaning": "Nhà, gia đình", "compounds": ["回家 (huí jiā)", "大家 (dà jiā)"]},
        {"char": "儿", "pinyin": "ér", "meaning": "Nhi, con", "compounds": ["儿子 (ér zi)", "女儿 (nǚ ér)"]},
        {"char": "再", "pinyin": "zài", "meaning": "Lại, lần nữa", "compounds": ["再见 (zài jiàn)"]},
        {"char": "问", "pinyin": "wèn", "meaning": "Hỏi", "compounds": ["请问 (qǐng wèn)"]},
        {"char": "国", "pinyin": "guó", "meaning": "Nước, quốc gia", "compounds": ["中国 (zhōng guó)", "美国 (měi guó)"]},
        {"char": "人", "pinyin": "rén", "meaning": "Người", "compounds": ["中国人 (zhōng guó rén)", "好人 (hǎo rén)"]}
    ],
    6: [
        {"char": "习", "pinyin": "xí", "meaning": "Tập, luyện", "compounds": ["学习 (xué xí)", "练习 (liàn xí)"]},
        {"char": "和", "pinyin": "hé", "meaning": "Và, với", "compounds": ["我和你 (wǒ hé nǐ)"]},
        {"char": "的", "pinyin": "de", "meaning": "Của (Trợ từ sở hữu)", "compounds": ["我的 (wǒ de)", "老师的 (lǎo shī de)"]},
        {"char": "这", "pinyin": "zhè", "meaning": "Đây, này", "compounds": ["这是 (zhè shì)", "这个人 (zhè ge rén)"]},
        {"char": "那", "pinyin": "nà", "meaning": "Kia, đó", "compounds": ["那是 (nà shì)"]},
        {"char": "谁", "pinyin": "shuí / shéi", "meaning": "Ai", "compounds": ["是谁 (shì shéi)", "谁的书 (shéi de shū)"]},
        {"char": "书", "pinyin": "shū", "meaning": "Sách", "compounds": ["看书 (kàn shū)", "中文书 (zhōng wén shū)"]},
        {"char": "词", "pinyin": "cí", "meaning": "Từ, lời", "compounds": ["词典 (cí diǎn)"]},
        {"char": "典", "pinyin": "diǎn", "meaning": "Điển, sách chuẩn", "compounds": ["词典 (cí diǎn)"]}
    ],
    7: [
        {"char": "今", "pinyin": "jīn", "meaning": "Nay, hiện tại", "compounds": ["今天 (jīn tiān)", "今年 (jīn nián)"]},
        {"char": "天", "pinyin": "tiān", "meaning": "Trời, ngày", "compounds": ["今天 (jīn tiān)", "明天 (míng tiān)"]},
        {"char": "星", "pinyin": "xīng", "meaning": "Sao, tinh", "compounds": ["星期 (xīng qī)"]},
        {"char": "期", "pinyin": "qī", "meaning": "Kỳ, thời hạn", "compounds": ["星期 (xīng qī)"]},
        {"char": "昨", "pinyin": "zuó", "meaning": "Hôm qua", "compounds": ["昨天 (zuó tiān)"]},
        {"char": "年", "pinyin": "nián", "meaning": "Năm", "compounds": ["今年 (jīn nián)", "2016年"]},
        {"char": "月", "pinyin": "yuè", "meaning": "Tháng, mặt trăng", "compounds": ["九月 (jiǔ yuè)"]},
        {"char": "日", "pinyin": "rì", "meaning": "Ngày, mặt trời", "compounds": ["星期日 (xīng qī rì)"]},
        {"char": "号", "pinyin": "hào", "meaning": "Số, ngày (khẩu ngữ)", "compounds": ["2号 (èr hào)"]},
        {"char": "生", "pinyin": "shēng", "meaning": "Sinh, ra đời", "compounds": ["生日 (shēng rì)", "学生 (xué sheng)"]},
        {"char": "岁", "pinyin": "suì", "meaning": "Tuổi", "compounds": ["二十岁 (èr shí suì)"]},
        {"char": "龙", "pinyin": "lóng", "meaning": "Rồng (Con giáp)", "compounds": ["属龙 (shǔ lóng)"]}
    ]
}

@st.cache_data
def get_quiz_data():
    return [
        {"category": "audio", "audioText": "dà xǐ", "question": "Nghe file audio và chọn phiên âm âm tiết đúng:", "options": ["dáxǐ", "daxi", "dàxǐ"], "correct": 2, "explanation": "File âm thanh đọc: dà xǐ (大喜 - Thanh 4 và Thanh 3)."},
        {"category": "audio", "audioText": "xī xīn", "question": "Nghe file audio và chọn âm tiết đúng:", "options": ["xīxìn", "xīxīn", "xíxīn"], "correct": 1, "explanation": "File âm thanh đọc: xī xīn (细心 - Tỉ mỉ, cẩn thận. Cả 2 âm mang thanh 1)."},
        {"category": "audio", "audioText": "yǎn yuán", "question": "Nghe file audio và chọn âm tiết đúng:", "options": ["yányuân", "yǎnyuán", "yányuán"], "correct": 1, "explanation": "File âm thanh đọc: yǎnyuán (演员 - Diễn viên)."},
        {"category": "audio", "audioText": "xū yào", "question": "Nghe file audio và chọn âm tiết đúng:", "options": ["xīyào", "xūyào", "jīyào"], "correct": 1, "explanation": "File âm thanh đọc: xūyào (需要 - Cần thiết)."},
        {"category": "audio", "audioText": "nǔ lì", "question": "Nghe file audio và chọn âm tiết đúng:", "options": ["nǔlì", "núlì", "nǔlí"], "correct": 0, "explanation": "File âm thanh đọc: nǔlì (努力 - Nỗ lực, cố gắng)."},
        {"category": "audio", "audioText": "ā yí hǎo", "question": "Nghe file audio và chọn câu chào đúng:", "options": ["您好", "阿姨好", "阿姨"], "correct": 1, "explanation": "File âm thanh đọc: ā yí hǎo (阿姨好! - Chào cô/dì!)."},
        {"category": "audio", "audioText": "qù qǔ qián", "question": "Nghe file audio và chọn cụm từ đúng:", "options": ["去邮局", "去取钱", "去银行"], "correct": 1, "explanation": "File âm thanh đọc: qù qǔ qián (去取钱 - Đi rút tiền)."},
        {"category": "audio", "audioText": "qǐng jìn", "question": "Nghe file audio và chọn từ đúng:", "options": ["请讲", "请进", "请教"], "correct": 1, "explanation": "File âm thanh đọc: qǐng jìn (请进 - Mời vào)."},
        {"category": "audio", "audioText": "xiè xie nǐ", "question": "Nghe file audio và chọn từ đúng:", "options": ["谢谢你", "谢谢您", "不客气"], "correct": 0, "explanation": "File âm thanh đọc: xiè xie nǐ (谢谢你 - Cảm ơn bạn)."},
        {"category": "audio", "audioText": "jiě jie", "question": "Nghe file audio và chọn từ đúng:", "options": ["姐姐", "妹妹", "妈妈"], "correct": 0, "explanation": "File âm thanh đọc: jiě jie (姐姐 - Chị gái)."},
        {"category": "audio", "audioText": "zhēn", "question": "Nghe và chọn thanh mẫu đúng của âm tiết được phát:", "options": ["ch", "zh"], "correct": 1, "explanation": "Âm tiết nghe được là 'en' trong 'zhēn', thanh mẫu đúng là: zh."},
        {"category": "audio", "audioText": "rōng", "question": "Nghe âm thanh vần '...ong' và chọn thanh mẫu đúng:", "options": ["s", "r"], "correct": 1, "explanation": "Âm tiết nghe được là 'rōng', thanh mẫu đúng là: r."},
        {"category": "audio", "audioText": "kè fú", "question": "Nghe file audio và chọn thanh điệu đúng cho từ kefu:", "options": ["kefǔ", "kèfǔ", "kèfú"], "correct": 2, "explanation": "Từ đúng là kèfú (克服 - Khắc phục)."},
        {"category": "audio", "audioText": "tū dì", "question": "Nghe file audio và chọn thanh điệu đúng cho từ tudi:", "options": ["tūdì", "túdì", "tūdi"], "correct": 2, "explanation": "Từ đúng là tūdi (徒弟 - Đồ đệ/Học trò)."},
        {"category": "audio", "audioText": "tài guó", "question": "Nghe file audio '... guó' và chọn âm đầu thích hợp:", "options": ["tài", "tái"], "correct": 0, "explanation": "File âm thanh đọc: Tài guó (泰国 - Thái Lan)."},
        {"category": "audio", "audioText": "Hàn yu", "question": "Nghe file audio '... yǔ' và chọn chữ Hán/âm đúng:", "options": ["Hán", "Hàn"], "correct": 1, "explanation": "File âm thanh đọc: Hàn (Hànyǔ - 汉语 Hán ngữ)."},

        # Radical & Hanzi Questions
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 彳", "options": ["Bộ Nhân, 2 nét", "Bộ Tâm, 3 nét", "Bộ Xích, 3 nét"], "correct": 2, "explanation": "Bộ Xích (Nhân kép) gồm 3 nét. Rất hay thi!"},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 亻", "options": ["Bộ Nữ, 2 nét", "Bộ Nhân, 2 nét", "Bộ Ngôn, 2 nét"], "correct": 1, "explanation": "Đây là bộ Nhân (Nhân đứng), gồm 2 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 忄", "options": ["Bộ Nhân, 2 nét", "Bộ Xích, 3 nét", "Bộ Tâm, 3 nét"], "correct": 2, "explanation": "Đây là bộ Tâm đứng, gồm 3 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 氵", "options": ["Bộ Thủy, 3 nét", "Bộ Miên, 2 nét", "Bộ Nữ, 3 nét"], "correct": 0, "explanation": "Đây là bộ Thủy (3 chấm thủy), gồm 3 nét."},
        {"category": "radical", "question": "Nêu tên bộ và số nét của bộ sau: 讠", "options": ["Bộ Ngôn, 3 nét", "Bộ Ngôn, 2 nét", "Bộ Miên, 3 nét"], "correct": 1, "explanation": "Đây là bộ Ngôn (dạng giản thể), gồm 2 nét."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: gege", "options": ["弟弟", "爸爸", "哥哥"], "correct": 2, "explanation": "哥哥 (gēge) = Anh trai."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: didi", "options": ["弟弟", "好", "女"], "correct": 0, "explanation": "弟弟 (dìdi) = Em trai."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 爸爸", "options": ["bàba", "nǚ", "dìdi"], "correct": 0, "explanation": "爸爸 (bàba) = Bố."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 妈妈", "options": ["mèimei", "māma", "bàba"], "correct": 1, "explanation": "妈妈 (māma) = Mẹ."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 你", "options": ["nǐ", "hǎo", "mèimei"], "correct": 0, "explanation": "你 (nǐ) = Bạn, cậu."},
        {"category": "radical", "question": "Ghép từ với phiên âm đúng: 女", "options": ["nǚ", "māma", "dìdi"], "correct": 0, "explanation": "女 (nǚ) = Nữ, con gái."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: hěn", "options": ["恨", "狠", "很"], "correct": 2, "explanation": "很 (hěn) = Rất."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: nán", "options": ["住", "摊", "难"], "correct": 2, "explanation": "难 (nán) = Khó."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: tài", "options": ["大", "太", "夫"], "correct": 1, "explanation": "太 (tài) nghĩa là Quá, lắm."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: dà", "options": ["大", "太"], "correct": 0, "explanation": "大 (dà) = To, lớn."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: bù", "options": ["木", "不", "否"], "correct": 1, "explanation": "不 (bù) = Không."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: wǒ", "options": ["我", "找"], "correct": 0, "explanation": "我 (wǒ) nghĩa là Tôi."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: tā", "options": ["作", "他", "也"], "correct": 1, "explanation": "他 (tā) = Anh ấy."},
        {"category": "radical", "question": "Chọn chữ Hán đúng cho phiên âm: yin", "options": ["钱", "银"], "correct": 1, "explanation": "银 (yín) = Ngân/Bạc."},
        {"category": "radical", "question": "Chọn phiên âm đúng của chữ Hán: 岁", "options": ["sui", "shui", "suì"], "correct": 2, "explanation": "岁 (suì) mang thanh 4, nghĩa là Tuổi."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 您", "options": ["ni", "nín"], "correct": 1, "explanation": "您 (nín) là đại từ xưng hô lịch sự."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 上午", "options": ["shàngwù", "zhōngwù", "xiàwù"], "correct": 0, "explanation": "上午 (shàngwù) = Buổi sáng."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 晚会", "options": ["wǎnhuì", "yǎnhuì", "uǎnhuì"], "correct": 0, "explanation": "晚会 (wǎnhuì) = Dạ hội / Tiệc tối."},
        {"category": "radical", "question": "Chọn phiên âm đúng cho chữ Hán: 多大", "options": ["duōdà", "duódà", "duòdā"], "correct": 0, "explanation": "多大 (duōdà) = Bao nhiêu tuổi."},

        # Grammar Questions
        {"category": "grammar", "question": "Chọn đáp án phiên âm đúng cho cụm từ: 不好 (Không tốt)", "options": ["bù hǎo", "bú máng", "bú hǎo"], "correct": 1, "explanation": "Đáp án chuẩn quy tắc biến điệu."},
        {"category": "grammar", "question": "Chọn đáp án phiên âm đúng cho cụm từ: 不大 (Không to)", "options": ["bù dà", "bú dà"], "correct": 1, "explanation": "Không to = bú dà (Thanh 4 đi với 不 thì 不 biến thành bú)."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王兰：你去邮局寄信吗？ 明玉：_______，去银行取钱。", "options": ["不去", "不好", "去"], "correct": 0, "explanation": "Vế sau đi ngân hàng nên vế trước từ chối đi bưu điện: 不去."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王兰：谢谢你！ 李军：_______", "options": ["谢谢", "谢谢你", "不客气"], "correct": 2, "explanation": "Đáp lại Cảm ơn (谢谢) là 不客气 (Không có gì)."},
        {"category": "grammar", "question": "Điền từ thích hợp: 王阿姨：你好！请进！ 李军：_______", "options": ["不去", "不客气", "谢谢您"], "correct": 2, "explanation": "Đáp lại lời mời lịch sự của người lớn: 谢谢您."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 她 _______ 英语", "options": ["叫", "教"], "correct": 1, "explanation": "教 (jiāo) = Dạy. Cô ấy dạy tiếng Anh."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 认识你很 ________", "options": ["贵姓", "高兴"], "correct": 1, "explanation": "认识你很高兴 (Rất vui được quen biết bạn)."},
        {"category": "grammar", "question": "Điền chữ Hán thích hợp: 我回 ________", "options": ["学生", "学校"], "correct": 1, "explanation": "回学校 (huí xuéxiào) = Về trường học."},
        {"category": "grammar", "question": "Chọn từ đúng chỉ ngày '2 tháng 9':", "options": ["9月2号", "2号9月", "6月2号"], "correct": 0, "explanation": "Thời gian tiếng Trung xếp từ Lớn -> Nhỏ: 9月2号."},
        {"category": "grammar", "question": "Chọn từ đúng chỉ năm '2016':", "options": ["2016年", "2019年", "2076年"], "correct": 0, "explanation": "2016年."},
        {"category": "grammar", "question": "Sắp xếp đoạn hội thoại: (1) 不是, liquidation是我的哥哥 (2) 他是你的弟弟吗？(3) 他忙吗？ (4) 他不太忙。", "options": ["1-2-3-4", "4-3-2-1", "2-1-3-4"], "correct": 2, "explanation": "Thứ tự logic: 2-1-3-4."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: 李军学习<b>经济</b>。", "options": ["李军学习什么？", "谁学习经济？", "李军是谁？"], "correct": 0, "explanation": "Từ gạch chân chỉ ngành học (经济), dùng '什么' để hỏi."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: <b>王兰</b>是我的同学。", "options": ["这也是谁？", "王兰是谁的同学？", "谁是 your/你的同学？"], "correct": 2, "explanation": "Từ gạch chân chỉ người (王兰), thay bằng '谁'."},
        {"category": "grammar", "question": "Chọn câu hỏi cho từ gạch chân: 这是<b>王老师的</b>书。", "options": ["这是谁的书？", "这是什么书？", "这是什么？"], "correct": 0, "explanation": "Từ gạch chân chỉ sở hữu (王老师的), thay bằng '谁的'."}
    ]

def render_hanzi_writer_component(character):
    """Embeds HanziWriter Stroke Order Animation & Quiz Engine into Streamlit Component."""
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/npm/hanzi-writer@3.5/dist/hanzi-writer.min.js"></script>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ font-family: sans-serif; background-color: transparent; margin: 0; padding: 10px; }}
            .mizige-bg {{
                background-color: #fffdfa;
                background-image: 
                    linear-gradient(to right, rgba(239, 68, 68, 0.2) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(239, 68, 68, 0.2) 1px, transparent 1px),
                    linear-gradient(45deg, transparent 49.5%, rgba(239, 68, 68, 0.15) 49.5%, rgba(239, 68, 68, 0.15) 50.5%, transparent 50.5%),
                    linear-gradient(-45deg, transparent 49.5%, rgba(239, 68, 68, 0.15) 49.5%, rgba(239, 68, 68, 0.15) 50.5%, transparent 50.5%);
                background-size: 100% 100%;
                border: 3px solid #ef4444;
                border-radius: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="flex flex-col md:flex-row items-center justify-center gap-6">
            <!-- HanziWriter Target Canvas -->
            <div class="relative">
                <div id="hanzi-target" class="mizige-bg w-[260px] h-[260px] sm:w-[280px] sm:h-[280px] flex items-center justify-center cursor-pointer shadow-md"></div>
                <span class="absolute bottom-2 right-3 text-[10px] font-bold text-red-400 uppercase tracking-widest pointer-events-none">米字格 Mǐzìgé</span>
            </div>
            
            <!-- Controls -->
            <div class="flex flex-col gap-2.5 w-full md:w-56">
                <button onclick="animateChar()" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2.5 px-4 rounded-xl text-sm shadow-sm flex items-center justify-center">
                    ▶️ Xem nét vẽ (Animate)
                </button>
                <button onclick="quizChar()" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-2.5 px-4 rounded-xl text-sm shadow-sm flex items-center justify-center">
                    ✍️ Tập viết theo nét (Quiz)
                </button>
                <button onclick="speakZH('{character}')" class="bg-amber-500 hover:bg-amber-600 text-white font-bold py-2.5 px-4 rounded-xl text-sm shadow-sm flex items-center justify-center">
                    🔊 Nghe phát âm
                </button>
                <div id="feedback" class="p-3 rounded-xl bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-700 text-center mt-1">
                    Bấm nút để bắt đầu luyện tập nét vẽ!
                </div>
            </div>
        </div>

        <script>
            var writer = HanziWriter.create('hanzi-target', '{character}', {{
                width: 260,
                height: 260,
                padding: 15,
                showOutline: true,
                strokeAnimationSpeed: 1.0,
                delayBetweenStrokes: 150,
                strokeColor: '#0f172a',
                outlineColor: '#fca5a5',
                drawingColor: '#dc2626',
                drawingWidth: 16
            }});

            function animateChar() {{
                document.getElementById('feedback').innerText = "Đang chạy hoạt ảnh nét vẽ...";
                writer.animateCharacter({{
                    onComplete: function() {{
                        document.getElementById('feedback').innerText = "Hoàn thành! Hãy thử chế độ 'Tập viết theo nét'.";
                    }}
                }});
            }}

            function quizChar() {{
                document.getElementById('feedback').innerText = "👉 Hãy vẽ nét đầu tiên lên ô Rice Grid...";
                writer.quiz({{
                    onComplete: function() {{
                        document.getElementById('feedback').innerText = "🎉 Xuất sắc! Bạn đã hoàn thành đúng thứ tự bút thuận!";
                        speakZH('{character}');
                    }},
                    onMistake: function() {{
                        document.getElementById('feedback').innerText = "⚠️ Sai nét rồi! Chú ý nét vẽ màu đỏ...";
                    }}
                }});
            }}

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
    </body>
    </html>
    """
    components.html(html_code, height=330)

def render_freehand_canvas_component(reference_char):
    """Embeds HTML5 Canvas for Freehand Brush Practice."""
    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body {{ font-family: sans-serif; background-color: transparent; margin: 0; padding: 10px; }}
            .mizige-bg {{
                background-color: #ffffff;
                background-image: 
                    linear-gradient(to right, rgba(239, 68, 68, 0.15) 1px, transparent 1px),
                    linear-gradient(to bottom, rgba(239, 68, 68, 0.15) 1px, transparent 1px);
                background-size: 100% 100%;
                border: 2px solid #fca5a5;
                border-radius: 16px;
            }}
        </style>
    </head>
    <body>
        <div class="flex flex-col items-center justify-center gap-3">
            <div class="relative">
                <div id="ref-overlay" class="absolute inset-0 flex items-center justify-center text-[180px] font-black text-slate-200 pointer-events-none select-none opacity-30">
                    {reference_char}
                </div>
                <canvas id="freehand" width="280" height="280" class="mizige-bg cursor-crosshair touch-none shadow-sm"></canvas>
            </div>
            
            <div class="flex items-center gap-2">
                <button onclick="setInk('#000000')" class="w-7 h-7 rounded-lg bg-black border-2 border-white shadow-xs"></button>
                <button onclick="setInk('#dc2626')" class="w-7 h-7 rounded-lg bg-red-600 border-2 border-white shadow-xs"></button>
                <button onclick="setInk('#2563eb')" class="w-7 h-7 rounded-lg bg-blue-600 border-2 border-white shadow-xs"></button>
                <button onclick="clearCanvas()" class="bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-3 py-1.5 rounded-lg text-xs border border-slate-200">
                    🗑️ Xóa bảng
                </button>
            </div>
        </div>

        <script>
            var canvas = document.getElementById('freehand');
            var ctx = canvas.getContext('2d');
            var isDrawing = false;
            var inkColor = '#000000';

            canvas.addEventListener('mousedown', start);
            canvas.addEventListener('mousemove', draw);
            canvas.addEventListener('mouseup', stop);
            canvas.addEventListener('mouseleave', stop);

            canvas.addEventListener('touchstart', function(e) {{
                e.preventDefault();
                var touch = e.touches[0];
                canvas.dispatchEvent(new MouseEvent('mousedown', {{ clientX: touch.clientX, clientY: touch.clientY }}));
            }}, {{ passive: false }});

            canvas.addEventListener('touchmove', function(e) {{
                e.preventDefault();
                var touch = e.touches[0];
                canvas.dispatchEvent(new MouseEvent('mousemove', {{ clientX: touch.clientX, clientY: touch.clientY }}));
            }}, {{ passive: false }});

            canvas.addEventListener('touchend', function() {{
                canvas.dispatchEvent(new MouseEvent('mouseup', {{}}));
            }});

            function start(e) {{
                isDrawing = true;
                var rect = canvas.getBoundingClientRect();
                ctx.beginPath();
                ctx.moveTo(e.clientX - rect.left, e.clientY - rect.top);
            }}

            function draw(e) {{
                if (!isDrawing) return;
                var rect = canvas.getBoundingClientRect();
                ctx.lineTo(e.clientX - rect.left, e.clientY - rect.top);
                ctx.strokeStyle = inkColor;
                ctx.lineWidth = 10;
                ctx.lineCap = 'round';
                ctx.lineJoin = 'round';
                ctx.stroke();
            }}

            function stop() {{ isDrawing = false; }}
            function clearCanvas() {{ ctx.clearRect(0, 0, canvas.width, canvas.height); }}
            function setInk(color) {{ inkColor = color; }}
        </script>
    </body>
    </html>
    """
    components.html(html_code, height=360)

def render_audio_button(text_to_speak, label="🔊 Nghe Audio"):
    """Embeds inline Web Speech TTS player."""
    clean_text = text_to_speak.replace("'", "\\'")
    html_code = f"""
    <button onclick="speakZH('{clean_text}')" style="
        background-color: #fff1f2;
        color: #dc2626;
        border: 1px solid #fca5a5;
        padding: 6px 14px;
        border-radius: 10px;
        font-weight: 700;
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
    components.html(html_code, height=45)

st.markdown("""
<div class="main-header">
    <h1>✍️ App Tiếng Trung 1 Pro - Ehou</h1>
    <p>Hệ thống Tích hợp Bút Thuận HanziWriter, Ôn Tập Cẩm Nang & 53 Câu Bài Tập Trắc Nghiệm Audio</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.title("📌 Danh Mục Ứng Dụng")
menu_choice = st.sidebar.radio(
    "Lựa chọn chức năng:",
    ["✍️ Tập Viết Chữ Hán Pro", "📖 Cẩm Nang Lý Thuyết (Bài 1 - 7)", "📝 Luyện Tập Trắc Nghiệm (53 câu)"]
)

if menu_choice == "✍️ Tập Viết Chữ Hán Pro":
    st.header("✍️ Luyện Viết Chữ Hán Theo Bút Thuận & Viết Tự Do")
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        st.subheader("🔍 Tìm / Chọn Chữ Hán")
        
        # Custom input search
        custom_input = st.text_input("Gõ 1 chữ Hán bất kỳ:", placeholder="VD: 你, 好, 学, 汉...")
        
        # Lesson Selector
        selected_lesson = st.selectbox("Hoặc chọn theo Bài học Ehou:", list(range(1, 8)), index=0)
        
        char_list = EHOU_CHAR_DATABASE[selected_lesson]
        
        # Find active character
        active_char_obj = char_list[0]
        if custom_input.strip():
            char_char = custom_input.strip()[0]
            # Search in DB
            found = None
            for l in range(1, 8):
                found = next((c for c in EHOU_CHAR_DATABASE[l] if c["char"] == char_char), None)
                if found:
                    break
            if not found:
                found = {"char": char_char, "pinyin": "Chữ tự chọn", "meaning": "Chữ Hán tùy chỉnh người dùng", "compounds": []}
            active_char_obj = found
        else:
            selected_char_text = st.radio(
                "Chọn chữ Hán:",
                [f"{c['char']} ({c['pinyin']})" for c in char_list],
                horizontal=True
            )
            char_symbol = selected_char_text.split(" ")[0]
            active_char_obj = next((c for c in char_list if c["char"] == char_symbol), char_list[0])

        st.markdown("---")
        st.markdown("### 💡 7 Quy Tắc Bút Thuận")
        st.caption("1. Ngang trước sổ sau (十)\n2. Phẩy trước mác sau (八)\n3. Trái trước phải sau (你)\n4. Trên trước dưới sau (六)\n5. Ngoài trước trong sau (月)\n6. Vào trước đóng sau (日)\n7. Giữa trước hai bên sau (小)")

    with col_right:
        # Active Character Card Header
        st.markdown(f"""
        <div style="background-color: #ffffff; padding: 1rem; border-radius: 16px; border: 1px solid #e2e8f0; margin-bottom: 1rem; display: flex; align-items: center; gap: 1rem;">
            <div style="font-size: 2.8rem; font-weight: 900; color: #dc2626; background-color: #fef2f2; width: 70px; height: 70px; border-radius: 14px; display: flex; align-items: center; justify-content: center; border: 2px solid #fca5a5;">
                {active_char_obj['char']}
            </div>
            <div>
                <h3 style="margin: 0; color: #0f172a; font-weight: 800;">{active_char_obj['pinyin']}</h3>
                <p style="margin: 0; color: #64748b; font-size: 0.9rem;">Ý nghĩa: <b>{active_char_obj['meaning']}</b></p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        tab_writer, tab_freehand = st.tabs(["✨ Chế Độ Bút Thuận (HanziWriter)", "🎨 Chế Độ Viết Tự Do (Freehand Brush)"])
        
        with tab_writer:
            render_hanzi_writer_component(active_char_obj['char'])
            
        with tab_freehand:
            render_freehand_canvas_component(active_char_obj['char'])
            
        st.subheader("📚 Từ ghép mẫu có chứa chữ này")
        if active_char_obj.get("compounds"):
            cols = st.columns(len(active_char_obj["compounds"]))
            for idx, comp in enumerate(active_char_obj["compounds"]):
                with cols[idx]:
                    st.info(f"**{comp}**")
                    render_audio_button(comp.split(" ")[0], label="🔊 Nghe")
        else:
            st.caption("Chưa có từ ghép mẫu.")

elif menu_choice == "📖 Cẩm Nang Lý Thuyết (Bài 1 - 7)":
    st.header("📖 Cẩm Nang Lý Thuyết Trọng Tâm (Bài 1 - Bài 7)")
    
    tabs = st.tabs([f"Bài {i}" for i in range(1, 8)])
    
    with tabs[0]:
        st.markdown("### Bài 1: 你好 (Chào bạn)")
        st.markdown("**1. Từ vựng:** 你 (nǐ), 好 (hǎo), 妈妈 (māma), 爸爸 (bàba), 哥哥 (gēge), 弟弟 (dìdi), 妹妹 (mèimei), 女 (nǚ), 大 (dà)")
        st.markdown("**2. Biến điệu 2 thanh 3:** `nǐ hǎo` ➔ `ní hǎo`")
        st.markdown("**3. 7 Nét cơ bản:** 点 (Chấm), 横 (Ngang), 竖 (Sổ), 撇 (Phẩy), 捺 (Mác), 提 (Hất), 钩 (Móc)")
        
    with tabs[1]:
        st.markdown("### Bài 2: 汉语难吗 (Tiếng Trung khó không)")
        st.markdown("**1. Từ vựng:** 忙 (máng), 很 (hěn), 他 (tā), 她 (tā), 汉语 (Hànyǔ), 难 (nán), 吗 (ma), 不 (bù), 太 (tài)")
        st.markdown("**2. Biến điệu của 不:** Đứng trước thanh 4 biến thành `bú` (VD: `bú dà`, `bú qù`).")

    with tabs[2]:
        st.markdown("### Bài 3: 谢谢您 (Cảm ơn ngài)")
        st.markdown("**1. Từ vựng:** 您 (nín), 请 (qǐng), 进 (jìn), 谢谢 (xièxie), 不客气 (bú kèqi), 去 (qù), 银行 (yínháng), 取钱 (qǔ qián), 邮局 (yóujú), 寄信 (jì xìn)")
        st.markdown("**2. Quy tắc j, q, x + ü:** Phải bỏ 2 chấm trên đầu ü (`ju`, `qu`, `xu`).")

    with tabs[3]:
        st.markdown("### Bài 4: 你叫什么名字 (Bạn tên là gì)")
        st.markdown("**1. Từ vựng:** 叫 (jiào), 什么 (shénme), 名字 (míngzi), 认识 (rènshi), 高兴 (gāoxìng), 也 (yě), 是 (shì), 老师 (lǎoshī), 教 (jiāo)")
        st.markdown("**2. Đại từ 什么:** Đặt trước danh từ để hỏi (VD: 什么名字).")

    with tabs[4]:
        st.markdown("### Bài 5: 你去哪儿 (Bạn đi đâu)")
        st.markdown("**1. Từ vựng:** 哪儿 (nǎr), 看 (kàn), 回 (huí), 家 (jiā), 请问 (qǐngwèn), 贵姓 (guìxìng), 国 (guó), 人 (rén)")
        st.markdown("**2. Kính ngữ 贵姓:** Hỏi `您贵姓？` -> Trả lời chỉ dùng `我姓...`.")

    with tabs[5]:
        st.markdown("### Bài 6: 这是我的书 (Đây là sách của tôi)")
        st.markdown("**1. Từ vựng:** 学习 (xuéxí), 和 (hé), 的 (de), 同学 (tóngxué), 这 (zhè), 那 (nà), 谁 (shéi), 书 (shū), 词典 (cídiǎn)")
        st.markdown("**2. Đại từ chỉ định:** 这 (Đây - gần), 那 (Kia - xa). Trợ từ sở hữu 的.")

    with tabs[6]:
        st.markdown("### Bài 7: 今天星期几 (Hôm nay thứ mấy)")
        st.markdown("**1. Từ vựng:** 今天 (jīntiān), 星期 (xīngqī), 年 (nián), 月 (yuè), 号 (hào), 生日 (shēngrì), 多大 (duōdà), 岁 (suì)")
        st.markdown("**2. Ngày tháng:** Năm ➔ Tháng ➔ Ngày (2016年9月2号).")

elif menu_choice == "📝 Luyện Tập Trắc Nghiệm (53 câu)":
    st.header("📝 Luyện Tập Trắc Nghiệm (Full 53 câu độc nhất)")
    
    quiz_questions = get_quiz_data()
    
    if "user_answers" not in st.session_state:
        st.session_state.user_answers = {}

    filter_cat = st.selectbox(
        "🎯 Lọc theo chủ đề:",
        ["Tất cả (Full 53 câu)", "File Nghe Audio", "Bộ Thủ & Chữ Hán", "Ngữ Pháp & Giao Tiếp"]
    )
    
    cat_map = {"Tất cả (Full 53 câu)": "all", "File Nghe Audio": "audio", "Bộ Thủ & Chữ Hán": "radical", "Ngữ Pháp & Giao Tiếp": "grammar"}
    selected_cat = cat_map[filter_cat]
    
    filtered_questions = [q for q in quiz_questions if selected_cat == "all" or q["category"] == selected_cat]
    
    # Calculate score
    correct_count = sum(1 for idx, q in enumerate(filtered_questions) if st.session_state.user_answers.get(idx) == q["correct"])
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Tổng số câu", len(filtered_questions))
    c2.metric("Số câu đã làm", len(st.session_state.user_answers))
    c3.metric("Điểm số", f"{correct_count} / {len(filtered_questions)}")
    
    st.markdown("---")
    
    for idx, q in enumerate(filtered_questions):
        st.markdown(f"#### Câu {idx + 1}: {q['question']}")
        
        if q.get("audioText"):
            render_audio_button(q["audioText"], label=f"🔊 Nghe Audio ('{q['audioText']}')")
            
        user_choice = st.radio(
            "Chọn đáp án:",
            q["options"],
            key=f"q_{idx}",
            index=None
        )
        
        if user_choice is not None:
            chosen_idx = q["options"].index(user_choice)
            st.session_state.user_answers[idx] = chosen_idx
            if chosen_idx == q["correct"]:
                st.success("✅ Đúng rồi!")
            else:
                st.error(f"❌ Sai rồi! Đáp án đúng: **{q['options'][q['correct']]}**")
            st.info(f"💡 **Giải thích:** {q['explanation']}")
            
        st.markdown("---")

    if st.button("🔄 Reset làm lại"):
        st.session_state.user_answers = {}
        st.rerun()