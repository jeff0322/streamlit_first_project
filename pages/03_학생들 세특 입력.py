import streamlit as st

# 학생 목록
students = ["학생1", "학생2", "학생3"]

# 특기사항 선택 항목과 대응되는 내용
remarks = {
    "SW 나눔축제": "SW 나눔축제에 적극적으로 참여하며 창의적인 아이디어를 제시하였습니다.",
    "프로젝트": "팀 프로젝트에서 주도적인 역할을 맡아 협업 능력을 발휘하였습니다.",
    "수업태도": "수업 시간에 성실하게 참여하며 적극적으로 질문하고 학습 태도가 우수하였습니다."
}

# 제목
st.title("학생 특기사항 생성기")

# 학생 선택
selected_student = st.selectbox("학생을 선택하세요:", students)

# 항목 선택
st.subheader("특기사항 항목 선택")
selected_remarks = st.multiselect(
    "특기사항에 포함할 항목을 선택하세요:",
    options=list(remarks.keys()),
    default=[]
)

# 결과 출력
st.subheader("생성된 특기사항")
if selected_remarks:
    # 선택한 특기사항을 한 줄로 합침
    combined_remarks = " ".join(remarks[item] for item in selected_remarks)
    
    # 글자 수 계산
    char_count = len(combined_remarks)
    
    # 출력
    st.write(f"**{selected_student}**에 대한 특기사항:")
    st.write(combined_remarks)
    st.write(f"총 글자 수: {char_count}자")
else:
    st.write("특기사항 항목을 선택해주세요.")
