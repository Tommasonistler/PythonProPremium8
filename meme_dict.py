meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "CHILL": "Non preocuparti/Qualcosa di rilassante"
            }
parola = (input("Scrivi una parola che non capisci:")).upper()
if parola in meme_dict.keys():
    print(parola, ":", meme_dict[parola])
else:
    print("Questa parola non è presente nel dizionario")
