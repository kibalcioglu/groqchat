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
            input=f"{word}\nquit\n",
        )

        try:
            output = result.stdout.decode("utf-8").strip()
        except UnicodeDecodeError:
            output = result.stdout.decode("latin5", errors="replace").strip()

        print(output)
    except Exception as e:
        print("🚨 Çalıştırma hatası:", e)

if __name__ == "__main__":
    analyze_with_zemberek("geliyormuşsunuz")
