
import streamlit as st

st.title("🎂 Ciasto na święta")
st.markdown("Wybierz odpowiedzi, a my powiemy Ci, które ciasto najbardziej do Ciebie pasuje!")

# Zmienne punktowe
punkty = {
    "thriatlon": 0,
    "rurki": 0,
    "to_cos_z_pistajowym_kremem": 0,
    "mazurek": 0
}

# Pytanie 1
q1 = st.radio("1️⃣ Czy lubisz pistacje?", ["Tak", "Nie"])
if q1 == "Tak":
    punkty["to_cos_z_pistajowym_kremem"] += 1
elif q1 == "Nie":
    punkty["rurki"] += 1
    punkty["mazurek"] += 1
    punkty["thriatlon"] += 1

# Pytanie 2
q2 = st.radio("2️⃣ Co najbardziej lubisz w cieście?", ["Chrupkość", "Śmietanę", "Pistacje", "Karmel"])
if q2 == "Chrupkość":
    punkty["thriatlon"] += 2
elif q2 == "Śmietanę":
    punkty["rurki"] += 2
elif q2 == "Pistacje":
    punkty["to_cos_z_pistajowym_kremem"] += 2
elif q2 == "Karmel":
    punkty["mazurek"] += 2

# Pytanie 3
q3 = st.radio("3️⃣ Co Mysia zaproponowała jako ciasto na święta?", ["Mazurek", "Rurki", "Triathlonowe", "Z pistacjami"])
if q3 == "Mazurek":
    punkty["mazurek"] += 3
elif q3 == "Rurki":
    punkty["rurki"] += 3
elif q3 == "Triathlonowe":
    punkty["thriatlon"] += 3
elif q3 == "Z pistacjami":
    punkty["to_cos_z_pistajowym_kremem"] += 3

# Przycisk pokazujący wynik
if st.button("🔍 Sprawdź swoje ciasto!"):
    wynik = max(punkty, key=punkty.get)

    nazwy = {
        "thriatlon": "Triathlonowe ciasto energetyczne 💪",
        "rurki": "Klasyczne rurki z kremem 🍦",
        "to_cos_z_pistajowym_kremem": "Coś z pistacjowym kremem 💚",
        "mazurek": "Tradycyjny mazurek 🇵🇱"
    }

    st.success(f"Twoje ciasto na święta to: **{nazwy[wynik]}**")
