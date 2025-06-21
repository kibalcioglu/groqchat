import subprocess

JAR_PATH = "zemberek-full.jar"
MAIN_CLASS = "zemberek.apps.morphology.MorphologyConsole"

def analyze_with_zemberek(word):
    print(f"Zemberek testi: '{word}'")
    try:
        result = subprocess.run(
            [
                "java",
                "-Dfile.encoding=UTF-8",
                "-cp",
                JAR_PATH,
                MAIN_CLASS,
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            input=f"{word}\nquit\n",
        )
        print(result.stdout.strip())
    except Exception as e:
        print("🚨 Çalıştırma hatası:", e)

if __name__ == "__main__":
    analyze_with_zemberek("geliyormuşsunuz")
