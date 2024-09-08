import streamlit as st

# Set the title of the contact page
st.markdown("<h2 style='text-align: center;'>CONTACT ME</h2>",unsafe_allow_html=True)

# Introduction textss
st.write("Feel free to reach out to me through any of the following channels:")

# GitHub with emoji
st.markdown(
    """
    - **GitHub:** [![GitHub](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/arhumhussain)
    """
)

# LinkedIn with emoji
st.markdown(
    """
    - **LinkedIn:** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/arhum-hussain-3b6b63283)
    """
)

# Gmail with emoji
st.markdown(
    """
    - **Email:** [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:arhumhussain49@gmail.com)
    """
)

# Add a footer if needed
st.write("Looking forward to connecting with you!")
