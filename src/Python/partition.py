favourites = [
    {"fruit": "apple"},
    {"food": "pasta"},
    {"drink": "coke"},
]

print(
    list(
        filter(
            lambda x: list(x.keys()) == ["fruit"], 
            favourites
        )
    )
)
