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

st.markdown("""<div class='message'>멀리 있으면 멀어서 보고 싶고, 옆에 있으면 가까이서 보고 싶은 것.
\n그게 너다.  - 원동연</div> """, unsafe_allow_html=True)

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

caps = [ 0 for i in range(len(imgs))
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
    인생은 육천오백이십사컷쯤
    </div>
    """, unsafe_allow_html=True)
with col2:
    with st.expander("📷"):
        html_blocks = ['<div class="gallery">']
        for img, cap in zip(imgs, caps):
            html_blocks.append(
                '<div class="gallery-item">'
                '<img src="' + img + '" >'
                '</div>'
            )
        html_blocks.append('</div>')
        
        gallery_html = "\n".join(html_blocks)
        st.markdown(gallery_html, unsafe_allow_html=True)

st.divider()

imgs = [
"https://lh3.googleusercontent.com/pw/AP1GczMrrqLxDwEBsH1g53o8y2wKJPqNMfZoIVls-jMXA4yffmvhlgkeRg9KPkh2wILQbCZ-2xfw46sihIWXCBvFzBoG-1juVhEptlnQR2BTGclbMYscscQAT1Q51sSNMgM7ebIp3rOHp_hX9wwGLOaaJFV_=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczM2jtRlP3ZO6fJDJJqXOM_7cSQrtFwhaiVc_PO_CRH1JTvy5KIJ59S3PUG4AcKMYVEbzjsDM_qboAVU4eltm05-okXikcSuGIf3M8_imp9b41ycu6dHNBuZvD68LBz3Opp5cVx4tS2pohse5EZjQzQy=w1277-h1277-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO5YL1yzsdq9HdBVAxLKn5Kf7d_ozH2EpNFb1BSP7RVinoHJObJRaurrfxcy7hgkW9uPpQM2Ew1NMjifDTYylhKLQ5_7jG5IffsKgl8-ar6owypv1BoEAtcSIgAKzwSSjl3_t0kvvpvGDpw0LywqOyf=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNLxN4FFlvi9CatPrD472wDurrlcSNdvC8Q-zvDDvSXWUjjmvLVrTemd094gexi3OhtITRBZNXSJKDce1o5P0BLPlbC2SizqCerraSoETNzFvnp22lp-gduTbxqXkqBVe5V3-b6feRQW7Yy8bA8h86V=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO5RIobH-ny7ITTIfKfFz65KQQDxucHEtFPKkiG8ubkiCBdI2q-2zMyLXTaUeT3Garv80Wv4veYm27cijn-_Yae7RAG0-Uo3n3OUZY1k_uRmtx6MntM8iCQJmTVYkRP67B5tDb9CwKxglzqDLXEUth2=w1277-h1277-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMQF480GUaXDGi7hJ67gNOTimVaVH-LtRTQZG1UozX8-dLikm_Q1zam5c8_MN2tc6zY163pRYjCEAf6vB7E4csuNZyiu-8xB-DxdCLI48yOI6BIi_Kc4Gd_DgEN5AWmVOPDB3LyvkiAibqGrI2S-SqC=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMOboI6xIdUzCS9JcwODukZVqMJ9butsnbFv_f7xXoBKrOigDzQ7Oh8milPntIU9ASTcqrKXxJHxVMgb6SHMkDcRD2MPplDRLjcwRBcddUdqWk67O6nPoTwXqG6DKRg1KXwKAPcDNibW4phta-F-faq=w1277-h1277-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNI8f-89e2JCnqx1mdnY7ckt7H44MbmCZx_Y2dMSr_WQsYc4Pr9PX10KPztgsV3BFwlEpZFyRdy7V6yZ4aLr9R8i98HV3EZ1Qv12MsxTrMPjqsUq_PdD-pZt9NuM0NVSPx_RtW5ydTj2yvRNn_izoNq=w758-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMkp0nC9cXu_KcWfo36XOh_ze7RBwoBWqFC1c-rfdLIs1vSlUxo0dD2NZhlV981auoaVJsdfpJL4ls_fswgxcxfND9qMM6MI9yEaK2LFHe-gttzkhWlcEH7aJH-fzfQrYfCZDR_aPzHIBVbMKSKstcU=w1277-h957-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOr_7sLp6928iFjT2fsHk4KJ-DBj9K_-czI_dAwOxidM6Jo4WqnMzhYVnGm1q-LTgu1V-4n93sIYId5e2l223IZdURAa-mKfihGgQCcjdrTuLAMTuhWrGWgYSaPzdIzVhaPLcaooNr06pu9g2A9Y56i=w1064-h1064-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczN9h9jpJNXpgxC1KzWjR96ul4DtAZNChXrbgCLtstb-Qr04JewGVVhDeCbMcAW4B36fx246FwA_OJdgfXNUGExuMYnbccQuXeD_ljipSXgubPrvv2OxrbJH_0d9nn-bj_Uk43fKREgbDwOL34Sa7a1u=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNsL1yPv5MqUYk-b1IMAgicjDSPWeNIUsSyZ9fLBCGCForvMEM1MLJNT7ZHTGLWiHrWIdQQFv6uvgcdBGbpFz9rxvGAnJJnAiwafJLgArnmHZ_ujDFIHf5iT1Ptc4677Q7AU050GUU12zQst73jO6w-=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO2Hv5YHuKYi-czyjXBrCKO9y9zxojzELSF4OuvkjEr2YGwD12fTu5lu58zWv2-zrUsryI6Swdfl_JA2RhSk0QlN9qRtJ0rWaZAnmybd696hejgFoOtbDPRVfHGylyIj1AwB5C_V8sI1HMvEp9DWwIR=w1277-h957-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOEtydW9CnGwc-T5QHT_hFtcedsYF3FPh1CzdRTUzsdpQ9EeajwkAnqBbFBX4rK5Fis7uQ1O56h6tgYNt7Qtp2CBrxorn0XcW1TAJh7zVts0NtrZtpNN1p6vOyD8jy-HGhrVT1hBfNkqYG2BswlsM5c=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPxBoFiJJF6UPSfw5xJzB52UdoTl-zkBO5dPFdPF4jgiFvyw7cYhF-hwDTULilMFweY3y5X_eXHxcs36cmUHgVe5csZMCpZiGDGbzJBULY85GUWvdLvMoxKPHA8uifzN4vhAeOWuy0u_Kw02A6rHrL7=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMWbfp0HmGvjs4JKhsa6yZCWmHqYfXCksDEdmj4QAD5WkFwCl17A88rgPm4G9HeUuIxIE96N5yRivUfb7bk73HV1uNbgd6I3IiL8FmSl6Nmt-im_Y5SQMyUV4mABBzZzOXcx_WubHPfK_7TQVTh9E2f=w1277-h957-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPSJRjkOjPYSZP6mO_DyxR6fzLpDM8qHVBLAkLYwVhz_LAfnRGEOJZ9mLQyV6q1Il4If4f4OD4EWA4JLQb7tfDLRlni4rqRha5gCtiyML6mVW8pThB5j4zSIE6OVy3xFzi4rTDLKZcczi9uGKjEVSPv=w721-h960-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO1l3TAB_I3GujR41o8j2dx-DryWSw9prCb4857NeHJHtLp5Up1ixZVwABOiU6OfOYHyOaWLsV0xH_vJVlx44-Fmn7tB0IYFtf_xLOrTzG6ijxaa0H1px_Tubx0Qbg91LgaXpmz3bG_fYLOzT5hyf5X=w1277-h957-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczM9-1Y-NHr7cY3kKc2jx7w3a7MV8jA6kA5NXVyjE7DilJI5RzuyDdpIeeguOUnKRRBG4oIK-mJrNuCWuFzea6cGhqTXwrNT2lDTJxsIWlEueXfJe0QkWzyMUkcoa-JFnH7JOCwLbo_Mmd_mYZ2iQCmo=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMXEulYxFYaArBz2KEvFrkDhyTEt9cpw9WjX1gfTT_2JTkSM4WuTnRIttq0DtnH4bwbfBQiJWlTvzcDrwodDfGwcvKPaQdqiois710KBA8R7hfGR-cZi-U5BawCTWXpnSLuIMCIYcbqDKUz-O3UZDSC=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNJd_cDRtGRgCerWq1KVzKNapNAlspT5mZj-mdOFpzUnGKKmG7kTCJQPIDlRdzXM36J5vF3mHsQKDSFPI7yQSr_SkZaaZRImj2_wMYm7toWDTgpxrvc85FazoSWpTnPUljrmtF35F_OLcFCmlC_Zry7=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOKOzAVJIuRDN0VNxaSLNH5V0DeXXFKoNO9YoTQw1yt_z8gj7IR0TYtGeNVY-0MSkPRRtmENq2R1GGKbEY6_lQSl3yihRMpE7o7nZ5PcOlc1H4XuxZuc60hEIzAwR_Wqws71z2sGkAo8QDKUqW1htDJ=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMw8L3wILyc3Ffq7jmx6utWFF75FM8CeZ5WDoylns2LfpesgdD1pxKGiYpYPS0_5nhNI2Xfaj7GD8fcZea-O9We773W_7hpyawBkZ1Av6-9fdTwK4P-5sa9T7lksQzFqyDfj2nyJdTHIgC_8xWH45Sm=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPMeMdouCrTUDyK4HFYtXq3E3ckuNKCFPjmbOVQ_Gdqgp1WqksENWhHfgi4mvG3ZyNvv3aynUWSqDnWd6unR_6LJco5OtQoRyp4jSwByCdMWr2rgQLNTdMLcSIH4fiFzKeC3iJ01Yb6n5A3b3DLq4ri=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOM_fcpLlfrOu26K1AaVzFOxwxvzPmA_OX15L-URpfUqGJC_tgBdJF8XqyMw9mFgtl_G6pbZyXDNilTo-T7z8it1qsZ-pqTRLlJ2CeiKJDf3Xj0jARZsNTcNZI5hcP76v0LlOFXegAbEW39hUwGRt2y=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczP18aZCY9KRadMg2wugChRDHqI9MgkxtbO9rBRQDPzGw4gZy4zjgZpAEYlvgLU43HxldbT86xsFR4eKRcYl41RYz6KRnJFzDjEn4vE6_wdFMPBfSQwPaZz0Wo8xma9EdOdFTALY33KQabTqXOk3Onoj=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPviGVRmw48wXyJz94mUAG9A3XuGPTD_Kem6_m-We5QznxLuaTHYlMQxlZFY4egh_HgtwP3ev4DuhHmccXDO__D40Dsbhb_y3bcoV1dyZ7oB0svipJqveZcTnX1btb0icNQpyRy7kWqdi_fpZv6kAx1=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMmbmBulyTTPc62RZfmOhXZ6TpH5vVw88kxBQpeIvbF8-oIMyl5uu8MRu2KKEsTvSIlagz58_A1J5IOXz69jk3Svvrr2sxmaLPnv9LhyjrIV23CyfKkpR4ESovT9FdKEzxhNe5W7YNGvEtelR4rI3IX=w1277-h957-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNtXsyoRv3Aa1YeQTK-pxJuZj00feJxyC_vtO5BvJVph4UMgOxvA4EdeDJDO6SD2sobqe8f-_Abq97gy2DdEzTPsRpsSQ1EgEj3WpqEgGYYsdyrNdbnTdOS2mhHl7Kg3SW0L67N3eyH-ySsp8Pk2hg0=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczPN0xlodK5ud3X5jgYEolEAvoiHx1dJStjukgDbOspsX9kqwe10SQQAPZkviTivin91_3Lk3bB55zPEixv4ftgTBNk4vOXI6r901dxXNp7n65y_Vyg0nloUDuiPS972psRDVzUUz99P4v9sSDPU3Gkg=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczNtfNIi_xSZkzmNhCM_8Rp2hScACiKh2dfRlhzMhp_FJvABpmAPf3sjPWkbT38U_W5uP5QcU43OX6AFHV2KcmaUAiR1DSy-fG19GF9UyCh5hGIaTe2NojSqsG0cEZlYjoe0_ZJEFFSzWIjpjObEd4WW=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczO9HswDwYdoAOpW5J5prVFrcz_BTFKehc0VpWs-lLl9z6HePCPguyYCDMAYabeCJr9lGySUAm_gOS2HGT_tsn5YCrtakfW6nlB7UFJYdoTpccE_T5OAiD4n5zfKDhrJ8TOGrPTUa3ZDp0-HIyBdXfkl=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczMvVMp_wjIzgtLCoLRsWyXUw-4C1UebkIQk4KlpEYDSikWcL8BD7VXHmVvyKWQuXNW0ReO-IqgfprTtkou8CN4Afdi9M4ZsobCJea3-tMZVqKfP_UE43_P8hkgvSgaADcJZVaXAm8YbxyUj6rWhuMxR=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOlp9UbhhPKieTl3TJIDQwRoybe2MK0GIdgbUkM_jMBZ09Ef2xpBSd2pKRnhKRUVKc31g-BD3wbof9qbQcRGgSTJ6ydvjR1XHAZl4nwNcf1CD6jRr4EcNuxIB3-onQDhzUN33CwkHdzO9Y9RHuyJGHW=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczM-oDMhuvtiLmZnqKph7iLypSI7c6HLRA-Lji1wW_98nger0sMpTJzNhMPVDCXnV48DH5AAa2_SyRlTrN8NQQR9CxM_-FkmyL3gVjDUiZKJa8p0XtsFxaeaHxWIRLirtSADnK6Kt9aT1zQ6sl9o7y5T=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczP0-DfwyXp0dn-a7E6d2iDWh7DIqP4KstNlnKVJy2gzlXArOzVA721dxnErl7h-tO2-gnxkCKCRSif7SNWuEsvY-r2Mr3WRYaQGS0VR2xSAI8nee4Yn89TmpgwMe2i5b_pe_Q-TkMMaFEx4MMtLt-C-=w1010-h1346-s-no-gm?authuser=0"
,"https://lh3.googleusercontent.com/pw/AP1GczOSxHQz0NQyakzaVHuP9wxHAzaloMjc3poeQvGu02gSjW4uEHqn-oce3dcj-qNuByixaYCg8a90_SQwmdRJ0BptKhcv0nTCRjtGIBk7t-32zeehE_qBHWuO7eTg8lg0bqevNdldyEVPV7m1nHVkqakh=w1010-h1346-s-no-gm?authuser=0"
]

caps = ["처음 같이 찍은 사진", "처음 받은 선물", "처음 해준 요리(?)","인상깊은 남한산성"
,"첫 드라이브","최애사진","처음 같이 보낸 밤","크리스마스","커플템(내가 따라삼)","84일.","죽어가는 원동연","시즌 종료","속초최고",
"그녀는 대게마녀","반차를 제물로 여자친구 소환","200일","옷뺌김","내인생최고야장","주말농장부부느낌쓰","21세기 현대미술의 역사","2025년 역대급 여름"
,"음식 사라지기 1분 20초전","그녀의 최애 캐릭은 미피","저 집은 얼마일까?","드디어..! 드디어..!","멋쟁이들","별들의기침","낭만 미쳤다잉"
,"톰하디를 보고 난 그녀","배드민턴","토끼 반지","핸드폰 사진","유독 이쁜 날(항상 이쁘지만)"
,"불꽃놀이"
,"또산공원"
,"말괄량이 혜정"
,"음 오늘 좀 이쁜걸~?"]
col1, col2 = st.columns([1,3])
with col1:
    st.markdown("""
    <div class='message'>
    가을, 겨울, 봄, 여름 다시 가을
    </div>
    """, unsafe_allow_html=True)
with col2:
    with st.expander("🍁"):
        html_blocks = ['<div class="gallery">']
        for img, cap in zip(imgs, caps):
            html_blocks.append(
                '<div class="gallery-item">'
                '<img src="' + img + '" alt="' + cap + '">'
                '<div class="caption">' + cap + '</div>'
                '</div>'
            )
        gallery_html = "\n".join(html_blocks)
        st.markdown(gallery_html, unsafe_allow_html=True)

st.divider()


# 편지 섹션
st.markdown("## 💌")
st.markdown("""
<div class='message'>
너와 함께한 모든 순간이 선물 같아. 
사랑해 ❤️
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>- From 당신의 이름 -</div>", unsafe_allow_html=True)
