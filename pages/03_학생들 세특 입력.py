import streamlit as st
import pandas as pd

# 특기사항 선택 항목과 대응되는 내용
remarks = {
    "SW 나눔축제": "SW 나눔축제에 적극적으로 참여하며 창의적인 아이디어를 제시하였습니다.",
    "프로젝트": "팀 프로젝트에서 주도적인 역할을 맡아 협업 능력을 발휘하였습니다.",
    "수업태도": "수업 시간에 성실하게 참여하며 적극적으로 질문하고 학습 태도가 우수하였습니다."
}

# 제목
st.title("학생 특기사항 생성기")

# CSV 파일 업로드
uploaded_file = st.file_uploader("학생과 특기사항이 담긴 CSV 파일을 업로드하세요:", type=["csv"])

if uploaded_file is not None:
    # CSV 파일 읽기
    data = pd.read_csv(uploaded_file)
    
    # 학생 목록 추출
    if "학생" in data.columns:
        students = data["학생"].unique().tolist()
        
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
    else:
        st.error("CSV 파일에 '학생' 열이 없습니다. 올바른 파일을 업로드해주세요.")
else:
    st.write("CSV 파일을 업로드하면 학생 목록을 불러올 수 있습니다.")
