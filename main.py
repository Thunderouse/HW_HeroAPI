import requests

def three_hero_chek():
    hulk = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/332.json")
    capitan_ameriсa = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/149.json")
    thanos = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/powerstats/655.json")
    hulk_dict = hulk.json()
    capitan_ameriсa_dict = capitan_ameriсa.json()
    thanos_dict = thanos.json()

    if thanos_dict["intelligence"] > hulk_dict["intelligence"]:
        if thanos_dict["intelligence"] > capitan_ameriсa_dict["intelligence"]:
            print(f"Танос самый умный, его интеллект равен {thanos_dict['intelligence']}")
        else:
            print(f"Капитам америка самый умный, его интеллект равен {capitan_ameriсa_dict['intelligence']}")
    elif hulk_dict["intelligence"] > capitan_ameriсa_dict["intelligence"]:
        print(f"Халк самый умный, его интеллект равен {hulk_dict['intelligence']}")
    else:
        print(f"Капитам америка самый умный, его интеллект равен {capitan_ameriсa_dict['intelligence']}")


if __name__ == "__main__":
    three_hero_chek()