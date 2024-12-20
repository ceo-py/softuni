from collections import deque

suggested_links = deque(int(x) for x in input().split())
featured_links = deque(int(x) for x in input().split())
final_feed_collection = []
target_engagement = int(input())


while suggested_links and featured_links:
    suggested_link, featured_link = suggested_links.popleft(),  featured_links.pop()

    if featured_link == suggested_link:
        final_feed_collection.append(0)
        continue

    remainder = abs(max(suggested_link, featured_link) %
                    min(suggested_link, featured_link))

    if featured_link > suggested_link:
        final_feed_collection.append(remainder)
        if remainder != 0:
            featured_links.append(remainder * 2)

    elif featured_link < suggested_link:
        final_feed_collection.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

print(f"Final Feed: {', '.join(str(x) for x in final_feed_collection)}")

total_engagement_value = sum(final_feed_collection)
if total_engagement_value >= target_engagement:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")

elif total_engagement_value < target_engagement:
    print(
        f"Goal not achieved! Short by: {target_engagement - total_engagement_value}")
