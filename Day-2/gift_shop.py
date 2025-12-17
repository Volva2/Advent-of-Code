class InvalidInput:
    def __init__(self, input):
        self.ranges = [range(int(i.split("-")[0]), int(i.split("-")[1])) for i in input.split(",")]
        self.range = input.split(",")
        self.invalid_id_count: int = 0

    # Part One
    def invalid_sum(self):
        for range in self.ranges:
            for r in range:
                r = str(r)
                if(len(r)%2 == 0 and len(r) > 1):
                    r_mid: int = len(r)//2
                    try:
                        if r[r_mid:] == r[:r_mid]:
                            self.invalid_id_count+=int(r)
                    except ValueError:
                        print(r)
        return self.invalid_id_count
    
    # Part Two
    def invalid_sum_2(self):
        counter: int = 0
        for item in self.range:
            start, end = item.split("-")
            for num in range(int(start), int(end)):
                string = str(num)
                for sublen in range(1, len(string) // 2 + 1):
                    if len(string) % sublen != 0:
                        continue
                    match = True
                    for i in range(len(string)):
                        if string[i] != string[i % sublen]:
                            match = False
                    if match:
                        counter += num
                        break
        return counter


# input="503950-597501,73731-100184,79705998-79873916,2927-3723,35155-50130,52-82,1139-1671,4338572-4506716,1991-2782,1314489-1387708,8810810-8984381,762581-829383,214957-358445,9947038-10058264,4848455367-4848568745,615004-637022,5827946-5911222,840544-1026063,19-46,372804-419902,486-681,815-1117,3928-5400,28219352-28336512,6200009-6404247,174-261,151131150-151188124,19323-26217,429923-458519,5151467682-5151580012,9354640427-9354772901,262-475,100251-151187,5407-9794,8484808500-8484902312,86-129,2-18"
# invalid = InvalidInput(input)
# print(invalid.invalid_sum(), "\n\n")

# input2="503950-597501,73731-100184,79705998-79873916,2927-3723,35155-50130,52-82,1139-1671,4338572-4506716,1991-2782,1314489-1387708,8810810-8984381,762581-829383,214957-358445,9947038-10058264,4848455367-4848568745,615004-637022,5827946-5911222,840544-1026063,19-46,372804-419902,486-681,815-1117,3928-5400,28219352-28336512,6200009-6404247,174-261,151131150-151188124,19323-26217,429923-458519,5151467682-5151580012,9354640427-9354772901,262-475,100251-151187,5407-9794,8484808500-8484902312,86-129,2-18"
# invalid2 = InvalidInput(input2)
# print(invalid2.invalid_sum_2())