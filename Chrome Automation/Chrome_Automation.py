
import webbrowser as wb
import subprocess

def webauto():
    googlechrome_path = "C:/Program Files/Google/Chrome/Application/Chrome.exe %s" ##  PLEASE CHANGE, YOUR CHROME PATH
    subprocess.Popen(googlechrome_path)
    URLS= (
        "github.com/cesasiesec",
        "gmail.com",
        "youtube.com",
        "udemy.com",
        "twitter.com"
        )
    for url in URLS:
        print("opening : "+url)
        wb.get(googlechrome_path).open(url)

webauto()