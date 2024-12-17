import streamlit as st

# 학생 목록
students = ["학생1", "학생2", "학생3"]

# 특기사항 세부 내용 (이모지 추가)
remarks = {
    "SW 나눔축제 🖥️": {
        "상": "🌟 SW 나눔축제에서 뛰어난 창의력을 발휘하며 우수한 성과를 거두었습니다.",
        "중": "✨ SW 나눔축제에 성실히 참여하며 적극적으로 의견을 제시하였습니다.",
        "하": "⚡ SW 나눔축제에 참여하였으나 개선의 여지가 있었습니다."
    },
    "프로젝트 💼": {
        "상": "🌟 프로젝트에서 주도적인 역할을 수행하며 팀의 성과를 크게 향상시켰습니다.",
        "중": "✨ 프로젝트에서 협업에 기여하며 책임감을 보였습니다.",
        "하": "⚡ 프로젝트에 참여했으나 더 많은 노력이 필요했습니다."
    },
    "수업태도 📚": {
        "상": "🌟 수업에 매우 적극적으로 참여하며 학습 태도가 우수했습니다.",
        "중": "✨ 수업에 성실히 참여하며 꾸준히 노력하는 모습을 보였습니다.",
        "하": "⚡ 수업 참여가 다소 부족하여 개선이 필요합니다."
    }
}

# 제목
st.title("📝 학생 특기사항 생성기")

# 학생 선택
selected_student = st.selectbox("👩‍🎓 학생을 선택하세요:", students)

# 항목 선택 및 세부 단계 선택
st.subheader("🎯 특기사항 항목 선택")
selected_remarks = {}

for category, levels in remarks.items():
    selected_level = st.selectbox(
        f"{category}에 대한 평가를 선택하세요:",
        options=["선택 안 함"] + list(levels.keys()),
        index=0
    )
    if selected_level != "선택 안 함":
        selected_remarks[category] = levels[selected_level]

# 결과 출력
st.subheader("✨ 생성된 특기사항")
if selected_remarks:
    combined_remarks = " ".join(selected_remarks.values())
    char_count = len(combined_remarks)
    
    st.write(f"**{selected_student}**에 대한 특기사항: 🎉")
    st.write(f"💡 {combined_remarks}")
    st.write(f"🖋️ 총 글자 수: {char_count}자")
else:
    st.write("🌸 특기사항 항목을 선택해주세요!")
