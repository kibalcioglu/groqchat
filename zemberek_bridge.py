import os
import subprocess
import argparse
import sys

JAR_PATH = os.path.join(os.path.dirname(__file__), "zemberek-full.jar")
MAIN_CLASS = "zemberek.apps.morphology.MorphologyConsole"
DEFAULT_WORD = "geliyormuşsunuz"

def analyze_with_zemberek(word):
    print(f"Zemberek testi: '{word}'")
    if not os.path.exists(JAR_PATH):
        print(f"🚨 Zemberek jar not found: {JAR_PATH}")
        sys.exit(1)
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
    parser = argparse.ArgumentParser(
        description="Run morphological analysis using Zemberek"
    )
    parser.add_argument(
        "--word",
        "-w",
        default=DEFAULT_WORD,
        help="Word to analyze",
    )
    args = parser.parse_args()

    analyze_with_zemberek(args.word)
