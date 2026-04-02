import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Smart Career Navigator", page_icon="🚀")

# ---------------- DATABASE ---------------- #
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# ---------------- AUTH ---------------- #
def signup(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users VALUES (NULL, ?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    user = c.fetchone()
    conn.close()
    return user and password == user[0]

# ---------------- SESSION ---------------- #
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------------- HEADER ---------------- #
st.title("🚀 Smart Career Navigator")
st.caption("Find your perfect career path with smart recommendations")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------- SIGNUP ---------------- #
if choice == "Signup":
    st.subheader("Create Account")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Signup"):
        if signup(user, pwd):
            st.success("Account created successfully!")
        else:
            st.error("User already exists")

# ---------------- LOGIN ---------------- #
elif choice == "Login":
    st.subheader("Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(user, pwd):
            st.session_state.logged_in = True
            st.session_state.username = user
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

# ---------------- MAIN APP ---------------- #
if st.session_state.logged_in:

    st.success(f"Welcome, {st.session_state.username} 👋")
    st.divider()

    interest = st.text_input("🎯 Enter your interests")
    skills = st.text_input("🛠 Enter your skills")

    if st.button("🚀 Find My Career"):

        # -------- Career Logic -------- #
        if "code" in skills.lower():
            result = "Software Developer"
        elif "design" in interest.lower():
            result = "UI/UX Designer"
        elif "data" in skills.lower():
            result = "Data Scientist"
        else:
            result = "Explore Multiple Fields"

        st.subheader("🎯 Recommended Career")
        st.success(result)

        # -------- Career Info -------- #
        career_info = {
            "Software Developer": {
                "desc": "Builds applications and systems.",
                "skills": "Python, Java, DSA, Web Development",
                "link": "https://roadmap.sh/software-engineer",
                "roadmap": ["Python Basics", "DSA", "Web Development", "Projects"]
            },
            "UI/UX Designer": {
                "desc": "Designs user-friendly interfaces.",
                "skills": "Figma, UX Principles, Creativity",
                "link": "https://roadmap.sh/design",
                "roadmap": ["Figma", "UI Principles", "UX Research", "Portfolio"]
            },
            "Data Scientist": {
                "desc": "Analyzes data and builds ML models.",
                "skills": "Python, Statistics, Machine Learning",
                "link": "https://roadmap.sh/data-scientist",
                "roadmap": ["Python", "Statistics", "ML", "Projects"]
            },
            "Explore Multiple Fields": {
                "desc": "Explore different domains.",
                "skills": "Basic Programming",
                "link": "https://roadmap.sh",
                "roadmap": ["Explore", "Learn Basics", "Choose Field"]
            }
        }

        info = career_info[result]

        st.write(f"📘 {info['desc']}")
        st.write(f"🛠 Skills Needed: {info['skills']}")
        st.markdown(f"[📍 View Detailed Roadmap]({info['link']})")

        # -------- Roadmap -------- #
        st.subheader("🛤 Learning Roadmap")
        for step in info["roadmap"]:
            st.write(f"➡ {step}")

        # -------- Skill Gap -------- #
        required_skills = {
            "Software Developer": ["python", "dsa", "html"],
            "UI/UX Designer": ["figma", "design"],
            "Data Scientist": ["python", "ml"]
        }

        user_skills = skills.lower().split()
        missing = [s for s in required_skills.get(result, []) if s not in user_skills]

        if missing:
            st.warning(f"⚠ Missing Skills: {', '.join(missing)}")

        # -------- DASHBOARD -------- #
        st.divider()
        st.subheader("📊 Career Insights Dashboard")

        # Skill Distribution
        if skills:
            skill_df = pd.DataFrame({
                "Skills": user_skills,
                "Count": [1] * len(user_skills)
            })

            st.write("### 🛠 Your Skills")
            fig1, ax1 = plt.subplots()
            ax1.bar(skill_df["Skills"], skill_df["Count"])
            ax1.set_xlabel("Skills")
            ax1.set_ylabel("Presence")
            st.pyplot(fig1)

        # Missing Skills Chart
        if missing:
            missing_df = pd.DataFrame({
                "Missing": missing,
                "Count": [1] * len(missing)
            })

            st.write("### ⚠ Missing Skills")
            fig2, ax2 = plt.subplots()
            ax2.bar(missing_df["Missing"], missing_df["Count"])
            st.pyplot(fig2)

        # Career Comparison
        st.write("### 📈 Career Comparison")
        careers = ["Software Dev", "Data Sci", "UI/UX"]
        scores = [3, 2, 2]

        fig3, ax3 = plt.subplots()
        ax3.plot(careers, scores, marker='o')
        ax3.set_ylabel("Suitability")
        st.pyplot(fig3)

    # ---------------- CHATBOT ---------------- #
    st.divider()
    st.subheader("💬 Career Assistant Chatbot")

    msg = st.text_input("Ask something...")

    if st.button("Send"):
        if "career" in msg.lower():
            st.info("Explore Software Dev, Data Science, UI/UX.")
        elif "data" in msg.lower():
            st.info("Learn Python, Statistics, ML.")
        elif "developer" in msg.lower():
            st.info("Learn Python, DSA, Web Dev.")
        elif "design" in msg.lower():
            st.info("Learn Figma, UX.")
        else:
            st.info("Ask about careers, skills, roadmap!")

    # ---------------- LOGOUT ---------------- #
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()
