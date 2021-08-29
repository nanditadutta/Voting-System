nominee_1 =input("enter the Nominee_1 Name: ")
nominee_2 =input("enter the Nominee_2 Name: ")

nominee_1_votes = 0
nominee_2_votes = 0
print("The voter_id number should be entered only between 1 to 10")

votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voters = len(votes_id)
while True:
    if votes_id== []:
        print("OOPS!!!,Voting session over")
        if(nominee_1_votes>nominee_2_votes):
            percent = (nominee_1_votes/num_of_voters)*100
            print(nominee_1,"has won", "with", percent, "%  votes")
            break
        elif(nominee_2_votes>nominee_1_votes):
            percent = (nominee_2_votes/num_of_voters)*100
            print(nominee_2,"has won", "with", percent, "%  votes")
            break    
    else: 
        voter =int(input("Enter your Voter ID Number: "))
        if voter in votes_id:
            print("You are a Voter ")
            votes_id.remove(voter)
            print("If you wanna vote for nominee_1 then enter 1 or else if you wanna vote for nominee_2 then enter 2")
            vote = int(input ("Enter your vote 1 or 2: "))
            if vote ==1:
                nominee_1_votes+=1
                print("Thanks for casting your Vote")
            elif vote ==2:
                nominee_2_votes+=1    
                print("Thanks for casting your Vote")
            else:
                print("You are not a voter or else you have already voted ")   


                # The above code is contributed by Nandita Dutta..... 