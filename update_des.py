def parse_node(node, text, script):
    index = 0
    #looping for each port
    for i in text:
        #if it is empty dont update description
        if i != "Empty":
            #writing commands to script
            script.write("edit ge-" + str(node) + "/0/" + str(index) + "\n")
            script.write("set description " + str(i) + "\n")
            script.write("up\n")
        #incrementing port number
        index = index + 1

def main():
    #opening file and creating text flow
    file = open("descriptions.txt","r")
    flow = file.readlines()

    #instantiating array
    text = []

    #loading text into the array
    for x in flow:
        #if there is an invisible character, delete it
        if "\n" in x:
            x = x[0:(len(x)-1)]
            text.append(x)
        #else just add the line to the array
        else: text.append(x)

    #setting file name and creating file
    script_name = text[0] + "_script.txt"
    script = open(script_name, "w+")

    #writing initial edit commands
    script.write("edit\n")
    script.write("edit interfaces\n")

    #node count lets us know how many times to loop
    node_count = (int)(len(text)/48)
    text.remove(text[0])

    #throw exception if format is incorrect
    if len(text)-(48*node_count) != node_count:
        raise Exception("There needs to be 48 entries per node!")

    #looping for each node
    for i in range(0,node_count):
        #passing first node only
        temp = text[1:49]
        parse_node(i,temp,script)

        #delete that node from the array after
        text = text[49:]

    #writing commit commands to the script
    script.write("commit check\n")
    script.write("commit and-quit")

#running main class here
if __name__ == "__main__":
    main()
