import re
# boolean function from RE tavnit
# function: XXX@mail.huji.ac.il to [XXX,mail,huji.ac.il]
if __name__ == "__main__":
    paragraph = input("Enter paragraph you want to extract emails from: ")

    emails = re.findall(r'[a-zA-Z0-9._-]+@[\w.-]+\.com', paragraph)

    print(emails)
    print (len(emails))

    with open("C:/Users/t8747382/Desktop/Okyanus/Okyanus/Tests/tests.txt", 'r') as f:
        queries = f.readlines()[:-1]
        for q in queries:
            print(re.findall(r'[a-zA-Z0-9._-]+@[\w.-]+\.com', q))

