import os
import subprocess
import argparse
import sys
import tempfile
from pathlib import Path
import shutil

JAR_PATH = os.path.join(os.path.dirname(__file__), "zemberek-full.jar")
MAIN_CLASS = "zemberek.apps.morphology.MorphologyConsole"
DEFAULT_WORD = "geliyormuşsunuz"

SPELL_CORRECT_JAVA = """
import zemberek.morphology.TurkishMorphology;
import zemberek.normalization.TurkishSpellChecker;

public class SpellCorrect {
    public static void main(String[] args) throws Exception {
        TurkishMorphology morphology = TurkishMorphology.createWithDefaults();
        TurkishSpellChecker sc = new TurkishSpellChecker(morphology);
        StringBuilder out = new StringBuilder();
        for (int i = 0; i < args.length; i++) {
            String tok = args[i];
            if (!sc.check(tok)) {
                java.util.List<String> sug = sc.suggestForWord(tok);
                if (!sug.isEmpty()) {
                    tok = sug.get(0);
                }
            }
            out.append(tok);
            if (i < args.length - 1) out.append(' ');
        }
        System.out.println(out.toString());
    }
}
"""

# Check once whether required Java tools are available
_java_missing = []
if not os.path.exists(JAR_PATH):
    _java_missing.append("zemberek-full.jar")
if shutil.which("java") is None:
    _java_missing.append("java")
if shutil.which("javac") is None:
    _java_missing.append("javac")

SPELL_AVAILABLE = not _java_missing
if _java_missing:
    print(
        f"\u26a0\ufe0f Spell correction disabled (missing {', '.join(_java_missing)})"
    )

def correct_text(text: str) -> str:
    """Return spell-corrected text using Zemberek if available."""
    if not SPELL_AVAILABLE:
        return text

    words = text.split()
    if not words:
        return text

    with tempfile.TemporaryDirectory() as tmpdir:
        java_file = Path(tmpdir) / "SpellCorrect.java"
        java_file.write_text(SPELL_CORRECT_JAVA, encoding="utf-8")

        compile_cmd = ["javac", "-cp", JAR_PATH, str(java_file)]
        try:
            subprocess.run(compile_cmd, capture_output=True, check=True)
        except FileNotFoundError:
            print("\u26a0\ufe0f Spell correction disabled (javac not found)")
            return text
        except subprocess.CalledProcessError as e:
            print("\u26a0\ufe0f Spell correction disabled")
            if e.stderr:
                print(e.stderr.decode("utf-8", errors="replace"))
            return text

        classpath = os.pathsep.join([str(tmpdir), JAR_PATH])
        run_cmd = [
            "java",
            "-cp",
            classpath,
            "SpellCorrect",
            *words,
        ]
        try:
            result = subprocess.run(run_cmd, capture_output=True, check=True)
            corrected = result.stdout.decode("utf-8").strip()
            return corrected if corrected else text
        except FileNotFoundError:
            print("\u26a0\ufe0f Spell correction disabled (java not found)")
            return text
        except subprocess.CalledProcessError as e:
            print("\u26a0\ufe0f Spell correction disabled")
            if e.stderr:
                print(e.stderr.decode("utf-8", errors="replace"))
            return text

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
