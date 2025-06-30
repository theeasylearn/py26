# working with for loop 
countries = ["india","china","Thailand", "Finland", "Iceland", "Ireland", "Switzerland", "New Zealand", "Poland", "Netherlands", "England", "Greenland", "Scotland", "Swaziland", "Liechtenstein", "Thailand", "Czechland", "Hungaryland", "Southland", "Northland", "Westland", "Eastland", "Rwanda", "Sri Lanka", "Jordan", "Bahrain", "Luxembourg", "Finland", "Portugal", "Germany", "Denmark", "Romania"]

# count = 0
# for country in countries:
#     print(country)
#     count = count + 1
# print(f"count of countries = {count}")

for country in countries:
    if 'land' in country:
        print(country)
# print(f"count of countries = {count}")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50)
#count odd numbers 
#count even numbers 
odd_count = 0
even_count = 0
for num in numbers:
    if num%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    print(num)

print(f"odd count = {odd_count} even count = {even_count}")

line = "the easylearn academy"
word_count = 1
for letter in line:
    if letter==' ':
        word_count+=1
print(f" word count = {word_count}")
india_info = {
    "country": "India",
    "capital": "New Delhi",
    "official_languages": ["Hindi", "English"],
    "currency": "Indian Rupee",
    "population": 1393409038,  # Approximate population
    "area": 3287263,  # Area in square kilometers
    "continent": "Asia",
    "independence_day": "August 15, 1947",
    "president": "Droupadi Murmu",
    "prime_minister": "Narendra Modi",
    "government_type": "Federal Parliamentary Republic",
    "calling_code": "+91",
    "timezone": "Indian Standard Time (IST)",
}
for key in india_info:
    print(india_info[key])