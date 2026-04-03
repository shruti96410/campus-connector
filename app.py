import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Campus Connector", page_icon="🎓")

# ---------------- DARK CUSTOM CSS ---------------- #
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}

.stApp {
    background-color: #0E1117;
}

h1, h2, h3, h4 {
    color: #FFFFFF;
}

.stButton>button {
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    border-radius: 10px;
    padding: 10px;
}

.stTextInput>div>div>input {
    background-color: #262730;
    color: white;
}

.css-1d391kg {
    background-color: #262730;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.title("🎓 Campus Connector")
st.caption("Connecting students, clubs, and opportunities")
st.divider()

# ---------------- SIDEBAR ---------------- #
menu = ["Home", "Events", "Clubs", "Profile", "Dashboard"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ---------------- #
if choice == "Home":
    st.subheader("🏠 Welcome to Campus Connector")

    st.write("""
    Campus Connector helps students:
    - Discover events 📅  
    - Join clubs 🎯  
    - Stay connected 🤝  
    """)

# ---------------- EVENTS ---------------- #
elif choice == "Events":
    st.subheader("📅 Upcoming Events")

    events = [
        {"name": "Hackathon 2026", "date": "10 April"},
        {"name": "AI Workshop", "date": "15 April"},
        {"name": "Tech Seminar", "date": "20 April"}
    ]

    for i, event in enumerate(events):
        st.markdown(f"### {event['name']}")
        st.info(f"📅 Date: {event['date']}")

        if st.button("Join Event", key=f"event_{i}"):
            st.success(f"You joined {event['name']}!")

# ---------------- CLUBS ---------------- #
elif choice == "Clubs":
    st.subheader("🎯 College Clubs")

    clubs = ["Coding Club", "AI Club", "Design Club", "Robotics Club"]

    for i, club in enumerate(clubs):
        st.markdown(f"### {club}")

        if st.button("Join Club", key=f"club_{i}"):
            st.success(f"You joined {club}!")

# ---------------- PROFILE ---------------- #
elif choice == "Profile":
    st.subheader("👤 Student Profile")

    name = st.text_input("Enter your name")
    branch = st.text_input("Branch")
    interests = st.text_input("Interests")

    if st.button("Save Profile"):
        st.success("Profile saved successfully!")

# ---------------- DASHBOARD ---------------- #
elif choice == "Dashboard":
    st.subheader("📊 Campus Insights Dashboard")

    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Students", 120)
    col2.metric("Events", 15)
    col3.metric("Clubs", 6)

    # Bar Chart
    categories = ["Students", "Events", "Clubs"]
    values = [120, 15, 6]

    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title("Campus Overview")
    st.pyplot(fig)

    # Pie Chart
    st.write("### 📌 Participation Overview")
    fig2, ax2 = plt.subplots()
    ax2.pie(values, labels=categories, autopct='%1.1f%%')
    st.pyplot(fig2)

# ---------------- FOOTER ---------------- #
st.markdown("---")
st.markdown("Made by Shruti Verma 🚀")
