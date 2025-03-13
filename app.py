import streamlit as st
import pandas as pd

# Initialize session state for idea tracking if not already present
if 'ideas' not in st.session_state:
    st.session_state['ideas'] = []

# Function to add a new idea
def add_idea(title, description):
    new_idea = {
        'title': title,
        'description': description,
        'likes': 0
    }
    st.session_state['ideas'].append(new_idea)

# Function to update likes
def like_idea(index):
    st.session_state['ideas'][index]['likes'] += 1

# Function to edit an idea
def edit_idea(index, new_title, new_description):
    st.session_state['ideas'][index]['title'] = new_title
    st.session_state['ideas'][index]['description'] = new_description

# Streamlit UI
st.title("💡 Ideation Portal")

# Form to submit new idea
with st.form("new_idea_form"):
    title = st.text_input("Idea Title")
    description = st.text_area("Idea Description")
    submitted = st.form_submit_button("Submit Idea")

    if submitted and title and description:
        add_idea(title, description)

# Display all ideas sorted by like count
if st.session_state['ideas']:
    st.subheader("📌 Ideas")

    # Sort ideas by likes in descending order
    sorted_ideas = sorted(st.session_state['ideas'], key=lambda x: x['likes'], reverse=True)

    for idx, idea in enumerate(sorted_ideas):
        st.write(f"### {idea['title']}")
        st.write(f"{idea['description']}")
        st.write(f"👍 Likes: {idea['likes']}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("👍 Like", key=f"like_{idx}"):
                original_index = st.session_state['ideas'].index(idea)
                like_idea(original_index)
        with col2:
            if st.button("✏️ Edit", key=f"edit_{idx}"):
                new_title = st.text_input("Edit Title", value=idea['title'], key=f"edit_title_{idx}")
                new_description = st.text_area("Edit Description", value=idea['description'], key=f"edit_desc_{idx}")
                if st.button("Save Changes", key=f"save_{idx}"):
                    original_index = st.session_state['ideas'].index(idea)
                    edit_idea(original_index, new_title, new_description)
