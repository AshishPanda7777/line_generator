def main():
    # Story template with placeholders
    story_template = (
        "Today I went to the {place}. I was really {adjective1} because I was going to meet {person}. "
        "When I arrived, I saw a {adjective2} {animal} jumping around. "
        "Then, {person} arrived and we decided to {verb} together. It was a {adjective3} day!"
    )

    # Prompt the user for inputs
    place = input("Enter a place: ")
    adjective1 = input("Enter an adjective: ")
    person = input("Enter a person's name: ")
    adjective2 = input("Enter another adjective: ")
    animal = input("Enter an animal: ")
    verb = input("Enter a verb: ")
    adjective3 = input("Enter one more adjective: ")

    # Insert user inputs into the story template
    story = story_template.format(
        place=place,
        adjective1=adjective1,
        person=person,
        adjective2=adjective2,
        animal=animal,
        verb=verb,
        adjective3=adjective3
    )

    # Print the final story
    print("\nHere is your story:\n")
    print(story)

if __name__ == "__main__":
    main()
