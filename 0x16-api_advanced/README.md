# 0x16. API advanced
## Description
Learning Objectives
- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Tasks
### 0. How many subs?

- Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
- Requirements:

  - Prototype: `python def number_of_subscribers(subreddit)`
  - If not a valid subreddit, return 0.
  - NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 1. Top Ten

- Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
- Requirements:

  - Prototype: `python def top_ten(subreddit)`
  - If not a valid subreddit, print None.
  - NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 2. Recurse it!

- Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
- Requirements:

  - Prototype: `python def recurse(subreddit, hot_list=[])`
  - Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a counter, but it must work without supplying a starting value in the main.
  - If not a valid subreddit, return None.
  - NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

### 3. Count it!

- Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).

- Prototype: `def count_words(subreddit, word_list)`
  - Note: You may change the prototype, but it must be able to be called with just a subreddit supplied and a list of keywords. AKA you can add a counter or anything else, but the function must work without supplying a starting value in the main.
  - Results should be printed in descending order, by the count, and if the count is the same for separate keywords, they should then be sorted alphabetically. Words with no matches should be skipped and not printed.
    Results are based on the number of times a keyword appears, not titles it appears in. ‘java java java’ counts as 3 separate occurrences of java.
  - To make life easier, ‘java.’ or ‘java!’ or ‘java\_’ should not count as ‘java’
  - If no posts match or the subreddit is invalid, print a newline.
  - NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are NOT following redirects.

