import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# 파일 업로더
st.title("📊 우리 지역 인구 구조를 알아보자!")
data_path = 


if uploaded_file is not None:
    # 데이터 읽기
    data = pd.read_csv(uploaded_file)
    data.columns = data.columns.str.strip()  # 컬럼명 공백 제거

    # 지역 선택
    region_list = data['지역'].unique().tolist()
    selected_region = st.selectbox("지역을 선택하세요", region_list)

    # 데이터 필터링
    region_data = data[data['지역'] == selected_region]

    # 그래프 생성
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(region_data['연령'], region_data['인구수'], color='skyblue', label='전체 연령')

    if 11 in region_data['연령'].values:
        eleven_population = region_data[region_data['연령'] == 11]['인구수'].values[0]
        ax.bar(11, eleven_population, color='orange', label='초등학교 5학년 (11세)')

    ax.set_title(f"{selected_region}의 나이별 인구 구조", fontsize=16)
    ax.set_xlabel("연령", fontsize=14)
    ax.set_ylabel("인구수", fontsize=14)
    ax.legend()
    plt.xticks(rotation=45)

    st.pyplot(fig)

    if 11 in region_data['연령'].values:
        st.write(f"### 초등학교 5학년 (11세) 인구: {eleven_population}명")
    else:
        st.write("### 초등학교 5학년 (11세) 인구 데이터가 없습니다.")
else:
    st.warning("CSV 파일을 업로드해주세요.")
