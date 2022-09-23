import streamlit as st
import meta as mt

def main():
    st.header("💾 Bellek Tabanlı Tavsiye Sistemi 💾")
    st.write("---")

    st.markdown(
        "Belleğe dayalı yöntemler, kullanıcılar veya öğeler arasındaki benzerliği hesaplamak için geçmiş kullanıcı "
        "derecelendirmesi verilerini kullanır. Bu yöntemlerin arkasındaki fikir, kullanıcılar veya öğeler arasında "
        "benzerlik ölçüsü tanımlamak ve görünmeyen öğeleri önermek için en benzer olanı bulmaktır."
        "İki ana bellek tabanlı işbirlikçi filtreleme algoritması türü vardır: "
        "Kullanıcı Tabanlı ve Ürün Tabanlı. Aralarında küçük farklar olsa da, pratikte çok farklı yaklaşımlar uygulanır. "
        "Bu nedenle elimizdeki durum için hangisinin uygun olduğunu bilmek çok önemlidir. \n"

        "- **Kullanıcı tabanlı:** Bu yötemde, benzer içeriği gören/derecelendiren kullanıcıları buluyor ve yeni öğeler önermek için tercihlerini kullanıyoruz.\n"
        "- **Ürün tabanlı:** Mantık benzerdir ancak bunun yerine belirli bir filmden (veya film setinden) başlayarak diğer kullanıcıların tercihlerine göre benzer filmler buluyoruz.")

    st.image("assets/images/memory_based.jpg")
    st.write("---")
    st.subheader("Model 🎯")
    with st.expander("Model Fonksiyonu",
                     expanded=False):
        code = (mt.meta6)
        st.code(code, language='python')

    st.subheader("Youtube 🎯")
    with st.expander("Videoları YT API Üzerinden Çekme İşlemi",
                     expanded=False):
        code = (mt.meta7)
        st.code(code, language='python')

    st.subheader("Ayrıntılar 🎯")
    with st.expander("get_details Fonksiyonu",
                     expanded=False):
        code = (mt.meta8)
        st.code(code, language='python')

