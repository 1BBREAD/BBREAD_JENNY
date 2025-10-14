import streamlit as st

# 이미지 캐시 삭제
st.cache_data.clear()  # Streamlit 1.18 이상

# 페이지 설정
st.set_page_config(page_title="💜우리의 기념일💚", page_icon="💖", layout="centered")

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
st.markdown("<div class='title'>💜우리의 1주년💚</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>2024.10.20 - 2025.10.20</div>", unsafe_allow_html=True)

# 📸 Google Drive 이미지 불러오기
# 🔹 공유한 Google Drive 파일의 ID를 이용 (예: https://drive.google.com/file/d/파일ID/view)
# main_photo_url = "https://drive.google.com/u/0/drive-viewer/AKGpihZaIg1rxzRjDX8LjZ-VbBEi51sJo7ZczS4Q3KCxVzQ6_bg_JjPvPGH1kzLG8UoI5bJg-Z7j2vD96-6gtV8K-u7I4j9Se9G9ups=s1600-rw-v1"

# google photo
#main_photo_url = "https://lh3.googleusercontent.com/pw/AP1GczNRX1dpYswv47pQMlY2nBjD8F_AECpIe2fkXdm3IAlUysbAHDIHFJnt1jh1IXoufK804rqGBWyjrO6SE4I2t9TqPeed1PODfplJQuBO4QoeY6eW0PzremVZyLJJt07XBWrfiQkrXPSy53vqA33Krgbp=w1010-h1346-s-no-gm?authuser=0"
main_photo_url = "https://lh3.googleusercontent.com/pw/AP1GczN7V-5Huymt8q5TjYN_hVjRlVQz7MUOJWXr0b7JEBK1FxHF-QkZfdZQklXiphbEmUImBIY27O3SAaJZMZHHlVKAFQyplxyEwtVNtxcWML3dpFP8WR2PdGXmQhJNec3l4DvrUItV8Zvta-rO1xJBksO4=w1523-h1142-s-no-gm?authuser=0"
photo1_url = "https://drive.google.com/uc?id=여기에_파일ID2"
photo2_url = "https://drive.google.com/uc?id=여기에_파일ID3"

# 음악 파일 (mp3)
music_url = "https://drive.google.com/uc?id=여기에_파일ID4"

# 인트로 사진
st.image(main_photo_url, caption="💖", use_container_width=True)

# 배경음악
st.markdown(f"""
<audio controls autoplay loop>
  <source src="{music_url}" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
# 타임라인
# st.markdown("## 🐷🐷🐷")
with st.expander("🐷🐷🐷"):

    with col1 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczMgGI7BMMSzXAlzC6lrRo4fzdkVOFBWJf9V_XXH38pY8ZK1K1chmvaT3nbE_rJLDm4CClv8uxAbdqoslQgB4s-uVSaMmyEp4uCTWJUYWUXKlfVZm_1Ka1WFfzX44HpBF3EA15XtmEOlfwHt2Bqxbf6k=w1346-h1346-s-no-gm?authuser=0", caption="첫 생일")
    with col2 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczOYbjYPivgTvuxSSkJJPNNSuID-5_1WLMCQsU8C9xrAkbPikvOVKzJCFWTaGPUKmGGudujMMeFGyx_qscih1Q3nKTdXE_IyvHpdOq3jQ253nGEcvl1OtMyWemgDZKfG-BqbdFS-gqwnjUPRhy3DeSlb=w1346-h1346-s-no-gm?authuser=0")
    with col1 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczNlnnp9YNYkc1o8iuaExpuA3VQ8W8O7yxW0oCLn1MOI2LDlIcT1UUwtD3g5aDaLR7ZbxQNOSnTz0MquAVHx_Yc9Eg-FgSnNOA5BGTFxGbEf8TRAKRtNuzPVd69P8PuFDasaZTj4z4l8E25jrUkF22pk=w1346-h1346-s-no-gm?authuser=0")
    with col2 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczOf3qqrO7XK4BTj8hoJg3aDej59xVzTZj2JC2YsNfX4FwzRMoPsubYDcJRAOPIgz-bG2qRFQ4wJQotTjFhs-B9uiABujA57qNzfHPeeFiXRjwZ3-KWZJ8ZH6qfiBqqYUWl2TBY9_BrV7cMaoWYKKsE2=w1346-h1346-s-no-gm?authuser=0")
    with col1 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczOyAFjIqosqOVjIQ1QYU80gZPGwTxy8ymnS_oEdN-YafSdQVyE6ZK5bce0Zfpc2x8c_VWhM1JNymgBEUI2Hb6hWytL3KOmsO1a1rNLLqPgMjmtkN6XDA_tv9ERSjiVIsJqt_WJkXdxzNh1vFBWGhSsP=w1010-h1346-s-no-gm?authuser=0")
    with col2 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczMOODThv19b7B7Xb_033pomtx-2PLN9NJCLetkbQTgxRCszQMZebYfVzv-Pkpo5hjF6fW2le55DhnYVgOYlnThH7j3fjoJrEgdsxxE8o8fE-wxVJyfkIoqUKNGOzS74OhEowdrh4WRjTXkRprcrv-jP=w1010-h1346-s-no-gm?authuser=0")
    with col1 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczOpZBMYz9__Si57_bLLdsLvXUeXks-T0A_MXCJv4VEhJV_Fhcys8XIFt_4R1PAEddDgiBYIbaN0V3bpLv6nIDCZE5vowxsNqGLhVyEmOxbsDGxFMIZyhtTI3PEEo-vmCZD8h3RRvSdqcxa7Ow2RpuIe=w1010-h1346-s-no-gm?authuser=0")
    with col2 : 
      st.image("https://lh3.googleusercontent.com/pw/AP1GczMXuJLEwpVJHLyZ6d-zztKQ0CMFQd4JgN2wzMlM8xoGheW1rzi70M4pfkbPyniXsx4cKc6Q0TjXszswSzr04So1jobI4bbWnDh3tivx5ZMatOc6SYNrMyI8278TrXZ8b_qq-2kEPqFSVbOGpAR92RHK=w1010-h1346-s-no-gm?authuser=0")

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
