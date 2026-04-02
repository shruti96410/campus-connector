import streamlit as st
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Smart Career Navigator", page_icon="🎓")

# ---------------- HEADER ---------------- #
st.title("🎓 Smart Career Navigator")
st.caption("Connecting students, clubs, and opportunities")
st.divider()

# ---------------- SIDEBAR ---------------- #
menu = ["Home", "Events", "Clubs", "Profile", "Dashboard"]
choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ---------------- #
if choice == "Home":
    st.subheader("🏠 Welcome to Campus Connector")

    st.write("""
    Smart Career Navigator helps students:
    - Discover events 📅
    - Join clubs 🎯
    - Stay connected 🤝
    """)

    if st.button("Explore Events"):
        st.success("Go to Events section from sidebar!")

# ---------------- EVENTS ---------------- #
elif choice == "Events":
    st.subheader("📅 Upcoming Events")

    events = [
        {"name": "Hackathon 2026", "date": "10 April"},
        {"name": "AI Workshop", "date": "15 April"},
        {"name": "Tech Seminar", "date": "20 April"}
    ]

    for event in events:
        st.write(f"🔹 {event['name']} - {event['date']}")
        if st.button(f"Join {event['name']}"):
            st.success(f"You joined {event['name']}!")

# ---------------- CLUBS ---------------- #
elif choice == "Clubs":
    st.subheader("🎯 College Clubs")

    clubs = ["Coding Club", "AI Club", "Design Club", "Robotics Club"]

    for club in clubs:
        st.write(f"🔸 {club}")
        if st.button(f"Join {club}"):
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

    # Sample data
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
