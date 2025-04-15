import streamlit as st
from processing.law_processor import process_laws, get_law_list_from_api

st.title("📘 부칙 개정 도우미 (전체 목록 + 링크)")

search_word = st.text_input("🔍 찾을 단어", placeholder="예: 지방법원")

if st.button("🚀 시작하기"):
    if not search_word:
        st.warning("찾을 단어를 입력해주세요.")
    else:
        with st.spinner("법령 검색 중..."):
            laws = get_law_list_from_api(search_word)
            st.success(f"✅ 총 {len(laws)}개의 법령을 찾았습니다.")
            for law in laws:
                st.markdown(f"- [{law['법령명']}]({law['URL']})", unsafe_allow_html=True)
