import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



faq_data = [
    {
        "question": "What is a yorker in cricket?",
        "answer": "A yorker is a delivery bowled so that it pitches at or near the batsman's feet, making it difficult to hit."
    },
    {
        "question": "What is an LBW in cricket?",
        "answer": "LBW stands for Leg Before Wicket. A batsman can be given out if the ball hits their leg before hitting the bat and would have gone on to hit the stumps."
    },
    {
        "question": "What is a bouncer in cricket?",
        "answer": "A bouncer is a short-pitched ball that rises quickly towards the batsman's chest or head."
    },
    {
        "question": "What is a maiden over?",
        "answer": "A maiden over is an over in which no runs are scored off the bat by the batting team."
    },
    {
        "question": "What is a hat-trick in cricket?",
        "answer": "A hat-trick happens when a bowler takes 3 wickets in 3 consecutive balls."
    },
    {
        "question": "What is powerplay in cricket?",
        "answer": "Powerplay is a period in limited-overs cricket where fielding restrictions apply, allowing only a limited number of fielders outside the circle."
    },
    {
        "question": "What is strike rate in cricket?",
        "answer": "Strike rate shows how quickly a batsman scores runs or how effectively a bowler takes wickets."
    },
    {
        "question": "What is run rate in cricket?",
        "answer": "Run rate is the average number of runs scored per over."
    },
    {
        "question": "What is DRS in cricket?",
        "answer": "DRS stands for Decision Review System. It allows players to challenge the umpire’s decision using technology."
    },
    {
        "question": "What is a googly in cricket?",
        "answer": "A googly is a deceptive delivery bowled by a leg spinner that turns in the opposite direction than expected."
    }
]




def preprocess_text(text):
    """
    Clean and preprocess input text:
    - Convert to lowercase
    - Remove special characters
    - Remove extra spaces
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text



questions = [preprocess_text(item["question"]) for item in faq_data]
answers = [item["answer"] for item in faq_data]


vectorizer = TfidfVectorizer()

faq_vectors = vectorizer.fit_transform(questions)


def get_best_answer(user_query):
    """
    Match user query with FAQ questions using cosine similarity
    and return the best matching answer.
    """


    user_query = preprocess_text(user_query)
    user_vector = vectorizer.transform([user_query])
    similarity_scores = cosine_similarity(user_vector, faq_vectors)


    best_match_index = np.argmax(similarity_scores)
    best_score = similarity_scores[0][best_match_index]


    if best_score < 0.25:
        return "Sorry, I couldn't find a good answer for that question."

    return answers[best_match_index]


def chatbot():
    print("\n====================================")
    print("      Cricket FAQ Chatbot")
    print("====================================")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you! Goodbye.")
            break

        response = get_best_answer(user_input)
        print("Bot:", response)
        print()

if __name__ == "__main__":
    chatbot()