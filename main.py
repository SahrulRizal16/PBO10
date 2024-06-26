
import streamlit as st
import requests

st.title("Interaksi API ChatPDF")
st.write("Masukkan pesan Anda untuk dikirim ke API ChatPDF:")

pesan_pengguna = st.text_input("Pesan Anda")

def panggil_api_chatpdf(pesan):
    headers = {
        'x-api-key': st.secrets['code'],  # Pastikan API key Anda benar
        'Content-Type': 'application/json',
    }
    
    data = {
        'sourceId': "src_DyXpC2nCbkMs3L22Le1Dj",  # Pastikan sourceId Anda benar
        'messages': [
            {
                'role': "user",
                'content': pesan,
            }
        ]
    }
    
    try:
        response = requests.post(
            'https://api.chatpdf.com/v1/chats/message', headers=headers, json=data)
        
        response.raise_for_status()
        
        hasil = response.json()
        return hasil.get('content', 'Tidak ada konten dalam respons')
    except requests.exceptions.RequestException as e:
        return f"Permintaan gagal: {e}"
    except ValueError:
        return "Gagal menguraikan respons dari API"

# Tombol untuk mengirim pesan
if st.button("Kirim"):
    if pesan_pengguna:
        with st.spinner('Mengirim pesan ke API...'):
            hasil = panggil_api_chatpdf(pesan_pengguna)
            st.write("Respons dari API:")
            st.write(hasil)
    else:
        st.write("Silakan masukkan pesan.")

