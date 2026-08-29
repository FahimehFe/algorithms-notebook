## 

Imagine you are looking for your doctor’s office number in your contacts. You type the name in instantly see the result. The data structure behind the process is called “Hash Map”.

With the help of Hash maps we are able to find an element in the dataset in an instant time O(1), no matter if there are 10 or 10000 elements inside the dataset. How cool is that? In the other classic data structures like arrays and linked-list, searching for a value would become more time-consuming as the number of contacts in your notebook grow. If an array is not sorted, it takes O(n) time to search for an item.

Every element in this data structure is a pair of key and value. In the doctor’s contact example:
Dr. Geller (🗝) → +49 166 000003 (Value)

How does it work? There is a mathematical function behind it called Hash Function which maps the key to its location. Inserting a new element will map the new key using the Hash function to a new point in the dataset. Insert, delete, search functions all are in the same order of O(1).

The idea is similar to when you reach for an index in an array. Hash maps also use the same concept by giving every key, a calculated address.

There’s a (not so common) potential for collision in the hash maps though. When you insert two different keys like Map and Pam that give the same result in Hash function , both entries land in the same location. Collisions (two keys, one slot) are resolved by chaining or probing. In case of collision, if you look for a key in a long chain, they search could reach O(n) in the worst case.

In case of putting a duplicate key, the Hash Map will overwrite it:
d = {}
d["Dr. Geller"] = “+49 166 000003”
d["Dr. Geller"] = “+49 168 878702”
print(d)        # {'Dr. Geller': ‘+49 168 878702’} — one entry, overwritten

Hash sets contain keys only. To help you better understand the Hash sets, think of the club bouncer. The bouncer has a list of guests and when a new person arrives, the bouncer only needs to know if they are on the list, they don’t care about additional information like their table number.

When inserting a duplicate item into a Hash Set, it’ll just ignore it as the membership function already sees the element in the dataset. delete, insert, search have the same O(1) complexity.

Hash Set vs. Hash Maps
- Hash Set: Keys vs. Hash Map: Key-Value pair
- Hash Set application: Used to check membership vs. Hash Map application: Call the value of the looked up key

When I need fast lookups by key I reach for a hash map. O(1) average, because it computes the location instead of searching for it.
