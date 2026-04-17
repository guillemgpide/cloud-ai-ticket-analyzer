import pandas as pd
import random
import os

print("🔄 Generant tiquets d'entrenament corregits...")

tech_subj = ["El router", "L'ordinador", "L'aplicació", "El servidor", "El programa", "El wifi", "El sistema"]
tech_neg_v = ["no s'encén", "va molt lent", "es penja constantment", "dona error de codi", "funciona fatal", "està trencat"]
tech_pos_v = ["va genial", "funciona molt bé", "és super ràpid", "s'ha arreglat", "no dona problemes"]

bill_neg = ["La factura és molt cara", "M'heu cobrat de més", "Error en el pagament", "No puc pagar la quota", "El preu és abusiu"]
bill_pos = ["Pagament realitzat amb èxit", "Factura pagada correctament", "Tot bé amb el cobrament", "Gràcies pel descompte"]
bill_neu = ["Vull la factura en PDF", "Quin és el percentatge d'IVA?", "Com canvio la targeta?", "Quan es cobra el rebut?"]

sales_neg = ["El procés de compra és un caos", "No trobo on comprar", "La web de vendes cau", "La llicència és massa cara"]
sales_pos = ["Vull comprar 10 llicències", "M'interessa el pla premium", "Servei de vendes excel·lent", "Compra fàcil i ràpida"]
sales_neu = ["Informació de preus sisplau", "Teniu plans per a empreses?", "Vull un pressupost", "Diferències entre plans"]

support_neg = ["L'atenció al client és pèssima", "El meu company és un incompetent", "M'han parlat molt malament", "No m'ajudeu gens", "L'operador no en té ni idea", "Estic enfadat amb el meu company"]
support_pos = ["Estic content amb el meu company", "L'operador m'ha ajudat molt", "Un equip fantàstic", "Molt bona atenció al client", "El noi de suport és un crack"]
support_neu = ["Com contacto amb recursos humans?", "Vull parlar amb un supervisor", "Quin és l'horari d'atenció?", "Passeu-me amb el meu company"]

feedback_neg = ["El disseny nou és lleig", "Falten moltes opcions", "No m'agrada aquesta actualització", "L'interfície és pitjor ara"]
feedback_pos = ["M'encanta la nova versió", "El disseny és preciós", "Bona feina amb l'app", "Molt intuïtiu i ràpid"]

suf_neg = ["", " avui mateix.", " i estic molt enfadat.", " quin desastre.", " és inacceptable.", " doneu-me una solució."]
suf_pos = ["", " gràcies.", " moltes gràcies.", " bona feina.", " felicitats.", " seguiu així."]
suf_neu = ["", " si us plau.", " gràcies.", " avui.", " quan pugueu."]

dades = []

for i in range(300):
    categoria = random.choice(["Technical", "Billing", "Sales", "Support", "Feedback"])
    
    if categoria == "Technical":
        sentiment = random.choice(["Negative", "Positive"])
        if sentiment == "Negative": text = f"{random.choice(tech_subj)} {random.choice(tech_neg_v)}"
        else: text = f"{random.choice(tech_subj)} {random.choice(tech_pos_v)}"
            
    elif categoria == "Billing":
        sentiment = random.choice(["Negative", "Positive", "Neutral"])
        if sentiment == "Negative": text = random.choice(bill_neg)
        elif sentiment == "Positive": text = random.choice(bill_pos)
        else: text = random.choice(bill_neu)
        
    elif categoria == "Sales":
        sentiment = random.choice(["Negative", "Positive", "Neutral"])
        if sentiment == "Negative": text = random.choice(sales_neg)
        elif sentiment == "Positive": text = random.choice(sales_pos)
        else: text = random.choice(sales_neu)
        
    elif categoria == "Support":
        sentiment = random.choice(["Negative", "Positive", "Neutral"])
        if sentiment == "Negative": text = random.choice(support_neg)
        elif sentiment == "Positive": text = random.choice(support_pos)
        else: text = random.choice(support_neu)
        
    else: 
        sentiment = random.choice(["Negative", "Positive"])
        if sentiment == "Negative": text = random.choice(feedback_neg)
        else: text = random.choice(feedback_pos)
        
    if sentiment == "Negative": text += random.choice(suf_neg)
    elif sentiment == "Positive": text += random.choice(suf_pos)
    else: text += random.choice(suf_neu)
    
    dades.append({"text": text.strip(), "category": categoria, "sentiment": sentiment})

df = pd.DataFrame(dades)
os.makedirs("data", exist_ok=True)
df.to_csv("data/dataset.csv", index=False, encoding="utf-8")
print(f"✅ Creat el fitxer 'data/dataset.csv' amb {len(df)} tiquets impecables!")