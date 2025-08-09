import streamlit as st

st.set_page_config(layout="wide", page_title="Chat with DEEPSEED")

# --- Sidebar ---
with st.sidebar:
    st.markdown("<div style='font-size: 1.5rem; font-weight: bold; color: #b5e853; display: flex; align-items: center; gap: 0.5rem;'>"
                "<span style='font-size: 1.7rem;'>🌱</span> DEEPSEED" 
                "</div>", unsafe_allow_html=True)
    st.markdown("<span style='color: #aaa; font-size: 0.9rem;'>one seed at a time</span>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<span style='font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem;'>📊 <b>Session Stats</b></span>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Messages", "2")
    with col2:
        st.metric("Total", "2")
    st.markdown("---")
    st.markdown("<span style='font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem;'>⚡ <b>Quick Actions</b></span>", unsafe_allow_html=True)
    st.button("💡 Tell me a joke", use_container_width=True)
    st.button("💡 Explain AI", use_container_width=True)
    st.button("💡 Help brainstorm", use_container_width=True)
    st.button("💡 Writing tips", use_container_width=True)
    st.button("💡 Book recommendations", use_container_width=True)
    st.markdown("---")
    st.markdown("<span style='font-size: 1.1rem; display: flex; align-items: center; gap: 0.5rem;'>🛠 <b>Controls</b></span>", unsafe_allow_html=True)
    st.markdown("<span style='color: #888;'>Previous</span>", unsafe_allow_html=True)

# --- Main Content ---
st.markdown("""
<div style='display: flex; align-items: center; gap: 0.5rem;'>
  <span style='font-size: 2rem;'>💬</span>
  <span style='font-size: 1.5rem; font-weight: bold;'>Chat with DEEPSEED</span>
</div>
""", unsafe_allow_html=True)



# --- Chat UI Section ---
st.markdown("""
<div style='background: #23242a; border-radius: 10px; padding: 2rem 2rem 1rem 2rem; margin-top: 1.5rem; min-height: 400px; display: flex; flex-direction: column; gap: 0;'>
  <!-- Chat History Section -->
  <div style='flex: 1 1 auto; max-height: 350px; overflow-y: auto; margin-bottom: 2rem; scrollbar-width: thin; scrollbar-color: #888 #23242a;'>
    <!-- User message (right) -->
    <div style='display: flex; align-items: flex-start; gap: 0.75rem; margin-bottom: 1.2rem; justify-content: flex-end;'>
      <div style='background: #18191f; color: #fff; border-radius: 8px; padding: 0.9rem 1.2rem; min-width: 120px; max-width: 80%; text-align: right;'>
        <span style='font-weight: 500;'>How do I use DEEPSEED?</span>
      </div>
      <span style='background: #23242a; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border: 1.5px solid #b5e853;'><span style='font-size: 1.2rem;'>🧑‍💻</span></span>
    </div>
    <!-- Bot message (left) -->
    <div style='display: flex; align-items: flex-start; gap: 0.75rem; margin-bottom: 1.2rem; justify-content: flex-start;'>
      <span style='background: #23242a; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border: 1.5px solid #5e9cff;'><span style='font-size: 1.2rem;'>🤖</span></span>
      <div style='background: #18191f; color: #f5c542; border-radius: 8px; padding: 0.9rem 1.2rem; min-width: 120px; max-width: 80%;'>
        <span>Welcome to the world of deepseeds! Based on your message, I can provide some insights on this. <span style='color: #ffd700;'>💡</span></span>
      </div>
    </div>
    <!-- User message 2 (right) -->
    <div style='display: flex; align-items: flex-start; gap: 0.75rem; margin-bottom: 1.2rem; justify-content: flex-end;'>
      <div style='background: #18191f; color: #fff; border-radius: 8px; padding: 0.9rem 1.2rem; min-width: 120px; max-width: 80%; text-align: right;'>
        <span style='font-weight: 500;'>Can you explain the session stats?</span>
      </div>
      <span style='background: #23242a; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border: 1.5px solid #b5e853;'><span style='font-size: 1.2rem;'>🧑‍💻</span></span>
    </div>
    <!-- Bot message 2 (left) -->
    <div style='display: flex; align-items: flex-start; gap: 0.75rem; margin-bottom: 1.2rem; justify-content: flex-start;'>
      <span style='background: #23242a; border-radius: 50%; width: 36px; height: 36px; display: flex; align-items: center; justify-content: center; border: 1.5px solid #5e9cff;'><span style='font-size: 1.2rem;'>🤖</span></span>
      <div style='background: #18191f; color: #f5c542; border-radius: 8px; padding: 0.9rem 1.2rem; min-width: 120px; max-width: 80%;'>
        <span>Session stats show the number of messages and total interactions in your current chat. 📊</span>
      </div>
    </div>
  </div>
  <!-- Input Section -->
  <div style='border-top: 1px solid #333; padding-top: 1.2rem; margin-top: 0.5rem;'>
    <form>
      <div style='display: flex; gap: 0.5rem;'>
        <input type='text' placeholder='Type your message here...' style='flex: 1 1 auto; padding: 0.75rem; border-radius: 6px; border: 1px solid #333; background: #18191f; color: #fff; font-size: 1rem;' />
        <button type='submit' style='background: #23242a; color: #fff; border: none; border-radius: 6px; padding: 0.75rem 1.2rem; font-size: 1rem;'>Send 🚀</button>
        <label style='background: #23242a; color: #fff; border-radius: 6px; padding: 0.75rem 1.2rem; font-size: 1rem; display: flex; align-items: center; cursor: pointer;'>
          <input type='file' style='display: none;' />
          Upload 📎
        </label>
      </div>
    </form>
  </div>
</div>
""", unsafe_allow_html=True)