def solution(N):
  
   res = [int(x) for x in str(N)] 
   result_perms = [[]]
   
   for n in res:
       new_perms = []
       for perm in result_perms:
         for i in range(len(perm)+1):
           new_perms.append(perm[:i] + [n] + perm[i:])
           result_perms = new_perms
   return result_perms
