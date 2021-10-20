def common_data(list1, list2):
    result = False
  
    # traverse in the 1st list
    for x in list1:
  
        # traverse in the 2nd list
        for y in list2:
    
            # if one common
            if x == y:
                result = True
                return result 
                  
    return result


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [5, 6, 7, 8, 9]
    print(common_data(a, b))
    
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9]
    print(common_data(a, b))

    strlist1 = ['dog', 'cat']
    strlist2 = ['cat', 'monkey']
    print(common_data(strlist1, strlist2))


