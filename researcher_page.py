import streamlit as st
import pandas as pd

# Title of the app
st.title("Fabio O'Ryan-Paulo")

# Collect basic information
name = "Fabio O'Ryan-Paulo"
degree = "BSc. Computer Science (Honours) and Physics"
institution = "University of Cape Town"
keywords = "Self-Taught Guitarist | UCT Physics and Computer Science (Hons) | Aspiring Artificial Intelligence Engineer | 22 | 🇿🇦 x 🇵🇹"
about = "I'm Fabio, a Computer Scientist and Physicist. I have recently completed my postgraduate studies in Computer Science Honours. My primary interests lie in simulation software, game development in Unity, Artificial Intelligence, Web Development, and Software development in general"


st.image("https://media.licdn.com/dms/image/v2/D4E03AQERTBd1_OewsQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1730352867664?e=1743638400&v=beta&t=ZKkb3rOzl5O_tvPWWv0e55t3Gy5JzsiYFvSWUjA7wfI", width=200)
st.write(f"**{keywords}**")
# Display basic profile information
st.header("Researcher Overview")
st.write(f"{about}")

st.header("Education")
st.write(f"**Degree:** {degree}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Projects")
st.write(f"**Java Herding Simulator:** In this project, I developed a realistic, Java-based herding simulator with animal-specific traits and dynamic terrain, integrated with "
		 "Unity for versatile 2D and 3D simulations. The software was developed in Java and used the Java swing library for the GUI. The software was developed as part of my Computer Science 3rd Year capstone project.")
st.write(f"**Determining the Neutron Energy Spectrum of AmBe:** Supervised by a physics PhD researcher at the University of Cape Town, the C++ based GEANT4 framework was "
		 "employed to simulate neutron production of an americium-beryllium neutron source. "
		 "Analysis and comparison of the simulated neutron energy spectrum against standardised data yielded valuable "
		 "insights into nuclear physics, with direct applicability to nuclear engineering and radiation physics.")
st.write(f"**A Participation Monitoring Tool for digital whiteboards (Miro):** This project proposes a digital tool that interfaces with Miro, a popular online collaborative whiteboard platform. The tool monitors participant engagement and provides real-time feedback to design thinking workshop facilitators to identify and address participation imbalances, promoting a more inclusive workshop.")


# Add a contact section
st.header("Contact Information")
email = "oryfab001@myuct.ac.za"
github = "https://github.com/FabsOP/FabsOP"
linkedIn = "https://www.linkedin.com/in/fabioory"
st.write(f"**Email:** {email}")
st.write(f"**GitHub:** {github}")
st.write(f"**LinkedIn:** {linkedIn}")
