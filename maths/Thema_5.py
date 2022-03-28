import sympy as sp


S = [x,y,z,a] = sp. symbols ('x y z a') # λίστα με τα σύμβολα μας
#a=1 #-> EmptySet
#a=-2 #-> Άπειρες Λύσεις 
A=sp.Matrix([[a,1,1],[1,a,1],[1,1,a]]) # ορίζουμε την πρώτη μήτρα
print ("Matrix A:",A)
B=sp.Matrix([1,2-a,3*a+1]) # ορίζουμε την δεύτερη μήτρα
print ("Matrix B:",B)

X=sp.linsolve([A,B],[x,y,z]) # προσπαθούμε να βρούμε την τιμή των συντεταγμένων
# print ("Solution:",X)  # Solution: {(-1/(a - 1), -a/(a - 1), (3*a - 1)/(a - 1))} (εικόνα 1)

#Η λύση που μας έδωσε η μέθοδος linsolve ορίζεται όταν a!=1 (εικόνα 2)

# Παρόλα αυτά θέλουμε να διερευνήσουμε αν είναι η μοναδική απάντηση και να κάνουμε επαλήθευση
D = sp. factor (A.det()) # Ο υπολογισμός της Ορίζουσας
print("D:",D)
roots = sp. solve(D,a) # Υπολογισμός των Ριζών της Ορίζουσας
print(" Roots of D:",roots)

#Όπως βλέπουμε το -2 αποτελεί ρίζα της Ορίζουσας D της μήτρας A οπότε μας επιστρέφει άπειρες λύσεις (εικόνα 3)
#Αυτό συμβαίνει όπως θα δούμε παρακάτω γιατί το -2 είναι ρίζα και όλων των οριζουσών Dx,Dy,Dz (εικόνα 4)

C=A.copy() # αντιγράφουμε την πρώτη μήτρα
for i in range(0,len(B)):
    for j in range(0,len(B)):
        C[j,i]=B[j] 
        if i>0:
            C[j,i-1]=A[j,i-1]
    D=sp.factor(C.det())
    roots = sp. solve(D,a)         
    print("A"+str(S[i])+":",C,
        "D"+str(S[i])+":",D,"|roots:",roots)

print(" Case a =", a, " Solutions:", X)