import re


parts = {"head": r"(?<=<head>)((.|\n)*)(?=<\/head>)", "body": r"(?<=<body>)((.|\n)*)(?=<\/body>)"}

for name, regex in parts.items():
    with open(f"dist/{name}.html", "w", encoding="utf-8") as fout:
        with open("dist/index.html", "r", encoding="utf-8") as fin:
            string = fin.read()
            substring = re.search(regex, string).group(0)
            fout.write(substring)
