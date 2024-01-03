favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        if len(languages) == 1:
            print(f"\t{name.title()}'s favorite language is {languages[0].title()}")
        else:
            print(f"\t{language.title()}")
