def parse_line(line):
    tmp = line.split("=")
    element = dict(value.strip().split(":") for value in tmp[1].split(", "))
    element["name"] = tmp[0].strip()
    return element

def main():
    try:
        with open("./periodic_table.txt") as file:
            for line in file:
                elements = parse_line(line)
                print(elements)
    except Exception as e:
        print(f"exception accurred: {e}")

    HTML = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Periodic Table</title>
            </head>
            <body>
                <table>
                    {body}
                <table>
            </body>
            </html>
        """
    CELL = """
            <td style="border: 1px solid black; padding:10px">
                <h4>{name}</h4>
                <ul>
                    <li>No {number}</li>
                    <li>{small}</li>
                    <li>{molar}</li>
                    <li>{electron} electron</li>
                </ul>
            </td>
        """
    body = ""
    pos = 0
    for element in elements:
        if element["position"] == 0:
            body = "<tr>"


if __name__ == "__main__":
    main()