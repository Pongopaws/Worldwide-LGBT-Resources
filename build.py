import os 

def main():
    home = os.getcwd()
    footer = ""
    header = ""
    with open(f"{home}{os.sep}templates{os.sep}footer.html", encoding="utf8") as foot:
        footer = foot.read()
    with open(f"{home}{os.sep}templates{os.sep}header.html", encoding="utf8") as head:
        header = head.read()
    for elem in os.listdir(f"{home}{os.sep}pages"):
        content = ""
        with open(f"{home}{os.sep}pages{os.sep}{elem}", encoding="utf8") as con:
            content = con.read()
        with open(f"{home}{os.sep}{elem}", "w+", encoding="utf8") as f:
            f.write(header + content + footer)

if __name__ == "__main__":
    main()
