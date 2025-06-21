import os
import subprocess

JAR_PATH = os.path.join(os.path.dirname(__file__), "zemberek-full.jar")
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
            input=f"{word}\nquit\n".encode("utf-8"),
        )

        try:
            output = result.stdout.decode("utf-8").strip()
        except UnicodeDecodeError:
            output = result.stdout.decode("latin5", errors="replace").strip()

        print(output)

        if result.stderr:
            try:
                error_output = result.stderr.decode("utf-8").strip()
            except UnicodeDecodeError:
                error_output = result.stderr.decode("latin5", errors="replace").strip()

            if error_output:
                print(error_output)
    except Exception as e:
        print("🚨 Çalıştırma hatası:", e)

if __name__ == "__main__":
    analyze_with_zemberek("geliyormuşsunuz")
