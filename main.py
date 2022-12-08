from fastapi import FastAPI
from poke_data.v2.poke_battle import battle_pokemon

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/battle/{first_poke}/{second_poke}")
async def battle(first_poke: int, second_poke: int):
    _battle = battle_pokemon(first_poke, second_poke)
    return {
        "poke_1": _battle[0],
        "poke_2": _battle[1],
        "winner": _battle[2],
    }
