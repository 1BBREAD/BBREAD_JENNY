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

############음식
st.markdown("""
<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 한 줄에 3장씩 */
  gap: 15px;
  margin-top: 15px;
}
.gallery-item {
  text-align: center;
}
.gallery-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;   /* 비율 유지하면서 동일한 높이 */
  border-radius: 15px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.15);
}
.caption {
  font-size: 0.9em;
  color: #555;
  margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)


# 타임라인
imgs = [
"https://lh3.googleusercontent.com/pw/AP1GczMgGI7BMMSzXAlzC6lrRo4fzdkVOFBWJf9V_XXH38pY8ZK1K1chmvaT3nbE_rJLDm4CClv8uxAbdqoslQgB4s-uVSaMmyEp4uCTWJUYWUXKlfVZm_1Ka1WFfzX44HpBF3EA15XtmEOlfwHt2Bqxbf6k=w1346-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOYbjYPivgTvuxSSkJJPNNSuID-5_1WLMCQsU8C9xrAkbPikvOVKzJCFWTaGPUKmGGudujMMeFGyx_qscih1Q3nKTdXE_IyvHpdOq3jQ253nGEcvl1OtMyWemgDZKfG-BqbdFS-gqwnjUPRhy3DeSlb=w1346-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNlnnp9YNYkc1o8iuaExpuA3VQ8W8O7yxW0oCLn1MOI2LDlIcT1UUwtD3g5aDaLR7ZbxQNOSnTz0MquAVHx_Yc9Eg-FgSnNOA5BGTFxGbEf8TRAKRtNuzPVd69P8PuFDasaZTj4z4l8E25jrUkF22pk=w1346-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOf3qqrO7XK4BTj8hoJg3aDej59xVzTZj2JC2YsNfX4FwzRMoPsubYDcJRAOPIgz-bG2qRFQ4wJQotTjFhs-B9uiABujA57qNzfHPeeFiXRjwZ3-KWZJ8ZH6qfiBqqYUWl2TBY9_BrV7cMaoWYKKsE2=w1346-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOyAFjIqosqOVjIQ1QYU80gZPGwTxy8ymnS_oEdN-YafSdQVyE6ZK5bce0Zfpc2x8c_VWhM1JNymgBEUI2Hb6hWytL3KOmsO1a1rNLLqPgMjmtkN6XDA_tv9ERSjiVIsJqt_WJkXdxzNh1vFBWGhSsP=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMOODThv19b7B7Xb_033pomtx-2PLN9NJCLetkbQTgxRCszQMZebYfVzv-Pkpo5hjF6fW2le55DhnYVgOYlnThH7j3fjoJrEgdsxxE8o8fE-wxVJyfkIoqUKNGOzS74OhEowdrh4WRjTXkRprcrv-jP=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOpZBMYz9__Si57_bLLdsLvXUeXks-T0A_MXCJv4VEhJV_Fhcys8XIFt_4R1PAEddDgiBYIbaN0V3bpLv6nIDCZE5vowxsNqGLhVyEmOxbsDGxFMIZyhtTI3PEEo-vmCZD8h3RRvSdqcxa7Ow2RpuIe=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMXuJLEwpVJHLyZ6d-zztKQ0CMFQd4JgN2wzMlM8xoGheW1rzi70M4pfkbPyniXsx4cKc6Q0TjXszswSzr04So1jobI4bbWnDh3tivx5ZMatOc6SYNrMyI8278TrXZ8b_qq-2kEPqFSVbOGpAR92RHK=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNg_VFuOtarPptZRh3iRD6N2lZSrUg0i_ozxzpjtjIe-NjCA78y1nnuohrJTaudc6foO1gAHCgrLAd0BC7otHn_1qU4RcNbp3lHgVb-YRlU5i34yg0Sj22U1ZxwCT4sE2c01Vrdmx-1yDR3hgFw1Nuq=w721-h960-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPvcIaUirSsg41Nr4hsybOFlNxnwZgCEgiBk085PNKhrx-zd_U4xpxtVgS9eAvp8EBTbdmCoaDP4-n-KcP7bO_5orx_i1AyVKORrUJWCQ_u2fuyywi0b34jO0uuaUzVI3DppygMxsFtdpcpI9j6Lf24=w721-h960-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczM-3-8TgG6ThO_2ZXkP5408YPSM6d-CzqvuErVgSxRzr7jdhG8e_8AhVWFDBqa4rAkZ3oc49aE9sYALmsuVb-DS7Js1dnbpxLJkrzd4M5DGZBhl2iZ9Ox5dDTCN9Z0RQyDiES6D0IK_2XbSsT-9xsuY=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO5Mei1A1-2Z6dFpSwk3csk1vbn4ySjxvA2J081nsfx12yOex0HLJ9UOea9UrPKY9r1DZjVrOMnVTln5_NV8yibqW9PtsLNVgovnuIMfcFvcFjrVs8gcUi1_4kewcvS5vB5TsVJeeQNlgkt6X8yt8FD=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPNkNZ1oT3HIryY-hPgFY7GQ9QxYRhDCr8SfGvjBufHviCpAanDMY-tqOKzWQOM8Znhc3QfnZCO53ZvuZ6uSoWe436bOwcaTXklOJEbSHuVTulz6FbnVoVyNIS_0exw2mrFzZ1kVGR9eez569ozxRLt=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMrE-hXtr-gr6FLyAmR2NPt0ykhNgp61N9rw8yj-egmXn18RvJCHJjodpv952i6XzYv4TYL0bb0oY1E2foNKCjOHvZSqRY_gPeiMT_rCGqLE_YEdOaShdmVnIyAsB18pnCPlhRoaqBRud-VjQhiGxku=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNzLeBC1dQ2cRj03_o_tYkFfrolk0FGKXEyhDr9YfH8nYI3OKjkv3Mhmxx_ExiYg-i7EQjL84h7omXjF4faMS9OcrtUZLwDz9WupTbNcdYuFx-B8Tif_zRiaM8sYa5My8dNMTAbh8KPx1rAbXw2lISA=w1440-h1080-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOZ1aUdOARb-orP3zVr8WYanbhs9VMqDo1K6Au77s_7subqQnbd17C965nqpIVYDUazbXbcxXN31CBfe7ri41VV77nNAxosCjCCPVnQgNpRejRAch2GrEan2iKH-Na5_ZmiRJnCsZ6ytNdfJGJXEqRK=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMhBdwNhs-5GDpK6dyejRNT2Bw0eD_BOSczyt7W3cjvUdYeAonsM6T6ExlXEn56v0Nmw5520jXgr4lYrdSiLHob51eqtCA175sE2nJrj06iuszlqRjNtp1jto8A8Zc4bSjWp5-jG_EXzbRUbFGGLI2E=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPw16yirmRRfrIUL8R8v2LGkvEp88PiYR_8QDwBF5gnVzbdSwaShvImg-XVFOmctEWKeydxwoJOJGRXjluhL3zOND5e3hGxEDDD1bJgLzcdnhecJ2l526Po3iC2xGVG9Njek5SeWjCO2w3DPmE4_WC1=w1440-h1080-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPterYS5eVooidIxjVVzH31cBi5O4r6H1p5wSfP-CSQhMrHEyseSDVRcD-pB9jvi-1uV-qt7235E_LXWn2FJ0-Apnx1FSihNLQj_2bUzkQYFQhSMJRUn9pfy6s9Q0q-UR2Y26yxF_QfibpiY99FchqS=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczP-jcxPtozX4TSWmGmv2E6R6VS5NYZGANVB3YVGRkheiQgNXiVPK4a7PHDpuWq0H8SW3H-4mOOpseEtNSVZG-9YFOoJ3aWUdNH6Q5dzRWEc7SYUbFKs5XWtFe_o3k9u1zU5L9HN0oZ4sd2W0dd7FV20=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPbQDBbiOKt7kAUykE93gVFUcQWlGJFX7WdCFUjffOi9sUMf2Ea8omaLdKyu1WeeS-s-w4HtSXNrkB3OP2eKH7fB3GFRFsv-Ha41PaF-j9cIqWsj8KDKY1NgQJsvuApAS-eImzBe8ni98vFq4Xeudqm=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNJIHAsumY6Pe-jsRygPwx7xtCXZaSaQit5COrppBZyGW1YCyM_MBBgquRnWSIH_ogM_Td1l7sLAfthgOfR4IHjIoO3z_kSZD45mxdhg0LJaJgf8WmES5Sns7AcpeXI2rHJPrUlMrXmEyQ0q2yBOfoY=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPmuJxWZ44Vemu0XwwmwbdFWuHJoY5EihlOPIps_IVd46YmKusjKiMbMx-LSXzr_ZybNWH5a5vsZt2Cs-L3YiiLULp7hsE4pqL-Q1C4e0n1IwHedAJpRweuHdLxH9C_Ly0-1n9Ft3OELZLGKtG4J60n=w1010-h1346-s-no-gm?authuser=0"
]

caps = [
"첫 생일"
,"2"
,"3"
,"4"
,"5"
,"6"
,"7"
,"8"
]

col1, col2 = st.columns([1,3])
with col1:
    st.markdown("""
    <div class='message'>
    너와 함께 먹으면, 그 무엇도 미슐랭이야.
    </div>
    """, unsafe_allow_html=True)
with col2:
    with st.expander("🐷"):
        html_blocks = ['<div class="gallery">']
        for img, cap in zip(imgs, caps):
            html_blocks.append(
                '<div class="gallery-item">'
                '<img src="' + img + '" alt="' + cap + '">'
                '<div class="caption">' + cap + '</div>'
                '</div>'
            )
        html_blocks.append('</div>')
        
        gallery_html = "\n".join(html_blocks)
        st.markdown(gallery_html, unsafe_allow_html=True)


st.divider()

imgs = [
"https://lh3.googleusercontent.com/pw/AP1GczP9ndamnKNw3R_h-SuWscR65j3GZJJpMGUhhikjqOC2Tet_FSu2-ZUDqxKsdNKny4irFOXNRFyUM8M3y3fPFBMK6s2EuXYgdiigHEDj8Zaf6_gaq69NgSHidlaK4YQA8EZ1jPYsP0ABG4NHPYcw1Hzk=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczM58CefN3VeMmZxvZXcl03shHL1XJiqTtbavfnXOMHw8uSx3ssG8p9AT6zPAAZr4nvFT_ELDPTugwlASCLhw2aTVcwZIu9KUrlIFDBdiS2gcOuSi2jHCm9DAFZi1XNmfTWzveTWAybOXbUa1CA7vvzE=w606-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNa7Ij9f4c4eNBAIU2vDhI6ClqBuIgUdbO4e98_3K-zkOUuX2pgWxm5e_7f0Gs9BexqcrrcWBs0CmaJ3Ho-jDPUl9nTxsxOVqqhy89ykVOB46SwoeBF2sqZfMZ1XlHSqZ_GM1_4mHrxQhcMykVvK2aj=w1077-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNlzTD7ojJ0y6S7jthTviDXI_WiAgZqcwgpDbe5F8pGxlgUTOvuWaAOvUlgXQ_975no3O55XliG3ctAo8KBeCskCzuMV3_qGoBo1h3BlAsxZZq0FnaIf6eUWOkjk8zbUbZoKka7AeYeRwCh38hB36NB=w897-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO94S1xI8BY0oZ_FEluJNn9wcCID1bSOcLGxF74KQA_WW3z1Dn4bmf0Mz6rQAhTwFLu_oNwSFTc2QvWeDGmRX0hEbVvB-jF1Sx5sxGQaUVcrUFN_IIQvcEmj1xyU4YCVQJ3Vkm910x8UuAgUMSqiFN8=w897-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMwmebzFSSAmSgFa_Eb8Gsz4M4Hsbh-G0KlGN8fg3VmGBelmDyycNgm39hTuj34kVkE0his6m4PO2Ky6Qeo2h8VH8qPC9W0gXi37jxCkkEy5emY_5YfhtqjKfCiju6eoR4hSHcR8o1y-wL8IRw8E6u-=w897-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMElZLbL9iUQcS0NqHpSGU-kKSNQzsnxHyP9OXymdm57KxAtbCH52NQh4WgOJHvNk-WkFGlJNFe3lXteNBeoUk3CNPcDlpcl4SABG6p3beTI0671ozt-wPc4vNzeHBYji52kuZ-fNPOIWdp0xPgsHk_=w1440-h483-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNUYtWu7Y7gopt3ohH0j3l1GJR5GCl5Z7fIfMV2mXZHP55k0qfBsu4gsu0DVWZCJ_AZs7RSJAGCZivAcDXebJVCDx2y3Zb3DbMAf_0Az81Z9ElTa8xgc_zzbmKiflCSRVdFLOAI9OrKCJyK0vDX0B3I=w897-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNWVnAE94f2rSMoccav5cJjiZQ_8Ic48AH2_99yceL7QFnBwvoMbENLIoJ6aFQBtm9ar2LmVx53_TpneQYR1NkFzFNs4GpDiaOCzo-wYFhPSTpZSEPf1cEA4ltahLDtx5U3WlJLpJPeKQ6bXLoUJGt0=w903-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczN7ZRYWF2_BehyULArMM5pdohGqGYw5YYeCOEXp-M4bs7FWkJNz0jdgqbo8u_ThNUY6Gw09Khk8_yM9nTNsno4I0C40NeaDW9xlZsr-UYK2rPUbaa2aWDgexnwjFqu2qHo7P6DF3zinrpJLjIKKWzzC=w897-h1346-s-no-gm?authuser=0"
]
col1, col2 = st.columns([1,3])
with col1:
    st.markdown("""
    <div class='message'>
    인생은 네컷으로 담기엔 부족해
    </div>
    """, unsafe_allow_html=True)
with col2:
    with st.expander("📷"):
        html_blocks = ['<div class="gallery">']
        for img, cap in zip(imgs, caps):
            html_blocks.append(
                '<div class="gallery-item">'
                '<img src="' + img + '" alt="' + cap + '">'
                '<div class="caption">' + cap + '</div>'
                '</div>'
            )
        html_blocks.append('</div>')
        
        gallery_html = "\n".join(html_blocks)
        st.markdown(gallery_html, unsafe_allow_html=True)

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
