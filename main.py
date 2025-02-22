def count_sheep(n):
    i=1
    text=''
    while i <=n :
        text+=f'{i} sheep...'
        i+=1
    return text
print(count_sheep(1000))