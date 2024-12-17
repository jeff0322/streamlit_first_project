import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 로드 (사용자가 업로드한 파일 경로를 반영)
file_path = "/mnt/data/age2411.csv"
data = pd.read_csv(file_path)

# 데이터 전처리 (가정: 파일에 '지역', '연령', '인구수' 컬럼이 있음)
data.columns = data.columns.str.strip()  # 컬럼명 공백 제거

# Streamlit 제목과 설명
st.title("📊 우리 지역 인구 구조를 알아보자!")
st.write("우리 지역의 나이별 인구 분포를 살펴보고, 초등학교 5학년 친구들이 얼마나 있는지 알아보세요!")

# 사용자 입력: 지역 선택
region_list = data['지역'].unique().tolist()
selected_region = st.selectbox("지역을 선택하세요", region_list)

# 선택한 지역의 데이터 필터링
region_data = data[data['지역'] == selected_region]

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(region_data['연령'], region_data['인구수'], color='skyblue', label='전체 연령')

# 초등학교 5학년 연령(11세) 강조
if 11 in region_data['연령'].values:
    eleven_population = region_data[region_data['연령'] == 11]['인구수'].values[0]
    ax.bar(11, eleven_population, color='orange', label='초등학교 5학년 (11세)')

# 그래프 꾸미기
ax.set_title(f"{selected_region}의 나이별 인구 구조", fontsize=16)
ax.set_xlabel("연령", fontsize=14)
ax.set_ylabel("인구수", fontsize=14)
ax.legend()
plt.xticks(rotation=45)

# 스트림릿에 그래프 표시
st.pyplot(fig)

# 추가 정보 표시
if 11 in region_data['연령'].values:
    st.write(f"### 초등학교 5학년 (11세) 인구: {eleven_population}명")
else:
    st.write("### 초등학교 5학년 (11세) 인구 데이터가 없습니다.")
