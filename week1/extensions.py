def main():
    filename = input("File name: ")
    print(extensionCheck(filename))


def extensionCheck(filename):
    extension = filename.lower().strip().split('.')[-1] #-1 means the last element of the list, which is the extension of the file

    match  extension:
        case "gif":
            return 'image/gif'
        case "jpg" | "jpeg":
            return 'image/jpeg'
        case "png":
            return 'image/png'
        case "pdf":
            return 'application/pdf'
        case "txt":
            return 'text/plain'
        case "zip":
            return 'application/zip'
        case _:
            return 'application/octet-stream'


main()
