 # pip install -r requirement.txt
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import plotly.graph_objects as go

from io import BytesIO



valid_usernames = {'balaji': 'password123', 'kannan': 'parentpass', 'leo': 'tutorpass','super_admin':'adminpass'}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

def login(username, password):
    if valid_usernames.get(username) == password:
        st.session_state.logged_in = True
        st.session_state.user_role = username
    else:
        st.error("Incorrect username or password")

def logout():
    st.session_state.logged_in = False
    st.session_state.user_role = None

def login_page():
    col1, col2, col3 = st.columns([0.2, 0.8, 0.1])
    with col1:
        #st.write("\n")
        st.write("\n")
        # st.image(r"C:\Users\XY663FG\Downloads\Pointed_LogoOutputs\Pointed_WhiteFull.jpg", width=150)

    with col2:
        #st.markdown("<h1 style='text-align: center; color: black;'>Pointed Educational Solutions</h1>", unsafe_allow_html=True)
        st.image(r"C:/Users/XY663FG/Downloads/GRADIENT BLACK.png", use_column_width=True)
    with col3:
        st.write("")


    #col1, col2, col3 = st.columns([1, 2, 1])
    #with col2:
    #st.title("Project    - :blue[REDE]")
    # st.caption("""Plot No. 51, Padmavathy Nagar, Rajajipuram, 
    #         Near Shree Nikethan Mat. School (Back Gate), 
    #         Tiruvallur - 602001""")
    # st.write("\n")

    page_bg_color = """
    <style>
    .stApp {
        background-color: #B3D9FF;
    }
    </style>
    """
    st.write("\n")
 
    st.markdown(page_bg_color, unsafe_allow_html=True)

    #role = st.selectbox('Login as:', ['Select Role', 'Student', 'Parent', 'Tutor'])
    role = None
    col4, col1, col2, col3, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
    
    with col4:
        if st.button('Student'):
            role = 'Student'

    with col2:
        if st.button('Tutor'):
            role = 'Tutor'

    with col5:
        if st.button('Parent'):
            role = 'Parent'

    with col6:
        if st.button('admin'):
            role = 'admin'

    if 'role' in locals():
    #if role != 'Select Role':
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.button("Submit"):
            login(username.lower(), password)

    st.markdown("""
        <style>
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        .main {
            flex: 1;
        }
        .footer {
            background-color: #2B2B4D;
            color: white;
            padding: 20px 0;
            width: 100%;
        }
        .footer .container {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
        }
        .footer .container div {
            flex: 1;
            margin: 10px;
        }
        .footer .container div h3 {
            font-weight: bold;
            margin-bottom: 15px;
        }
        .footer .container div ul {
            list-style: none;
            padding: 0;
        }
        .footer .container div ul li {
            margin: 5px 0;
        }
        .footer .container div ul li a {
            color: white;
            text-decoration: none;
        }
        .footer .container div ul li a:hover {
            text-decoration: underline;
        }
        .footer .social-icons a {
            margin-right: 10px;
            color: white;
        }
        .footer .social-icons a i {
            font-size: 18px;
        }
        .footer .bottom-text {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #CCCCCC;
        }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    <br><br>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="footer">
            <div class="container">
                <div>
                    <h3>myScheme</h3>
                    <p>Powered by</p>
                    <p>Pointed Educational Solutions (PES)<br>
                    Redefined Education (REDE)<br>
                    Educational Institute </p>
                    <div class="social-icons">
                        <a href="#"><i class="fa fa-linkedin"></i></a>
                        <a href="#"><i class="fa fa-facebook"></i></a>
                        <a href="#"><i class="fa fa-twitter"></i></a>
                        <a href="#"><i class="fa fa-instagram"></i></a>
                    </div>
                </div>
                <div>
                    <h3>Quick Links</h3>
                    <ul>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact Us</a></li>
                        <li><a href="#">Screen Reader</a></li>
                        <li><a href="#">Accessibility Statement</a></li>
                        <li><a href="#">Frequently Asked Questions</a></li>
                        <li><a href="#">Disclaimer</a></li>
                        <li><a href="#">Terms & Conditions</a></li>
                    </ul>
                </div>
                <div>
                    <h3>Useful Links</h3>
                    <div style="display: flex; flex-wrap: wrap;">
                        <img src="https://example.com/link1.png" width="50" style="margin: 5px;">
                        <img src="https://example.com/link2.png" width="50" style="margin: 5px;">
                        <img src="https://example.com/link3.png" width="50" style="margin: 5px;">
                        <!-- Add more images as required -->
                    </div>
                </div>
                <div>
                    <h3>Get in touch</h3>
                    <p>Location<br>
                    <p>Plot No. 51, Padmavathy Nagar, Rajajipuram <br>
                    Near Shree Nikethan Mat. School (Back Gate) Thiruvallur, chennai - 110003, India</p>
                </div>
            </div>
            <div class="bottom-text">
                Last Updated On : 15/08/2024 | v-2.1.9
            </div>
        </div>
    """, unsafe_allow_html=True)


def login_page_2():
    from PIL import Image
    st.set_page_config(page_title="REDE Sign Up", layout="centered")
    image = Image.open(r"C:\Users\XY663FG\Downloads\login.jpg")  
    #col1, col2 = st.columns([1, 1])
    image_path = r"C:\Users\XY663FG\Downloads\login.jpg"

    col1, col2 = st.columns([2, 3])

# CSS to make the image column fill the entire height
    st.markdown(
        f"""
        <style>
        .full-height-image {{
            object-fit: cover;
            width: 100%;
            height: 100vh;
        }}
        .css-18e3th9 {{
            flex-grow: 1;
            width: 100%;
            height: 100vh;
            padding: 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the image in the left column with full height
    with col1:
        st.image(image)
        #st.markdown(f'<img src="{image_path}" class="full-height-image">', unsafe_allow_html=True)

    with col2:
        st.markdown("# Sign up")
        st.markdown("Join Redefined Education for free as a")

        #selected_role = st.radio("", ("Learner", "Teacher", "Parent"), index=2)
        role = None
        col1, col2, col3= st.columns([1, 1, 1])
        
        with col1:
            if st.button('Student'):
                role = 'Student'

        with col2:
            if st.button('Tutor'):
                role = 'Tutor'

        with col3:
            if st.button('Parent'):
                role = 'Parent'

        if 'role' in locals():
        #if role != 'Select Role':
            username = st.text_input("User Name")
            password = st.text_input("Password", type='password')
            if st.button("Submit"):
                login(username.lower(), password)
        st.button("Continue with Google")
        st.button("Continue with Facebook")
        st.button("Continue with Apple")
        st.button("Sign up with Email")

        st.markdown("[Already have an account?](#)")

    st.markdown("""
        <style>
            .support-text {
                position: absolute;
                bottom: 20px;
                left: 20px;
                color: white;
                font-size: 20px;
            }
        </style>
        <div class="support-text">
            Support your child’s learning through Pointed Educational Solutions
        </div>
    """, unsafe_allow_html=True)


def feed_page():
    # Example posts
    posts = [
        {"text": "Had a great day!", "time": "2024-08-14 18:45:00"},
        {"text": "Excited about the new project launch tomorrow!", "time": "2024-08-13 09:30:00"},
        {"text": "Just finished a great book on AI and machine learning.", "time": "2024-08-12 14:20:00"},
    ]

    # Page Header
    st.markdown("---")
    st.markdown("""
        <style>
        .header {
            background-color: #3b5998;
            color: white;
            padding: 10px;
            font-size: 24px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
        <div class="header">Redefined Education</div>
    """, unsafe_allow_html=True)

    # Check if the user is a super admin
    if 'role' not in st.session_state:
        st.session_state.role = 'user'  # Default role is 'user'; change to 'super_admin' for testing

    if st.session_state.role == 'super_admin':
        # Post input section (enabled for super admin)
        st.subheader("Create Post")
        new_post = st.text_area("What's on your mind?", height=100)
        if st.button("Post"):
            if new_post:
                # Normally, you would save this post to a database
                posts.insert(0, {"text": new_post, "time": "2024-08-14 18:45:00"})
                st.success("Post added successfully!")
            else:
                st.warning("Post cannot be empty.")
    else:
        # Display a message if the user is not a super admin
        st.warning("You do not have the authority to post.")

    # Displaying the feed
    st.subheader("News Feed")
    for i, post in enumerate(posts):
        st.markdown("""
            <style>
            .post-container {
                background-color: #f0f2f5;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 15px;
            }
            .post-header {
                font-weight: bold;
                font-size: 16px;
                margin-bottom: 5px;
            }
            .post-time {
                color: #555;
                font-size: 12px;
                margin-bottom: 10px;
            }
            .post-text {
                font-size: 14px;
            }
            </style>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="post-container">
                <div class="post-header">REDE</div>
                <div class="post-time">{post['time']}</div>
                <div class="post-text">{post['text']}</div>
            </div>
        """, unsafe_allow_html=True)
        col_like, col_share, col_reply = st.columns([1, 1, 1])
        with col_like:
            if st.button("👍 Like", key=f"like_{i}"):
                st.write("You liked this!")

        with col_share:
            if st.button("🔗 Share", key=f"share_{i}"):
                st.write("Share button clicked!")

        with col_reply:
            if st.button("💬 Reply", key=f"reply_{i}"):
                st.write("Reply button clicked!")
def student_forum_page():
    st.markdown("---")

    st.sidebar.markdown("### Project")
    st.sidebar.button(":blue[General]", key="space_data_ai_ml")
    st.sidebar.button(":blue[Project 1]", key="alumni_gl_connect")
    st.sidebar.button(":blue[Project 2]", key="alumni_gl_connect_1")
    #st.sidebar.markdown("### Expertise")
    #st.sidebar.button("Expertise", key="alumni_gl_connect")
    st.sidebar.markdown("**Terms** · © Copyright 2024")

    for _ in range(5):  
        st.sidebar.write("")

    logout_container = st.sidebar.container()

    with logout_container:
        if st.sidebar.button("Log Out", key="logout_bottom"):
            logout()
            st.experimental_rerun()
    logout_container.markdown('<div class="logout-container"></div>', unsafe_allow_html=True)


    st.title(":sunglasses :blue[Balaji Kannan]")
    st.subheader("St.Joseph Matric Hr Sec School")
    #st.subheader("Entrepreneurship")
    st.markdown("---")

    col1, col2 = st.columns([0.7, 0.3])

    with col1:
        st.subheader("What's on your mind?")

        with st.form(key="new_discussion"):
            user_input = st.text_area("Post your thoughts or questions here...", height=20)
            submit_button = st.form_submit_button(label="Post")

        #st.markdown("### Newest")

        if submit_button:
            st.write("**Balaji**")
            st.caption("10 sec ago · Posted in Entrepreneurship")
            st.write(user_input)
            st.markdown("---")

        st.write("**Sathish Kumar**")
        st.caption("3 minutes ago · Posted in Entrepreneurship")
        st.write("Entrepreneurship is the process by which either an individual or a team identifies a business opportunity and acquires and deploys the necessary resources required for its exploitation.")

        col_img, col_text, col_actions = st.columns([0.1, 0.6, 0.3])

        image_path = r"C:\Users\XY663FG\Downloads/error_status.png"
        with col_img:
            st.image(image_path, width=50)

        with col_text:
            st.write("**error_code.png**")
            st.caption("83.71KB")

        with col_actions:
            view_button = st.button("👁️", key="view")
            st.download_button("⬇️", data=open(image_path, 'rb'), file_name="error_code.png", key="download")

            if view_button:
                st.image(image_path, caption="error_code.png", width=500)
        col_like, col_share, col_reply = st.columns([1, 1, 1])

        with col_like:
            if st.button("👍 Like"):
                st.write("You liked this!")

        with col_share:
            if st.button("🔗 Share"):
                st.write("Share button clicked!")

        with col_reply:
            if st.button("💬 Reply"):
                st.write("Reply button clicked!")

    with col2:
        st.markdown("")
        st.markdown("### Project Info")

        
        st.write("Project Name : XXXX")
        st.write("Tutor : YYYY")
        st.write("Student Classification : ZZZZ")

        # st.markdown("---")
        # st.markdown("### Tags")
        # st.button("Business")
        # st.button("Weekend Challenge ⚡")
        # st.button("Statistics")
        # st.button("Question of the Day 💡")
        # st.button("Entrepreneurship")

def student_org_tree():
    students = [
    {"name": "Aravinth", "photo": "https://via.placeholder.com/150"},
    {"name": "Bala", "photo": "https://via.placeholder.com/150"},
    {"name": "Balaji", "photo": "https://via.placeholder.com/150"},
    {"name": "Barath", "photo": "https://via.placeholder.com/150"},
    {"name": "Deepak", "photo": "https://via.placeholder.com/150"},
    {"name": "Manivannan", "photo": "https://via.placeholder.com/150"},
    {"name": "Leo", "photo": "https://via.placeholder.com/150"},
    {"name": "Sandy", "photo": "https://via.placeholder.com/150"},
    {"name": "Ice", "photo": "https://via.placeholder.com/150"},
    {"name": "Nandhini", "photo": "https://via.placeholder.com/150"},
    ]

    st.write("\n")
    skills = ["Entrepreneur", "Speaking", "Leadership", "Creativity"]
    st.write("\n")

    selected_skill = None
    cols = st.columns(len(skills))
    for i, skill in enumerate(skills):
        if cols[i].button(skill):
            selected_skill = skill

    if selected_skill:
        st.write(f"Students with skill: {selected_skill}")
        num_columns = 3
        cols = st.columns(num_columns)
        for i, student in enumerate(students):
            with cols[i % num_columns]:
                st.image(student["photo"], width=100)
                if st.button(student["name"]):
                    st.write(f"{student['name']} selected")


def logout():
    st.session_state.clear()

def tutor_forum_page():
    st.markdown("---")
    st.sidebar.markdown("### Skills")

    if st.sidebar.button("Entrepreneurship", key="btn_entrepreneurship"):
        st.session_state.selected_page = "entrepreneurship"
    if st.sidebar.button("Speaking", key="btn_speaking"):
        st.session_state.selected_page = "speaking"

    st.sidebar.markdown("### Alumni")
    st.sidebar.button("REDE Alumni", key="btn_alumni")
    st.sidebar.markdown("**Terms** · © Copyright 2024")

    for _ in range(15):
        st.sidebar.write("")

    logout_container = st.sidebar.container()
    with logout_container:
        if st.sidebar.button("Log Out", key="logout_bottom"):
            logout()
            st.experimental_rerun()
    logout_container.markdown('<div class="logout-container"></div>', unsafe_allow_html=True)

    if "entrepreneurship_response" not in st.session_state:
        st.session_state["entrepreneurship_response"] = ""
    if "speaking_response" not in st.session_state:
        st.session_state["speaking_response"] = ""

    def submit_entrepreneurship_response():
        st.session_state["entrepreneurship_response"] = st.session_state.get("user_response_entrepreneurship", "")

    def submit_speaking_response():
        st.session_state["speaking_response"] = st.session_state.get("user_response_speaking", "")

    tab1, tab2 = st.tabs(["Forum", "Students"])

    with tab1:
        col1, col2 = st.columns([0.7, 0.3])

        with col1:
            if "selected_page" in st.session_state:
                if st.session_state.selected_page == "entrepreneurship":
                    st.title("Entrepreneurship")
                    st.markdown("##### Newest")
                    st.write("**Sathish Kumar**")
                    st.caption("3 minutes ago · Posted in Entrepreneurship")
                    st.write("Entrepreneurship is the process by which either an individual or a team identifies a business opportunity and acquires and deploys the necessary resources required for its exploitation.")

                    # Display the form within a button-click context
                    if st.button('Respond', key="btn_respond_entrepreneurship"):
                        with st.form(key="new_discussion_entrepreneurship"):
                            st.text_area(" ", key="user_response_entrepreneurship", height=100)
                            st.form_submit_button(label="Post", on_click=submit_entrepreneurship_response)

                    if st.session_state["entrepreneurship_response"]:
                        st.write("**Tutor Response (Leo):**")
                        st.write(st.session_state["entrepreneurship_response"])
                        st.write("---")

                if st.session_state.selected_page == "speaking":
                    st.title("Speaking")
                    st.markdown("##### Newest")
                    st.write("**Balaji**")
                    st.caption("3 minutes ago · Posted in Speaking")
                    st.write("How to improve pronunciation.")

                    if st.button('Respond', key="btn_respond_speaking"):
                        with st.form(key="new_discussion_speaking"):
                            st.text_area(" ", key="user_response_speaking", height=100)
                            st.form_submit_button(label="Post", on_click=submit_speaking_response)

                    if st.session_state["speaking_response"]:
                        st.write("**Tutor Response (Leo):**")
                        st.write(st.session_state["speaking_response"])
                        st.write("---")

        with col2:
            st.write('\n\n')
            st.markdown("### Tags")
            st.button("Business")
            st.button("Weekend Challenge⚡")
            st.button("Statistics")
            st.button("Question of the Day💡")
            st.button("Entrepreneurship")
            st.write('\n \n \n')
            st.write('\n \n \n')
            st.write('\n \n \n')
            st.markdown("---")
            st.markdown("### Leaderboard")
            st.info("Leaderboard feature is under development.")

    with tab2:
        st.markdown("### School and Student Details")

        for school, projects in SCHOOLS.items():
            with st.expander(school):
                for project, students in projects.items():
                    st.markdown(f"**{project}:**")
                    for student_data in students:
                        student = student_data["student"]
                        post_count = len(student_data["posts"])
                        if st.button(f"{student} ({post_count} posts)", key=f"btn_{student}"):
                            with st.expander(f"Posts by {student}"):
                                for post in student_data["posts"]:
                                    st.write(f"**Post ID {post['post_id']}:** {post['content']}")
                                    if st.button(f"Respond to Post ID {post['post_id']}", key=f"btn_respond_{post['post_id']}"):
                                        with st.form(key=f"response_form_{post['post_id']}"):
                                            response_content = st.text_area("Your response:", key=f"response_content_{post['post_id']}")
                                            if st.form_submit_button(label="Submit"):
                                                post['responses'].append(response_content)
                                                st.success("Response submitted!")
                                                st.experimental_rerun()

def tutor_module_page():
    # Example data structure for dropdown filters
    data = {
        "School A": {
            "Project X": ["Aravinth", "Bala", "Balaji"],
            "Project Y": ["Barath", "Deepak"]
        },
        "School B": {
            "Project Z": ["Manivannan", "Leo"],
            "Project W": ["Sandy", "Ice", "Nandhini"]
        }
    }

    # Initialize session state to store data
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame({
            "Week": ["Week 1", "Week 2", "Week 3"],
            "Expert": ["John Doe", "Jane Smith", "Alice Brown"],
            "Date": ["2024-08-01", "2024-08-08", "2024-08-15"],
            "Topic": ["Introduction to Entrepreneurship", "Market Research", "Business Planning"],
            "Recording": ["[Link](https://example.com/rec1)", "[Link](https://example.com/rec2)", "[Link](https://example.com/rec3)"],
            "Notes": ["[Link](https://example.com/notes1)", "[Link](https://example.com/notes2)", "[Link](https://example.com/notes3)"],
        })

    # School Dropdown
    selected_school = st.selectbox("Select School", options=list(data.keys()))

    # Project Dropdown - filtered by selected school
    if selected_school:
        selected_project = st.selectbox("Select Project", options=list(data[selected_school].keys()))
    else:
        selected_project = st.selectbox("Select Project", options=[])

    # Student Dropdown - filtered by selected project
    if selected_project:
        selected_student = st.selectbox("Select Student", options=data[selected_school][selected_project])
    else:
        selected_student = st.selectbox("Select Student", options=[])

    # Display the selected values
    st.write(f"Selected School: {selected_school}")
    st.write(f"Selected Project: {selected_project}")
    st.write(f"Selected Student: {selected_student}")

    # Add a link to navigate to student module
    if selected_student:
        st.markdown(f"[Go to Student Module for {selected_student}](/student_module_page?student={selected_student})")

    # Section for Weekly Expert Sessions with CSV upload or manual entry
    st.markdown("### Weekly Expert Sessions")
    
    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file:
        new_data = pd.read_csv(uploaded_file)
        st.session_state.df = pd.concat([st.session_state.df, new_data], ignore_index=True)
        st.success("Data added successfully from CSV!")
    
    st.write("Or manually add a new record:")
    
    # Manual entry form
    with st.form(key="add_record_form"):
        week = st.text_input("Week")
        expert = st.text_input("Expert Name")
        date = st.date_input("Date")
        topic = st.text_input("Topic")
        recording = st.text_input("Recording URL")
        notes = st.text_input("Notes URL")
        submit_button = st.form_submit_button(label="Add Record")
        
        if submit_button:
            new_entry = pd.DataFrame({
                "Week": [week],
                "Expert": [expert],
                "Date": [date],
                "Topic": [topic],
                "Recording": [f"[Link]({recording})"],
                "Notes": [f"[Link]({notes})"]
            })
            st.session_state.df = pd.concat([st.session_state.df, new_entry], ignore_index=True)
            st.success("New record added successfully!")
    
    # # Display the current data
    # st.markdown("### Current Expert Sessions")
    # st.dataframe(st.session_state.df, width=1000, height=None)

    # Delete data section
    st.markdown("### Delete a Session")
    delete_index = st.number_input("Select row index to delete", min_value=0, max_value=len(st.session_state.df)-1, step=1)
    if st.button("Delete Session"):
        st.session_state.df = st.session_state.df.drop(delete_index).reset_index(drop=True)
        st.success("Session deleted successfully!")
    
    # Display updated data
    st.write("Updated Expert Sessions")
    st.dataframe(st.session_state.df, width=1000, height=None)

    # # Add a link to navigate to student module
    # if selected_student:
    #     st.markdown(f"[Go to Student Module for {selected_student}](/student_module_page?student={selected_student})")


def student_module_page():
    st.title(":sunglasses :blue[Balaji Kannan]")
    st.subheader("St.Joseph Matric Hr Sec School")
    st.markdown("---")
    st.subheader(f"My Progress - :blue[Phase 1]")
    st.write("\n")
    header_col, content_col = st.columns([2, 1])

    with header_col:
        st.markdown("<div style='text-align: left;'>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Upcoming", "Ongoing", "Completed", "Psychometric Test", "Psychometric Test Upload"])

        # with tab1:
        #     st.write("### Upcoming Tasks")
        #     st.write("1. **Google Meeting:** [Join here](https://meet.google.com/) at 10:00 AM, 16th Aug 2024")
        #     st.write("2. **Course Video:** Introduction to Entrepreneurship, Due by 20th Aug 2024")

        with tab2:
            st.write("### Ongoing Tasks")
            st.write("1. **Assignment:** Submit by 25th Aug 2024")
            st.write("2. **Group Project:** Entrepreneurship in REDE, Progress: 50%")

        with tab3:
            st.write("### Completed Tasks")
            st.write("1. **Course Video:** 'Entrepreneurship', Completed on 10th Aug 2024")
            st.write("2. **Quiz:** Entrepreneurship Fundamentals, Score: 85%")

        with tab4:
            st.write("### Psychometric Test Classification")

        with tab5:
            st.write("### Psychometric Test Upload")
            uploaded_file = st.file_uploader("Upload a Word Document", type=["docx"])
            if uploaded_file:
                # Save the uploaded file temporarily
                with open("uploaded_test.docx", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success("File uploaded successfully!")
                st.write("**Uploaded File:**")
                st.download_button(label="Download the Word Document", data=uploaded_file, file_name="uploaded_test.docx")
                # You can add logic here to read and display the contents of the document if needed

        st.markdown("</div>", unsafe_allow_html=True)

    with content_col:
        st.markdown("""
            <style>
            .metric-box {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                margin-bottom: 20px;
            }
            .attendance-box {
                background-color: #e6f7ff;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                font-size: 24px;
                color: #007bff;
            }
            .metric-label {
                color: #6c757d;
                font-size: 14px;
            }
            .metric-value {
                font-size: 24px;
                font-weight: bold;
            }
            </style>
        """, unsafe_allow_html=True)

        with st.container():
            fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=90,  
            number={'suffix': "%"}, 
            gauge={
                'axis': {'range': [0, 100]},  
                'bar': {'color': "green"},  
            },
            domain={'x': [0, 1], 'y': [0, 1]}, 
            title={'text': "Attendance"}
        ))

            fig.update_layout(
                width=180, 
                height=180, 
                margin=dict(l=20, r=20, t=40, b=20) 
            )
            st.plotly_chart(fig, use_container_width=False)
            st.markdown('<div class="attendance-box"><div class="metric-label">Gradebook</div>', unsafe_allow_html=True)
            st.write("")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("In Progress", "0")
            with col2:
                st.metric("Completed", "5")
            with col3:
                st.metric("Incomplete", "2")
            
    st.markdown("---")
    st.write("**No progress yet!**")
    st.write("When we see some activity, progress will show up here.")


def student_module_page_1():
    
    st.markdown("---")
    st.subheader(f"My Progress - :blue[Phase 1]")
    st.write("\n")
    header_col, content_col = st.columns([2, 1])

    with header_col:
        st.markdown("<div style='text-align: left;'>", unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["Upcoming", "Ongoing", "Completed","Psychometric Test Upload"])

        with tab1:
            st.write("### Upcoming Tasks")
            st.write("1. **Google Meeting:** [Join here](https://meet.google.com/) at 10:00 AM, 16th Aug 2024")
            st.write("2. **Course Video:** Introduction to Entrepreneurship, Due by 20th Aug 2024")

        with tab2:
            st.write("### Ongoing Tasks")
            st.write("1. **Assignment:** Submit by 25th Aug 2024")
            st.write("2. **Group Project:** Entrepreneurship in REDE, Progress: 50%")

        with tab3:
            st.write("### Completed Tasks")
            st.write("1. **Course Video:** 'Entrepreneurship', Completed on 10th Aug 2024")
            st.write("2. **Quiz:** Entrepreneurship Fundamentals, Score: 85%")

        with tab4:
            st.write("### Psychometric Test Upload")
            uploaded_file = st.file_uploader("Upload a Word Document", type=["docx"])
            if uploaded_file:
                with open("uploaded_test.docx", "wb") as f:
                    f.write(uploaded_file.getbuffer())
                st.success("File uploaded successfully!")
                st.write("**Uploaded File:**")
                st.download_button(label="Download the Word Document", data=uploaded_file, file_name="uploaded_test.docx")
                
        st.markdown("</div>", unsafe_allow_html=True)

        # Project Dropdown and Status
        st.markdown("### Project Selection")
        project_name = st.selectbox("Select Project", ["Project A", "Project B", "Project C"])
        # Circular Gauge for Progress
        completion_percentage = st.slider("Set Project Completion Percentage", 0, 100, 5)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=completion_percentage,
            gauge={'axis': {'range': [0, 100]},
                   'bar': {'color': "#4caf50"},
                   'steps': [
                       {'range': [0, 100], 'color': "#81c784"}],
                   'threshold': {'line': {'color': "red", 'width': 2}, 'thickness': 0.50, 'value': 90}},
            title={'text': "Completion"}))

        fig.update_layout(width=300, height=300)

        st.plotly_chart(fig)
        
        # Weekly Expert Details Table
        st.markdown("### Weekly Expert Sessions")
        if 'df' in st.session_state:
            df = st.session_state.df
            st.dataframe(df, width=1000, height=None)
        else:
            st.write("No data available")

        st.markdown("---")
        st.write("**No progress yet!**")
        st.write("When we see some activity, progress will show up here.")

    with content_col:
        # The content_col section remains as it was with the attendance bar and icons
        from PIL import Image
        import requests
        from io import BytesIO

        def load_local_image(path):
            return Image.open(path) 

        def load_image(url):
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            return img

        graduation_icon_path = r"C:\Users\XY663FG\Downloads\cap.jpeg"  # Replace with actual URL
        trophy_icon_path = r"C:\Users\XY663FG\Downloads\tropy.jpeg"  # Replace with actual URL

        graduation_icon = load_local_image(graduation_icon_path)
        trophy_icon = load_local_image(trophy_icon_path)

        st.markdown("""
            <style>
            .attendance-container {
                background-color: #d9edf7;
                border-radius: 10px;
                padding: 10px;
                text-align: center;
                margin-top: 5px;
                font-size: 20px;
                color: #0056b3;
                cursor: pointer;
                animation: bounce 2s infinite;
            }
            .attendance-bar {
                width: 90%;
                background-color: #d9edf7;
                border-radius: 12px;
                height: 30px;
                position: relative;
                overflow: hidden;
                box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
                animation: slideIn 1s ease-out;
                margin: 0 20px; 
            }
            .attendance-bar-fill {
                background: linear-gradient(to right, #4caf50, #81c784);
                font-size: 24px; /* Larger text size */
                color: #007bff; /* Blue text color */
                height: 100%;
                border-radius: 12px;
                text-align: right;
                line-height: 30px;
                color: white;
                font-weight: bold;
                padding-right: 15px;
                position: absolute;
                top: 0;
                left: -100%;
                transition: left 1s ease-in-out;
                display: flex;
                align-items: center;
                justify-content: flex-end;
            }
            .attendance-bar-fill.show {
                left: 0;
            }
            .attendance-icon {
                margin-left: 10px;
            }
            .gradebook-box {
                background-color: #d9edf7;
                border-radius: 10px;
                padding: 10px;
                text-align: center;
                margin-top: 10px;
                font-size: 20px;
                color: #0056b3;
                cursor: pointer;
                animation: bounce 2s infinite;
            }
            .metric-box {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                margin-bottom: 20px;
                animation: fadeIn 1s ease-out;
            }
            .metric-label {
                color: #6c757d;
                font-size: 14px;
            }
            .metric-value {
                font-size: 24px;
                font-weight: bold;
            }
            .progress-box {
                text-align: center;
                padding: 10px;
                animation: slideIn 1s ease-out;
            }
            
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-30px); }
                60% { transform: translateY(-15px); }
            }
            
            @keyframes slideIn {
                from { transform: translateY(20px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }
            </style>
        """, unsafe_allow_html=True)

        with st.container():

            # Gradebook button with animation
            st.markdown('<div class="gradebook-box">Gradebook</div>', unsafe_allow_html=True)
            st.markdown('---')

            # Metrics for In Progress, Completed, and Incomplete
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown('<div class="progress-box"><div class="metric-label">In Progress</div><div class="metric-value">1</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown('<div class="progress-box"><div class="metric-label">Completed</div><div class="metric-value">5</div></div>', unsafe_allow_html=True)
            with col3:
                st.markdown('<div class="progress-box"><div class="metric-label">Incomplete</div><div class="metric-value">2</div></div>', unsafe_allow_html=True)

            st.markdown('<div class="attendance-container">Attendance</div>', unsafe_allow_html=True)
            st.markdown('---')

            col1, col2, col3 = st.columns([1, 8, 1])

            with col1:
                st.image(graduation_icon, width=35)  # Graduation cap icon

            with col2:
                st.markdown(f"""
                    <div class="attendance-bar">
                        <div class="attendance-bar-fill show" style="width: 90%;">
                            90% <img src="{graduation_icon}" class="attendance-icon" width="20" />
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.image(trophy_icon, width=35)  # Trophy icon

            st.markdown('</div>', unsafe_allow_html=True)



def parent_page():
    # Sidebar with profile and logout buttons
    for _ in range(20):  
        st.sidebar.write("")
    
    st.sidebar.button("Profile", key="bottom")
    logout_container = st.sidebar.container()

    with logout_container:
        if st.sidebar.button("Log Out", key="logout_bottom"):
            logout()
            st.experimental_rerun()

    logout_container.markdown('<div class="logout-container"></div>', unsafe_allow_html=True)

    # Tabs similar to student module
    tab1, tab2, tab3 = st.tabs(["Student Activity", "Tutor Details", "Team Members"])

    with tab1:
        st.subheader("Student Activity")
        student_activity_data = {
            "Student": ["Balaji", "Balaji", "Ram"],
            "Skill": ["Entrepreneurship", "Speaking", "Leadership"],
            "Rank": [1, 2, 3],
            "Attendance (%)": [95, 87, 93],
            "Tutor Remarks": ["Excellent progress", "Needs improvement in speaking", "Good leadership skills"],
            "Upcoming Tasks": ["Psychometric Test", "Practice speech", "Group project"],
        }
        student_activity_df = pd.DataFrame(student_activity_data)
        st.table(student_activity_df)
        
        tab10, tab11 = st.tabs(["Rank", "Attendance (%)"])

        with tab10:
            st.subheader("Student Rank by Skill")
            fig, ax = plt.subplots()
            skills = student_activity_df["Skill"].unique()
            bar_width = 0.2
            import numpy as np
            indices = np.arange(len(student_activity_df))
            for i, skill in enumerate(skills):
                skill_data = student_activity_df[student_activity_df["Skill"] == skill]
                ax.bar(indices + i * bar_width, skill_data["Rank"], width=bar_width, label=skill)
            ax.set_xlabel("Student Name")
            ax.set_ylabel("Rank")
            ax.set_title("Rank of Students by Skill")
            ax.set_xticks(indices + bar_width)
            ax.set_xticklabels(student_activity_df["Student"])
            ax.legend(title="Skill")
            ax.set_ylim(0, max(student_activity_df["Rank"]) + 1)
            st.pyplot(fig)

        with tab11:
            st.subheader("Student Attendance (%) by Skill")
            fig, ax = plt.subplots()
            for i, skill in enumerate(skills):
                skill_data = student_activity_df[student_activity_df["Skill"] == skill]
                ax.bar(indices + i * bar_width, skill_data["Attendance (%)"], width=bar_width, label=skill)
            ax.set_xlabel("Student Name")
            ax.set_ylabel("Attendance (%)")
            ax.set_title("Attendance Percentage of Students by Skill")
            ax.set_xticks(indices + bar_width)
            ax.set_xticklabels(student_activity_df["Student"])
            ax.legend(title="Skill")
            ax.set_ylim(0, 100)
            st.pyplot(fig)

    with tab2:
        st.subheader("Tutor Details")
        tutor_details_data = {
            "Tutor Name": ["Leo", "Aravinth", "Deepak"],
            "Expertise": ["Entrepreneurship", "Public Speaking", "Leadership"],
            "Contact": ["+919944223399", "+919944223399", "+919944223399"],
            "Availability": ["Mon-Fri, 9 AM - 5 PM", "Mon-Fri, 10 AM - 4 PM", "Tue-Thu, 11 AM - 3 PM"],
        }
        tutor_details_df = pd.DataFrame(tutor_details_data)
        st.table(tutor_details_df)

    with tab3:
        st.subheader("Team Members")
        team_members_data = {
            "Team Member": ["Balaji", "Bharath", "Manoj"],
            "Role": ["Captain", "Vice Captain", "Team Person"],
            "Contact": ["+919944223399", "+919944223399", "+919944223399"],
            "Photo": [
                "https://via.placeholder.com/150",
                "https://via.placeholder.com/150",
                "https://via.placeholder.com/150"
            ]
        }
        team_members_df = pd.DataFrame(team_members_data)

        st.table(team_members_df)

        with st.expander("Team Photos"):
            for index, row in team_members_df.iterrows():
                st.markdown(
                    f"""
                    **{row['Team Member']}** - {row['Role']}
                    [View Photo]({row['Photo']})
                    """
                )



def show_student_profile_page():
    st.title("Balaji Kannan")
    
    # Sample data
    school_name = "Sunrise High School"
    dob = "2005-09-15"
    grade = "10th Grade"
    syllabus = 'CBSC'
    email = 'xyz@gmail.com'

    st.write("**User Name:** Balaji Kannan")
    st.write("**Change Password:** [Click here to change password](#)")  # Example link for changing password

    st.write("**School Name:**", school_name)
    st.write("**Syllabus:**", syllabus)
    st.write("**Date of Birth:**", dob)
    st.write("**Grade:**", grade)
    st.write("**Mail ID:**", email)

    st.write("**Certificate:**")
    st.write("**Project completed:**")

def show_tutor_profile_page():
    st.title("Leo Akash")
    
    # Sample data
    school_name = "Sunrise High School"
    dob = "1985-09-15"
    grade = "10th Grade"
    syllabus = 'CBSE'  # Corrected spelling for the syllabus
    email = 'xyz@gmail.com'  # Assigned email to a variable
    
    st.write("**User Name:** Leo Akash")
    st.write("**Change Password:** [Click here to change password](#)")  # Example link for changing password

    st.write("**School Name:**", school_name)
    st.write("**Syllabus:**", syllabus)
    st.write("**Date of Birth:**", dob)
    st.write("**Grade:**", grade)
    st.write("**Mail ID:**", email)

    task_tree = """
        digraph G {
            "Leo Akash" -> "Aravinth";
            "Leo Akash" -> "Balaji";
            "Leo Akash" -> "Bala";
            "Leo Akash" -> "Deepak";
            "Deepak" -> "Sajjad";
            "Sajjad" -> "School A Supervisor";
            "School A Supervisor" -> "Tutor A";
            "Balaji" -> "manivannan";
            "manivannan" -> "School B Supervisor";
            "School B Supervisor" -> "Tutor B";
        }
        """
    st.graphviz_chart(task_tree)


SCHOOLS = {
    "School A": {
        "Project X": [
            {"student": "Aravinth", "posts": [
                {"post_id": 1, "content": "How can I improve my business pitch?", "responses": []},
                {"post_id": 2, "content": "Any tips for effective market research?", "responses": []}
            ]},
            {"student": "Bala", "posts": [
                {"post_id": 3, "content": "Best practices for financial planning?", "responses": []}
            ]}
        ]
    },
    "School B": {
        "Project Z": [
            {"student": "Manivannan", "posts": [
                {"post_id": 4, "content": "How to identify a profitable business idea?", "responses": []}
            ]},
            {"student": "Leo", "posts": [
                {"post_id": 5, "content": "Tips for pitching to investors?", "responses": []}
            ]}
        ]
    }
}


# Function to display the tutor-student hierarchy
def tutor_student_hierarchy():
    st.title("Tutor-Student Hierarchy")

    # Get all unique school names, projects, and student names
    school_names = list(schools.keys())
    project_names = sorted({project for school_data in schools.values() for project in school_data['projects']})
    student_names = sorted({student for school_data in schools.values() for student in school_data['students']})

    st.markdown("---")  # Separator line

    # Filters
    st.subheader("Search and Filter")

    # School name filter dropdown
    col1,col2,col3 = st.columns([1,1,1])
    with col1:
        school_filter = st.selectbox("Select School Name", ["All Schools"] + school_names)
    with col2:
    # Project filter dropdown
        project_filter = st.selectbox("Select Project", ["All Projects"] + project_names)
    with col3:
    # Student name filter dropdown
        student_filter = st.selectbox("Select Student Name", ["All Students"] + student_names)

    # Apply filters and display results
    st.subheader("Doubts")

    for school_name, school_data in schools.items():
        if school_filter == "All Schools" or school_filter == school_name:
            if project_filter == "All Projects" or project_filter in school_data['projects']:
                filtered_students = {
                    student: questions for student, questions in school_data['students'].items()
                    if student_filter == "All Students" or student_filter == student
                }
                if filtered_students:  # Only display if there are matching students
                    with st.expander(f"{school_name} - Questions Asked: {school_data['total_questions']}"):
                        for student_name, questions_asked in filtered_students.items():
                            st.write(f"{student_name}: {questions_asked} questions")

def profile_page():
    # Display profile information
    st.title("Profile Information")
    # Add your profile information here
    st.image("C:\\Users\\Admin\\Downloads\\profile-picture.png", width=150)  # Replace with actual path
    st.subheader("Personal Information")
    st.write("**Name:** Balaji Kannan")
    st.write("**School:** st joseph mat hr sec school")
    st.write("**Date of Birth:** March 4 1997")
    st.write("**Class:** 10th Grade")
    st.write("**Syllabus:** CBSC")
    st.write("**MAIL ID:** balajicr****@gmail.com")
    # Add more information as needed

def dashboard():
    # Page background color
    page_bg_color = """
    <style>
    .stApp {
        background-color: #C8A2C8;  /* Light blue background */
    }
    .fixed-bottom {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #fff;
        padding: 10px;
        border-top: 1px solid #ccc;
        box-shadow: 0 -2px 5px rgba(0,0,0,0.1);
        text-align: center;
        z-index: 1000;  /* Ensure it stays on top of other content */
    }
    </style>
    """
    st.markdown(page_bg_color, unsafe_allow_html=True)

    # Initialize selected_page if not already set
    if 'selected_page' not in st.session_state:
        st.session_state.selected_page = 'Feed'

    selected_page = st.session_state.selected_page

    # Sidebar for page selection using buttons
    st.sidebar.header("Navigation")

    # Profile button
    profile_button = st.sidebar.button('profile')
    
    if st.sidebar.button("Feed"):
        st.session_state.selected_page = 'Feed'
        st.experimental_rerun()

    if st.sidebar.button("Forum"):
        st.session_state.selected_page = 'Forum'
        st.experimental_rerun()

    if st.sidebar.button("Module"):
        st.session_state.selected_page = 'Module'
        st.experimental_rerun()

    if profile_button:
        st.session_state.selected_page = 'PROFILE'
        st.experimental_rerun()
        
    # Page content based on selected page
    if selected_page == 'PROFILE':
        profile_page()

    # elif st.session_state.user_role == 'kannan':
    #     parent_page()

    else:
        if selected_page == 'Feed':
            st.write("\n" * 20)  # Add vertical space to simulate sidebar behavior
            logout_container = st.container()
            with logout_container:
                if st.button("Log Out", key="logout_button"):
                    logout()
                    st.experimental_rerun()
            feed_page()

        elif selected_page == 'Forum':
            if st.session_state.user_role.capitalize() == 'Balaji':
                student_forum_page()
            elif st.session_state.user_role.capitalize() == 'Leo':
                tutor_forum_page()
            elif st.session_state.user_role.capitalize() == 'Kannan':
                student_forum_page()    

        elif selected_page == 'Module':
            st.write("\n" * 18)  # Add vertical space for module pages
            logout_container = st.container()
            with logout_container:
                if st.button("Log Out", key="logout_button"):
                    logout()
                    st.experimental_rerun()
            if st.session_state.user_role.capitalize() == 'Balaji':
                student_module_page_1()
            elif st.session_state.user_role.capitalize() == 'Leo':
                tutor_module_page()
            elif st.session_state.user_role.capitalize() == 'Kannan':
                student_module_page_1()
                parent_page()

    # Fixed position navigation menu
    st.markdown("""
    <div class="fixed-bottom">
        <button onclick="window.location.href='#Feed'">Feed</button>
        <button onclick="window.location.href='#Forum'">Forum</button>
        <button onclick="window.location.href='#Module'">Module</button>
    </div>
    """, unsafe_allow_html=True)

    # JavaScript to handle button clicks
    st.markdown("""
    <script>
    document.querySelectorAll('.fixed-bottom button').forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const page = e.target.textContent;
            const pages = ['Feed', 'Forum', 'Module'];
            if (pages.includes(page)) {
                document.querySelector('#' + page).scrollIntoView({behavior: 'smooth'});
            }
        });
    });
    </script>
    """, unsafe_allow_html=True)

if not st.session_state.logged_in:
    login_page()
else:
    dashboard()

