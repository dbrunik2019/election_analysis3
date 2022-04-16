print("hello world")
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)
    
for i in range(len(counties)):
    print(counties[i])




candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")









temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#what is the score?
score=int(input("What is your test score?"))
#determine the grade.
if score>=90:
    print('your grade is an A.')
else:
    if score>=80:
        print('your grade is a B.')
    else:
        if score >=70:
            print('your grade is a C.')
        else:
            if score>=60:
                print('your grade is a D.')
            else:
                print('your grade is an F.')


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')
