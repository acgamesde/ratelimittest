import os
import time
import subprocess
from datetime import datetime

# ➤ Hier deinen lokalen Pfad zum geklonten Repo eintragen
REPO_PATH = "C:/Users/F1410/Desktop/test/ratelimittest"  # <- ANPASSEN

# Git-Konfig
GIT_USERNAME = "acgamesde"
GIT_EMAIL = "f141007@t-online.de"

def run_git_command(command, cwd):
    result = subprocess.run(command, cwd=cwd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print("Fehler:", result.stderr)
    return result.stdout

def main():
    run_git_command(f'git config user.name "{GIT_USERNAME}"', REPO_PATH)
    run_git_command(f'git config user.email "{GIT_EMAIL}"', REPO_PATH)

    while True:
        # Vorherige .txt-Dateien löschen
        for file in os.listdir(REPO_PATH):
            if file.endswith(".txt"):
                os.remove(os.path.join(REPO_PATH, file))

        # Neue Datei anlegen
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
        filepath = os.path.join(REPO_PATH, filename)

        with open(filepath, "w") as f:
            f.write("")

        # Git-Aktionen
        run_git_command("git add .", REPO_PATH)
        run_git_command(f'git commit -m "Update: {filename}"', REPO_PATH)
        run_git_command("git push", REPO_PATH)

        print(f"Gepusht: {filename}")
        time.sleep(1)

if __name__ == "__main__":
    main()
