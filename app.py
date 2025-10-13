import streamlit as st

# 이미지 캐시 삭제
st.cache_data.clear()  # Streamlit 1.18 이상

# 페이지 설정
st.set_page_config(page_title="우리의 기념일 💕", page_icon="💖", layout="centered")

# CSS 스타일
st.markdown("""
<style>
body { background-color: #fff0f5; }
.title { text-align: center; font-size: 48px; color: #ff4b8b; font-weight: bold; margin-top: 40px; }
.subtitle { text-align: center; font-size: 22px; color: #555; margin-bottom: 40px; }
.message { font-size: 20px; text-align: center; color: #333; margin: 20px 60px; line-height: 1.6; }
.footer { text-align: center; color: #888; margin-top: 60px; }
</style>
""", unsafe_allow_html=True)

# 🎉 제목
st.markdown("<div class='title'>우리의 1주년 💕</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>2024.10.13 - 2025.10.13</div>", unsafe_allow_html=True)

# 📸 Google Drive 이미지 불러오기
# 🔹 공유한 Google Drive 파일의 ID를 이용 (예: https://drive.google.com/file/d/파일ID/view)
main_photo_url = "https://drive.google.com/u/0/drive-viewer/AKGpihZaIg1rxzRjDX8LjZ-VbBEi51sJo7ZczS4Q3KCxVzQ6_bg_JjPvPGH1kzLG8UoI5bJg-Z7j2vD96-6gtV8K-u7I4j9Se9G9ups=s1600-rw-v1"
photo1_url = "https://drive.google.com/uc?id=여기에_파일ID2"
photo2_url = "https://drive.google.com/uc?id=여기에_파일ID3"

# 음악 파일 (mp3)
music_url = "https://drive.google.com/uc?id=여기에_파일ID4"

# 인트로 사진
st.image(main_photo_url, caption="우리의 첫 만남 💖", use_container_width=True)

# 배경음악
st.markdown(f"""
<audio controls autoplay loop>
  <source src="{music_url}" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

# 타임라인
st.markdown("## 🌷 우리의 이야기")

col1, col2 = st.columns(2)
with col1:
    st.image(photo1_url, use_container_width=True)
with col2:
    st.markdown("""
    <div class='message'>
    첫 데이트 날의 설렘,  
    아직도 그 순간이 선명하게 기억나.  
    함께 웃고, 함께 걸었던 그 길이  
    우리의 시작이었어 🌸
    </div>
    """, unsafe_allow_html=True)

st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class='message'>
    어느새 1년,  
    하루하루가 너로 인해 특별했어.  
    나의 모든 계절 속에  
    너와 함께 있고 싶어 🍀
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.image(photo2_url, use_container_width=True)

st.divider()

# 편지 섹션
st.markdown("## 💌 전하고 싶은 말")
st.markdown("""
<div class='message'>
너와 함께한 모든 순간이 선물 같아.  
앞으로도 같은 하늘 아래,  
같은 길을 걸어가자.  
사랑해 ❤️
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>- From 당신의 이름 -</div>", unsafe_allow_html=True)
