def solution(clothes):
    answer = 1
    clothe_dic = {}
    for c_nma,c_kind in clothes:
      if c_kind in clothe_dic:
        clothe_dic[c_kind] +=1
      else:
        clothe_dic[c_kind] = 1
    for c_kind in clothe_dic:
      answer = answer * (clothe_dic[c_kind] + 1)
    answer -= 1
    return answer
  
solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])