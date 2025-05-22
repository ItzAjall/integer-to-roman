def Inttoroman(num: int):
    roman = ""
    num = str(num)
    nums: list[str] = []
    symbol = {
        '1' : 'I',
        '5' : 'V',
        '10' : 'X',
        '50' : 'L',
        '100' : 'C',
        '500' : 'D',
        '1000' : "M"
    }
    j = len(num) -1
    for i in range(len(num)):
        nums.append(num[i] + j * "0")
        j -= 1
    for i in range(len(nums)):
        if nums[i] in symbol.keys():
            roman += symbol[nums[i]]
        else:
            if len(nums[i]) == 1 :
                if (5 - int(nums[i])) == 1:
                    roman += "IV"
                elif (10 - int(nums[i])) == 1:
                    roman += "IX"
                else:
                    if int(nums[i]) > 5:
                        nums[i] = str(int(nums[i]) - 5)
                        roman += symbol['5']
                        a = int(nums[i]) // 1
                    for _ in range(a):
                        roman += symbol['1']
            elif len(nums[i]) == 2 :
                if (50 - int(nums[i])) == 10:
                    roman += "XL"
                elif (100 - int(nums[i])) == 10:
                    roman += "XC"
                else:
                    if int(nums[i]) > 50:
                        nums[i] = str(int(nums[i]) - 50)
                        roman += symbol['50']
                    a = int(nums[i]) // 10
                    for _ in range(a):
                        roman += symbol['10']
            elif len(nums[i]) == 3:
                if (500 - int(nums[i])) == 100:
                    roman += "CD"
                elif (1000 - int(nums[i])) == 100:
                    roman += "CM"
                else:
                    if int(nums[i]) > 500:
                        nums[i] = str(int(nums[i]) - 500)
                        roman += symbol['500']
                    a = int(nums[i]) // 100
                    for _ in range(a):
                        roman += symbol['100']
            elif len(nums[i]) == 4:
                a = int(nums[i]) // 1000
                for _ in range(a):
                    roman += symbol['1000']
    return roman
