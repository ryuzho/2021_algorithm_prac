#9953번 paula`s search
def shops_visited_count_func(current_index, findingIndex):

    shops_visited_count = 1
    min_index = -1
    max_index = 50

    while current_index != findingIndex:
        if current_index > findingIndex:
            max_index = current_index
            current_index = (min_index + current_index)//2
        else:
            min_index = current_index
            current_index = (max_index + current_index)//2
        
        shops_visited_count += 1

    return shops_visited_count

while True:
    current_index = 24
    findingShop = int(input())
    if findingShop == 0:
        break
    else:
        if findingShop % 2 == 0: #50에서 바로 시작
            findingIndex = (findingShop - 2 ) // 2
            result = shops_visited_count_func(current_index, findingIndex)
        elif findingShop % 2 == 1: #50 -> 49 에서 시작
            findingIndex = (findingShop - 1 ) // 2
            result = shops_visited_count_func(current_index, findingIndex) + 1
        print(result)

        
       






        

            
