import streamlit as st

# Home Section
st.title('Welcome to My Portfolio')

col1, col2 = st.columns([1, 3])  

with col1:
    image_url = "https://raw.githubusercontent.com/ayaz0065/Ayaz-Bashir/main/Image.jpeg"
    st.image(image_url, width=180, length=100)

with col2:
    st.write("""
        ## Hello, I'm Ayaz Bashir
        I'm a passionate Data Science Student with expertise in data analysis,
        machine learning, and statistical modeling.. 
        Welcome to my personal portfolio! Here, you can explore my skills, 
        projects, and get in touch with me.
    """)
    st.write("""
        I specialize in data cleaning, feature engineering, predictive modeling, 
        and statistical analysis, with hands-on experience in Python, R, SQL, and machine learning libraries
        such as Scikit-learn, TensorFlow, and Keras.
        Feel free to browse through my work and contact me for any opportunities or collaborations
        in the field of data science.
    """)

# Sidebar Navigation
menu = st.sidebar.selectbox('Navigate', ['Home', 'About Me', 'Projects', 'Skills', 'Contact'])

if menu == 'Home':
    st.write("This is the home section where we introduce the portfolio!")
elif menu == 'About Me':
    st.write("This is the About Me section where I describe myself.")
elif menu == 'Projects':
    st.write("This is the Projects section where I showcase my work.")
elif menu == 'Skills':
    st.write("This is the Skills section where I highlight my expertise.")
elif menu == 'Contact':
    st.write("This is the Contact section where you can reach out to me.")

# About me Section

if menu == 'About Me':
    st.header('About Me')
    st.write("""
        I am a passionate developer with a background in Data Science. 
        I graduate in 2026 from University Of Central Punjab [UCP] with a degree in BS Data Science. 
        I have experience in data analysis, machine learning, and software development and specialize
        in Python, R, SQL, data visualization, and building predictive models using machine 
        learning frameworks like Scikit-learn and TensorFlow.
    """)
    st.subheader('Skills & Expertise')
    st.write("""
        - Python
        - Data Analysis
        - Machine Learning
        - Web Development
        - C++
        - C
        - Word + Excel
    """)

# Project Section

if menu == 'Projects':
    st.header('Projects')
    
    st.subheader('Project 1: **Car Showroom Dealership Sales Analysis**')
    st.write("""
        This project focuses on analyzing car dealership sales data to gain insights into customer preferences,
        sales trends, and the performance of various car models. 
        Using historical sales data, I built a model to predict sales performance and recommend strategies for
        improving sales efficiency. 
        The analysis includes visualizations of monthly sales trends, customer demographics, and car model 
        performance.
    """)
    st.write("Technologies used: Python, Pandas, SQL")
    st.markdown("[GitHub Repo](https://github.com/ayazjutt/car-dealership-sales-analysis)")

    st.subheader('Project 2: **Car Inventory Management System**')
    st.write("""
        This project involves creating an inventory management system for a car showroom dealership. 
        The system tracks available car models, sales transactions, 
        and stock levels. I built a predictive model to optimize the inventory, ensuring the dealership has
        the right number of cars in stock based on sales patterns.
    """)
    st.write("Technologies used: Python, SQL, Pandas, HTML")
    st.markdown("[GitHub Repo](https://github.com/ayazjutt/car-inventory-management-system)")

    st.subheader('Project 3: **Car Price Prediction Model**')
    st.write("""
        In this project, I developed a machine learning model to predict the price of used cars based on
        features such as the car's age, mileage, brand, and condition. 
        The model helps the dealership set competitive prices and offer fair trade-in values to customers.
    """)
    st.write("Technologies used: Python, Pandas, SQL")
    st.markdown("[GitHub Repo](https://github.com/ayazjutt/car-price-prediction)")

    # Skill Section

if menu == 'Skills':
    st.header('Skills')
    st.subheader('Programming Skills')

    st.write("Python: ")
    st.progress(90)  
    
    st.write("Machine Learning: ")
    st.progress(77)
    
    st.write("Web Development: ")
    st.progress(85)

    st.write("Data Analysis: ")
    st.progress(88)

    st.write("C++: ")
    st.progress(89)

  # Contact Section

if menu == 'Contact':
    st.header('Contact Me')
    st.write("""
        You can reach out to me using the form below or through my professional profiles.
    """)

    name = st.text_input('Name')
    email = st.text_input('Email')
    message = st.text_area('Message')

    if st.button('Send Message'):
        if name and email and message:
            st.write(f"Message from {name} sent successfully!")
        else:
            st.error("Please fill in all fields before sending the message.")

    # Professional links
    st.write("Find me on:")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/AyazBashir)")
    st.markdown("[GitHub](https://github.com/Ayaz123)")


