from click import pass_obj


class MojWyjatek(Exception):
    pass


try:
    raise MojWyjatek
except MojWyjatek:
    print("Zdarzylo sie Moj wyjatek")
except ZeroDivisionError:
    print("Dzielenie przez 0")
except Exception:
    print("Cos innego")


try:
    # duzo kodu
    1 / 0
except Exception as e:
    print(e)