import streamlit as st
from PIL import Image 
import imagehash
import os, os.path

st.title("Image Plagarism Checker Project")

nav = st.sidebar.radio("Go to:",["Home","About the Project", "About the Developer"])

if (nav == "Home"):

    st.subheader("Home")
    
    Home_text_1 = """Here you can upload a file and a path of a folder. 
    If the uploaded file is already present in the folder path provided by you then our
    algorithm will detect it and will say it is **PLAGARISED**"""
    st.write(Home_text_1)

    images_dir = "images"
    db_path = st.text_input("File Path",images_dir) # By default it will use the images path that comes with this project
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    f=0
    if image_file is not None:
        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,"filesize":image_file.size}
        st.write(file_details)
        
        # Converting using imagehash
        if (image_file.type == "image/png") or (image_file.type == "image/jpg") or (image_file.type == "image/jpeg"):
            f = 1
        image_file = Image.open(image_file)
        image_file_hash = imagehash.average_hash(image_file)
    
    if st.button("Check"):
        if(f == 1):
            flag = 0
            count = 0
            directory = db_path # iterate over files in that directory
            
            for filename in os.listdir(directory):
                split_file = os.path.splitext(filename)
                file_ext  = split_file[1]
                if(file_ext == ".png") or (file_ext == ".jpg") or (file_ext == ".jpeg"):
                    count = 1
                    image_file_db = Image.open(directory + "/" + filename)
                    image_file_db_hash = imagehash.average_hash(image_file_db) # Converting using imagehash
                    if (image_file_hash == image_file_db_hash):
                        flag = 1
                        st.markdown('### The Image is **PLAGARISED**')
                        st.text("Uploaded Image :")
                        st.image(image_file)
                        st.text("Matched Image :")
                        st.image(image_file_db)
                        break

            if flag == 0 and count == 1:
                st.markdown('### The Image is **NOT PLAGARISED** ') 
            elif flag == 0 and count == 0:
                st.markdown('### No Image found in the folder path you entered ')
        
        else:
            st.markdown("### Uploaded Image format is not recognized")

if (nav == "About the Project"):
    st.subheader("About the Project")
    ATP_1 = """ This Project was created with vision of detecting Plagarised image content
    by taking an image input from you and a folder path where it can search if the uploaded image
    by you is already present in that folder or not. This project
    conatins a folder of some images(randomly downloaded from internet) which will be used
    as the default folder if you do not provide any folder path. This simple project is created using 
    the powerful tool [imagehash](https://github.com/JohannesBuchner/imagehash) created by 
    [Johannes Buchner](https://astrost.at/istics/index.html)"""
    st.write(ATP_1)
if (nav == "About the Developer"):
    st.subheader("About the Developer")
    about_me = """Hi, I am Diptaraj Sen, currently a Computer Science Engineering 
    undergrad with the love for programming in Python. My research interests are broadly in
    the domain of Machine Learning, Deep learning, Natural Language Processing, Computer Vision
    etc."""
    st.write(about_me)
    st.subheader("Find me at:")
    st.write("[LinkedIn](https://www.linkedin.com/in/diptaraj23/)")
    st.write("[GitHub](https://github.com/diptaraj23)")
    st.write("[Kaggle](https://www.kaggle.com/diptaraj23)")
    st.write("[Google Scholar](https://scholar.google.com/citations?user=SWK7cSgAAAAJ&hl=en)")
    st.write("[Medium](https://medium.com/@diptaraj23)")




