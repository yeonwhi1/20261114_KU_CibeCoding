import streamlit as st

# 1. 기사 제목
st.title("인공지능, 학생들의 공부 방법을 바꾸다")

# 2. 작성자와 날짜 (캡션)
st.caption("작성자: 연휘 | 2026-01-16")

# 3. 이미지 (URL 사용)
st.image(
    "https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg",
    caption="AI와 함께 공부하는 학생들",
    use_column_width=True
)

# 4. 본문 내용 (마크다운)
st.markdown(
"""
전 세계 학교에서 인공지능(AI)을 활용한 학습 도구가 빠르게 확산되고 있습니다.  
특히 개인의 학습 속도와 수준에 맞추어 문제를 추천해 주는 시스템이 큰 관심을 받고 있습니다.

전문가들은 AI가 **반드시 교사를 대체하는 것이 아니라, 교사를 보조하는 도구**가 될 것이라고 전망합니다.  
학생들은 반복 학습과 피드백을 AI에게 맡기고, 교사는 더 창의적인 활동과 토론에 집중할 수 있게 됩니다.

또한, 학습 데이터가 쌓이면서 학생 개개인의 **취약한 개념, 강점, 학습 패턴**을 분석할 수 있어  
보다 정밀한 맞춤형 교육이 가능해질 것으로 기대됩니다.
"""
)

# 5. 관련 정보 박스 (info)
st.info(
"""
참고: 교육 분야에서 많이 사용되는 AI 기술들
- 학습 추천 시스템 (Learning Recommender System)
- 자동 채점 및 피드백
- 학습 행동 분석(러닝 애널리틱스)
- 인터랙티브 튜터 챗봇
"""
)

# 6. 코드나 데이터 예시 (code)
example_code = """
import random

students = ["연휘", "민수", "지현", "서준"]
scores = {name: random.randint(60, 100) for name in students}

# 80점 이상인 학생만 추천 학습 코스를 제공
recommended = {name: s for name, s in scores.items() if s >= 80}

print("전체 점수:", scores)
print("추천 학습 제공 대상:", recommended)
"""

st.code(example_code, language="python")
