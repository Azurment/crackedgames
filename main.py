from customtkinter import *
import webbrowser

class CreateRadioButton(CTkRadioButton):
    def __init__(self, parent, text, variable, value, link, **kwargs):
        super().__init__(parent, text=text, variable=variable, value=value, **kwargs)
        self.link = link

def open_website():
    selected_value = scrollable_frame.variable.get()
    for widget in scrollable_frame.winfo_children():
        if isinstance(widget, CreateRadioButton) and widget.cget("value") == selected_value:
            webbrowser.open(widget.link)
            break

games = {
    "Geometry Dash": "https://tpi.li/freegeometry",
    "GTA I": "https://tpi.li/gtaI",
    "GTA II": "https://tpi.li/gtaII",
    "GTA III": "https://tpi.li/gtaIII",
    "GTA IV": "https://tpi.li/gtaIV",
    "GTA V": "https://tpi.li/gtaVfree",
    "GTA San Andreas": "https://tpi.li/gtasanandreasfree",
    "GTA The Trilogy (Definitive Edition)": "https://tpi.li/gtatrilogy",
    "GTA Vice City": "https://tpi.li/gtavice",
    "Project IGI": "https://tpi.li/igi1",
    "Project IGI 2": "https://tpi.li/igi2free",
    "Need For Speed Carbon": "https://tpi.li/nfscarbon",
    "Need For Speed Heat": "https://tpi.li/nfsheat",
    "Need For Speed Hot Persuit": "https://tpi.li/nfspersuit",
    "Need For Speed Hot Persuit II": "https://tpi.li/nfspersuit2",
    "Need For Speed II": "https://tpi.li/nfs2",
    "Minecraft": "https://tpi.li/freeminecraftsk",
    "Need For Speed Most Wanted 2012": "https://tpi.li/nfsmw2012free",
    "Need For Speed Most Wanted 2005": "https://tpi.li/nfsmw2005",
    "Need For Speed Payback": "https://tpi.li/nfspayback",
    "Need For Speed Porsche Unleased": "https://tpi.li/nfsporscheunleashed",
    "Need For Speed ProStreet": "https://tpi.li/nfsprostreet",
    "Need For Speed Rivals": "https://tpi.li/nfsrivals",
    "Need For Speed Shift": "https://tpi.li/nfsshift",
    "Need For Speed The Run": "https://tpi.li/nfsrun",
    "Need For Speed Undercover": "https://tpi.li/nfsundercover",
    "Need For Speed Under Ground": "https://tpi.li/nfsunderground",
    "Need For Speed Under Ground II": "https://tpi.li/nfsunderground2",
    "Terraria": "https://tpi.li/terraria"
}

app = CTk()
app.geometry("800x600")
app.title("Free Games")
app.resizable(False, False)
app.iconbitmap("icon.ico")

bg = CTkFrame(app, fg_color="#1e2229")
bg.pack(fill="both", expand=True)

CTkLabel(bg, text="Free Games", font=("Times New Roman", 32, "bold"), text_color="#dce1ec").pack(pady=10)

scrollable_frame = CTkScrollableFrame(bg, width=600, height=400)
scrollable_frame.variable = IntVar()
scrollable_frame.pack(pady=10)

# Sorting the games alphabetically (case-insensitive)
for i, (name, link) in enumerate(sorted(games.items(), key=lambda x: x[0].lower())):
    CreateRadioButton(scrollable_frame, text=name, font=("Comic Sans MS", 20, "bold"),
                      variable=scrollable_frame.variable, value=i + 1, link=link, fg_color="#c3ccdf", text_color="#8a95aa").pack(anchor=W)

CTkButton(bg, text="Download", font=("Arial", 20, "bold"), command=open_website).pack(pady=10)

app.mainloop()
