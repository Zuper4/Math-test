import random

a1 = random.randint(1, 11)
b1 = random.randint(1, 11)
c1 = random.randint(1, 11)

a2 = random.randint(10, 21)
b2 = random.randint(10, 21)
c2 = random.randint(10, 21)

a3 = random.randint(10, 41)
b3 = random.randint(10, 41)
c3 = random.randint(10, 41)

a4 = random.randint(1, 21)
b4 = random.randint(1, 21)
c4 = random.randint(1, 21)

a5 = random.randint(10, 21)
b5 = random.randint(10, 21)
c5 = random.randint(1, 101)

a6 = random.randint(20, 31)
b6 = random.randint(20, 31)
c6 = random.randint(1, 2)

a7 = random.randint(100, 501)
b7 = random.randint(100, 501)
c7 = random.randint(100, 501)

a8 = random.randint(10, 21)
b8 = random.randint(10, 21)
c8 = random.randint(10, 21)

a9 = random.randint(1, 8)
b9 = random.randint(1, 3)
c9 = random.randint(100, 201)

a10 = random.randint(50, 101)
b10 = random.randint(50, 101)
c10 = random.randint(500, 1001)

score = 0

def good():
    print("Well done! Next question:")

def bad():
    print("Missed !!!! Noob")

def sc_final():
    print("Your score is " + str(score) + ".")

print("This test contains 10 questions. A correct answer earns you 1 point. ") 
print("If your answer is false, your test ends. ")
print("For each question, you must answer with an integer, otherwise, you will have to start all over !!")
Reponse = input("Did you understand and are you ready? (Answer yes or no)")

if Reponse == str("yes"):
    Q1 = int(input("Question 1: " + str(a1) + "+" + str(b1) + "+" + str(c1) + "=: "))

    if Q1 == a1+b1+c1:
        good()
        score += 1
        Q2 = int(input("Question 2: " + str(a2) + "+" + str(b2) + "+" + str(c2) + "=: "))

        if Q2 == a2+b2+c2:
            good()
            score += 1
            Q3 = int(input("Question 3: " + str(a3) + "+" + str(b3) + "+" + str(c3) + "=: "))

            if Q3 == a3+b3+c3:
                good()
                score += 1
                Q4 = int(input("Question 4: " + str(a4) + "x" + str(b4) + "x" + str(c4) + "=: "))

                if Q4 == a4*b4*c4:
                    good()
                    score += 1
                    Q5 = int(input("Question 5: " + str(a5) + "x" + str(b5) + "+" + str(c5) + "=: "))

                    if Q5 == a5*b5+c5:
                        good()
                        score += 1
                        Q6 = int(input("Question 6: " + str(a6) + "x" + str(b6) + "x" + str(c6) + "=: "))

                        if Q6 == a6*b6*c6:
                            good()
                            score += 1
                            Q7 = int(input("Question 7: " + str(a7) + "+" + str(b7) + "+" + str(c7) + "=: "))

                            if Q7 == a7+b7+c7:
                                good()
                                score += 1
                                Q8 = int(input("Question 8: " + str(a8) + "x" + str(b8) + "x" + str(c8) + "=: "))

                                if Q8 == a8*b8*c8:
                                    good()
                                    score += 1
                                    Q9 = int(input("Question 9: " + str(a9) + "^" + str(b9) + "+" + str(c9) + "=: "))

                                    if Q9 == a9**b9+c9:
                                        good()
                                        score += 1
                                        Q10 = int(input("Question 10: " + str(a10) + "x" + str(b10) + "-" + str(c10) + "=: "))

                                        if Q10 == a10*b10-c10:
                                            score += 1
                                            print("CONGRATULATIONS !! You have passed the test ")
                                            sc_final()
                                        else:
                                            bad()
                                            sc_final()
                                    else:
                                        bad()
                                        sc_final()
                                else:
                                    bad()
                                    sc_final()
                            else:
                                bad()
                                sc_final()              
                        else:
                            bad()
                            sc_final()                  
                    else:
                        bad()
                        sc_final()
                else:
                    bad()
                    sc_final()
            else:
                bad()
                sc_final()            
        else:
            bad()
            sc_final()
    else:
        bad()
        sc_final()
        
else:
    print("Read again carefully ")

Fin = input("Did you like the test? (Answer yes or no) ")

if Fin == str("yes"):
    print("Thanks !!") 

elif  Fin == str("no"):  
    print("UNGREATFULL !!! IT TOOK ME MORE THAN AN HOUR TO DO ALL OF THIS, AND YOU JUST BECAUSE YOU ARE A NOOB, YOU CRITICIZE !!! ")

else:
    print("Sorry, I don't know what you meant here")
