perguntas = {
    "Pergunta 1": {
        "pergunta": " Quanto é 2 + 2 ? ",
        "alternativas": {"a": 1, "b": 4, "c": 5},
        "resposta": "b",
    },
    "Pergunta 2": {
        "pergunta": " Quanto é 7 * 7 ? ",
        "alternativas": {"a": 1, "b": 44, "c": 49},
        "resposta": "c",
    },
}

for pk, pv in perguntas.items():
    print(f'{pk}:{pv["pergunta"]}')
    print("Respostas:")
    for rk, rv in pv["alternativas"].items():
        print(f"[{rk}]: {rv}")

    resp_usr = str(input("Resposta: "))
    if resp_usr == pv["resposta"]:
        print("Acertou o mizeravi!!!")
    else:
        print("~~~ Errouuu ~~~")
    print()
