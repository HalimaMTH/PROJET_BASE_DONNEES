import streamlit as st
import sqlite3
import pandas as pd

def get_conn():
    return sqlite3.connect("hotel.db", check_same_thread=False)

# Afficher les réservations
def afficher_reservations():
    conn = get_conn()
    try:
        df = pd.read_sql_query("""
            SELECT R.id, R.date_debut, R.date_fin, C.nom, H.ville AS ville_hotel
            FROM Reservation R
            JOIN Client C ON R.id_client = C.id
            JOIN Chambre CH ON R.id_chambre = CH.id
            JOIN Hotel H ON CH.id_hotel = H.id
        """, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors de la récupération des réservations : {e}")

# Afficher les clients
def afficher_clients():
    conn = get_conn()
    try:
        df = pd.read_sql_query("SELECT * FROM Client", conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors de la récupération des clients : {e}")

# Afficher les chambres disponibles
def chambres_disponibles(debut, fin):
    conn = get_conn()
    try:
        df = pd.read_sql_query(f"""
            SELECT * FROM Chambre
            WHERE id NOT IN (
                SELECT id_chambre FROM Reservation
                WHERE NOT (date_fin < '{debut}' OR date_debut > '{fin}')
            )
        """, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Erreur lors de la récupération des chambres disponibles : {e}")

# Ajouter un client
def ajouter_client():
    st.subheader("Ajouter un nouveau client")
    with st.form("form_client"):
        adresse = st.text_input("Adresse")
        ville = st.text_input("Ville")
        code_postal = st.text_input("Code postal")
        email = st.text_input("Email")
        telephone = st.text_input("Téléphone")
        nom = st.text_input("Nom complet")
        submitted = st.form_submit_button("Ajouter")
        if submitted:
            try:
                conn = get_conn()
                conn.execute("""
                    INSERT INTO Client (adresse, ville, code_postal, email, telephone, nom)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (adresse, ville, code_postal, email, telephone, nom))
                conn.commit()
                st.success("✅ Client ajouté avec succès.")
            except Exception as e:
                st.error(f"Erreur lors de l'ajout du client : {e}")

# Ajouter une réservation
def ajouter_reservation():
    st.subheader("Ajouter une réservation")
    with st.form("form_reservation"):
        id_client = st.number_input("ID Client", min_value=1, step=1)
        id_chambre = st.number_input("ID Chambre", min_value=1, step=1)
        date_debut = st.date_input("Date de début")
        date_fin = st.date_input("Date de fin")
        submitted = st.form_submit_button("Réserver")
        if submitted:
            try:
                conn = get_conn()
                conn.execute("""
                    INSERT INTO Reservation (date_debut, date_fin, id_client, id_chambre)
                    VALUES (?, ?, ?, ?)
                """, (str(date_debut), str(date_fin), id_client, id_chambre))
                conn.commit()
                st.success("✅ Réservation ajoutée.")
            except Exception as e:
                st.error(f"Erreur lors de l'ajout de la réservation : {e}")

# Interface utilisateur
st.title("🏨 Gestion Hôtelière")

menu = st.sidebar.radio("Menu", [
    "📋 Liste des réservations",
    "👤 Liste des clients",
    "🔍 Chambres disponibles",
    "➕ Ajouter un client",
    "🛎️ Ajouter une réservation"
])

if menu == "📋 Liste des réservations":
    afficher_reservations()
elif menu == "👤 Liste des clients":
    afficher_clients()
elif menu == "🔍 Chambres disponibles":
    debut = st.date_input("Date de début")
    fin = st.date_input("Date de fin")
    if debut and fin:
        chambres_disponibles(str(debut), str(fin))
elif menu == "➕ Ajouter un client":
    ajouter_client()
elif menu == "🛎️ Ajouter une réservation":
    ajouter_reservation()
