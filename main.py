import streamlit as st

# MBTI 유형과 관련된 설명 데이터
data = {
    "ISTJ": {
        "career": "📊 효율적인 분석가로서 회계사, 행정가, 공무원 등 체계적이고 규칙적인 직업에서 두각을 나타냅니다!",
        "compatibility": "💡 ENFP와 같이 창의적이고 유연한 사람과 팀을 이루면 완벽한 균형을 만들어냅니다."
    },
    "ISFJ": {
        "career": "🤝 타인을 돕는 데 열정을 가진 ISFJ는 간호사, 교사, 상담사 등에서 빛을 발합니다!",
        "compatibility": "✨ ENTP 같은 혁신적인 파트너와 함께라면 서로의 강점을 극대화할 수 있습니다."
    },
    "INFJ": {
        "career": "🌟 깊은 통찰력을 가진 INFJ는 작가, 심리학자, 예술가 등에서 그들의 비전을 실현합니다.",
        "compatibility": "💬 ENFP와 함께라면 꿈을 현실로 만드는 멋진 팀을 이룰 수 있습니다."
    },
    "INTJ": {
        "career": "📈 전략적 사고를 가진 INTJ는 과학자, 엔지니어, 기업가 같은 분야에서 활약합니다!",
        "compatibility": "🔥 ENFP와 협력하면 창의성과 실행력이 조화를 이룹니다."
    },
    "ISTP": {
        "career": "🛠️ 현실적이고 문제 해결에 강한 ISTP는 엔지니어, 기술자, 탐정 같은 직업에서 뛰어납니다.",
        "compatibility": "🌈 ESFJ 같은 사교적인 파트너와 함께라면 ISTP의 기술이 더욱 빛납니다."
    },
    "ISFP": {
        "career": "🎨 예술적 감각이 뛰어난 ISFP는 디자이너, 음악가, 요리사 같은 분야에서 창의성을 발휘합니다.",
        "compatibility": "🌟 ESTJ와 같은 계획적인 파트너와 조화를 이루며 성장할 수 있습니다."
    },
    "INFP": {
        "career": "📝 이상주의적인 INFP는 작가, 예술가, 상담사 등에서 그들의 가치를 실현합니다!",
        "compatibility": "🤝 ENTJ 같은 리더형과 함께라면 비전을 실행에 옮길 수 있습니다."
    },
    "INTP": {
        "career": "🔍 지적 호기심이 넘치는 INTP는 연구원, 개발자, 철학자 같은 분야에서 독창성을 발휘합니다.",
        "compatibility": "🎯 ENTJ 같은 체계적인 파트너와 협력하면 상상을 현실로 바꿀 수 있습니다."
    },
    "ESTP": {
        "career": "🎯 모험적이고 에너지가 넘치는 ESTP는 세일즈, 이벤트 플래너, 기업가로 활약합니다!",
        "compatibility": "🌸 ISFJ 같은 따뜻한 지원형 파트너와 함께하면 시너지 효과를 냅니다."
    },
    "ESFP": {
        "career": "🎤 사람들과 어울리기를 좋아하는 ESFP는 배우, 연예인, 마케터로 두각을 나타냅니다!",
        "compatibility": "💼 ISTJ 같은 계획적인 파트너와 함께라면 더욱 큰 성취를 이룰 수 있습니다."
    },
    "ENFP": {
        "career": "🌈 창의적이고 열정적인 ENFP는 마케터, 작가, 강연자 같은 직업에서 빛납니다!",
        "compatibility": "🔗 INTJ 같은 전략가와 함께라면 아이디어를 현실로 만듭니다."
    },
    "ENTP": {
        "career": "🚀 혁신적이고 도전적인 ENTP는 기업가, 변호사, 발명가로 성공합니다!",
        "compatibility": "🌟 INFJ 같은 통찰력 있는 파트너와 협력하면 큰 변화를 이끌어냅니다."
    },
    "ESTJ": {
        "career": "📋 책임감이 강한 ESTJ는 관리자, 군인, 공무원으로 탁월합니다!",
        "compatibility": "🎨 ISFP 같은 창의적인 파트너와 함께하면 완벽한 팀워크를 이룹니다."
    },
    "ESFJ": {
        "career": "🤗 사교적이고 따뜻한 ESFJ는 간호사, 교사, 이벤트 코디네이터로 잘 어울립니다!",
        "compatibility": "🛠️ ISTP 같은 문제 해결형 파트너와 함께라면 강력한 팀이 됩니다."
    },
    "ENFJ": {
        "career": "🌍 타인을 이끄는 데 탁월한 ENFJ는 코치, 상담가, 지도자로 활약합니다!",
        "compatibility": "🔬 INTP 같은 지적인 파트너와 함께라면 큰 성공을 거둘 수 있습니다."
    },
    "ENTJ": {
        "career": "🏆 리더십이 강한 ENTJ는 기업가, CEO, 변호사로 최적입니다!",
        "compatibility": "🎨 INFP 같은 창의적인 파트너와 함께라면 이상을 현실로 만듭니다."
    }
}

# Streamlit 앱 구성
st.title("✨ MBTI로 알아보는 직업과 궁합! ✨")

# 드롭다운 메뉴
selected_mbti = st.selectbox(
    "당신의 MBTI를 선택하세요!",
    list(data.keys())
)

# 결과 표시
if selected_mbti:
    st.subheader(f"당신의 MBTI: {selected_mbti}")
    st.write(data[selected_mbti]["career"])
    st.write(data[selected_mbti]["compatibility"])
