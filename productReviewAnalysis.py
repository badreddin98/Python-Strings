def keyword_highlighter(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for word in keywords:
            review = review.replace(word, word.upper())
        highlighted_reviews.append(review)
        print(review)
    return highlighted_reviews

def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0

    for review in reviews:
        for word in positive_words:
            positive_count += review.lower().count(word)
        for word in negative_words:
            negative_count += review.lower().count(word)

    return positive_count, negative_count

def review_summary(reviews, summary_length=30):
    summaries = []
    for review in reviews:
        if len(review) > summary_length:
            cutoff = review[:summary_length].rfind(" ")
            if cutoff == -1:
                cutoff = summary_length
            summaries.append(review[:cutoff] + "…")
        else:
            summaries.append(review)
    return summaries

# Data
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Task 1: Keyword Highlighting
print("Highlighted Reviews:")
highlighted_reviews = keyword_highlighter(reviews, keywords)
print("\n")

# Task 2: Sentiment Tally
positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print(f"Positive words count: {positive_count}")
print(f"Negative words count: {negative_count}")
print("\n")

# Task 3: Review Summary
summaries = review_summary(reviews)
print("Review Summaries:")
for summary in summaries:
    print(summary)