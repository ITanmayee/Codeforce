"""

You are an upcoming movie director, and you have just released your first movie. You have also launched a simple review site with two buttons to press — upvote and downvote.

However, the site is not so simple on the inside. There are two servers, each with its separate counts for the upvotes and the downvotes.

n reviewers enter the site one by one. Each reviewer is one of the following types:

type 1: a reviewer has watched the movie, and they like it — they press the upvote button;
type 2: a reviewer has watched the movie, and they dislike it — they press the downvote button;
type 3: a reviewer hasn't watched the movie — they look at the current number of upvotes and downvotes of the movie on the server they are in and decide what button to press. If there are more downvotes than upvotes, then a reviewer downvotes the movie. Otherwise, they upvote the movie.
Each reviewer votes on the movie exactly once.

Since you have two servers, you can actually manipulate the votes so that your movie gets as many upvotes as possible. When a reviewer enters a site, you know their type, and you can send them either to the first server or to the second one.

What is the maximum total number of upvotes you can gather over both servers if you decide which server to send each reviewer to?

"""

def up_votes(votes):
    return len(list(filter(lambda i: i==1 or i == 3, votes)))

for _ in range(int(input())):
    no_of_people = int(input())
    votes = list(map(int, input().split()))

    print(up_votes(votes))
