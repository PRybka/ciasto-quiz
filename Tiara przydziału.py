import streamlit as st

st.title("🧙‍♂️ Tiara Przydziału")
st.markdown("Rozwiąż quiz i dowiedz się, do którego domu w Hogwarcie trafisz!")

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0

# Pytanie 1
q1 = st.radio("1️⃣ Czy wolisz świt czy zmierzch?", ["Świt", "Zmierzch"])
if q1 == "Świt":
    gryffindor += 1
    ravenclaw += 1
elif q1 == "Zmierzch":
    hufflepuff += 1
    slytherin += 1

# Pytanie 2
q2 = st.radio("2️⃣ Jak chcesz być zapamiętany/a po śmierci?", ["Dobry", "Wielki", "Mądry", "Odważny"])
if q2 == "Dobry":
    hufflepuff += 2
elif q2 == "Wielki":
    slytherin += 2
elif q2 == "Mądry":
    ravenclaw += 2
elif q2 == "Odważny":
    gryffindor += 2

# Pytanie 3
q3 = st.radio("3️⃣ Który instrument najbardziej Ci się podoba?", ["Skrzypce", "Trąbka", "Fortepian", "Bęben"])
if q3 == "Skrzypce":
    slytherin += 4
elif q3 == "Trąbka":
    hufflepuff += 4
elif q3 == "Fortepian":
    ravenclaw += 4
elif q3 == "Bęben":
    gryffindor += 4

# Przycisk z wynikiem
if st.button("🎓 Pokaż mój dom w Hogwarcie!"):
    # Punktacja
    st.subheader("📊 Punktacja")
    st.write(f"🦁 Gryffindor: {gryffindor}")
    st.write(f"🦡 Hufflepuff: {hufflepuff}")
    st.write(f"🦅 Ravenclaw: {ravenclaw}")
    st.write(f"🐍 Slytherin: {slytherin}")

    # Oblicz dom z największą liczbą punktów
    domy = {
        "Gryffindor 🦁": gryffindor,
        "Hufflepuff 🦡": hufflepuff,
        "Ravenclaw 🦅": ravenclaw,
        "Slytherin 🐍": slytherin
    }
    wybrany_dom = max(domy, key=domy.get)

    st.success(f"🏆 Tiara Przydziału mówi... **{wybrany_dom}**!")

