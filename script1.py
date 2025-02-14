import random
import pandas as pd

def genera_dati():
    nomi = ["Luca", "Marco", "Giulia", "Sofia", "Marta"]
    cognomi = ["Rossi", "Bianchi", "Verdi", "Neri", "Gialli"]
    email_domains = ["example.com", "test.org"]
    utenti = []
    
    for _ in range(10):
        nome = random.choice(nomi)
        cognome = random.choice(cognomi)
        email = f"{nome.lower()}.{cognome.lower()}@{random.choice(email_domains)}"
        telefono = f"+39{random.randint(1000000000, 9999999999)}"
        utenti.append({"Nome": nome, "Cognome": cognome, "Email": email, "Telefono": telefono})
    
    return pd.DataFrame(utenti)

dati = genera_dati()
dati.to_excel("utenti.xlsx", index=False)
print("File Excel generato.")
