from fastapi import FastAPI
from poke_data.v2.poke_battle import battle_pokemon
from poke_data.v2.poke_testing import get_two_pokemon
from poke_data.v2.ML_models.rfc import predict_battle
import numpy as np

app = FastAPI()


@app.get("/")
async def root():
    return "Hello this is backend poke api battle thing."


@app.get("/battle/{poke_one}/{poke_two}")
async def battle(poke_one: int, poke_two: int):
    pokemons = get_two_pokemon(poke_one, poke_two, normalize=False)
    actual = battle_pokemon(poke_one, poke_two)
    pred = predict_battle(pokemons)
    data = np.ndarray.tolist(pred[0])

    winner = poke_one if data == [1] else poke_two
    return {
        "poke_one": poke_one,
        "poke_two": poke_two,
        "actualWinner": actual[2],
        "winner": winner,
        "accuracy": pred[1],
    }
