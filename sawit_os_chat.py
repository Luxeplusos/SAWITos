import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("sawitOS")
root.geometry("1280x720")

# =====================
# BIOS
# =====================

bios = tk.Toplevel(root)
bios.title("sawitOS BIOS")
bios.geometry("800x500")
bios.configure(bg="navy")

tk.Label(
    bios,
    text="SAWITOS BIOS v1.0",
    bg="navy",
    fg="white",
    font=("Consolas", 22, "bold")
).pack(pady=20)

tk.Label(
    bios,
    text="""
CPU : Virtual x64
RAM : 4096 MB
Storage : 64 GB

F5 = Exit BIOS
""",
    bg="navy",
    fg="white",
    font=("Consolas", 14)
).pack()

bios.withdraw()

def open_bios(event=None):
    bios.deiconify()

def close_bios(event=None):
    bios.withdraw()

root.bind("<F2>", open_bios)
root.bind("<F5>", close_bios)

# =====================
# BOOT SCREEN
# =====================

boot = tk.Frame(root, bg="black")
boot.place(relwidth=1, relheight=1)

logo = tk.Label(
    boot,
    text="sawitOS",
    fg="white",
    bg="black",
    font=("Segoe UI", 28, "bold")
)
logo.pack(expand=True)

loading = tk.Label(
    boot,
    text="Starting system...",
    fg="white",
    bg="black",
    font=("Segoe UI", 12)
)
loading.pack(pady=20)

# =====================
# DESKTOP
# =====================

desktop = tk.Frame(root, bg="#d9d9d9")

def show_desktop():
    boot.destroy()
    desktop.place(relwidth=1, relheight=1)

    title = tk.Label(
        desktop,
        text="sawitOS Desktop",
        bg="#d9d9d9",
        font=("Segoe UI", 20, "bold")
    )
    title.place(x=20, y=20)

    # Explorer (biru)
    tk.Button(
        desktop,
        text="📁\nExplorer",
        bg="#4dabf7",
        width=12,
        height=4
    ).place(x=40, y=80)

    # Calculator (kuning)
    tk.Button(
        desktop,
        text="🧮\nCalculator",
        bg="#ffd43b",
        width=12,
        height=4,
        command=open_calculator
    ).place(x=180, y=80)

    # Notes (ungu)
    tk.Button(
        desktop,
        text="📝\nNotes",
        bg="#b197fc",
        width=12,
        height=4,
        command=open_notes
    ).place(x=320, y=80)

    # Game (merah)
    tk.Button(
        desktop,
        text="🎮\nPing Game",
        bg="#ff6b6b",
        width=12,
        height=4,
        command=open_game
    ).place(x=460, y=80)

    # Store (hijau)
    tk.Button(
        desktop,
        text="🛒\nSawit Store",
        bg="#51cf66",
        width=12,
        height=4,
        command=open_store
    ).place(x=600, y=80)

    taskbar = tk.Frame(desktop, bg="#202124", height=40)
    taskbar.pack(side="bottom", fill="x")

    tk.Button(
        taskbar,
        text="Shutdown",
        command=root.destroy
    ).pack(side="right", padx=10)

def boot_animation():
    messages = [
        "Initializing kernel...",
        "Loading drivers...",
        "Loading services...",
        "Starting desktop..."
    ]

    def step(i=0):
        if i < len(messages):
            loading.config(text=messages[i])
            root.after(1200, lambda: step(i+1))
        else:
            show_desktop()

    step()

# =====================
# CALCULATOR
# =====================

def open_calculator():
    win = tk.Toplevel(root)
    win.title("Calculator")

    e = tk.Entry(win, width=25)
    e.pack(padx=10, pady=10)

    def calc():
        try:
            result = eval(e.get())
            e.delete(0, tk.END)
            e.insert(0, str(result))
        except:
            messagebox.showerror("Error", "Input salah")

    tk.Button(win, text="Hitung", command=calc).pack()

# =====================
# NOTES
# =====================

def open_notes():
    win = tk.Toplevel(root)
    win.title("Notes")

    text = tk.Text(win, width=60, height=20)
    text.pack()

# =====================
# PING GAME
# =====================

def open_game():
    win = tk.Toplevel(root)
    win.title("Ping Game")

    score = [0]

    lbl = tk.Label(win, text="Score: 0", font=("Arial", 16))
    lbl.pack()

    def hit():
        score[0] += 1
        lbl.config(text=f"Score: {score[0]}")

    tk.Button(
        win,
        text="PING!",
        font=("Arial", 20),
        bg="yellow",
        command=hit
    ).pack(pady=20)

# =====================
# STORE
# =====================

def open_store():
    win = tk.Toplevel(root)
    win.title("Sawit Store")

    tk.Label(
        win,
        text="Sawit Store",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    apps = [
        "Paint",
        "Calendar",
        "Browser Lite",
        "Terminal"
    ]

    for app in apps:
        tk.Button(
            win,
            text=f"Install {app}",
            width=20
        ).pack(pady=2)

root.after(1000, boot_animation)

root.mainloop()
