def recommend_location(city):
    locations = {
        "Bali":["Seminyak","Canggu","Kuta","Ubud","Nusa Dua"],
        "Jakarta":["SCBD","PIK","Kemang","Senopati"],
        "Batam":["Nagoya"],
        "Surabaya":["Tunjungan"],
        "Bandung":["Dago","Riau"],
        "Lombok":["Senggigi","Mandalika"]
    }
    return locations.get(city, ["Commercial Area"])