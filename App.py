def calcTotaalInkomen (jaarInkomen, jaarInkomenPartner):
    return jaarInkomen + jaarInkomenPartner

def calcMaxcHypotheek (totaalnkomen, studieSchuld):
    if (studieSchuld):
        return totaalnkomen * 4.25 * 0.75
    else:
      return totaalnkomen * 4.25

def calcMaxHypotheekMetTermijnen(termijnen, hypotheek):
    match termijnen:
        case 1:
            return hypotheek * 1.02
        case 5:
           return hypotheek * 1.03
        case 10:
            return hypotheek * 1.035
        case 20:
           return hypotheek * 1.045
        case 30:
           return hypotheek * 1.05
    

def MaxHypotheekPartner():
    def VraagPostcode():
        PostCode = input("Wat is je postcode? :  ")
        if not PostCode:
            print("Je hebt geen postcode ingevuld")
            VraagPostcode()
            return

        try:
            PostcodeNummer = int(PostCode)
        except ValueError:
            print("Dit is geen geldige postcode, probeer opnieuw.")
            VraagPostcode()
            return

        if len(PostCode) != 4 or PostcodeNummer in [9679, 9681, 9682]:
            print("Dit is geen geldige postcode, probeer opnieuw.")
            VraagPostcode()
        else:
            VraagJaarInkomen()

    def VraagJaarInkomen():
        JaarInkomen = input("Wat is je jaarinkomen? :  ")
        try:
            jaarInkomenNummer = int(JaarInkomen)
        except ValueError:
            print("Dit is geen geldig jaarinkomen, probeer opnieuw.")
            VraagJaarInkomen()
            return

        VraagPartner(jaarInkomenNummer)

    def VraagPartner(jaarInkomenNummer):
        BoolPartner = input("Heb je een partner? (ja/nee) :  ").strip().lower()
        if BoolPartner == "nee":
            VraagStudieSchuld(jaarInkomenNummer, 0)
        elif BoolPartner == "ja":
            jaarInkomenPartner = input("Wat is het jaarinkomen van je partner? :  ")
            try:
                jaarInkomenPartner = int(jaarInkomenPartner)
            except ValueError:
                print("Dit is geen geldig jaarinkomen voor je partner, probeer opnieuw.")
                VraagPartner(jaarInkomenNummer)
                return

            VraagStudieSchuldPartner(jaarInkomenNummer, jaarInkomenPartner)
        else:
            print("Antwoord met 'ja' of 'nee'.")
            VraagPartner(jaarInkomenNummer)

    def VraagStudieSchuldPartner(jaarInkomenNummer, jaarInkomenPartner):
        BoolStudieSchuld = input("Heeft een van jullie studieSchuld? (ja/nee) :  ").strip().lower()
        if BoolStudieSchuld == "ja":
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, True)
        elif BoolStudieSchuld == "nee":
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, False)
        else:
            print("Antwoord met 'ja' of 'nee'.")
            VraagStudieSchuldPartner(jaarInkomenNummer, jaarInkomenPartner)

    def VraagStudieSchuld(jaarInkomenNummer, jaarInkomenPartner):
        BoolStudieSchuld = input("Heb je studieSchuld? (ja/nee) :  ")
        if BoolStudieSchuld == "ja":
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, True)
        elif BoolStudieSchuld == "nee":
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, False)
        else:
            print("Antwoord met 'ja' of 'nee'.")
            VraagStudieSchuld()

    def VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, studieSchuld):
        termijnen = input("In hoeveel termijnen wil je betalen, keuzes: 1, 5, 10, 20, 30 : ")
        try:
            termijnen = int(termijnen)
        except ValueError:
            print("Ongeldige keuze voor termijnen. Kies uit: 1, 5, 10, 20, 30.")
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, studieSchuld)
            return

        if termijnen in [1, 5, 10, 20, 30]:
            MaxHypotheek(jaarInkomenNummer, jaarInkomenPartner, studieSchuld, termijnen)
        else:
            print("Ongeldige keuze voor termijnen. Kies uit: 1, 5, 10, 20 of 30.")
            VraagTermijnen(jaarInkomenNummer, jaarInkomenPartner, studieSchuld)

    def MaxHypotheek(jaarInkomenNummer, jaarInkomenPartner, studieSchuld, termijnen):

        totaalInkomen = calcTotaalInkomen(jaarInkomenNummer, jaarInkomenPartner )

        hypotheek = calcMaxcHypotheek(totaalInkomen, studieSchuld)

        maxHypotheek = calcMaxHypotheekMetTermijnen(termijnen,hypotheek )

        print("Je maximale hypotheek is ", maxHypotheek )




    VraagPostcode()
if __name__ == "__main__":
    MaxHypotheekPartner()

       