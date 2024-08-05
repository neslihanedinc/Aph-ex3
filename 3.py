def palindrom_is(n):
    n =n.replace(" ","").lower()
    #n.replace(" ", ""): String'deki tüm boşlukları kaldırır.
    #.lower(): String'i küçük harflere çevirir. 
    return n == n[::-1]
    #s string'ini ters çevirir. Örneğin, "abcd" string'i "dcba" olur.
    #return ise Ters çevrilmiş haliyle orijinal hali aynı mı diye kontrol eder.
    #Aynıysa True, değilse False döner.

    #0 la 3 ve 1 le 2 yi değiştirerek dene while ile

while True:
    try:
        user_input=input("enter a word(or type 'exit' to quit ): ")
        if user_input.lower()== 'exit':
            print("good bye")
            break
        if palindrom_is(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")
    except exception as e:
    # input() fonksiyonu genellikle ValueError atmaz 
    # bu nedenle Exception yakalayıcı daha uygun  
    # Ancak, burada ValueError'ı yakalamasına gerek yok, 
    # çünkü input() kullanıcıdan bir string döndürür ve bu string işlemleri hataya neden olmaz.
        print(f"an error occured:{e}")





