def contacts(queries):
    #
    # Write your code here.
    #

    contact = {}
    result = []

    for val in queries:
        q = val.split()
        if q[0] == "add":
            if q[1] in contact:
                contact[q[1]] += 1
            else:
                contact[q[1]] = 1
        elif q[0] == "find":
            temp = 0
            for sub_val in contact.keys():
                if sub_val.find(q[1]) > -1:
                    temp += 1
                elif q[1].find(sub_val) > -1:
                    temp += 1
            result.append(temp)
        else:
            result.append(0)

    return result


if __name__ == "__main__":
    print contacts(["add hack",
                    "add hackerrank",
                    "find hac",
                    "find hak"])
