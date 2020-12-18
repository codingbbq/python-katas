class Solution2015:
    def processInstructions(self, instructions, mapOfKnownInputs):
        for indice, i in enumerate(instructions):
            # Flag to use in the list when the instuction is successfully executed
            remove = False

            # Split the string to get input and output
            ii = str(i).split("->")
            input = ii[0].strip()
            output = ii[1].strip()

            # For puzzle 2
            if "b" in mapOfKnownInputs:
                mapOfKnownInputs['b'] = 956
            
            #If the input is just a number
            if input.isdigit():
                mapOfKnownInputs[output] = input
                remove = True # Flag to Remove this instruction from the list
            else:
                # Break the input based on various conditions
                x = self.inputbreakup(input)
                if x["wire1"] in mapOfKnownInputs and x["wire2"] in mapOfKnownInputs:

                    if x["operation"] == "&":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire1"]]) & int(mapOfKnownInputs[x["wire2"]])
                        remove = True

                    if x["operation"] == "|":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire1"]]) | int(mapOfKnownInputs[x["wire2"]])
                        remove = True

                if x["wire1"] != None and x["wire1"].isdigit() and x["wire2"] in mapOfKnownInputs:

                    if x["operation"] == "&":
                        mapOfKnownInputs[output] = int(x["wire1"]) & int(mapOfKnownInputs[x["wire2"]])
                        remove = True

                    if x["operation"] == "|":
                        mapOfKnownInputs[output] = int(x["wire1"]) | int(mapOfKnownInputs[x["wire2"]])
                        remove = True

                if x["wire2"] != None and x["wire2"].isdigit() and x["wire1"] in mapOfKnownInputs:

                    if x["operation"] == "&":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire2"]]) & int(x["wire2"])
                        remove = True

                    if x["operation"] == "|":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire2"]]) | int(x["wire2"])
                        remove = True

                if x["wire1"] in mapOfKnownInputs:
                    
                    if x["operation"] == "assign":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire1"]])
                        remove = True

                    if x["operation"] == "!":
                        mapOfKnownInputs[output] = 65535 - int(mapOfKnownInputs[x["wire1"]])
                        remove = True

                    if x["operation"] == "LSHIFT":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire1"]]) << int(x["wire2"])
                        remove = True

                    if x["operation"] == "RSHIFT":
                        mapOfKnownInputs[output] = int(mapOfKnownInputs[x["wire1"]]) >> int(x["wire2"])
                        remove = True

            # To remove the instuction from the list, we assign 0 as the value
            if remove == True:
                instructions[indice] = 0

        # Create a new list from the existing list by discarding 0
        updatedInstructions = []
        updatedInstructions = [t for t in instructions if t != 0]
        
        # Perform this operation until the list has no instructions
        if(len(updatedInstructions) > 0):
            self.processInstructions(updatedInstructions, mapOfKnownInputs)

        # This dictionary contains all the wires and the value that it has
        return mapOfKnownInputs

    def inputbreakup(self, input):
        """
        We break the input string to check for AND, OR, NOT, LSHIFT and RSHIFT operations
        """
        s = input.split(' ')

        # for case lx -> a
        if len(s) == 1:
            return { "wire1": s[0], "operation": "assign", "wire2": None}

        if s[0].lower() == "not":
            return { "wire1" : s[1], "operation": "!", "wire2" : None }

        if s[1].lower() == "and":
            return { "wire1" : s[0], "operation": "&", "wire2" : s[2] }

        if s[1].lower() == "or":
            return { "wire1" : s[0], "operation": "|", "wire2" : s[2] }

        if s[1].lower() == "lshift":
            return { "wire1" : s[0], "operation": "LSHIFT", "wire2" : s[2] }

        if s[1].lower() == "rshift":
            return { "wire1" : s[0], "operation": "RSHIFT", "wire2" : s[2] }
        

with open("./advent_of_code/2015/input/day07.txt", "r") as file:
    inpt = [line.rstrip() for line in file.readlines()]

    mapOfKnownInputs = {}
    puzzle1 = Solution2015().processInstructions(inpt, mapOfKnownInputs)
    print(puzzle1['a'])
