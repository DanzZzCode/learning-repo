def main():
    x = input("File name: ").strip().lower()
    x = x.split(".")[-1]
    checkt(x)

def checkt(ftype):
    match ftype:
        case "gif":
            print("image/gif")
        case "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()