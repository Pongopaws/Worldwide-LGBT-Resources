import os 
import sys 
import time 

def replace_title(original_header: str, file_name: str) -> str:
    return original_header.replace(
        "Worldwide LGBT Resources", 
        " ".join(
            e.capitalize() for e in file_name[:-5].split("_")
        )
    )

def no_sidebar(original_header: str) -> str: 
    return original_header.replace(
        "margin-left: 25%; /* sidebar */", ""
    ).replace(
        "width: 80%; /* sidebar */", "width: 100%;"
    ).replace(
        "margin-left: 20%; /* sidebar */", ""
    )
        

def main():
    home = os.getcwd()
    footer = ""
    header = ""
    sidebar = ""
    with open(f"{home}{os.sep}templates{os.sep}footer.html", encoding="utf8") as foot:
        footer = foot.read()
    with open(f"{home}{os.sep}templates{os.sep}header.html", encoding="utf8") as head:
        header = head.read()
    with open(f"{home}{os.sep}templates{os.sep}sidebar.html", encoding="utf8") as side:
        sidebar = side.read()
    for elem in os.listdir(f"{home}{os.sep}pages"):
        new_header = (
            no_sidebar(header) if elem == "index.html" else replace_title(header, elem)
        )
        content = ""
        with open(f"{home}{os.sep}pages{os.sep}{elem}", encoding="utf8") as con:
            content = con.read()
        final_content = (
            new_header + content + footer if elem == "index.html" else new_header + sidebar + content + footer 
        )
        with open(f"{home}{os.sep}{elem}", "w+", encoding="utf8") as f:
            f.write(final_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "watch":
            while True:
                main()
                time.sleep(1)
        else:
            print("unknonw arg: {arg}")
    else:
        main()
