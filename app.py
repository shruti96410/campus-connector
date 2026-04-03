import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Smart Career Navigator",
    page_icon="🚀",
    layout="wide"
)

# ---------------- DARK THEME CSS ---------------- #
st.markdown("""
<style>
/* Main background */
.stApp {
    background-color: #0E1117;
}

/* Text */
h1, h2, h3, h4, h5, h6, p, label {
    color: #FFFFFF !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1C1F26;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px;
}

/* Input fields */
.stTextInput input {
    background-color: #262730;
    color: white;
}

/* Cards look */
.block-container {
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.title("🚀 Smart Career Navigator")
st.caption("AI-Powered Career Guidance & Student Engagement Platform")
st.divider()

# ---------------- SIDEBAR ---------------- #
menu = ["Home", "Career Guidance", "Roadmap", "Dashboard", "Profile"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ---------------- #
if choice == "Home":
    st.subheader("🏠 Welcome")

    st.write("""
    Smart Career Navigator helps you:
    - 🎯 Choose the right career path  
    - 📊 Analyze skill gaps  
    - 🛣️ Get personalized roadmap  
    - 📈 Track your progress  
    """)

# ---------------- CAREER GUIDANCE ---------------- #
elif choice == "Career Guidance":
    st.subheader("🎯 Career Recommendation")

    interest = st.text_input("Enter your interest")
    skills = st.text_input("Enter your skills (comma separated)")

    if st.button("Find Career"):
        skills_lower = skills.lower()

        if "code" in skills_lower:
            career = "Software Developer"
        elif "design" in interest.lower():
            career = "UI/UX Designer"
        elif "data" in skills_lower:
            career = "Data Scientist"
        else:
            career = "Explore Multiple Fields"

        st.success(f"Recommended Career: {career}")

        st.session_state["career"] = career
        st.session_state["skills"] = skills_lower

# ---------------- ROADMAP ---------------- #
elif choice == "Roadmap":
    st.subheader("🛣️ Personalized Roadmap")

    career = st.session_state.get("career", None)
    skills = st.session_state.get("skills", "")

    if not career:
        st.warning("Please go to Career Guidance first!")
    else:
        roadmap = {
            "Software Developer": [
                "Week 1-2: Learn Python Basics",
                "Week 3-4: Data Structures",
                "Week 5-6: Web Development",
                "Week 7-8: Build Projects"
            ],
            "UI/UX Designer": [
                "Week 1-2: Learn Design Principles",
                "Week 3-4: Figma Basics",
                "Week 5-6: UX Research",
                "Week 7-8: Build Portfolio"
            ],
            "Data Scientist": [
                "Week 1-2: Python + Pandas",
                "Week 3-4: Statistics",
                "Week 5-6: Machine Learning",
                "Week 7-8: Projects"
            ]
        }

        steps = roadmap.get(career, ["Explore multiple domains"])

        for step in steps:
            st.write("✔", step)

# ---------------- DASHBOARD ---------------- #
elif choice == "Dashboard":
    st.subheader("📊 Career Progress Dashboard")

    col1, col2, col3 = st.columns(3)
    col1.metric("Skills Learned", 5)
    col2.metric("Projects Done", 2)
    col3.metric("Progress", "60%")

    categories = ["Skills", "Projects", "Progress"]
    values = [5, 2, 60]

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title("Progress Overview")
    st.pyplot(fig)

# ---------------- PROFILE ---------------- #
elif choice == "Profile":
    st.subheader("👤 Profile")

    name = st.text_input("Name")
    branch = st.text_input("Branch")
    goal = st.text_input("Career Goal")

    if st.button("Save Profile"):
        st.success("Profile saved successfully!")

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown("Made by Shruti Verma 🚀")

 
