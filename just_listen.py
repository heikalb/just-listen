from textblob import TextBlob

# Messages to choose from
welcome_msg = "Ahoy! I'm here to listen. What's on your mind? (enter 'q' to quit)"
exit_msg = "I am glad to have talked to you. I bid you farewell."

# Cutoff point between different sentiment categories
cp = 0.4

reponses = {
    lambda s: s[0] <= -cp and s[1] <= cp: "That doesn't sound good",
    lambda s: s[0] <= -cp and s[1] > cp: "It sounds that that is upsetting you :(",
    lambda s: -cp < s[0] < cp and s[1] <= cp: "I see",
    lambda s: -cp < s[0] < cp and s[1] > cp: "I hear you",
    lambda s: s[0] >= cp and s[1] <= cp: "That sounds good",
    lambda s: s[0] >= cp and s[1] > cp: "I'm happy to hear that :)",
    lambda s: True: "I'm not sure what to say, but go on"
}


def get_response(user_input):
    """
    Choose a response based on user input.
    :param user_input: string of user input
    :return: response string
    """
    if '?' in user_input:
        return "I'm not sure what to say, but go on"

    for r in reponses:
        sentiment = TextBlob(user_input).sentiment

        if r(sentiment):
            return reponses[r]


def main():
    """
    Get user input and output response.
    """
    # Welcome message
    print(welcome_msg)

    # Get user input
    user_input = input('>>> ')

    # Repeat until user wants to quit
    while user_input != 'q':
        response = get_response(user_input)
        print(response)
        user_input = input('>>>\t')

    # Say goodbye
    print(exit_msg)


if __name__ == '__main__':
    main()
    exit(0)
