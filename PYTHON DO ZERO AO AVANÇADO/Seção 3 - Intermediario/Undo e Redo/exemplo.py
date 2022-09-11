"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
"""


def ls(list):
    print(f"\nTarefas:\n")
    for task in list:
        print(f"- {task}")
    if len(list) == 0:
        print(" ~ Sem tarefas.")


def add(task, list):
    list.append(task)
    return list


def undo(list, backup_list):
    if len(list) == 0:
        print("Nada para desfazer")
        return
    else:
        ult_desfazer = list.pop()
        backup_list.append(ult_desfazer)


def redo(list, backup_list):
    if len(backup_list) == 0:
        print("-" * 13)
        print("Nada a refazer")
        return
    else:
        ult_refazer = backup_list.pop()
        list.append(ult_refazer)


if __name__ == "__main__":
    task_list = []
    backup_tasks = []

    while True:
        print("-" * 42)
        op = input("Digite um tarefa ou [ls / undo / redo / ls]: ")

        if op == "ls":
            ls(task_list)
            continue
        elif op == "redo":
            redo(task_list, backup_tasks)
            continue
        elif op == "undo":
            undo(task_list, backup_tasks)
            continue
        task = op
        add(task, task_list)
