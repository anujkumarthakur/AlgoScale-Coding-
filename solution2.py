''' Q2.RACE DIFFERENCE PROBLEM:
            Many people have participated in Algoscale&#39;s marathon. Everyone in the event has
            successfully completed the marathon except for ONE participant.
            Write a method with a signature findIncomplete(participant, completion) that returns the
            name of the participant who was in the participant array but is not in the completion
            array.
'''

def findIncomplete(participant, completion):
    for i in range(0, len(participant)):
        for j in range(0, len(completion)):
            if(participant[i] == completion[j]):
                i = i+1
        print(participant[i])
if __name__ == "__main__":
    participant = ['leo', 'kiki', 'eden']
    completion = ['leo', 'eden']
    findIncomplete(participant, completion) 
