import os 

def main():
    home = os.getcwd()
    footer = ""
    header = ""
    with open(f"{home}{os.sep}templates{os.sep}footer.html") as foot:
        footer = foot.read()
    with open(f"{home}{os.sep}templates{os.sep}header.html") as head:
        header = head.read()
    for elem in os.listdir(f"{home}{os.sep}pages"):
        content = ""
        with open(f"{home}{os.sep}pages{os.sep}{elem}") as con:
            content = con.read()
        with open(f"{home}{os.sep}{elem}", "w+") as f:
            f.write(header + content + footer)

if __name__ == "__main__":
    main()
