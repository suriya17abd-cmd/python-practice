quetion=[
    {"quetion":"india how many world cup winners in odl?",
    "option":["A.5","B.9","C.0","D.2"],
    "answer":"D"},
    {"quetion":"2027 world cup will be held in which country?",
    "option":["A.India","B.Australia","C.South Africa","D.England"],
    "answer":"C"},  
    {"quetion":"who is the highest hundred in odi?",
    "option":["A.Sachin Tendulkar","B.Ricky Ponting","C.Virat Kohli","D.Brian Lara"],
    "answer":"C"},
    {"quetion":"who is the fast hundred in odi?",
    "option":["A.Muttiah Muralitharan","B.AB de Villiers","C.Mahendra Singh Dhoni","D.Wasim Akram"],
    "answer":"B"},
    {"quetion":"who is the best cricketer in india you choice?",
    "option":["A.Sachin Tendulkar","B.Virat Kohli","C.Mahendra Singh Dhoni","D.All option"],
    "answer":"D"}
]
score=0
print("welcome to the cricket quiz game")
print(30*"-")
for q in quetion:
    print("\n"+q["quetion"])
    for option in q["option"]:
        print(option)
    while True:
        answer=input("enter the answer :").strip().upper()
        if answer in["A","B","C","D"]:
            break
        else:
            print("invalid choice!plase enter a,b,c,d")
        if answer ==q["answer"]:
            print("correct🎉")
            score+=1
        else:
            print("this wrong answer😔")
            print("the correct answer is :",q["answer"])

print("\nQuiz completed")
print("your score is :",score,"/",len(quetion))
if score<=5:
    print("super bro🎉")
else:
    print("sorry bro try again")

print("thank you for answering")
input("press Enter to exit....")
