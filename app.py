import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Kişisel Yapay Zekâm", page_icon="✦", layout="centered")

st.title("Kişisel Yapay Zekâm")
st.caption("İlk sürüm · Sohbet geçmişi bu oturum boyunca tutulur.")

# Secrets are configured in Streamlit Cloud → App settings → Secrets.
try:
    app_password = st.secrets["APP_PASSWORD"]
    api_key = st.secrets["GOOGLE_API_KEY"]
except Exception:
    st.error(
        "Kurulum eksik. Streamlit uygulama ayarlarında APP_PASSWORD ve "
        "GOOGLE_API_KEY sırlarını tanımlayın. README dosyasındaki adımları izleyin."
    )
    st.stop()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    with st.form("login"):
        entered_password = st.text_input("Erişim şifresi", type="password")
        submitted = st.form_submit_button("Giriş yap")
    if submitted:
        if entered_password == app_password:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Şifre doğru değil.")
    st.info("Bu ilk sürüm basit bir erişim kapısı kullanır; hassas veriler için profesyonel kimlik doğrulama değildir.")
    st.stop()

with st.sidebar:
    st.subheader("Asistan ayarları")
    assistant_name = st.text_input("Asistanın adı", value="Atlas")
    personality = st.selectbox(
        "Konuşma tarzı",
        ["Samimi ve rahat", "Sakin ve ciddi", "Esprili", "Kısa ve doğrudan"],
    )
    st.caption("Sohbet geçmişi şu an yalnızca açık oturumda tutulur.")
    if st.button("Sohbeti temizle"):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

system_instruction = f"""
Senin adın {assistant_name}. Kullanıcının kişisel yapay zekâ asistanısın.
Türkçe konuş. Konuşma tarzın: {personality}.
Yardımcı, dürüst ve açık ol. Bilmediğin şeyi biliyormuş gibi gösterme.
Kullanıcıdan açık izin almadan dış dünyada işlem yaptığını iddia etme.
Gizli anahtarları, parolaları veya uygulama sırlarını asla isteme.
"""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Bir şey sor...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        client = genai.Client(api_key=api_key)
        contents = []
        for message in st.session_state.messages:
            role = "user" if message["role"] == "user" else "model"
            contents.append(
                types.Content(
                    role=role,
                    parts=[types.Part(text=message["content"])]
                )
            )

        with st.chat_message("assistant"):
            with st.spinner("Düşünüyorum..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.8,
                    ),
                )
                answer = response.text or "Bu sefer yanıt oluşturamadım. Tekrar dener misin?"
                st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})
    except Exception as exc:
        st.error(
            "Yanıt alınamadı. API anahtarını, model erişimini ve ücretsiz kullanım "
            "limitini kontrol et. Teknik ayrıntı: " + str(exc)
        )
