import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

# Initialize session state
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None

def get_headers():
    return {"Authorization": f"Bearer {st.session_state.token}"}

# ---------- Login Page ----------
def login_page():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        data = {
            "username": username,
            "password": password
        }
        res = requests.post(f"{BASE_URL}/token", data=data)
        if res.status_code == 200:
            st.session_state.token = res.json()["access_token"]
            st.session_state.username = username
            st.success("✅ Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("❌ Login failed. Check your credentials.")

# ---------- Note List + Delete ----------
def list_notes():
    st.header(f"📚 Abdellahi, welcome to your note management tool")
    st.markdown("---")

    st.subheader("📝 Create a New Note")
    with st.form("create_note_form"):
        title = st.text_input("Title")
        content = st.text_area("Content")
        submitted = st.form_submit_button("Create")
        if submitted:
            note_data = {
                "title": title,
                "content": content,
                "username": st.session_state.username
            }
            res = requests.post(f"{BASE_URL}/notes", json=note_data, headers=get_headers())
            if res.status_code == 201:
                st.success("✅ Note created successfully!")
                st.experimental_rerun()
            else:
                st.error("❌ Failed to create note.")

    st.markdown("### 📋 Your Notes")

    res = requests.get(f"{BASE_URL}/notes", headers=get_headers())
    if res.status_code == 200:
        notes = res.json()
        if not notes:
            st.info("No notes found.")
        for note in notes:
            col1, col2, col3 = st.columns([4, 6, 1])
            with col1:
                st.markdown(f"**{note['title']}**")
            with col2:
                st.markdown(note['content'])
            with col3:
                if st.button("🗑️", key=note["id"]):
                    delete_res = requests.delete(f"{BASE_URL}/notes/{note['id']}", headers=get_headers())
                    if delete_res.status_code == 200:
                        st.success("✅ Note deleted!")
                        st.experimental_rerun()
                    else:
                        st.error("❌ Failed to delete note.")
    else:
        st.error("Failed to retrieve notes.")

# ---------- Main Logic ----------
if st.session_state.token:
    list_notes()
else:
    login_page()
