import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import smtplib
from email.message import EmailMessage
import google.generativeai as genai

# //AIzaSyAs9nOfHfbJLTEKJgwoYAZw4n0JT4wqcPQ
api_key = st.secrets["dggd"]
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')


def send_email(name, subject, message):
    sender_email = "sasmithajayasinghe1@gmail.com"  # Replace with your email
    password = "fnyg xhpn xpum nrha"

    msg = EmailMessage()
    msg.set_content(f"Name: {name}\n\nSubject: {subject}\n\nMessage: {message}")

    msg['Subject'] = f"Contact Form Submission from {name}"
    msg['From'] = sender_email
    msg['To'] = "sasmithajayasinghe1@gmail.com"

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"Error occurred: {e}")
    finally:
        server.quit()


def load_animation(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_animation("https://lottie.host/2614c7a1-f658-48e5-a2ca-06cf8ecc6903/dAR9h6DXMU.json")

st.set_page_config(layout="wide")
colm1, colm2 = st.columns(2)

with colm1:
    st.subheader("Hey Guys :wave:")
    st.title("I am Thisara Jayasinghe")
    st.write("""
    I'm Thisara Jayasinghe 21 years old, a  highly motivated and dedicated Software Engineering undergraduate with strong programming
fundamentals and proficiency in Java, MERN stack, C++, Spring framework, AI/ML and more. A quick learner
with excellent teamwork, leadership, time management and communication abilities.
    """)
    st.markdown("[Read More About Me](https://www.linkedin.com/in/thisara-jayasinghe/)")
    st.markdown("""
            <style>
            .icon-row {
                display: flex;
                justify-content: flex-start;
                gap: 10px;
                padding: 10px 0;
            }
            .icon-row a {
                display: inline-block;
                width: 50px;
                height: 50px;
                border-radius: 50%;
                background-color: #f0f0f0;
                text-align: center;
                line-height: 50px;
                transition: background-color 0.3s;
                overflow: hidden;  /* Ensure the image fits within the circle */
            }
            .icon-row a:hover {
                background-color: #ccc;
            }
            .icon-row img {
                width: 100%;
                height: 100%;
                object-fit: cover;  /* Ensure the image covers the entire circle */
                border-radius: 50%;
            }
            </style>
            <div class="icon-row">
                <a href="mailto:sasmithajayasinghe1@gmail.com" title="Email">
                    <img src="https://th.bing.com/th/id/R.080256b553ed23e061409d3c668f2cd4?rik=aVU7u33cH1dr8g&riu=http%3a%2f%2flksd.ss10.sharpschool.com%2fUserFiles%2fServers%2fServer_98428%2fImage%2f6.Staff+Portal%2fStaff+Portal-Quick+Link+Icons%2fGmail+-+White.png&ehk=b4vqulEJuK4mKGVElaYisG3mCpVj9AZRuW0%2frNvbutY%3d&risl=&pid=ImgRaw&r=0" alt="Email">
                </a>
                <a href="https://www.linkedin.com/in/thisara-jayasinghe/" title="LinkedIn">
                    <img src="https://www.pngitem.com/pimgs/m/70-708610_circle-linkedin-logo-transparent-hd-png-download.png" alt="LinkedIn">
                </a>
                <a href="https://github.com/ThisaraJayas" title="GitHub">
                    <img src="https://th.bing.com/th/id/OIP.9B4NoA0XTQUhk62iCKkCdQHaH7?rs=1&pid=ImgDetMain" alt="GitHub">
                </a>
                <a href="https://www.youtube.com/@DevExplains" title="YouTube">
                    <img src="https://www.seekpng.com/png/detail/145-1450088_youtube-logo-png-circle.png" alt="YouTube">
                </a>
            </div>
            """, unsafe_allow_html=True)

with colm2:
    st_lottie(lottie_animation)

st.markdown('---')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )


persona = """ You are Thisara AI bot. You help people answer questions about your self (i.e Thisara)
Answer as if you are responding . dont answer in second or third person. 
 If you don't know they answer you simply say "That's a secret"
 Here is more info about Murtaza: 
 I'm Thisara Jayasinghe 21 years old, a highly motivated and dedicated Software Engineering undergraduate 
 with strong programming fundamentals and proficiency in Java, MERN stack, C++, Spring framework, AI/ML and more.
A quick learner with excellent teamwork, leadership, time management and communication abilities.
 """
if selected == 'About':
    with st.container():
        st.title("Thisara's AI Bot")
        User_question = st.text_input("Ask anything about me")
        if st.button("ASK", use_container_width=400):
            prompt = persona +"Here is the question that the user asked"+ User_question
            response = model.generate_content(prompt)
            st.write(response.text)
        st.title("")
        colum1, colum2 = st.columns(2)

        with colum1:
            st.subheader("Youtube Channel")
            st.write("- 1000+ Subscribers")
            st.write("- Posting video once a month")
            st.write("- Technology Channel")
            st.write("- Over 300K Views")
            st.write("- More than 4000 Watch Hours")

        with colum2:
            st.markdown(
                """
                <iframe width="100%" height="300" src="https://www.youtube.com/embed/LZWXrPZKVNY" 
                frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen></iframe>
                """,
                unsafe_allow_html=True
            )
        st.markdown('---')

        with st.container():
            col3,col4=st.columns(2)
            with col3:
                st.subheader("Education")
                st.write("""
                **Sri Lanka Institute of Information Technology**
                - Bachelor of Science in Information Technology (Special), Software Engineering
                - Object Oriented Programming, Data Structures and Algorithms
                - Current GPA: 3.5
                """)
            with col4:
                st.subheader("Skills")
                st.write("""
                **Languages:**
                - Java, JavaScript, PHP, Python, Kotlin, C, C++, R, HTML/CSS
        
                **Frameworks & Libraries:**
                - Spring Framework (Spring Boot), MERN Stack (MongoDB, Express.js, React.js, Node.js), Flutter, NumPy, pandas, matplotlib
        
                **Databases:**
                - MySQL, MongoDB, Ms SQL Server, PostgreSQL, H2, SQLite, Firebase
        
                **Dependency Management:**
                - Maven, NPM
        
                **Other:**
                - Git, GitHub, Jupyter Notebook, Postman
                """)






if selected == 'Projects':
    with st.container():
        st.title("My Projects")

        image1 = Image.open("images/electrical.png")
        col5,col6=st.columns(2)
        with col5:
            st.image(image1,use_column_width=True)
        with col6:
            st.subheader("Electrical and Service Management System (MERN Stack) ReactJs, ExpressJs, MongoDB, NodeJs")
            st.write("""
                - Developed for the ITP Module using the MERN stack with agile methodology. Utilizes MongoDB as
                the database, implements JWT and OAuth for user authentication with Firebase for file handling, and
                is deployed to Vercel.
                - Allows customers to schedule service appointments efficiently.
            """)
            st.markdown("[Github Link](https://github.com/ThisaraJayas/ITP_Project__NewtonElectrical)")
            st.markdown("[Website Link](https://itp-project-newton-electrical.vercel.app/)")

        image2 = Image.open("images/project1.jpg")
        col7, col8 = st.columns(2)
        with col7:
            st.image(image2,use_column_width=True)
        with col8:
            st.subheader("Financial Management System (Java Spring Boot)")
            st.write("""
                    - Independently developed using Java Spring Boot for backend API development and ReactJS for the
                    frontend development.
                    - Integrated PostgreSQL as the database and implemented Spring Security for user authentication.
            """)
            st.markdown("[GitHub (Backend) Link](https://github.com/ThisaraJayas/Financial-Management-System-Backend)")
            st.markdown("[GitHub (Frontend) Link](https://github.com/ThisaraJayas/Financial-Management-System-Frontend)")



        image2 = Image.open("images/project1.jpg")
        col9, col10 = st.columns(2)
        with col9:
            st.image(image2, use_column_width=True)
        with col10:
            st.subheader("Transport Management System (Java Servlet & JSP)")
            st.write("""
                            - Developed using Java, JSP, and Servlets and Integrates MySQL as the database
                            - Allows users to book vehicles and schedule vehicle appointments
                    """)
            st.markdown("[GitHub Link](https://github.com/ThisaraJayas/OnlineTransportSystem-Taxi-Booking)")

        image2 = Image.open("images/project1.jpg")
        col9, col10 = st.columns(2)
        with col9:
            st.image(image2, use_column_width=True)
        with col10:
            st.subheader("Pharmacy Management System (PHP HTML/CSS)")
            st.write("""
                        Developed for the IWT module using PHP, HTML, and CSS and Integrates MySQL as the database
                        Facilitates the purchasing of medicine through the store and also allows customers to order
                        medicine by uploading prescriptions
                            """)
            st.markdown("[GitHub Link](https://github.com/ThisaraJayas/Pharmacy-Management-System)")

        image2 = Image.open("images/project1.jpg")
        col9, col10 = st.columns(2)
        with col9:
            st.image(image2, use_column_width=True)
        with col10:
            st.subheader("My Portfolio Website (Python & Streamlit)")
            st.write("""
                               Developed using Python and Streamlit, this portfolio website showcases my projects, skills, and contact me direcly.
                Key features include:
                - An AI chatbot that answers questions about my background, skills, and projects, providing an interactive user experience.
                - Integration with various social media platforms for easy access to my professional profiles.
                - A project gallery with detailed descriptions and links to GitHub repositories.
                - Contact form that allows visitors to reach out to me directly.
                                    """)
            st.markdown("[GitHub Link](https://github.com/ThisaraJayas/My-Portfolio-Website)")




        st.title(" ")

        st.markdown(
            """
            <div style='text-align: center; color: #B2BEB5;'>
                <h2>More Projects on GitHub.</h2>
            </div>
            """,
            unsafe_allow_html=True
        )







elif selected == 'Contact':
    st.title("Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            if not name or not subject or not message:
                st.warning("Please fill out all fields.")
            else:
                send_email(name, subject, message)