def solution(n, words):
    answer = []
    turn = 1
    last_word = words[0][-1]
    pool = {words[0]}
    person = 2
    for word in words[1:]:
        if word in pool or last_word!=word[0]:
            answer = [person,turn]
            break
        else:
            last_word = word[-1]
            pool.add(word)
            if person >= n:
                turn+=1
                person = 1
            else:
                person += 1
    else:
        answer = [0,0]
                
            

    return answer